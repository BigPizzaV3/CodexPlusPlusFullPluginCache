#!/usr/bin/env python3
"""Run four representative one-page PDF generation checks."""

from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile


SCRIPT = Path(__file__).resolve().with_name("generate.py")
SKILL_DIR = SCRIPT.parents[1]
EXPECTED_ASSETS = {
    "canvas.html",
    "promotion-certificate.html",
    "ctfs.png",
    "stc.jpg",
    "hype.png",
}
EXPECTED_HYPE_SHA256 = "00adb977c2e8c4580c6d08bb5fe1782e02df816dbb2ad0321cc33168b2cdc9db"


CASES = [
    [
        "record",
        "--brand",
        "ctfs",
        "--title",
        "Most Profit",
        "--subtitle",
        "In a Day",
        "--value",
        "$300",
        "--name",
        "Cameron",
        "--date",
        "Aug 11th",
    ],
    [
        "record",
        "--brand",
        "stc",
        "--title",
        "Most Donor",
        "--subtitle",
        "In a Week",
        "--value",
        "15",
        "--name",
        "Helia",
        "--date",
        "July 24th",
    ],
    [
        "featured",
        "--title",
        "Best Leader of the Week",
        "--name",
        "Helia",
        "--date",
        "July 20th - 26th",
    ],
    [
        "promotion",
        "--name",
        "Sriya Indrakanti",
        "--date",
        "August 7 2026",
        "--role",
        "Corporate Trainer",
    ],
]


def main() -> int:
    assets_dir = SKILL_DIR / "assets"
    missing = sorted(name for name in EXPECTED_ASSETS if not (assets_dir / name).is_file())
    if missing:
        print(f"FAIL: missing bundled assets: {', '.join(missing)}", file=sys.stderr)
        return 1

    hype_digest = hashlib.sha256((assets_dir / "hype.png").read_bytes()).hexdigest()
    if hype_digest != EXPECTED_HYPE_SHA256:
        print("FAIL: bundled Hype logo is not the approved print-corrected version", file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory(prefix="hype-skill-test-") as directory:
        output_dir = Path(directory)
        for index, arguments in enumerate(CASES, start=1):
            command = [sys.executable, str(SCRIPT), "--output-dir", str(output_dir), *arguments]
            completed = subprocess.run(command, capture_output=True, text=True, timeout=90)
            if completed.returncode != 0:
                print(f"FAIL {index}: {completed.stderr.strip()}", file=sys.stderr)
                return 1
        pdfs = sorted(output_dir.glob("*.pdf"))
        if len(pdfs) != len(CASES):
            print(f"FAIL: expected {len(CASES)} PDFs, found {len(pdfs)}", file=sys.stderr)
            return 1
        print(f"PASS: {len(pdfs)}/{len(CASES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
