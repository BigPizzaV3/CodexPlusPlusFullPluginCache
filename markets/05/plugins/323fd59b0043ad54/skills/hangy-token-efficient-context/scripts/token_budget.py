#!/usr/bin/env python3
"""Measure text tokens or compare an original with a reduced candidate."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import tiktoken


@dataclass(frozen=True)
class Measurement:
    source: str
    characters: int
    utf8_bytes: int
    lines: int
    tokens: int


def read_text(source: str) -> str:
    if source == "-":
        return sys.stdin.read()
    return Path(source).read_text(encoding="utf-8-sig")


def measure(source: str, encoding_name: str) -> Measurement:
    text = read_text(source)
    encoding = tiktoken.get_encoding(encoding_name)
    return Measurement(
        source="stdin" if source == "-" else "input-file",
        characters=len(text),
        utf8_bytes=len(text.encode("utf-8")),
        lines=len(text.splitlines()),
        tokens=len(encoding.encode(text)),
    )


def comparison(before: Measurement, after: Measurement) -> dict[str, object]:
    saved = before.tokens - after.tokens
    percent = (saved / before.tokens * 100) if before.tokens else 0.0
    return {
        "before": asdict(before),
        "after": asdict(after),
        "tokens_saved": saved,
        "percent_saved": round(percent, 2),
        "candidate_is_smaller": saved > 0,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", nargs="*", help="UTF-8 text files, or - for stdin")
    parser.add_argument(
        "--compare",
        nargs=2,
        metavar=("ORIGINAL", "CANDIDATE"),
        help="compare two UTF-8 files",
    )
    parser.add_argument("--encoding", default="o200k_base")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    if bool(args.compare) == bool(args.sources):
        parser.error("provide either sources or --compare ORIGINAL CANDIDATE")
    if args.sources.count("-") > 1:
        parser.error("stdin can be read only once")
    return args


def main() -> int:
    args = parse_args()
    if args.compare:
        payload: object = comparison(
            measure(args.compare[0], args.encoding),
            measure(args.compare[1], args.encoding),
        )
    else:
        payload = [asdict(measure(source, args.encoding)) for source in args.sources]

    if args.as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    elif args.compare:
        data = payload
        assert isinstance(data, dict)
        before = data["before"]
        after = data["after"]
        assert isinstance(before, dict) and isinstance(after, dict)
        print(f"before_tokens: {before['tokens']}")
        print(f"after_tokens: {after['tokens']}")
        print(f"tokens_saved: {data['tokens_saved']}")
        print(f"percent_saved: {data['percent_saved']}%")
    else:
        assert isinstance(payload, list)
        for item in payload:
            print(
                f"{item['source']}\ttokens={item['tokens']}\t"
                f"chars={item['characters']}\tlines={item['lines']}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
