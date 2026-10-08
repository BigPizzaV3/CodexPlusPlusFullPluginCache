#!/usr/bin/env python3
"""Create the standard A4 PDF from a self-contained report HTML.

The helper has no Python package dependency. It uses an installed Chromium-family
browser in headless mode, writes through a temporary file, and only promotes a
PDF to the requested output path after print-layout and structural checks pass.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from chromium_print import ChromiumError, LayoutOverflow, measure_and_print
from delivery_links import delivery_markdown
from render_report import DISCLAIMER


MIN_PDF_BYTES = 4_096
DEFAULT_TIMEOUT_SECONDS = 60
EXPECTED_PAGE_RANGE = range(8, 11)


class PdfRenderError(Exception):
    pass


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_canonical_paths(html_path: Path, output_path: Path) -> None:
    if html_path.parent != output_path.parent:
        raise PdfRenderError("HTMLとPDFは同じ最終出力directoryに置く必要があります")
    if html_path.stem != output_path.stem:
        raise PdfRenderError("HTMLとPDFは拡張子以外が同じfile名である必要があります")


def find_browser(explicit: str | None = None) -> Path:
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit).expanduser())
    for command in (
        "google-chrome-stable",
        "google-chrome",
        "chromium",
        "chromium-browser",
        "chrome",
        "microsoft-edge",
    ):
        resolved = shutil.which(command)
        if resolved:
            candidates.append(Path(resolved))
    candidates.extend(
        [
            Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
            Path("/Applications/Chromium.app/Contents/MacOS/Chromium"),
            Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
        ]
    )
    for candidate in candidates:
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return candidate.resolve()
    raise PdfRenderError(
        "headless PDF生成に使えるChrome、ChromiumまたはEdgeが見つかりません"
    )


def pdfinfo(path: Path) -> dict[str, Any]:
    command = shutil.which("pdfinfo")
    if not command:
        return {"pages": None, "a4": None}
    result = subprocess.run(
        [command, str(path)],
        check=False,
        capture_output=True,
        text=True,
        timeout=20,
    )
    if result.returncode != 0:
        raise PdfRenderError("pdfinfoで生成PDFを読み取れませんでした")
    pages_match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    size_match = re.search(r"^Page size:\s+(.+)$", result.stdout, re.MULTILINE)
    pages = int(pages_match.group(1)) if pages_match else None
    page_size = size_match.group(1).strip() if size_match else ""
    return {"pages": pages, "a4": "(A4)" in page_size, "page_size": page_size}


def text_check(path: Path) -> bool | None:
    command = shutil.which("pdftotext")
    if not command:
        return None
    result = subprocess.run(
        [command, str(path), "-"],
        check=False,
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0 or len(result.stdout.strip()) < 500:
        raise PdfRenderError("生成PDFの本文を確認できませんでした")
    if "PDFとして保存" in result.stdout or "印刷画面を開く" in result.stdout:
        raise PdfRenderError("画面専用のPDF保存ボタンがPDF本文へ混入しています")
    expected_footer = "".join(DISCLAIMER.split())
    pages = [page for page in result.stdout.split("\f") if page.strip()]
    if len(pages) not in EXPECTED_PAGE_RANGE:
        raise PdfRenderError("PDF本文を8〜10ページごとに確認できませんでした")
    for index, page in enumerate(pages, 1):
        if expected_footer not in "".join(page.split()):
            raise PdfRenderError(f"PDF {index}ページの固定免責本文を確認できませんでした")
    return True


def verify_pdf(path: Path) -> dict[str, Any]:
    payload = path.read_bytes()
    if len(payload) < MIN_PDF_BYTES or not payload.startswith(b"%PDF-"):
        raise PdfRenderError("生成物が有効なPDFではありません")
    if b"%%EOF" not in payload[-4_096:]:
        raise PdfRenderError("PDFが最後まで書き込まれていません")
    details = pdfinfo(path)
    pages = details.get("pages")
    if pages is not None and pages not in EXPECTED_PAGE_RANGE:
        raise PdfRenderError(f"PDFが{pages}ページです。8〜10ページが必要です")
    if details.get("a4") is False:
        raise PdfRenderError(f"PDFがA4ではありません: {details.get('page_size', '不明')}")
    details["text_check"] = text_check(path)
    details["footer_text_check"] = details["text_check"]
    details["bytes"] = len(payload)
    return details


def render_pdf(
    html_path: Path,
    output_path: Path,
    *,
    browser_path: str | None,
    timeout: int,
    overwrite: bool,
) -> dict[str, Any]:
    html_path = html_path.expanduser().resolve()
    output_path = output_path.expanduser().resolve()
    if not html_path.is_file() or html_path.suffix.lower() != ".html":
        raise PdfRenderError(f"入力HTMLが見つかりません: {html_path}")
    if output_path.suffix.lower() != ".pdf":
        raise PdfRenderError("出力file名は.pdfで終える必要があります")
    validate_canonical_paths(html_path, output_path)
    if output_path.exists() and not overwrite:
        raise PdfRenderError(
            f"出力先が既に存在します。-v2等の別名か--overwriteを使ってください: {output_path}"
        )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    browser = find_browser(browser_path)
    html_sha256 = sha256_file(html_path)

    file_descriptor, temporary_name = tempfile.mkstemp(
        prefix=".rognalia-pdf-", suffix=".pdf", dir=output_path.parent
    )
    os.close(file_descriptor)
    temporary_pdf = Path(temporary_name)
    temporary_pdf.unlink()

    try:
        layout = measure_and_print(browser, html_path, temporary_pdf, timeout)

        details = verify_pdf(temporary_pdf)
        if sha256_file(html_path) != html_sha256:
            raise PdfRenderError("PDF生成中に入力HTMLが変更されました")
        pdf_sha256 = sha256_file(temporary_pdf)
        os.replace(temporary_pdf, output_path)
        return {
            "receipt_version": 2,
            "status": "ok",
            "renderer": "chromium-family-headless",
            "html": str(html_path),
            "pdf": str(output_path),
            "browser": str(browser),
            "html_sha256": html_sha256,
            "pdf_sha256": pdf_sha256,
            "layout_check": layout,
            "delivery_markdown": delivery_markdown(html_path, output_path),
            **details,
        }
    finally:
        if temporary_pdf.exists():
            temporary_pdf.unlink()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path, help="self-contained report HTML")
    parser.add_argument("--output", required=True, type=Path, help="delivery PDF path")
    parser.add_argument("--browser", help="Chrome/Chromium/Edge executable path")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.timeout < 10 or args.timeout > 300:
        print("ERROR: --timeoutは10〜300秒にしてください", file=sys.stderr)
        return 2
    try:
        result = render_pdf(
            args.html,
            args.output,
            browser_path=args.browser,
            timeout=args.timeout,
            overwrite=args.overwrite,
        )
    except LayoutOverflow as exc:
        print(json.dumps({
            "receipt_version": 2,
            "status": "needs_content_revision",
            "renderer": "chromium-family-headless",
            "html": str(args.html.expanduser().resolve()),
            "pdf_created": False,
            "layout_check": exc.result,
            "reason": str(exc),
        }, ensure_ascii=False, indent=2))
        return 3
    except (OSError, ValueError, KeyError, IndexError, PdfRenderError,
            ChromiumError, subprocess.SubprocessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
