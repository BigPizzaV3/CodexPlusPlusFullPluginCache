#!/usr/bin/env python3
"""Process large market depth JSON from get_market_depth (6.8MB+).

Usage:
    python3 process_market_depth.py <file.json> [options]
    python3 process_market_depth.py depth.json --top 20
    python3 process_market_depth.py depth.json --pair SOLN-USD
    python3 process_market_depth.py depth.json --top 50 --min-depth 50000 --sort spread
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lukka_notation import load as _load  # noqa: E402


def parse_depth_record(rec):
    """Extract depth metrics from a single market depth record."""
    pair = rec.get("pairCode") or f'{rec.get("baseAssetCode", "?")}-{rec.get("counterAssetCode", "?")}'
    source = rec.get("entityName") or rec.get("sourceName") or rec.get("sourceId") or "?"

    # Lukka nests depth fields under meanDepth; flat shape also supported.
    mean = rec.get("meanDepth") if isinstance(rec.get("meanDepth"), dict) else rec

    bids_1 = float(mean.get("bids_1") or mean.get("bids1") or 0)
    asks_1 = float(mean.get("asks_1") or mean.get("asks1") or 0)
    total_depth = bids_1 + asks_1

    best_bid = float(rec.get("lastBestBidPrice") or rec.get("bestBid") or rec.get("best_bid") or 0)
    best_ask = float(rec.get("lastBestAskPrice") or rec.get("bestAsk") or rec.get("best_ask") or 0)
    mid = float(rec.get("lastMidPrice") or ((best_bid + best_ask) / 2 if (best_bid and best_ask) else 0))
    spread_bps = ((best_ask - best_bid) / mid * 10000) if mid > 0 else 0

    # bids_1/asks_1 are depth in BASE-ASSET units (e.g. XBT), NOT USD.
    # Multiply by mid price to get a USD-notional figure.
    return {
        "exchange": source,
        "pair": pair,
        "bid_1pct": bids_1,            # base-asset units
        "ask_1pct": asks_1,            # base-asset units
        "total_depth": total_depth,    # base-asset units
        "total_depth_usd": total_depth * mid if mid > 0 else 0,
        "spread_bps": round(spread_bps, 2),
        "mid_price": round(mid, 6),
    }


def format_usd(val):
    if val >= 1_000_000:
        return f"${val/1_000_000:.2f}M"
    if val >= 1_000:
        return f"${val/1_000:.1f}K"
    return f"${val:.2f}"


def fmt_base(val):
    # base-asset units (NOT USD) - no $ sign
    if val >= 1_000_000:
        return f"{val/1_000_000:.2f}M"
    if val >= 1_000:
        return f"{val/1_000:.1f}K"
    return f"{val:.4f}"


def print_table(rows):
    headers = ["Exchange", "Pair", "Bid 1% (base)", "Ask 1% (base)", "Depth (base)", "Depth ~USD", "Spread bps", "Mid Price"]
    lines = [headers]
    for r in rows:
        lines.append([
            str(r["exchange"])[:20],
            r["pair"],
            fmt_base(r["bid_1pct"]),
            fmt_base(r["ask_1pct"]),
            fmt_base(r["total_depth"]),
            format_usd(r["total_depth_usd"]),
            f'{r["spread_bps"]:.1f}',
            f'${r["mid_price"]:,.6f}' if r["mid_price"] < 1 else f'${r["mid_price"]:,.2f}',
        ])

    widths = [max(len(row[i]) for row in lines) for i in range(len(headers))]
    sep = " | ".join("-" * w for w in widths)

    for idx, row in enumerate(lines):
        print(" | ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)))
        if idx == 0:
            print(sep)


def print_csv(rows):
    print("exchange,pair,bid_1pct_base,ask_1pct_base,total_depth_base,total_depth_usd,spread_bps,mid_price")
    for r in rows:
        print(f'{r["exchange"]},{r["pair"]},{r["bid_1pct"]},{r["ask_1pct"]},{r["total_depth"]},{r["total_depth_usd"]:.2f},{r["spread_bps"]},{r["mid_price"]}')


def main():
    parser = argparse.ArgumentParser(description="Process market depth JSON from get_market_depth")
    parser.add_argument("file", help="JSON file from get_market_depth")
    parser.add_argument("--pair", help="Filter specific pair (e.g. SOLN-USD)")
    parser.add_argument("--top", type=int, help="Top N pairs by depth")
    parser.add_argument("--min-depth", type=float, default=0, help="Min total depth USD")
    parser.add_argument("--sort", choices=["depth", "spread", "volume"], default="depth", help="Sort by (default: depth)")
    parser.add_argument("--format", choices=["table", "csv", "json"], default="table", dest="fmt")
    args = parser.parse_args()

    data = _load(args.file)

    # Handle various response shapes
    if isinstance(data, dict):
        records = data.get("data") or data.get("results") or data.get("depth") or []
        if not records and any(k for k in data if k not in ("pagination", "size", "meta")):
            records = [data]
    elif isinstance(data, list):
        records = data
    else:
        print("Error: unexpected JSON shape", file=sys.stderr)
        sys.exit(1)

    rows = [parse_depth_record(r) for r in records]

    # Filters
    if args.pair:
        pair_upper = args.pair.upper()
        rows = [r for r in rows if r["pair"].upper() == pair_upper]

    if args.min_depth > 0:
        rows = [r for r in rows if r["total_depth"] >= args.min_depth]

    # Sort
    sort_key = {
        "depth": lambda r: -r["total_depth"],
        "spread": lambda r: r["spread_bps"],
        "volume": lambda r: -r["total_depth"],
    }[args.sort]
    rows.sort(key=sort_key)

    if args.top:
        rows = rows[:args.top]

    print(f"# Market Depth: {len(rows)} pairs (from {len(records)} total)", file=sys.stderr)

    if args.fmt == "table":
        print_table(rows)
    elif args.fmt == "csv":
        print_csv(rows)
    else:
        json.dump(rows, sys.stdout, indent=2)
        print()


if __name__ == "__main__":
    main()
