#!/usr/bin/env python3
"""Normalize multi-horizon return comparisons and benchmark-relative context.

Input JSON shape:
{
  "candidates": [
    {
      "ticker": "ABC",
      "returns_pct": {"1M": 2.0, "3M": 6.0, "6M": 10.0, "YTD": 12.0, "1Y": 15.0},
      "benchmark_returns_pct": {"1M": 1.0, "3M": 4.0, "6M": 8.0, "YTD": 10.0, "1Y": 13.0}
    }
  ]
}

Outputs compound relative returns and, where possible, the preceding 3-month
return implied by 6M and latest-3M returns. Percent inputs/outputs use percentage
points (e.g. 5.2 means 5.2%).
"""

import json
import sys
from pathlib import Path

HORIZONS = ("1M", "3M", "6M", "YTD", "1Y")


def load_payload(path: str) -> dict:
    if path == "-":
        return json.load(sys.stdin)
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle)


def as_decimal(value):
    if value is None:
        return None
    return float(value) / 100.0


def relative_return(candidate_pct, benchmark_pct):
    c = as_decimal(candidate_pct)
    b = as_decimal(benchmark_pct)
    if c is None or b is None:
        return None
    if b <= -1:
        raise ValueError("Benchmark return must be greater than -100%")
    return ((1 + c) / (1 + b) - 1) * 100


def preceding_three_month_return(six_month_pct, latest_three_month_pct):
    six = as_decimal(six_month_pct)
    latest = as_decimal(latest_three_month_pct)
    if six is None or latest is None:
        return None
    if latest <= -1:
        raise ValueError("Latest 3M return must be greater than -100%")
    return ((1 + six) / (1 + latest) - 1) * 100


def process_candidate(candidate: dict) -> dict:
    ticker = candidate.get("ticker")
    if not ticker:
        raise ValueError("Each candidate requires ticker")
    returns = candidate.get("returns_pct", {})
    benchmark = candidate.get("benchmark_returns_pct", {})

    rel = {}
    for horizon in HORIZONS:
        value = relative_return(returns.get(horizon), benchmark.get(horizon))
        if value is not None:
            rel[horizon] = round(value, 2)

    prior_3m = preceding_three_month_return(returns.get("6M"), returns.get("3M"))
    benchmark_prior_3m = preceding_three_month_return(
        benchmark.get("6M"), benchmark.get("3M")
    )

    output = {
        "ticker": ticker,
        "relative_returns_pct": rel,
    }
    if prior_3m is not None:
        output["preceding_3m_return_pct"] = round(prior_3m, 2)
    if benchmark_prior_3m is not None:
        output["benchmark_preceding_3m_return_pct"] = round(benchmark_prior_3m, 2)
    if prior_3m is not None and benchmark_prior_3m is not None:
        output["preceding_3m_relative_return_pct"] = round(
            relative_return(prior_3m, benchmark_prior_3m), 2
        )
    return output


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: return_context.py <returns.json|->")
    payload = load_payload(sys.argv[1])
    candidates = payload.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise ValueError("Payload requires a non-empty candidates list")
    result = {"candidates": [process_candidate(c) for c in candidates]}
    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
