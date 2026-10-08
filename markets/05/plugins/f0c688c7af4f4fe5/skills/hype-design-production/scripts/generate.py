#!/usr/bin/env python3
"""Deterministically render Hype Events PDFs from the bundled HTML templates."""

from __future__ import annotations

import argparse
import html
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


SKILL_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = SKILL_DIR / "assets"
LOGO_FILES = ("ctfs.png", "stc.jpg", "hype.png")


def escaped(value: str) -> str:
    return html.escape(value.strip(), quote=True)


def replace_one(source: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, source, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"Template field not found exactly once: {label}")
    return updated


def replace_element_text(source: str, tag: str, class_value: str, value: str) -> str:
    pattern = rf'(<{tag}\s+class="{re.escape(class_value)}"[^>]*>).*?(</{tag}>)'
    return replace_one(
        source,
        pattern,
        lambda match: f"{match.group(1)}{escaped(value)}{match.group(2)}",
        class_value,
    )


def inject_css(source: str, css: str) -> str:
    marker = "</style>"
    if marker not in source:
        raise RuntimeError("Template style block is missing")
    return source.replace(marker, f"\n{css}\n{marker}", 1)


def build_record_html(args: argparse.Namespace) -> str:
    source = (ASSETS_DIR / "canvas.html").read_text(encoding="utf-8")
    old_print = ".poster { transform: scale(.75556); transform-origin: top left; }"
    new_print = ".poster { zoom: .75556; transform: none; overflow: hidden; }"
    if old_print not in source:
        raise RuntimeError("Record template print scaling marker is missing")
    source = source.replace(old_print, new_print, 1)

    brand = args.brand if args.mode == "record" else "hype"
    layout = "featured" if args.mode == "featured" else "record"
    main_pattern = r'(<main\s+class="poster")\s+data-brand="[^"]*"([^>]*>)'
    source = replace_one(
        source,
        main_pattern,
        lambda match: (
            f'{match.group(1)} data-brand="{brand}" data-layout="{layout}"{match.group(2)}'
        ),
        "poster attributes",
    )

    if args.mode == "featured":
        title = args.title
        subtitle = ""
        value = args.name
        lower_name = ""
        source = inject_css(
            source,
            """
    .poster[data-layout="featured"] .subtitle-row,
    .poster[data-layout="featured"] .name-box { display: none; }
    .poster[data-layout="featured"] .title-box { height: 185px; }
    .poster[data-layout="featured"] .value-box {
      top: 350px;
      height: 690px;
    }
    .poster[data-layout="featured"] .value {
      letter-spacing: 2px;
    }
    .poster[data-layout="featured"] .winner-row { top: 1082px; }
    .poster[data-layout="featured"] .date-row { top: 1212px; }
            """.strip(),
        )
    else:
        title = args.title
        subtitle = args.subtitle
        value = args.value
        lower_name = args.name or ""
        if not lower_name:
            source = inject_css(
                source,
                """
    .poster[data-layout="record"] .name-box { display: none; }
    .poster[data-layout="record"] .winner-row { top: 1070px; }
    .poster[data-layout="record"] .date-row { top: 1185px; }
                """.strip(),
            )

    source = replace_element_text(source, "div", "fit display title", title)
    source = replace_element_text(source, "div", "fit subtitle", subtitle)
    source = replace_element_text(source, "div", "fit display value", value)
    source = replace_element_text(source, "div", "fit display name", lower_name)
    source = replace_element_text(source, "div", "fit date", args.date)
    source = inject_css(
        source,
        """
    .logo-stc {
      background: #fff;
      filter: contrast(1.08) brightness(1.04) saturate(1.02);
    }
        """.strip(),
    )
    return source


def build_promotion_html(args: argparse.Namespace) -> str:
    source = (ASSETS_DIR / "promotion-certificate.html").read_text(encoding="utf-8")
    source = replace_element_text(source, "span", "recipient", args.name)
    source = replace_element_text(source, "p", "role", args.role)
    source = replace_element_text(source, "div", "award-date", f"Awarded {args.date}")
    return source


def clean_component(value: str) -> str:
    value = re.sub(r"[\x00-\x1f/\\:*?\"<>|]", "-", value.strip())
    value = re.sub(r"\s+", " ", value).strip(" .-")
    return value or "Untitled"


def output_filename(args: argparse.Namespace) -> str:
    if args.filename:
        stem = Path(args.filename).stem
    elif args.mode == "promotion":
        stem = "-".join(("Promotion Certificate", args.name, args.date))
    elif args.mode == "featured":
        stem = "-".join((args.title, args.name, args.date))
    else:
        subtitle = args.subtitle.strip()
        full_title = args.title
        if subtitle:
            full_title = f"{args.title} {subtitle[0].lower()}{subtitle[1:]}"
        parts = [full_title]
        if args.name:
            parts.append(args.name)
        parts.extend((args.value, args.date))
        stem = "-".join(parts)
    return clean_component(stem) + ".pdf"


def default_output_dir() -> Path:
    if SKILL_DIR.parent.name == "skills" and SKILL_DIR.parent.parent.name == ".agents":
        return SKILL_DIR.parent.parent.parent / "result"
    return Path.cwd() / "result"


def locate_chrome(explicit: str | None) -> Path:
    candidates: list[str] = []
    if explicit:
        candidates.append(explicit)
    if os.environ.get("CHROME_PATH"):
        candidates.append(os.environ["CHROME_PATH"])
    candidates.extend(
        [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
        ]
    )
    for command in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        resolved = shutil.which(command)
        if resolved:
            candidates.append(resolved)
    for candidate in candidates:
        path = Path(candidate).expanduser()
        if path.is_file() and os.access(path, os.X_OK):
            return path
    raise RuntimeError(
        "Google Chrome was not found. Install Chrome or set CHROME_PATH to its executable."
    )


def pdf_page_count(path: Path) -> int:
    data = path.read_bytes()
    if not data.startswith(b"%PDF-"):
        raise RuntimeError("Chrome output is not a valid PDF")
    return len(re.findall(rb"/Type\s*/Page\b", data))


def render(args: argparse.Namespace) -> Path:
    output_dir = Path(args.output_dir).expanduser().resolve() if args.output_dir else default_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    chrome = locate_chrome(args.chrome)
    work_dir = Path(tempfile.mkdtemp(prefix=".hype-temp-", dir=output_dir))

    try:
        for logo in LOGO_FILES:
            shutil.copy2(ASSETS_DIR / logo, work_dir / logo)

        generated_html = (
            build_promotion_html(args) if args.mode == "promotion" else build_record_html(args)
        )
        html_path = work_dir / "design.html"
        html_path.write_text(generated_html, encoding="utf-8")

        staged_pdf = work_dir / "output.pdf"
        command = [
            str(chrome),
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={staged_pdf}",
            html_path.as_uri(),
        ]
        completed = subprocess.run(command, capture_output=True, text=True, timeout=60)
        if completed.returncode != 0 or not staged_pdf.exists() or staged_pdf.stat().st_size == 0:
            detail = (completed.stderr or completed.stdout).strip()
            raise RuntimeError(f"Chrome PDF export failed: {detail or 'no output'}")

        pages = pdf_page_count(staged_pdf)
        if pages != 1:
            raise RuntimeError(f"Expected a one-page PDF, but Chrome produced {pages} pages")

        final_pdf = output_dir / output_filename(args)
        os.replace(staged_pdf, final_pdf)
        shutil.rmtree(work_dir)
        return final_pdf
    except Exception:
        print(f"Temporary HTML retained at: {work_dir}", file=sys.stderr)
        raise


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", help="Destination result directory")
    parser.add_argument("--chrome", help="Path to the Chrome executable")
    parser.add_argument("--filename", help="Optional output filename override")
    subparsers = parser.add_subparsers(dest="mode", required=True)

    record = subparsers.add_parser("record", help="Generate a normal record poster")
    record.add_argument("--brand", choices=("ctfs", "stc", ""), required=True)
    record.add_argument("--title", required=True)
    record.add_argument("--subtitle", required=True)
    record.add_argument("--value", required=True)
    record.add_argument("--name", default="")
    record.add_argument("--date", required=True)

    featured = subparsers.add_parser("featured", help="Generate a Hype featured award poster")
    featured.add_argument(
        "--title",
        choices=("Best Leader of the Week", "New Kids on the Block This Week"),
        required=True,
    )
    featured.add_argument("--name", required=True)
    featured.add_argument("--date", required=True)
    featured.set_defaults(brand="hype", subtitle="", value="")

    promotion = subparsers.add_parser("promotion", help="Generate a promotion certificate")
    promotion.add_argument("--name", required=True)
    promotion.add_argument("--date", required=True)
    promotion.add_argument("--role", default="Corporate Trainer")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        result = render(args)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
