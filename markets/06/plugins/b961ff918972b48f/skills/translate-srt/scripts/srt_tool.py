"""Inspect and rebuild SRT subtitles without translating or using the network."""
import argparse
import codecs
import hashlib
import json
import re
import sys
from pathlib import Path

TIME = r"\d{2,}:\d{2}:\d{2},\d{3}"
TIMING = re.compile(rf"^({TIME})[ \t]+-->[ \t]+({TIME})(?:[ \t]+[^\r\n]+)?[ \t]*$")
TOKENS = re.compile(r"<[^>\r\n]+>|\{\\[^}\r\n]*\}|\\[Nnh]")


def ms(value):
    h, m, rest = value.split(":")
    s, milli = rest.split(",")
    if int(m) > 59 or int(s) > 59:
        raise ValueError(f"Invalid timestamp: {value}")
    return ((int(h) * 60 + int(m)) * 60 + int(s)) * 1000 + int(milli)


def parse(text):
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    blocks = re.split(r"\n[ \t]*\n(?:[ \t]*\n)*", normalized.strip("\n"))
    cues = []
    for position, block in enumerate(blocks):
        lines = block.split("\n")
        if len(lines) < 3 or not re.fullmatch(r"[ \t]*[0-9]+[ \t]*", lines[0]):
            raise ValueError(f"Malformed cue at position {position}: expected number, timing, and text")
        match = TIMING.fullmatch(lines[1])
        if not match:
            raise ValueError(f"Malformed timestamp at position {position}")
        start, end = ms(match[1]), ms(match[2])
        if end < start:
            raise ValueError(f"Cue ends before it starts at position {position}")
        body = "\n".join(lines[2:])
        if not body.strip():
            raise ValueError(f"Empty source cue at position {position}")
        cues.append(dict(position=position, number=lines[0], timestamp=lines[1], text=body,
                         start_ms=start, end_ms=end))
    if not cues:
        raise ValueError("No SRT cues found")
    return cues


def load_source(path, encoding=None):
    raw = Path(path).read_bytes()
    if encoding:
        codec = encoding
    elif raw.startswith(codecs.BOM_UTF16_LE) or raw.startswith(codecs.BOM_UTF16_BE):
        codec = "utf-16"
    else:
        codec = "utf-8-sig"
    try:
        text = raw.decode(codec, errors="strict").lstrip("\ufeff")
    except (UnicodeError, LookupError) as exc:
        raise ValueError("Cannot decode source safely; supply the correct --encoding") from exc
    crlf = text.count("\r\n")
    lone_lf = text.count("\n") - crlf
    lone_cr = text.count("\r") - crlf
    newline = max(((crlf, "\r\n"), (lone_lf, "\n"), (lone_cr, "\r")), key=lambda item: item[0])[1]
    if not crlf and not lone_lf and not lone_cr:
        newline = "\n"
    cues = parse(text)
    warnings = [f"Source cue at position {b['position']} starts before the previous cue ends; timings preserved."
                for a, b in zip(cues, cues[1:]) if b["start_ms"] < a["end_ms"]]
    return raw, cues, newline, raw.startswith(codecs.BOM_UTF8), codec, warnings


def write_new(path, data, protected):
    target = Path(path)
    if target.resolve() in {Path(p).resolve() for p in protected}:
        raise ValueError("Output must not overwrite a source or another task artifact")
    if target.exists():
        raise ValueError(f"Output already exists; choose a new filename: {target.name}")
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("xb") as handle:
        handle.write(data)


def json_bytes(data):
    return (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def build(source, translations, output, report_path=None, encoding=None, bilingual=False):
    raw, cues, newline, bom, codec, warnings = load_source(source, encoding)
    items = json.loads(Path(translations).read_text(encoding="utf-8-sig"))
    if not isinstance(items, list):
        raise ValueError("Translations must be a JSON array")
    translated = {}
    for item in items:
        if not isinstance(item, dict) or type(item.get("position")) is not int or not isinstance(item.get("text"), str):
            raise ValueError("Every translation requires integer position and string text")
        position = item["position"]
        if position in translated:
            raise ValueError(f"Duplicate translation position: {position}")
        body = item["text"].replace("\r\n", "\n").replace("\r", "\n")
        if not body.strip() or body != body.strip("\n") or re.search(r"\n[ \t]*\n", body) or "\x00" in body:
            raise ValueError(f"Blank or structurally invalid translation at position {position}")
        translated[position] = body
    if set(translated) != set(range(len(cues))):
        missing = sorted(set(range(len(cues))) - set(translated))
        extra = sorted(set(translated) - set(range(len(cues))))
        raise ValueError(f"Incomplete coverage: missing={missing[:20]}, extra={extra[:20]}")
    blocks = []
    for cue in cues:
        body = translated[cue["position"]]
        if TOKENS.findall(body) != TOKENS.findall(cue["text"]):
            raise ValueError(f"Formatting/control tokens changed at position {cue['position']}")
        if bilingual:
            body = cue["text"] + "\n" + body
        blocks.append(cue["number"] + "\n" + cue["timestamp"] + "\n" + body)
    result = "\n\n".join(blocks) + "\n"
    verified = parse(result)
    checks = {
        "cue_count_unchanged": len(verified) == len(cues),
        "number_lines_unchanged": [c["number"] for c in verified] == [c["number"] for c in cues],
        "timestamp_lines_unchanged": [c["timestamp"] for c in verified] == [c["timestamp"] for c in cues],
        "all_positions_translated_once": len(translated) == len(cues),
        "protected_tokens_preserved": True,
    }
    if not all(checks.values()):
        raise ValueError("Generated file failed structural validation")
    data = (codecs.BOM_UTF8 if bom else b"") + result.replace("\n", newline).encode("utf-8")
    report = dict(status="passed", cue_count=len(cues), mode="bilingual" if bilingual else "translation",
                  source_encoding=codec, output_encoding="utf-8-sig" if bom else "utf-8",
                  source_sha256=hashlib.sha256(raw).hexdigest(), output_sha256=hashlib.sha256(data).hexdigest(),
                  checks=checks, warnings=warnings)
    protected = [source, translations]
    if report_path:
        if Path(report_path).resolve() in {Path(p).resolve() for p in protected + [output]} or Path(report_path).exists():
            raise ValueError("Report path must be new and distinct from all input/output files")
    write_new(output, data, protected)
    if report_path:
        write_new(report_path, json_bytes(report), protected + [output])
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    inspect = sub.add_parser("inspect")
    inspect.add_argument("source")
    inspect.add_argument("--output", required=True)
    inspect.add_argument("--encoding")
    create = sub.add_parser("build")
    create.add_argument("source")
    create.add_argument("translations")
    create.add_argument("--output", required=True)
    create.add_argument("--report")
    create.add_argument("--encoding")
    create.add_argument("--bilingual", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "inspect":
            raw, cues, newline, bom, codec, warnings = load_source(args.source, args.encoding)
            manifest = dict(cue_count=len(cues), source_encoding=codec, warnings=warnings, cues=cues)
            write_new(args.output, json_bytes(manifest), [args.source])
            print(json.dumps(dict(status="inspected", cue_count=len(cues), warnings=warnings)))
        else:
            print(json.dumps(build(args.source, args.translations, args.output, args.report,
                                   args.encoding, args.bilingual), ensure_ascii=False))
    except (ValueError, OSError) as exc:
        print(json.dumps(dict(status="error", error=str(exc)), ensure_ascii=False), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
