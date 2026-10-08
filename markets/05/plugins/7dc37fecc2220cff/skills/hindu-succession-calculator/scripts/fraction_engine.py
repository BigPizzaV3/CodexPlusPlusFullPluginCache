#!/usr/bin/env python3
"""Exact recursive share allocator for a legally classified statutory unit tree."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
from pathlib import Path
from typing import Any


class InputError(ValueError):
    pass


def parse_fraction(value: Any, field: str) -> Fraction:
    if isinstance(value, bool):
        raise InputError(f"{field} must be a positive number or fraction")
    try:
        result = Fraction(str(value))
    except (ValueError, ZeroDivisionError) as exc:
        raise InputError(f"{field} is not a valid number or fraction: {value!r}") from exc
    if result <= 0:
        raise InputError(f"{field} must be greater than zero")
    return result


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def percentage_text(value: Fraction) -> str:
    percent = (Decimal(value.numerator) * Decimal(100) / Decimal(value.denominator)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
    return f"{percent:.2f}%"


def money_text(value: Fraction, whole_asset_value: Fraction) -> str:
    amount = value * whole_asset_value
    decimal_amount = (Decimal(amount.numerator) / Decimal(amount.denominator)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
    return f"{decimal_amount:.2f}"


def validate_node(node: Any, seen_ids: set[str], path: str) -> None:
    if not isinstance(node, dict):
        raise InputError(f"{path} must be an object")
    node_id = node.get("id")
    if not isinstance(node_id, str) or not node_id.strip():
        raise InputError(f"{path}.id must be a non-empty string")
    if node_id in seen_ids:
        raise InputError(f"duplicate node id: {node_id}")
    seen_ids.add(node_id)

    has_beneficiary = "beneficiary_id" in node
    has_children = "children" in node
    if has_beneficiary == has_children:
        raise InputError(f"{path} must contain exactly one of beneficiary_id or children")

    if has_beneficiary:
        beneficiary_id = node["beneficiary_id"]
        if not isinstance(beneficiary_id, str) or not beneficiary_id.strip():
            raise InputError(f"{path}.beneficiary_id must be a non-empty string")
        return

    children = node["children"]
    if not isinstance(children, list) or not children:
        raise InputError(f"{path}.children must be a non-empty array")
    for index, child in enumerate(children):
        validate_node(child, seen_ids, f"{path}.children[{index}]")


def allocate_node(
    node: dict[str, Any],
    share: Fraction,
    trail: list[str],
    totals: dict[str, Fraction],
    labels: dict[str, str],
    trace: list[dict[str, str]],
) -> None:
    node_label = str(node.get("label") or node["id"])
    current_trail = [*trail, node_label]
    if "beneficiary_id" in node:
        beneficiary_id = node["beneficiary_id"]
        totals[beneficiary_id] += share
        labels.setdefault(beneficiary_id, str(node.get("beneficiary_label") or node_label))
        trace.append(
            {
                "path": " > ".join(current_trail),
                "beneficiary_id": beneficiary_id,
                "allocated_share": fraction_text(share),
            }
        )
        return

    children = node["children"]
    child_share = share / len(children)
    for child in children:
        allocate_node(child, child_share, current_trail, totals, labels, trace)


def calculate(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise InputError("input must be a JSON object")
    estate_share = parse_fraction(payload.get("estate_share", "1"), "estate_share")
    units = payload.get("units")
    if not isinstance(units, list) or not units:
        raise InputError("units must be a non-empty array")

    seen_ids: set[str] = set()
    for index, unit in enumerate(units):
        validate_node(unit, seen_ids, f"units[{index}]")

    whole_asset_value = None
    if payload.get("whole_asset_value") is not None:
        whole_asset_value = parse_fraction(payload["whole_asset_value"], "whole_asset_value")

    totals: dict[str, Fraction] = defaultdict(Fraction)
    labels: dict[str, str] = {}
    trace: list[dict[str, str]] = []
    top_share = estate_share / len(units)
    for unit in units:
        allocate_node(unit, top_share, [], totals, labels, trace)

    distributed = sum(totals.values(), Fraction(0))
    if distributed != estate_share:
        raise RuntimeError(
            f"share conservation failed: distributed {fraction_text(distributed)}, "
            f"expected {fraction_text(estate_share)}"
        )

    beneficiaries = []
    for beneficiary_id in sorted(totals):
        share = totals[beneficiary_id]
        item = {
            "beneficiary_id": beneficiary_id,
            "label": labels[beneficiary_id],
            "share": fraction_text(share),
            "percentage_of_whole": percentage_text(share),
        }
        if whole_asset_value is not None:
            item["value"] = money_text(share, whole_asset_value)
        beneficiaries.append(item)

    result = {
        "status": "CALCULATED",
        "estate_share": fraction_text(estate_share),
        "top_level_unit_count": len(units),
        "beneficiaries": beneficiaries,
        "conservation": {
            "distributed": fraction_text(distributed),
            "expected": fraction_text(estate_share),
            "pass": True,
        },
        "trace": trace,
    }
    if whole_asset_value is not None:
        result["whole_asset_value"] = fraction_text(whole_asset_value)
    return result


def load_payload(input_path: str | None) -> dict[str, Any]:
    if input_path:
        return json.loads(Path(input_path).read_text(encoding="utf-8"))
    return json.load(sys.stdin)


def run_self_test() -> None:
    cases = [
        (
            {
                "units": [
                    {"id": "w", "beneficiary_id": "W"},
                    {"id": "s", "beneficiary_id": "S"},
                    {"id": "d", "beneficiary_id": "D"},
                ]
            },
            {"W": "1/3", "S": "1/3", "D": "1/3"},
        ),
        (
            {
                "units": [
                    {
                        "id": "widow_group",
                        "children": [
                            {"id": "w1", "beneficiary_id": "W1"},
                            {"id": "w2", "beneficiary_id": "W2"},
                        ],
                    },
                    {"id": "son", "beneficiary_id": "S"},
                ]
            },
            {"W1": "1/4", "W2": "1/4", "S": "1/2"},
        ),
        (
            {
                "estate_share": "1/2",
                "units": [
                    {"id": "widow", "beneficiary_id": "W"},
                    {
                        "id": "predeceased_son_branch",
                        "children": [
                            {"id": "gs", "beneficiary_id": "GS"},
                            {"id": "gd", "beneficiary_id": "GD"},
                        ],
                    },
                ],
            },
            {"W": "1/4", "GS": "1/8", "GD": "1/8"},
        ),
    ]
    for payload, expected in cases:
        result = calculate(payload)
        actual = {item["beneficiary_id"]: item["share"] for item in result["beneficiaries"]}
        if actual != expected:
            raise AssertionError(f"expected {expected}, got {actual}")
    print(f"self-test passed: {len(cases)} cases")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", help="JSON input file; omit to read standard input")
    parser.add_argument("--self-test", action="store_true", help="run built-in tests")
    args = parser.parse_args()

    try:
        if args.self_test:
            run_self_test()
            return 0
        result = calculate(load_payload(args.input))
        json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
        return 0
    except (InputError, json.JSONDecodeError, OSError) as exc:
        print(f"input error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
