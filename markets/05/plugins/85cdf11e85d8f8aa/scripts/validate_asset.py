#!/usr/bin/env python3
"""Validate generated Ads Manager image assets against shared upload-safe contracts."""

from __future__ import annotations

import argparse
import json
import mimetypes
import sys
from pathlib import Path

MAX_BYTES = 10 * 1024 * 1024
ACCOUNT_LOGO_CANONICAL_MAX_DIMENSION = 1024
FORMAT_TO_MIME = {
    "JPEG": "image/jpeg",
    "PNG": "image/png",
    "WEBP": "image/webp",
}
ALLOWED_FORMATS = {
    "account-logo": {"JPEG", "PNG", "WEBP"},
    "ad-creative": {"JPEG", "PNG", "WEBP"},
}
MIN_DIMENSIONS = {
    "account-logo": 128,
    "ad-creative": 256,
}
EXPECTED_SUFFIXES = {
    "JPEG": {".jfif", ".jpe", ".jpeg", ".jpg"},
    "PNG": {".png"},
    "WEBP": {".webp"},
}


def _failures_for(path: Path, kind: str) -> tuple[dict[str, object], list[str]]:
    failures: list[str] = []
    report: dict[str, object] = {
        "ok": False,
        "kind": kind,
        "path": str(path),
    }

    if not path.is_file():
        return report, ["File does not exist or is not a regular file."]

    size_bytes = path.stat().st_size
    report["size_bytes"] = size_bytes
    if size_bytes <= 0:
        failures.append("File must not be empty.")
    if size_bytes > MAX_BYTES:
        failures.append(f"File exceeds the 10 MiB limit ({size_bytes} bytes).")

    try:
        from PIL import Image, ImageOps, UnidentifiedImageError
    except ImportError:
        return report, [
            "Pillow is required for deterministic image validation but is not installed."
        ]

    try:
        with Image.open(path) as image:
            image.load()
            image_format = (image.format or "").upper()
            width, height = image.size
            frame_count = int(getattr(image, "n_frames", 1))
            mode = image.mode
            with ImageOps.exif_transpose(image) as canonical_image:
                if max(canonical_image.size) > ACCOUNT_LOGO_CANONICAL_MAX_DIMENSION:
                    canonical_image.thumbnail(
                        (
                            ACCOUNT_LOGO_CANONICAL_MAX_DIMENSION,
                            ACCOUNT_LOGO_CANONICAL_MAX_DIMENSION,
                        ),
                        Image.Resampling.LANCZOS,
                    )
                canonical_width, canonical_height = canonical_image.size
    except (UnidentifiedImageError, OSError, ValueError) as exc:
        return report, [f"Could not decode image contents: {exc}"]

    mime_type = FORMAT_TO_MIME.get(image_format)
    suffix = path.suffix.lower()
    guessed_mime_type, _ = mimetypes.guess_type(path.name)
    animated = frame_count > 1
    report.update(
        {
            "format": image_format or None,
            "mime_type": mime_type,
            "extension": suffix or None,
            "extension_mime_type": guessed_mime_type,
            "width": width,
            "height": height,
            "canonical_width": canonical_width,
            "canonical_height": canonical_height,
            "mode": mode,
            "frame_count": frame_count,
            "animated": animated,
        }
    )

    if image_format not in ALLOWED_FORMATS[kind]:
        allowed = ", ".join(sorted(ALLOWED_FORMATS[kind]))
        failures.append(
            f"Actual image format must be one of {allowed}; got {image_format or 'unknown'}."
        )
    if width <= 0 or height <= 0:
        failures.append("Image dimensions must be positive.")
    minimum = MIN_DIMENSIONS[kind]
    if canonical_width < minimum or canonical_height < minimum:
        failures.append(
            f"{kind} images must remain at least {minimum}x{minimum} pixels after "
            f"canonical resizing (got {canonical_width}x{canonical_height})."
        )
    if animated:
        failures.append("Generated Ads Manager image assets must be static/non-animated.")

    expected_suffixes = EXPECTED_SUFFIXES.get(image_format)
    if expected_suffixes is not None and suffix not in expected_suffixes:
        expected = ", ".join(sorted(expected_suffixes))
        failures.append(
            f"Filename extension must match the actual {image_format} content; expected {expected}."
        )

    return report, failures


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a generated Ads Manager ad creative image or account logo."
    )
    parser.add_argument(
        "--kind",
        required=True,
        choices=sorted(ALLOWED_FORMATS),
        help="Asset contract to validate.",
    )
    parser.add_argument("path", type=Path, help="Image file to validate.")
    args = parser.parse_args()

    report, failures = _failures_for(args.path, args.kind)
    report["failures"] = failures
    report["ok"] = not failures
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
