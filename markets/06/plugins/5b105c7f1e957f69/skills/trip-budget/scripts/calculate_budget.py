#!/usr/bin/env python3
"""Validate and reconcile a travel budget JSON file without dependencies."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path


CENT = Decimal("0.01")


def decimal_value(value: object, field: str, *, nullable: bool = False) -> Decimal | None:
    if value is None and nullable:
        return None
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"{field} must be numeric") from exc
    if not result.is_finite():
        raise ValueError(f"{field} must be finite")
    return result


def money(value: Decimal) -> str:
    return str(value.quantize(CENT, rounding=ROUND_HALF_UP))


def calculate(data: dict) -> dict:
    travelers = int(data.get("travelers", 1))
    if travelers < 1:
        raise ValueError("travelers must be at least 1")
    base_currency = str(data.get("base_currency") or data.get("currency") or "USD").upper()
    target = decimal_value(data.get("target"), "target", nullable=True)
    if target is not None and target < 0:
        raise ValueError("target cannot be negative")
    contingency_rate = decimal_value(data.get("contingency_rate", 0), "contingency_rate")
    if contingency_rate is None or contingency_rate < 0:
        raise ValueError("contingency_rate cannot be negative")

    categories: dict[str, Decimal] = defaultdict(Decimal)
    status_totals: dict[str, Decimal] = defaultdict(Decimal)
    normalized = []
    eligible_subtotal = Decimal("0")

    for index, item in enumerate(data.get("items", []), start=1):
        quantity = decimal_value(item.get("quantity", 1), f"items[{index}].quantity")
        unit_cost = decimal_value(item.get("unit_cost"), f"items[{index}].unit_cost")
        if quantity is None or unit_cost is None or quantity < 0 or unit_cost < 0:
            raise ValueError(f"items[{index}] quantity and unit_cost cannot be negative")
        item_currency = str(item.get("currency", base_currency)).upper()
        if item_currency == base_currency:
            fx_rate = Decimal("1")
        else:
            fx_rate = decimal_value(item.get("fx_rate"), f"items[{index}].fx_rate")
            if fx_rate is None or fx_rate <= 0:
                raise ValueError(f"items[{index}] requires a positive fx_rate from {item_currency} to {base_currency}")
            if not item.get("fx_rate_date"):
                raise ValueError(f"items[{index}] requires fx_rate_date")

        original_amount = quantity * unit_cost
        base_amount = original_amount * fx_rate
        status = "excluded" if item.get("excluded", False) else "optional" if item.get("optional", False) else "included"
        status_totals[status] += base_amount
        category = str(item.get("category", "uncategorized"))
        if status == "included":
            categories[category] += base_amount
            if item.get("contingency_eligible", True):
                eligible_subtotal += base_amount
        normalized.append({
            "index": index,
            "description": item.get("description", ""),
            "category": category,
            "status": status,
            "quantity": str(quantity),
            "unit_cost": str(unit_cost),
            "original_currency": item_currency,
            "original_amount": money(original_amount),
            "fx_rate": str(fx_rate),
            "base_amount": money(base_amount),
            "contingency_eligible": bool(item.get("contingency_eligible", True)),
        })

    subtotal = status_totals["included"]
    contingency = eligible_subtotal * contingency_rate
    total = subtotal + contingency
    if target is None:
        variance = None
        variance_status = "target_not_provided"
    else:
        variance_value = target - total
        variance = money(variance_value)
        variance_status = "under_target" if variance_value > 0 else "over_target" if variance_value < 0 else "on_target"

    return {
        "base_currency": base_currency,
        "travelers": travelers,
        "categories": {key: money(value) for key, value in sorted(categories.items())},
        "status_totals": {key: money(status_totals[key]) for key in ("included", "optional", "excluded")},
        "items": normalized,
        "subtotal": money(subtotal),
        "contingency_eligible_subtotal": money(eligible_subtotal),
        "contingency_rate": str(contingency_rate),
        "contingency": money(contingency),
        "total": money(total),
        "per_person": money(total / travelers),
        "target": money(target) if target is not None else None,
        "target_variance": variance,
        "target_status": variance_status,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate and reconcile a travel budget JSON file")
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = calculate(json.loads(args.input.read_text(encoding="utf-8")))
    rendered = json.dumps(result, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
