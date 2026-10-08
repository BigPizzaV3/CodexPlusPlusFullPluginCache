#!/usr/bin/env python3
"""Count Japanese article body characters without headings, tags, or whitespace."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


HEADING_PREFIXES = ("[大見出し]", "[小見出し]")
TAG_LINE_PATTERN = re.compile(r"^#[^\s#]+(?: #[^\s#]+){4,5}$")


def find_tag_line(lines: list[str]) -> tuple[int | None, int]:
    """Return the final dedicated note tag line index and its tag count."""
    for index in range(len(lines) - 1, -1, -1):
        stripped = lines[index].strip()
        if not stripped:
            continue
        if TAG_LINE_PATTERN.fullmatch(stripped):
            return index, len(stripped.split(" "))
        break
    return None, 0


def count_body(text: str) -> dict[str, int]:
    lines = text.splitlines()
    tag_line_index, tag_count = find_tag_line(lines)
    body_lines = [
        line
        for index, line in enumerate(lines)
        if index != tag_line_index
        and not line.lstrip().startswith(HEADING_PREFIXES)
    ]
    body = "\n".join(body_lines)
    return {
        "body_characters": sum(1 for char in body if not char.isspace()),
        "heading_count": sum(
            1 for line in lines if line.lstrip().startswith(HEADING_PREFIXES)
        ),
        "tag_count": tag_count,
        "total_characters": len(text),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="見出し行、末尾のnoteタグ行、空白文字を除いた本文文字数を数えます。"
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        help="本文ファイル。省略時は標準入力から読みます。",
    )
    parser.add_argument("--min", dest="minimum", type=int, default=2000)
    parser.add_argument("--max", dest="maximum", type=int, default=2400)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.minimum < 0 or args.maximum < args.minimum:
        raise SystemExit("文字数範囲が不正です。")

    text = (
        args.path.read_text(encoding="utf-8")
        if args.path is not None
        else sys.stdin.read()
    )
    result = count_body(text)
    result.update(
        {
            "minimum": args.minimum,
            "maximum": args.maximum,
            "within_range": args.minimum
            <= result["body_characters"]
            <= args.maximum,
        }
    )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["within_range"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
