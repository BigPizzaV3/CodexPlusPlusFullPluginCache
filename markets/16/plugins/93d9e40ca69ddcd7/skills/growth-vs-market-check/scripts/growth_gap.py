#!/usr/bin/env python3
"""Compare internal revenue growth with market growth and flag over-optimistic rows.

Internal CSV:   segment,country,year,revenue,type      (type: actual | forecast)
Market CSV:     segment,country,year,market_revenue    (same segment names as the internal file)

Usage:
    python growth_gap.py --internal internal.csv --market market.csv [--gap-threshold 5] [--run-gap 3] [--run-years 3] [--out results.md]

Growth is year on year. Gap = revenue growth minus market growth, in percentage points.
Implied share = revenue / market_revenue; share change is in percentage points versus the prior year.

Flags (raised on forecast rows only):
    above-threshold   gap above --gap-threshold in that year
    sustained-gap     gap above --run-gap in --run-years consecutive years ending in that year (actual years count towards the run)
"""

import argparse
import csv
import sys
from collections import defaultdict


def read(path, value_col):
    data = defaultdict(dict)
    types = {}
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        needed = {"segment", "country", "year", value_col}
        missing = needed - set(reader.fieldnames or [])
        if missing:
            sys.exit(f"{path}: missing columns {sorted(missing)}")
        for row in reader:
            key = (row["segment"].strip(), row["country"].strip())
            try:
                year = int(row["year"])
                value = float(row[value_col])
            except ValueError:
                continue
            data[key][year] = value
            if "type" in row and row["type"]:
                types[(key, year)] = row["type"].strip().lower()
    return data, types


def growth(series, year):
    prev = series.get(year - 1)
    cur = series.get(year)
    if prev in (None, 0) or cur is None:
        return None
    return (cur / prev - 1) * 100


def pct(value, digits=1):
    return "" if value is None else f"{value:.{digits}f}%"


def pp(value, digits=1):
    return "" if value is None else f"{value:+.{digits}f}"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--internal", required=True)
    parser.add_argument("--market", required=True)
    parser.add_argument("--gap-threshold", type=float, default=5.0, help="percentage points, single-year flag")
    parser.add_argument("--run-gap", type=float, default=3.0, help="percentage points, sustained-gap flag")
    parser.add_argument("--run-years", type=int, default=3, help="consecutive years for the sustained-gap flag")
    parser.add_argument("--out")
    args = parser.parse_args()

    internal, types = read(args.internal, "revenue")
    market, _ = read(args.market, "market_revenue")

    lines = ["| Segment | Country | Year | Type | Revenue growth | Market growth | Gap (pp) | Implied share | Share change (pp) | Flag |",
             "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    missing = []
    flagged = 0

    for key in sorted(internal):
        if key not in market:
            missing.append(key)
            continue
        years = sorted(internal[key])
        gaps = {}
        for year in years:
            g_int = growth(internal[key], year)
            g_mkt = growth(market[key], year)
            gaps[year] = None if g_int is None or g_mkt is None else g_int - g_mkt
        run = 0
        for year in years:
            g_int = growth(internal[key], year)
            g_mkt = growth(market[key], year)
            gap = gaps[year]
            row_type = types.get((key, year), "")
            mkt_value = market[key].get(year)
            share = None if not mkt_value else internal[key][year] / mkt_value * 100
            prev_mkt = market[key].get(year - 1)
            prev_share = None if not prev_mkt or (year - 1) not in internal[key] else internal[key][year - 1] / prev_mkt * 100
            share_change = None if share is None or prev_share is None else share - prev_share

            flags = []
            if gap is not None and gap > args.run_gap:
                run += 1
            else:
                run = 0
            if row_type == "forecast" and gap is not None and gap > args.gap_threshold:
                flags.append("above-threshold")
            if row_type == "forecast" and run >= args.run_years:
                flags.append("sustained-gap")
            if flags:
                flagged += 1
            lines.append(f"| {key[0]} | {key[1]} | {year} | {row_type} | {pct(g_int)} | {pct(g_mkt)} | {pp(gap)} | {pct(share, 2)} | {pp(share_change, 2)} | {', '.join(flags)} |")

    if missing:
        lines += ["", "No market series found for:"] + [f"- {s} / {c}" for s, c in missing]

    text = "\n".join(lines) + "\n"
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(text)
        print(f"wrote {args.out}: {flagged} flagged rows, {len(missing)} pairs without market data")
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
