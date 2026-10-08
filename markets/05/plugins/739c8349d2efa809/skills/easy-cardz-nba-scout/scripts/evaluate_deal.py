#!/usr/bin/env python3
"""Calculate NBA card deal economics and a conservative Buy/Watch/Pass result."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any


REQUIRED = ("listing_price", "estimated_resale")
LIQUIDITY_VALUES = {"high", "medium", "low", "unknown"}


def number(data: dict[str, Any], key: str, default: float = 0.0) -> float:
    value = data.get(key, default)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{key} must be a number")
    value = float(value)
    if not math.isfinite(value):
        raise ValueError(f"{key} must be finite")
    return value


def evaluate(data: dict[str, Any]) -> dict[str, Any]:
    missing = [key for key in REQUIRED if key not in data]
    if missing:
        raise ValueError(f"missing required fields: {', '.join(missing)}")

    listing_price = number(data, "listing_price")
    buyer_fee_rate = number(data, "buyer_fee_rate")
    buyer_fee_fixed = number(data, "buyer_fee_fixed")
    inbound_shipping = number(data, "inbound_shipping")
    import_cost = number(data, "import_cost")
    estimated_resale = number(data, "estimated_resale")
    seller_fee_rate = number(data, "seller_fee_rate", 0.0)
    seller_fee_fixed = number(data, "seller_fee_fixed")
    outbound_shipping = number(data, "outbound_shipping")
    other_sale_cost = number(data, "other_sale_cost")
    min_profit = number(data, "min_profit", 0.0)
    min_roi = number(data, "min_roi", 0.20)
    min_total_cost = number(data, "min_total_cost", 10.0)
    max_total_cost_limit = number(data, "max_total_cost", 250.0)
    confidence = number(data, "comp_confidence", 0.0)
    liquidity = str(data.get("liquidity", "unknown")).lower()

    nonnegative = {
        "listing_price": listing_price,
        "buyer_fee_rate": buyer_fee_rate,
        "buyer_fee_fixed": buyer_fee_fixed,
        "inbound_shipping": inbound_shipping,
        "import_cost": import_cost,
        "estimated_resale": estimated_resale,
        "seller_fee_rate": seller_fee_rate,
        "seller_fee_fixed": seller_fee_fixed,
        "outbound_shipping": outbound_shipping,
        "other_sale_cost": other_sale_cost,
        "min_profit": min_profit,
        "min_roi": min_roi,
        "min_total_cost": min_total_cost,
        "max_total_cost": max_total_cost_limit,
    }
    for key, value in nonnegative.items():
        if value < 0:
            raise ValueError(f"{key} must be non-negative")
    if seller_fee_rate >= 1:
        raise ValueError("seller_fee_rate must be below 1")
    if confidence < 0 or confidence > 1:
        raise ValueError("comp_confidence must be between 0 and 1")
    if liquidity not in LIQUIDITY_VALUES:
        raise ValueError(f"liquidity must be one of {sorted(LIQUIDITY_VALUES)}")

    fixed_buy_costs = buyer_fee_fixed + inbound_shipping + import_cost
    buyer_fee = listing_price * buyer_fee_rate + buyer_fee_fixed
    all_in = listing_price + buyer_fee + inbound_shipping + import_cost

    seller_fee = estimated_resale * seller_fee_rate + seller_fee_fixed
    resale_net = estimated_resale - seller_fee - outbound_shipping - other_sale_cost
    profit = resale_net - all_in
    roi = profit / all_in if all_in > 0 else None

    max_cost_profit = resale_net - min_profit
    max_cost_roi = resale_net / (1 + min_roi)
    permitted_all_in = min(max_cost_profit, max_cost_roi, max_total_cost_limit)
    max_listing_price = (permitted_all_in - fixed_buy_costs) / (1 + buyer_fee_rate)
    max_listing_price = max(0.0, max_listing_price)

    in_budget = min_total_cost <= all_in <= max_total_cost_limit
    financial_pass = profit >= min_profit and roi is not None and roi >= min_roi
    evidence_pass = liquidity in {"high", "medium"} and confidence >= 0.75

    if in_budget and financial_pass and evidence_pass:
        decision = "BUY"
    elif (
        in_budget
        and confidence >= 0.5
        and liquidity != "unknown"
        and (
            financial_pass
            or (max_listing_price > 0 and listing_price <= max_listing_price * 1.10)
        )
    ):
        decision = "WATCH"
    else:
        decision = "PASS"

    warnings: list[str] = []
    if not in_budget:
        warnings.append("All-in cost is outside the configured EUR 10-250 range.")
    if liquidity in {"low", "unknown"}:
        warnings.append("Liquidity is insufficient for a fast-flip Buy recommendation.")
    if confidence < 0.75:
        warnings.append("Comp confidence is below the Buy threshold of 0.75.")
    if not financial_pass:
        warnings.append("The deal misses the configured profit or ROI threshold.")

    def rounded(value: float | None) -> float | None:
        return None if value is None else round(value, 2)

    return {
        "currency": "EUR",
        "listing_price": rounded(listing_price),
        "buyer_fee": rounded(buyer_fee),
        "all_in_cost": rounded(all_in),
        "estimated_resale": rounded(estimated_resale),
        "seller_fee": rounded(seller_fee),
        "resale_net": rounded(resale_net),
        "expected_profit": rounded(profit),
        "expected_roi_pct": rounded(roi * 100 if roi is not None else None),
        "max_all_in_cost": rounded(max(0.0, permitted_all_in)),
        "max_listing_price": rounded(max_listing_price),
        "liquidity": liquidity,
        "comp_confidence": rounded(confidence),
        "decision": decision,
        "warnings": warnings,
    }


def load_input(source: str) -> dict[str, Any]:
    if source == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(source).read_text(encoding="utf-8")
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("input JSON must be an object")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", default="-", help="JSON file or - for stdin")
    args = parser.parse_args()
    try:
        result = evaluate(load_input(args.source))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
