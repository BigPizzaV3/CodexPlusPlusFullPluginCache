#!/usr/bin/env python3
"""Calculate Graham revised growth-formula bear/base/bull values."""

import argparse
import json

def graham_value(eps: float, growth_percent: float, aaa_yield_percent: float) -> float:
    if eps <= 0:
        raise ValueError("EPS must be positive")
    if aaa_yield_percent <= 0:
        raise ValueError("AAA yield must be positive")
    return eps * (8.5 + 2 * growth_percent) * 4.4 / aaa_yield_percent

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--eps", type=float, required=True)
    parser.add_argument("--aaa-yield", type=float, required=True)
    parser.add_argument("--bear-growth", type=float, required=True)
    parser.add_argument("--base-growth", type=float, required=True)
    parser.add_argument("--bull-growth", type=float, required=True)
    args = parser.parse_args()
    growths = [args.bear_growth, args.base_growth, args.bull_growth]
    if growths != sorted(growths):
        raise ValueError("Growth assumptions must satisfy bear <= base <= bull")
    values = {
        label: round(graham_value(args.eps, growth, args.aaa_yield), 2)
        for label, growth in zip(("bear", "base", "bull"), growths)
    }
    print(json.dumps(values, sort_keys=True))

if __name__ == "__main__":
    main()
