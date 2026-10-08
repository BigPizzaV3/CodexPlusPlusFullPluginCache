#!/usr/bin/env python3
"""Build a standalone AAC card HTML file from JSON and local/host-provided images."""

from __future__ import annotations

import argparse
import base64
import json
import sys
from pathlib import Path


IMAGE_MIME_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
    ".svg": "image/svg+xml",
}
SUPPORTED_LAYOUTS = {1, 2, 4, 8}
DATA_TOKEN = "__AAC_DATA__"


def require_text(value: object, field_name: str) -> str:
    if value is None or not str(value).strip():
        raise ValueError(f"Required field is empty: {field_name}")
    return str(value)


def resolve_output_path(raw_path: str) -> Path:
    path = Path(raw_path)
    return path.resolve() if path.is_absolute() else (Path.cwd() / path).resolve()


def resolve_image_path(raw_path: str, input_directory: Path) -> Path:
    path = Path(raw_path)
    return path.resolve() if path.is_absolute() else (input_directory / path).resolve()


def load_cards(input_path: Path) -> tuple[dict, list[dict]]:
    try:
        data = json.loads(input_path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError("Input JSON must contain an object")

    title = require_text(data.get("title"), "title")
    profile_alias = require_text(data.get("profile_alias"), "profile_alias")
    try:
        cards_per_page = int(data.get("cards_per_page"))
    except (TypeError, ValueError) as exc:
        raise ValueError("cards_per_page must be one of: 1, 2, 4, 8") from exc
    if cards_per_page not in SUPPORTED_LAYOUTS:
        raise ValueError("cards_per_page must be one of: 1, 2, 4, 8")

    cards = data.get("cards")
    if not isinstance(cards, list) or not cards:
        raise ValueError("cards must contain at least one card")

    state_cards = []
    seen_ids = set()
    for card in cards:
        if not isinstance(card, dict):
            raise ValueError("cards[] must contain objects")
        card_id = require_text(card.get("id"), "cards[].id")
        label = require_text(card.get("label"), "cards[].label")
        image_reference = require_text(card.get("image_path"), "cards[].image_path")
        if card_id in seen_ids:
            raise ValueError(f"Duplicate card id: {card_id}")
        seen_ids.add(card_id)
        state_cards.append(
            {
                "id": card_id,
                "label": label,
                "image_reference": image_reference,
            }
        )

    metadata = {
        "title": title,
        "profile_alias": profile_alias,
        "cards_per_page": cards_per_page,
    }
    return metadata, state_cards


def embed_cards(metadata: dict, cards: list[dict], input_directory: Path) -> dict:
    embedded_cards = []
    for card in cards:
        image_path = resolve_image_path(card["image_reference"], input_directory)
        if not image_path.is_file():
            raise FileNotFoundError(
                f"Image file does not exist for card '{card['id']}': {image_path}"
            )

        extension = image_path.suffix.lower()
        if extension not in IMAGE_MIME_TYPES:
            raise ValueError(f"Unsupported image extension: {image_path}")

        encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
        embedded_cards.append(
            {
                "id": card["id"],
                "label": card["label"],
                "image_data": f"data:{IMAGE_MIME_TYPES[extension]};base64,{encoded}",
                "imageTransform": {"scale": 1, "x": 0, "y": 0},
            }
        )

    return {
        **metadata,
        "fontSize": 32,
        "fontFamily": "Noto Sans KR, Arial, sans-serif",
        "cards": embedded_cards,
    }


def build(input_json: str, output_html: str) -> Path:
    input_path = Path(input_json).resolve()
    if not input_path.is_file():
        raise FileNotFoundError(f"Input JSON does not exist: {input_path}")

    output_path = resolve_output_path(output_html)
    if output_path.exists():
        raise FileExistsError(f"Output already exists: {output_path}")
    if not output_path.parent.is_dir():
        raise FileNotFoundError(f"Output directory does not exist: {output_path.parent}")

    template_path = (Path(__file__).resolve().parent / ".." / "assets" / "aac-editor-template.html").resolve()
    if not template_path.is_file():
        raise FileNotFoundError(f"HTML template does not exist: {template_path}")

    metadata, cards = load_cards(input_path)
    state = embed_cards(metadata, cards, input_path.parent)
    state_json = json.dumps(state, ensure_ascii=False, separators=(",", ":"))
    state_json = state_json.replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")

    template = template_path.read_text(encoding="utf-8-sig")
    if template.count(DATA_TOKEN) != 1:
        raise ValueError(f"HTML template must contain exactly one {DATA_TOKEN} token")

    output_path.write_text(template.replace(DATA_TOKEN, state_json), encoding="utf-8", newline="")
    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--InputJson", required=True, help="Path to the card JSON input")
    parser.add_argument("--OutputHtml", required=True, help="Path for the generated HTML")
    args = parser.parse_args()

    try:
        print(build(args.InputJson, args.OutputHtml))
        return 0
    except Exception as exc:  # noqa: BLE001 - CLI should report a concise user-facing error.
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
