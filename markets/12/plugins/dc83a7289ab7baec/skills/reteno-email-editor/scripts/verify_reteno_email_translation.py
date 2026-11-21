#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
import html as html_lib
import json
from pathlib import Path
import re
import sys
from typing import Any


DEFAULT_FORBIDDEN_PHRASES = (
    "Welcome to our community",
    "to our community",
    "Plagiarism",
    "AI Detector",
    "AI Writing Assistant",
    "Smart Research Helper",
)
HTML_SUFFIXES = {".html", ".htm"}
JSON_SUFFIXES = {".json"}
HTML_LIKE_RE = re.compile(r"(?is)<(?:!doctype\s+html|html\b|body\b|table\b|tr\b|td\b|span\b|a\b)")
OPEN_TAG_RE = re.compile(r"""(?is)<\s*(?!/)(?P<tag>[a-z][a-z0-9:-]*)\b(?:(?:"[^"]*"|'[^']*'|[^"'>])*>|[^>]*>)""")
CLASS_ATTR_RE = re.compile(r"""(?is)\bclass\s*=\s*(["'])(.*?)\1""")
RESPONSIVE_CLASSES = ("es-desk-hidden", "es-mobile-hidden")
# --- shared merge-token grammar; keep byte-identical with edit_reteno_email_html.py ---
# Velocity/merge tokens as they appear in Reteno builder exports: $name, $!name, ${name},
# $!{name} with optional .member chains and (...) call syntax, plus VTL directives.
MERGE_TOKEN_RE = re.compile(
    r"""(?x)
    \$!?\{[^{}]*\}
    | \$!?[A-Za-z_][A-Za-z0-9_-]*(?:\([^()]*\))?(?:\.[A-Za-z_][A-Za-z0-9_-]*(?:\([^()]*\))?)*
    | \#(?:set|foreach|if|elseif|else|end|macro|parse|include|stop|break)\b
    """
)
# A directive that carries no arguments is indistinguishable from prose ("#end of season
# sale"), so it counts as a token only in a document that also opens a real VTL block.
BARE_VELOCITY_DIRECTIVES = frozenset({"#end", "#else", "#stop", "#break"})
VELOCITY_OPENER_RE = re.compile(r"#(?:if|foreach|macro)\s*\(")


def _merge_token_counts(html: str) -> Counter[str]:
    has_opener = VELOCITY_OPENER_RE.search(html) is not None
    return Counter(
        token
        for token in (match.group(0) for match in MERGE_TOKEN_RE.finditer(html))
        if has_opener or token not in BARE_VELOCITY_DIRECTIVES
    )
# --- end shared merge-token grammar ---


@dataclass(frozen=True)
class Issue:
    path: str
    location: str
    phrase: str
    excerpt: str


@dataclass(frozen=True)
class ReplacementCheck:
    old: str
    new: str
    preheader: bool = False
    inline_html: str | None = None


class RetenoTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.visible_parts: list[str] = []
        self.preheader_parts: list[str] = []
        self.anchor_parts: list[str] = []
        self.image_alt_parts: list[str] = []
        self.image_title_parts: list[str] = []
        self._skip_depth = 0
        self._hidden_preheader_depth = 0
        self._anchor_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attrs_dict = {name.lower(): value or "" for name, value in attrs}
        if tag in {"head", "script", "style", "noscript"}:
            self._skip_depth += 1
        if tag == "span" and (self._hidden_preheader_depth or _class_contains(attrs_dict.get("class", ""), "esd-hidden-preheader")):
            self._hidden_preheader_depth += 1
        if tag == "a":
            self._anchor_depth += 1
        if tag == "img":
            alt = attrs_dict.get("alt", "")
            title = attrs_dict.get("title", "")
            if alt:
                self.image_alt_parts.append(alt)
            if title:
                self.image_title_parts.append(title)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "a" and self._anchor_depth:
            self._anchor_depth -= 1
        if tag == "span" and self._hidden_preheader_depth:
            self._hidden_preheader_depth -= 1
        if tag in {"head", "script", "style", "noscript"} and self._skip_depth:
            self._skip_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._skip_depth:
            return
        if self._hidden_preheader_depth:
            self.preheader_parts.append(data)
            return
        self.visible_parts.append(data)
        if self._anchor_depth:
            self.anchor_parts.append(data)

    @property
    def visible_text(self) -> str:
        return _normalize_text(" ".join(self.visible_parts))

    @property
    def anchor_text(self) -> str:
        return _normalize_text(" ".join(self.anchor_parts))

    @property
    def image_alt_text(self) -> str:
        return _normalize_text(" ".join(self.image_alt_parts))

    @property
    def image_title_text(self) -> str:
        return _normalize_text(" ".join(self.image_title_parts))


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Verify localized Reteno email artifacts do not retain known English source phrases "
            "in visible text, anchor text, or image alt/title attributes. Use --include-preheader "
            "when verifying requested preheader localization, including saved read-back."
        )
    )
    parser.add_argument("paths", nargs="+", type=Path, help="Localized .html/.json files or directories to scan.")
    parser.add_argument("--include-preheader", action="store_true", help="Scan requested native metadata.preheader.text and compiled hidden preheaders.")
    parser.add_argument(
        "--phrase",
        action="append",
        dest="phrases",
        help="Forbidden English source phrase to scan for. Can be passed multiple times.",
    )
    parser.add_argument("--json-report", type=Path, help="Optional path to write a JSON report.")
    parser.add_argument(
        "--replacements",
        type=Path,
        help="Optional replacement JSON; every old string must be gone and every non-empty new string present.",
    )
    parser.add_argument(
        "--source-html",
        type=Path,
        help="Optional source HTML whose responsive visibility signature must match each localized HTML file.",
    )
    parser.add_argument("--source-css", type=Path, help="Optional source CSS for byte-equality verification.")
    parser.add_argument("--localized-css", type=Path, help="Localized CSS that must equal --source-css byte-for-byte.")
    parser.add_argument(
        "--allow-empty",
        action="store_true",
        help="Exit successfully when no supported .html/.json artifacts are found.",
    )
    return parser.parse_args()


def _class_contains(class_value: str, expected: str) -> bool:
    return re.search(rf"\b{re.escape(expected)}\b", class_value, re.IGNORECASE) is not None


def _normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def _load_replacement_pairs(path: Path) -> tuple[ReplacementCheck, ...]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"replacements file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"replacements file is not valid JSON: {path}: {exc}") from exc
    if isinstance(payload, dict):
        payload = payload.get("replacements")
    if not isinstance(payload, list):
        raise ValueError("replacements JSON must be a list or an object with a 'replacements' list")
    pairs: list[ReplacementCheck] = []
    for index, item in enumerate(payload):
        if not isinstance(item, dict):
            raise ValueError(f"replacement[{index}] must be an object")
        old = item.get("old")
        new = item.get("new")
        if not isinstance(old, str) or not old:
            raise ValueError(f"replacement[{index}] old must be a non-empty string")
        if not isinstance(new, str):
            raise ValueError(f"replacement[{index}] new must be a string")
        inline_html = new if item.get("text_mode") == "inline" else None
        if inline_html is not None:
            texts = []
            for fragment in (old, new):
                parser = RetenoTextExtractor()
                parser.feed(fragment)
                parser.close()
                texts.append(parser.visible_text)
            old, new = texts
        elif item.get("block_type") != "image":
            # old matches serialized HTML; plain new is literal user-visible text.
            old = html_lib.unescape(old)
        pairs.append(ReplacementCheck(old, new, item.get("block_type") == "hidden_preheader", inline_html))
    return tuple(pairs)


def _responsive_signature(html: str) -> tuple[tuple[str, tuple[str, ...]], ...]:
    signature: list[tuple[str, tuple[str, ...]]] = []
    for match in OPEN_TAG_RE.finditer(html):
        class_match = CLASS_ATTR_RE.search(match.group(0))
        if class_match is None:
            continue
        class_value = class_match.group(2)
        responsive = tuple(
            class_name
            for class_name in RESPONSIVE_CLASSES
            if _class_contains(class_value, class_name)
        )
        if responsive:
            signature.append((match.group("tag").lower(), responsive))
    return tuple(signature)


def _read_utf8(path: Path, *, label: str) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ValueError(f"{label} file not found: {path}") from exc
    except UnicodeDecodeError as exc:
        raise ValueError(f"{label} file is not valid UTF-8: {path}: {exc}") from exc


def _phrase_pattern(phrase: str) -> re.Pattern[str]:
    escaped = re.escape(phrase)
    if phrase[:1].isascii() and phrase[:1].isalnum():
        escaped = rf"(?<![A-Za-z0-9]){escaped}"
    if phrase[-1:].isascii() and phrase[-1:].isalnum():
        escaped = rf"{escaped}(?![A-Za-z0-9])"
    return re.compile(escaped, flags=re.IGNORECASE)


def _excerpt(text: str, phrase: str, *, radius: int = 50) -> str:
    match = _phrase_pattern(phrase).search(text)
    if match is None:
        return text[: radius * 2].strip()
    start = max(0, match.start() - radius)
    end = min(len(text), match.end() + radius)
    return text[start:end].strip()


def _issues_for_text(path: Path, location: str, text: str, phrases: tuple[str, ...]) -> list[Issue]:
    issues: list[Issue] = []
    if not text:
        return issues
    for phrase in phrases:
        if _phrase_pattern(phrase).search(text):
            issues.append(
                Issue(
                    path=str(path),
                    location=location,
                    phrase=phrase,
                    excerpt=_excerpt(text, phrase),
                )
            )
    return issues


def _extract_html_issues(path: Path, html: str, phrases: tuple[str, ...], *, location_prefix: str, include_preheader: bool = False) -> list[Issue]:
    parser = RetenoTextExtractor()
    parser.feed(html)
    parser.close()
    issues: list[Issue] = []
    if include_preheader:
        issues.extend(_issues_for_text(path, f"{location_prefix}.hidden_preheader", _normalize_text(" ".join(parser.preheader_parts)), phrases))
    issues.extend(_issues_for_text(path, f"{location_prefix}.visible_text", parser.visible_text, phrases))
    issues.extend(_issues_for_text(path, f"{location_prefix}.anchor_text", parser.anchor_text, phrases))
    issues.extend(
        _issues_for_text(path, f"{location_prefix}.image_alt", parser.image_alt_text, phrases)
    )
    issues.extend(
        _issues_for_text(path, f"{location_prefix}.image_title", parser.image_title_text, phrases)
    )
    return issues


def _scan_json_value(path: Path, value: Any, phrases: tuple[str, ...], *, location: str, include_preheader: bool = False) -> list[Issue]:
    issues: list[Issue] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_location = f"{location}.{key}" if location else str(key)
            key_lower = str(key).lower()
            if isinstance(child, str) and key_lower in {"html", "body", "content"} and HTML_LIKE_RE.search(child):
                issues.extend(_extract_html_issues(path, child, phrases, location_prefix=child_location, include_preheader=include_preheader))
                continue
            if key_lower in {"preheader", "hiddenpreheader", "hidden_preheader"}:
                if include_preheader:
                    text = child.get("text") if isinstance(child, dict) else child
                    if isinstance(text, str):
                        issues.extend(_issues_for_text(path, child_location, _normalize_text(text), phrases))
                continue
            issues.extend(_scan_json_value(path, child, phrases, location=child_location, include_preheader=include_preheader))
        return issues
    if isinstance(value, list):
        for index, child in enumerate(value):
            issues.extend(_scan_json_value(path, child, phrases, location=f"{location}[{index}]", include_preheader=include_preheader))
    return issues


def _scan_file(path: Path, phrases: tuple[str, ...], *, include_preheader: bool = False) -> list[Issue]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [Issue(path=str(path), location="file", phrase="<utf-8>", excerpt=str(exc))]

    suffix = path.suffix.lower()
    if suffix in HTML_SUFFIXES:
        return _extract_html_issues(path, text, phrases, location_prefix="html", include_preheader=include_preheader)
    if suffix in JSON_SUFFIXES:
        try:
            payload = json.loads(text)
        except json.JSONDecodeError as exc:
            return [Issue(path=str(path), location="json", phrase="<valid-json>", excerpt=str(exc))]
        return _scan_json_value(path, payload, phrases, location="$", include_preheader=include_preheader)
    return []


def _iter_supported_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(
                sorted(
                    child
                    for child in path.rglob("*")
                    if child.is_file() and child.suffix.lower() in HTML_SUFFIXES | JSON_SUFFIXES
                )
            )
        elif path.is_file() and path.suffix.lower() in HTML_SUFFIXES | JSON_SUFFIXES:
            files.append(path)
    return files


def main() -> int:
    args = _parse_args()
    try:
        replacement_pairs = (
            _load_replacement_pairs(args.replacements) if args.replacements is not None else ()
        )
        source_html = (
            _read_utf8(args.source_html, label="source HTML")
            if args.source_html is not None
            else None
        )
        if (args.source_css is None) != (args.localized_css is None):
            raise ValueError("--source-css and --localized-css must be provided together")
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    replacement_pairs = tuple(item for item in replacement_pairs if args.include_preheader or not item.preheader)
    phrases = tuple(dict.fromkeys((*(args.phrases or DEFAULT_FORBIDDEN_PHRASES), *(item.old for item in replacement_pairs if item.old != item.new))))
    files = _iter_supported_files(args.paths)
    if not files and not args.allow_empty:
        print("error: no supported .html/.json artifacts found", file=sys.stderr)
        return 1

    issues: list[Issue] = []
    for path in files:
        issues.extend(_scan_file(path, phrases, include_preheader=args.include_preheader))

    source_signature = _responsive_signature(source_html) if source_html is not None else None
    source_tokens = _merge_token_counts(source_html) if source_html is not None else None
    responsive_checks: list[dict[str, Any]] = []
    merge_token_checks: list[dict[str, Any]] = []
    replacement_checks: list[dict[str, Any]] = []
    for path in files:
        if path.suffix.lower() not in HTML_SUFFIXES:
            continue
        try:
            html = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if source_signature is not None:
            localized_signature = _responsive_signature(html)
            matched = localized_signature == source_signature
            responsive_checks.append(
                {
                    "path": str(path),
                    "matched": matched,
                    "source_count": len(source_signature),
                    "localized_count": len(localized_signature),
                }
            )
            if not matched:
                issues.append(
                    Issue(
                        path=str(path),
                        location="html.responsive_visibility",
                        phrase="<responsive-signature>",
                        excerpt=(
                            f"source={source_signature!r}; localized={localized_signature!r}"
                        )[:500],
                    )
                )
        if source_tokens is not None:
            localized_tokens = _merge_token_counts(html)
            tokens_matched = localized_tokens == source_tokens
            merge_token_checks.append(
                {
                    "path": str(path),
                    "matched": tokens_matched,
                    "source_count": sum(source_tokens.values()),
                    "localized_count": sum(localized_tokens.values()),
                }
            )
            if not tokens_matched:
                added = sorted((localized_tokens - source_tokens).elements())
                removed = sorted((source_tokens - localized_tokens).elements())
                issues.append(
                    Issue(
                        path=str(path),
                        location="html.merge_tokens",
                        phrase="<merge-tokens>",
                        excerpt=(f"added={added!r}; removed={removed!r}")[:500],
                    )
                )
        parser = RetenoTextExtractor()
        parser.feed(html)
        parser.close()
        searchable_text = _normalize_text(
            f"{parser.visible_text} {parser.image_alt_text} {parser.image_title_text}"
        )
        for replacement in replacement_pairs:
            old, new = replacement.old, replacement.new
            target_text = _normalize_text(" ".join(parser.preheader_parts)) if replacement.preheader else searchable_text
            new_present = new == "" or _phrase_pattern(new).search(target_text) is not None
            if replacement.inline_html is not None:
                new_present = new_present and replacement.inline_html in html
            replacement_checks.append(
                {
                    "path": str(path),
                    "old": old,
                    "new": new,
                    "new_present": new_present,
                }
            )
            if not new_present:
                issues.append(
                    Issue(
                        path=str(path),
                        location="html.replacement_new",
                        phrase=new,
                        excerpt="replacement text or required inline markup is absent from its localized target",
                    )
                )

    css_check: dict[str, Any] | None = None
    if args.source_css is not None and args.localized_css is not None:
        try:
            source_css_bytes = args.source_css.read_bytes()
            localized_css_bytes = args.localized_css.read_bytes()
        except FileNotFoundError as exc:
            print(f"error: CSS file not found: {exc.filename}", file=sys.stderr)
            return 1
        css_equal = source_css_bytes == localized_css_bytes
        css_check = {
            "source": str(args.source_css),
            "localized": str(args.localized_css),
            "equal": css_equal,
            "source_bytes": len(source_css_bytes),
            "localized_bytes": len(localized_css_bytes),
        }
        if not css_equal:
            issues.append(
                Issue(
                    path=str(args.localized_css),
                    location="css.byte_equality",
                    phrase="<byte-identical-css>",
                    excerpt="localized CSS differs from the source CSS",
                )
            )

    report = {
        "files_scanned": [str(path) for path in files],
        "forbidden_phrases": list(phrases),
        "issue_count": len(issues),
        "issues": [asdict(issue) for issue in issues],
        "merge_token_checks": merge_token_checks,
        "replacement_checks": replacement_checks,
        "responsive_checks": responsive_checks,
        "css_check": css_check,
    }
    if args.json_report is not None:
        args.json_report.parent.mkdir(parents=True, exist_ok=True)
        args.json_report.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")

    if issues:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True), file=sys.stderr)
        return 1

    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
