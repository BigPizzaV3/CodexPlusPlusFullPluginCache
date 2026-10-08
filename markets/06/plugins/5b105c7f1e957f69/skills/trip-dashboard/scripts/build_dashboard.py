#!/usr/bin/env python3
"""Build a standalone trip dashboard from validated JSON data."""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from urllib.parse import urlparse


MARKER = "__TRIP_DATA_JSON__"
REQUIRED_ARRAYS = (
    "assumptions", "fixed_costs", "hotels", "activities", "restaurants",
    "transport", "days", "sources",
)
VALID_STATUSES = {"observed", "estimated", "included", "optional", "excluded", "confirmed", "lead-only"}


def require_text(record: dict, field: str, path: str) -> str:
    value = record.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{path}.{field} must be non-empty text")
    return value.strip()


def require_amount(value: object, path: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{path} must be numeric")
    number = float(value)
    if not math.isfinite(number) or number < 0:
        raise ValueError(f"{path} must be finite and nonnegative")
    return number


def validate_url(value: object, path: str, *, required: bool = False) -> None:
    if value in (None, "") and not required:
        return
    if not isinstance(value, str):
        raise ValueError(f"{path} must be a URL")
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"{path} must use http or https")


def validate_text_list(value: object, path: str, *, required: bool = False) -> None:
    if value is None and not required:
        return
    if not isinstance(value, list) or (required and not value):
        raise ValueError(f"{path} must be {'a non-empty ' if required else 'an '}array")
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f"{path}[{index}] must be non-empty text")


def validate_images(value: object, path: str) -> None:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{path} must be a non-empty image array")
    for index, image in enumerate(value):
        ipath = f"{path}[{index}]"
        if not isinstance(image, dict):
            raise ValueError(f"{ipath} must be an object")
        validate_url(image.get("url"), f"{ipath}.url", required=True)
        require_text(image, "alt", ipath)
        require_text(image, "credit", ipath)
        validate_url(image.get("source_url"), f"{ipath}.source_url", required=True)


def validate(data: dict) -> dict:
    if not isinstance(data, dict):
        raise ValueError("dashboard input must be an object")
    meta = data.get("meta")
    if not isinstance(meta, dict):
        raise ValueError("meta must be an object")
    for field in ("title", "currency", "route", "researched_at"):
        require_text(meta, field, "meta")
    if not re.fullmatch(r"[A-Z]{3}", meta["currency"]):
        raise ValueError("meta.currency must be a three-letter uppercase code")
    travelers = meta.get("travelers")
    trip_days = meta.get("trip_days")
    if not isinstance(travelers, int) or travelers < 1:
        raise ValueError("meta.travelers must be a positive integer")
    if not isinstance(trip_days, int) or trip_days < 1:
        raise ValueError("meta.trip_days must be a positive integer")
    if meta.get("target") is not None:
        require_amount(meta["target"], "meta.target")
    canonical_total = require_amount(meta.get("canonical_total"), "meta.canonical_total")
    contingency_rate = require_amount(meta.get("contingency_rate"), "meta.contingency_rate")
    if contingency_rate > 0.5:
        raise ValueError("meta.contingency_rate cannot exceed 0.5")

    for key in REQUIRED_ARRAYS:
        if not isinstance(data.get(key), list):
            raise ValueError(f"{key} must be an array")

    ids: set[str] = set()
    for i, item in enumerate(data["assumptions"]):
        path = f"assumptions[{i}]"
        item_id = require_text(item, "id", path)
        if item_id in ids:
            raise ValueError(f"duplicate id: {item_id}")
        ids.add(item_id)
        for field in ("label", "category", "status"):
            require_text(item, field, path)
        for field in ("value", "min", "max", "step"):
            require_amount(item.get(field), f"{path}.{field}")
        if item["min"] > item["value"] or item["value"] > item["max"] or item["step"] <= 0:
            raise ValueError(f"{path} min/value/max/step are inconsistent")

    for i, item in enumerate(data["fixed_costs"]):
        path = f"fixed_costs[{i}]"
        for field in ("label", "category", "status"):
            require_text(item, field, path)
        require_amount(item.get("amount"), f"{path}.amount")

    bases: set[str] = set()
    for i, stay in enumerate(data["hotels"]):
        path = f"hotels[{i}]"
        base = require_text(stay, "base", path)
        if base in bases:
            raise ValueError(f"duplicate hotel base: {base}")
        bases.add(base)
        options = stay.get("options")
        if not isinstance(options, list) or not options:
            raise ValueError(f"{path}.options must be a non-empty array")
        selected = 0
        for j, option in enumerate(options):
            opath = f"{path}.options[{j}]"
            option_id = require_text(option, "id", opath)
            if option_id in ids:
                raise ValueError(f"duplicate id: {option_id}")
            ids.add(option_id)
            for field in ("name", "location", "description", "why_fit"):
                require_text(option, field, opath)
            require_amount(option.get("amount"), f"{opath}.amount")
            require_amount(option.get("nights"), f"{opath}.nights")
            if not isinstance(option.get("selected"), bool):
                raise ValueError(f"{opath}.selected must be Boolean")
            selected += int(option["selected"])
            validate_url(option.get("url"), f"{opath}.url")
            validate_images(option.get("images"), f"{opath}.images")
            for field in ("amenities", "pros", "cautions"):
                validate_text_list(option.get(field), f"{opath}.{field}")
        if selected != 1:
            raise ValueError(f"{path} must have exactly one selected option")

    for i, activity in enumerate(data["activities"]):
        path = f"activities[{i}]"
        activity_id = require_text(activity, "id", path)
        if activity_id in ids:
            raise ValueError(f"duplicate id: {activity_id}")
        ids.add(activity_id)
        for field in ("name", "day", "source_type", "description", "why_fit"):
            require_text(activity, field, path)
        require_amount(activity.get("amount"), f"{path}.amount")
        if not isinstance(activity.get("selected"), bool):
            raise ValueError(f"{path}.selected must be Boolean")
        validate_url(activity.get("url"), f"{path}.url")
        validate_url(activity.get("direct_url"), f"{path}.direct_url")
        validate_images(activity.get("images"), f"{path}.images")
        for field in ("includes", "pros", "cautions"):
            validate_text_list(activity.get(field), f"{path}.{field}")

    for i, restaurant in enumerate(data["restaurants"]):
        path = f"restaurants[{i}]"
        restaurant_id = require_text(restaurant, "id", path)
        if restaurant_id in ids:
            raise ValueError(f"duplicate id: {restaurant_id}")
        ids.add(restaurant_id)
        for field in ("name", "location", "cuisine", "description", "why_fit"):
            require_text(restaurant, field, path)
        require_amount(restaurant.get("amount", 0), f"{path}.amount")
        if not isinstance(restaurant.get("selected"), bool):
            raise ValueError(f"{path}.selected must be Boolean")
        if restaurant.get("budget_mode", "included") not in {"included", "additive"}:
            raise ValueError(f"{path}.budget_mode must be included or additive")
        validate_url(restaurant.get("url"), f"{path}.url")
        validate_images(restaurant.get("images"), f"{path}.images")
        for field in ("signature_dishes", "dietary", "pros", "cautions"):
            validate_text_list(restaurant.get(field), f"{path}.{field}")

    for i, leg in enumerate(data["transport"]):
        path = f"transport[{i}]"
        require_text(leg, "leg", path)
        options = leg.get("options")
        if not isinstance(options, list) or not options:
            raise ValueError(f"{path}.options must be a non-empty array")
        selected = 0
        for j, option in enumerate(options):
            opath = f"{path}.options[{j}]"
            option_id = require_text(option, "id", opath)
            if option_id in ids:
                raise ValueError(f"duplicate id: {option_id}")
            ids.add(option_id)
            for field in ("name", "mode", "description", "why_fit"):
                require_text(option, field, opath)
            require_amount(option.get("amount"), f"{opath}.amount")
            if not isinstance(option.get("selected"), bool):
                raise ValueError(f"{opath}.selected must be Boolean")
            selected += int(option["selected"])
            validate_url(option.get("url"), f"{opath}.url")
            validate_images(option.get("images"), f"{opath}.images")
            for field in ("pros", "cautions"):
                validate_text_list(option.get(field), f"{opath}.{field}")
        if selected != 1:
            raise ValueError(f"{path} must have exactly one selected option")

    for i, day in enumerate(data["days"]):
        path = f"days[{i}]"
        for field in ("label", "date", "base", "morning", "afternoon", "evening", "transit", "notes"):
            require_text(day, field, path)
        commitments = day.get("commitments")
        if not isinstance(commitments, int) or commitments < 0:
            raise ValueError(f"{path}.commitments must be a nonnegative integer")

    for i, source in enumerate(data["sources"]):
        path = f"sources[{i}]"
        for field in ("label", "type", "checked_at"):
            require_text(source, field, path)
        validate_url(source.get("url"), f"{path}.url", required=True)
    subtotal = sum(float(item["value"]) for item in data["assumptions"])
    subtotal += sum(float(item["amount"]) for item in data["fixed_costs"] if item["status"] in {"included", "observed", "estimated"})
    subtotal += sum(float(option["amount"]) for stay in data["hotels"] for option in stay["options"] if option["selected"])
    subtotal += sum(float(item["amount"]) for item in data["activities"] if item["selected"])
    subtotal += sum(
        float(item.get("amount", 0)) for item in data["restaurants"]
        if item["selected"] and item.get("budget_mode", "included") == "additive"
    )
    subtotal += sum(
        float(option["amount"]) for leg in data["transport"]
        for option in leg["options"] if option["selected"]
    )
    computed_total = round(subtotal * (1 + contingency_rate), 2)
    if abs(computed_total - canonical_total) > 0.005:
        raise ValueError(f"dashboard total {computed_total:.2f} does not match meta.canonical_total {canonical_total:.2f}")
    return data


def build(data_path: Path, output_path: Path, template_path: Path | None = None) -> Path:
    if template_path is None:
        template_path = Path(__file__).resolve().parents[1] / "assets" / "trip-dashboard-template.html"
    data = validate(json.loads(data_path.read_text(encoding="utf-8")))
    template = template_path.read_text(encoding="utf-8")
    if template.count(MARKER) != 1:
        raise ValueError(f"template must contain exactly one {MARKER} marker")
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(template.replace(MARKER, payload), encoding="utf-8")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a validated interactive trip dashboard")
    parser.add_argument("input", type=Path, help="Trip dashboard JSON")
    parser.add_argument("output", type=Path, help="Standalone HTML output")
    parser.add_argument("--template", type=Path)
    args = parser.parse_args()
    print(build(args.input, args.output, args.template))


if __name__ == "__main__":
    main()
