#!/usr/bin/env python3
"""Build a self-contained Style Me gallery fragment from bundled JPEG previews."""

from __future__ import annotations

import argparse
import base64
import json
from pathlib import Path
import re
import uuid


MAX_FRAGMENT_BYTES = 1_000_000
TIERS = ("Accessible", "Premium", "Luxury", "Mix it up")
STYLES = (
    ("W1", "womenswear", "Sculptural Ease", "Fluid draping, a long silhouette, and unexpected flat shoes.", "01-sculptural-ease.jpg"),
    ("W2", "womenswear", "Modern Structure", "A clean black base, a full skirt, and strong texture contrast.", "02-modern-structure.jpg"),
    ("W3", "womenswear", "Relaxed Polish", "A soft knit, a crisp short skirt, and a pointed shoe.", "03-relaxed-polish.jpg"),
    ("M1", "menswear", "Textured Classics", "A textured knit, a crisp shirt, and dark denim with grounded shoes.", "men/01-textured-classics.jpg"),
    ("M2", "menswear", "Colorful Layers", "A blue utility jacket, a green knit, and relaxed denim with loafers.", "men/02-colorful-layers.jpg"),
    ("M3", "menswear", "Clean Lines", "A white tee, fluid tailored trousers, and minimal white sneakers.", "men/03-clean-lines.jpg"),
)


def build(category: str, tier: str | None, selected: list[str], budget_context: str, output: Path, qa: bool = False) -> dict:
    skill_root = Path(__file__).resolve().parents[1]
    visible = [entry for entry in STYLES if category == "both" or entry[1] == category]
    valid_ids = {entry[0] for entry in visible}
    normalized = set()
    for item in selected:
        for token in re.split(r"[\s,]+", item.strip()):
            if not token:
                continue
            value = token.upper()
            if value in {"1", "2", "3"} and category != "both":
                value = ("W" if category == "womenswear" else "M") + value
            if value not in valid_ids:
                raise ValueError(f"Unknown or ambiguous style {token!r}; use {', '.join(sorted(valid_ids))}.")
            normalized.add(value)
    if len(budget_context) > 1000:
        raise ValueError("Keep --budget-context at most 1000 characters.")
    if output.suffix.lower() != ".html":
        raise ValueError("--output must name an .html fragment.")
    if output.is_symlink():
        raise ValueError("--output must not be a symbolic link.")

    images = []
    for style_id, clothing_category, name, caption, filename in visible:
        preview = skill_root / "assets" / "gallery-previews" / filename
        data = preview.read_bytes()
        if not (data.startswith(b"\xff\xd8\xff") and data.endswith(b"\xff\xd9")):
            raise ValueError(f"Preview is not a complete JPEG: {preview}")
        images.append({
            "id": style_id,
            "category": clothing_category,
            "label": style_id if category == "both" else style_id[1:],
            "name": name,
            "caption": caption,
            "image": "data:image/jpeg;base64," + base64.b64encode(data).decode("ascii"),
        })
    config = {
        "schemaVersion": 2,
        "category": category,
        "tier": tier,
        "selected": [entry[0] for entry in visible if entry[0] in normalized],
        "budgetContext": budget_context,
        "qa": qa,
        "styles": images,
    }
    serialized = json.dumps(config, ensure_ascii=True, separators=(",", ":"), sort_keys=True)
    root_id = "style-me-gallery-" + uuid.uuid4().hex
    serialized = serialized.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    template = (skill_root / "assets" / "gallery-template.html").read_text(encoding="utf-8")
    if template.count("__GALLERY_CONFIG__") != 1 or "__GALLERY_ID__" not in template:
        raise ValueError("Gallery template placeholders are missing or invalid.")
    fragment = template.replace("__GALLERY_ID__", root_id).replace("__GALLERY_CONFIG__", serialized)
    encoded = fragment.encode("utf-8")
    if len(encoded) >= MAX_FRAGMENT_BYTES:
        raise ValueError(f"Gallery is {len(encoded)} bytes; keep it below {MAX_FRAGMENT_BYTES} bytes.")
    output = output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(encoded)
    return {"path": str(output), "bytes": len(encoded), "category": category, "images": len(images)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--category", required=True, choices=("womenswear", "menswear", "both"))
    parser.add_argument("--tier", choices=TIERS)
    parser.add_argument("--style", action="append", nargs="+", default=[], metavar="ID", help="Selected IDs, e.g. --style W1 W3. Repeat or separate with commas. Single categories also accept 1-3.")
    parser.add_argument("--budget-context", default="", help="An already supplied cap, with known currency/scope. Allows continuing without a named tier.")
    parser.add_argument("--qa", action="store_true", help="Mark follow-up selections as synthetic QA fixtures, not personal preferences.")
    parser.add_argument("--output", required=True, type=Path, help="Absolute path in the current host's writable task directory.")
    args = parser.parse_args()
    if not args.output.is_absolute():
        parser.error("--output must be an absolute path in the current host's writable task directory.")
    try:
        result = build(args.category, args.tier, [item for group in args.style for item in group], args.budget_context.strip(), args.output, args.qa)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=True))


if __name__ == "__main__":
    main()
