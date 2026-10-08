#!/usr/bin/env python3
"""Verify that a delivered HTML file is the exact fixed-renderer output."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from render_report import build_html
from validate_report import ValidationError, validate_report
from delivery_links import delivery_markdown


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def validate_canonical_html(data: dict[str, Any], document: str) -> str:
    """Reject hand-built lookalikes, post-render edits, and alternate templates."""
    validate_report(data)
    expected = build_html(data)
    if document != expected:
        raise ValidationError(
            "html: 固定render_report.pyの出力と完全一致しません。"
            "手動render、生成後編集、別templateを使わず、report JSONから再生成してください。"
            f" actual_sha256={sha256_text(document)}"
            f" expected_sha256={sha256_text(expected)}"
        )
    return sha256_text(document)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report_json", type=Path, help="Validated report JSON")
    parser.add_argument("report_html", type=Path, help="Rendered report HTML")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        data = json.loads(args.report_json.read_text(encoding="utf-8"))
        document = args.report_html.read_text(encoding="utf-8")
        digest = validate_canonical_html(data, document)
    except (OSError, json.JSONDecodeError, ValidationError) as exc:
        print(f"HTML VERIFY FAILED: {exc}", file=sys.stderr)
        return 1
    pages = document.count('class="sheet report-page')
    print(
        f"HTML VERIFIED: {args.report_html} / fixed renderer exact match / "
        f"{pages} pages / sha256={digest}"
    )
    print(f"HTML_DELIVERY: {delivery_markdown(args.report_html)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
