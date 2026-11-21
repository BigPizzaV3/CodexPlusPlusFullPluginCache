#!/usr/bin/env python3
"""Render a complete, offline script from validated JSON. Standard library only."""

import argparse
import datetime
import html
import json
import re
from pathlib import Path
from urllib.parse import urlsplit


ZEROICHI_HEADINGS = [
    "動画タイトル", "サムネイルで使用するテキスト", "【ダイジェスト】",
    "【キャッチフレーズ＋自己紹介 例）〇〇を専門に診療している〇〇科医の〇〇です】",
    "【視聴者の悩み共感パート】", "【動画を最後まで見るべき理由】", "【動画本編】",
    "【Call to Action 例）チャンネル登録、グッドボタン、コメントをぜひお願いいたします。】",
    "引用論文", "引用論文まとめ",
]
ZEROICHI_ROLES = ["metadata", "metadata", "digest", "spoken", "spoken", "spoken",
                  "spoken", "spoken", "references", "references"]
CITATION = re.compile(r"(?:\(\*(?P<legacy>[1-9][0-9]*)\)|（引用文献挿入：(?P<number>[1-9][0-9]*)）)")
CSS = """
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f4f3f6;
color:#24202b;font-family:system-ui,-apple-system,'Hiragino Sans','Yu Gothic',sans-serif}
main{max-width:1000px;margin:24px auto;padding:clamp(20px,5vw,56px);background:#fff}
h1{font-size:clamp(26px,5vw,38px);line-height:1.45}h2{font-size:26px;margin:2.3em 0 .8em}
h3{font-size:22px;margin:1.8em 0 .7em}p,li{font-size:19px;line-height:1.9}
p{margin:0 0 1.1em;white-space:pre-wrap;overflow-wrap:anywhere}a{color:#563299;overflow-wrap:anywhere}
.citation-marker{font-size:.85em}.meta,.label{font-size:15px;color:#645d6e}.label{margin-bottom:.7em}
nav{border-block:1px solid #ddd5e7;padding:12px 0}nav ul{padding-left:1.3em}
nav li{font-size:16px;line-height:1.8}section,aside,footer{scroll-margin-top:20px}
.digest,.notes{background:#f7f4fb;border-left:4px solid #8b70b0;padding:16px 20px;margin:28px 0}
.digest h2,.notes h2{margin-top:0}.digest-source{color:#b00020;font-weight:800}
.references li{margin-bottom:1.4em}.references p{margin:.3em 0;font-size:17px}
.references ol{padding-left:2em}.references a{font-size:17px}
@media(max-width:600px){main{margin:0;padding:20px}h2{font-size:23px}h3{font-size:21px}}
@media print{body{background:#fff}main{margin:0;max-width:none;padding:0}nav,.screen-only{display:none}
h2,h3{break-after:avoid}p{orphans:3;widows:3}a{color:inherit}.digest-source{color:#b00020}}
"""


def require(condition, message):
    if not condition:
        raise ValueError(message)


def string(value, label, allow_empty=False):
    require(isinstance(value, str) and (allow_empty or value.strip()), f"{label}: text required")
    return value


def sequence(value, label):
    require(isinstance(value, list), f"{label}: array required")
    return value


def mapping(value, label):
    require(isinstance(value, dict), f"{label}: object required")
    return value


def allowed_keys(value, keys, label):
    require(not (set(value) - set(keys)), f"{label}: unknown fields {sorted(set(value) - set(keys))}")


def safe_url(value):
    string(value, "reference URL")
    require(not any(c.isspace() or ord(c) < 32 for c in value), "reference URL: whitespace/control character")
    try:
        parts = urlsplit(value)
        port = parts.port
        require(parts.scheme in {"https", "http"} and bool(parts.hostname)
                and not parts.username and not parts.password, "reference URL: HTTP(S) URL required")
        require(not any(c in parts.netloc for c in '\\<>\"'), "reference URL: invalid host")
    except ValueError as exc:
        raise ValueError(f"reference URL: {exc}") from exc
    return value


def citation_id(match):
    return match["number"] or match["legacy"]


def inline(text):
    # Normalize only at rendering time: source/digest offsets remain unchanged.
    def render(match):
        rid = citation_id(match)
        return (f'<span class="citation-marker" data-role="editorial-citation">'
                f'<a href="#ref-{rid}">（引用文献挿入：{rid}）</a></span>')
    return CITATION.sub(render, html.escape(text))


def marked(text, spans):
    merged = []
    for start, end in sorted(spans):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    result, previous = [], 0
    for start, end in merged:
        result.extend([inline(text[previous:start]), '<strong class="digest-source">',
                       inline(text[start:end]), '</strong>'])
        previous = end
    result.append(inline(text[previous:]))
    return ''.join(result)


def render_script(data):
    mapping(data, "document")
    allowed_keys(data, {"title", "version", "date", "author", "layout", "sections", "references"}, "document")
    for field in ("title", "version", "date"):
        string(data.get(field), field)
    require(re.fullmatch(r"\d{4}-\d{2}-\d{2}", data["date"]), "date: YYYY-MM-DD required")
    datetime.date.fromisoformat(data["date"])
    if "author" in data:
        string(data["author"], "author")
    require(data.get("layout", "standard") in {"standard", "zeroichi"}, "unknown layout")
    sections = sequence(data.get("sections"), "sections")
    require(sections, "at least one section required")
    refs, used_refs, ids, paragraphs, highlights = {}, set(), set(), {}, {}

    def identifier(value):
        string(value, "ID")
        require(re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", value), f"invalid ID: {value}")
        require(value not in ids and value not in {"script-document", "page-title", "toc"}
                and not value.startswith(("ref-", "digest-item-")), f"duplicate/reserved ID: {value}")
        ids.add(value)

    for ref in sequence(data.get("references", []), "references"):
        mapping(ref, "reference")
        allowed_keys(ref, {"id", "authors", "title", "year", "url", "kind", "scope", "bibliography", "summary", "supports", "short"}, "reference")
        rid = ref.get("id")
        require(type(rid) is int and rid > 0 and rid not in refs, "reference ID: unique positive integer required")
        for field in ("authors", "title", "year", "kind", "scope"):
            string(ref.get(field), f"reference {rid}.{field}")
        for field in ("bibliography", "summary", "supports", "short"):
            if field in ref:
                string(ref[field], f"reference {rid}.{field}")
        safe_url(ref.get("url"))
        refs[rid] = ref

    reference_sections, digest_count, spoken_count = [], 0, 0
    for section in sections:
        mapping(section, "section")
        role = section.get("role")
        require(role in {"metadata", "spoken", "digest", "references", "notes"}, "unknown section role")
        common_keys = {"id", "heading", "role"}
        allowed_keys(section, common_keys | ({"items"} if role == "digest" else {"style"} if role == "references" else {"blocks"}), "section")
        identifier(section.get("id"))
        string(section.get("heading"), "section heading")
        if role == "references":
            require(section.get("style") in {"short", "full"}, "reference section style: short/full required")
            reference_sections.append(section["style"])
        elif role == "digest":
            sequence(section.get("items"), "digest items")
            digest_count += 1
        else:
            for block in sequence(section.get("blocks"), "blocks"):
                mapping(block, "block")
                allowed_keys(block, {"id", "text", "heading"}, "block")
                identifier(block.get("id"))
                require(("text" in block) != ("heading" in block), "block needs exactly one text or heading")
                text = string(block.get("text", block.get("heading")), "block content")
                if "text" in block and role == "spoken":
                    paragraphs[block["id"]] = text
                    spoken_count += 1
                for token in re.finditer(r"\(\*[^)]*\)|（引用文献挿入[^）]*）", text):
                    require(CITATION.fullmatch(token[0]), f"malformed citation: {token[0]}")
                remaining = CITATION.sub("", text)
                require("(*" not in remaining and "引用文献挿入" not in remaining,
                        "malformed or incomplete citation marker")
                for match in CITATION.finditer(text):
                    rid = int(citation_id(match))
                    require(rid in refs, f"missing reference: {rid}")
                    require(role == "spoken" and "text" in block, "citations belong in spoken paragraphs")
                    used_refs.add(rid)
    require(spoken_count, "full spoken script required")
    require(digest_count <= 1, "only one digest section allowed")
    require(len(reference_sections) == len(set(reference_sections)), "duplicate reference section style")
    require(not refs or reference_sections.count("full") == 1, "full references section required")
    require(used_refs == set(refs), f"unused references: {sorted(set(refs) - used_refs)}")
    if data.get("layout") == "zeroichi":
        require([s["heading"] for s in sections[:10]] == ZEROICHI_HEADINGS, "zeroichi: preserve all 10 fixed headings in order")
        require([s["role"] for s in sections[:10]] == ZEROICHI_ROLES, "zeroichi: incorrect fixed section roles")
        require(sections[8].get("style") == "short" and sections[9].get("style") == "full", "zeroichi: short then full references required")
        require(all(s["role"] == "notes" for s in sections[10:]), "zeroichi: only separate notes may follow the 10 sections")
        for ref in refs.values():
            for field in ("bibliography", "short", "summary", "supports"):
                string(ref.get(field), f"zeroichi reference {ref['id']}.{field}")

    digest_html = []
    for section in sections:
        if section["role"] != "digest":
            continue
        for index, item in enumerate(section["items"], 1):
            mapping(item, "digest item")
            allowed_keys(item, {"source", "quote", "occurrence", "masks"}, "digest item")
            source, quote = item.get("source"), string(item.get("quote"), "digest quote")
            require(isinstance(source, str) and source in paragraphs, "digest source: spoken paragraph ID required")
            text = paragraphs[source]
            starts = [m.start() for m in re.finditer('(?=' + re.escape(quote) + ')', text)]
            require(starts, f"digest quote is absent from {source}")
            occurrence = item.get("occurrence", 1)
            require(type(occurrence) is int and 1 <= occurrence <= len(starts), "digest occurrence out of range")
            require(len(starts) == 1 or "occurrence" in item, "ambiguous digest quote: specify occurrence")
            start, end = starts[occurrence - 1], starts[occurrence - 1] + len(quote)
            for citation in CITATION.finditer(text):
                require(not (citation.start() < start < citation.end() or citation.start() < end < citation.end()), "digest cannot split a citation marker")
            highlights.setdefault(source, []).append((start, end))
            shown, previous = [], 0
            for mask in sequence(item.get("masks", []), "digest masks"):
                mapping(mask, "mask")
                allowed_keys(mask, {"start", "end"}, "mask")
                a, b = mask.get("start"), mask.get("end")
                require(type(a) is int and type(b) is int and previous <= a < b <= len(quote), "mask ranges must be ordered, disjoint, within quote")
                require(a != 0 or b != len(quote), "cannot mask the whole quote")
                require(not any(a < c.end() and b > c.start() for c in CITATION.finditer(quote)), "cannot mask citation marker")
                shown.extend([quote[previous:a], "？？"])
                previous = b
            shown.append(quote[previous:])
            require(sum(m["end"] - m["start"] for m in item.get("masks", [])) < len(quote), "cannot mask the whole quote")
            digest_html.append(f'<li id="digest-item-{index}"><p>{inline("".join(shown))}<br>'
                               f'<a class="label" href="#{source}">本文の該当箇所へ</a></p></li>')

    chunks = []
    for section in sections:
        role, sid = section["role"], section["id"]
        tag = "aside" if role == "digest" else "footer" if role == "notes" else "section"
        chunks.append(f'<{tag} id="{sid}" class="{role}" data-role="{role}"><h2>{html.escape(section["heading"])}</h2>')
        if role in {"digest", "notes"}:
            chunks.append('<p class="label">編集・制作用（読み上げ本文外）</p>')
        if role == "digest":
            chunks.append('<ul>')
            chunks.extend(digest_html)
            chunks.append('</ul>')
        elif role == "references":
            chunks.append('<ol>')
            for rid, ref in sorted(refs.items()):
                description = ref.get("bibliography", f'{ref["authors"]}. {ref["title"]}. {ref["year"]}.')
                if section["style"] == "short":
                    chunks.append(f'<li value="{rid}"><a href="#ref-{rid}">{html.escape(ref.get("short", description))}</a></li>')
                else:
                    chunks.append(f'<li id="ref-{rid}" value="{rid}"><p>{html.escape(description)}</p>'
                                  f'<p><a href="{html.escape(ref["url"], quote=True)}">{html.escape(ref["url"])}</a></p>'
                                  f'<p>種類：{html.escape(ref["kind"])}／確認範囲：{html.escape(ref["scope"])}</p>')
                    for field in ("summary", "supports"):
                        if field in ref:
                            chunks.append(f'<p>{html.escape(ref[field])}</p>')
                    chunks.append('</li>')
            chunks.append('</ol>')
        else:
            for block in section["blocks"]:
                bid = block["id"]
                if "heading" in block:
                    chunks.append(f'<h3 id="{bid}">{html.escape(block["heading"])}</h3>')
                else:
                    chunks.append(f'<p id="{bid}">{marked(block["text"], highlights.get(bid, []))}</p>')
        chunks.append(f'</{tag}>')
    metadata = " ／ ".join([data["version"], data["date"]] + ([data["author"]] if data.get("author") else []))
    toc = ''.join(f'<li><a href="#{s["id"]}">{html.escape(s["heading"])}</a></li>' for s in sections)
    return (f'<!doctype html>\n<html lang="ja"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{html.escape(data["title"])}</title><style>{CSS}</style></head><body>'
            f'<main id="script-document"><header><h1 id="page-title">{html.escape(data["title"])}</h1>'
            f'<p class="meta">{html.escape(metadata)}</p><p class="label screen-only">本文は文字を選択してコピーできます。</p></header>'
            f'<nav id="toc" aria-label="目次"><ul>{toc}</ul></nav>{"".join(chunks)}</main></body></html>\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="script JSON")
    parser.add_argument("output", type=Path, help="actual HTML output file")
    args = parser.parse_args()
    try:
        require(args.input.resolve() != args.output.resolve(), "input and output must differ")
        result = render_script(json.loads(args.input.read_text(encoding="utf-8")))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding="utf-8")
        require(args.output.read_text(encoding="utf-8") == result, "saved file readback mismatch")
    except (ValueError, OSError, TypeError) as exc:
        parser.exit(2, f"error: {exc}\n")
    print(json.dumps({"output": str(args.output.resolve()), "bytes": args.output.stat().st_size}, ensure_ascii=False))


if __name__ == "__main__":
    main()
