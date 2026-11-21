#!/usr/bin/env python3
"""Process block data JSON from mcp__Lukka-UDA__UDA___get_block.

Usage:
    python3 process_block.py <file.json> [options]
    python3 process_block.py block.json --stats
    python3 process_block.py block.json --sample 5
    python3 process_block.py blocks.jsonl --range-stats
"""

import argparse
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lukka_notation import loads as _loads  # noqa: E402


def parse_block(block):
    """Normalize block data.

    Lukka-UDA ``get_block`` returns every numeric field as a hex
    string (``0x...``) side-by-side with a ``*_decoded`` integer form,
    plus ``time`` as epoch-millis. Prefer the decoded / epoch fields
    where available; fall back to hex via ``_maybe_int`` and to
    Etherscan-style camelCase keys for non-hosted sources.
    """
    txs = block.get("transactions") or block.get("tx") or block.get("transactionHashes") or []
    tx_count = len(txs) if isinstance(txs, list) else _maybe_int(txs)

    timestamp = _format_timestamp(
        block.get("time")
        or block.get("timestamp")
        or block.get("blockTimestamp")
        or block.get("time_decoded")
    )

    gas_used = _maybe_int(block.get("gas_used_decoded") or block.get("gasUsed") or block.get("gas_used"))
    gas_limit = _maybe_int(block.get("gas_limit_decoded") or block.get("gasLimit") or block.get("gas_limit"))
    gas_pct = (gas_used / gas_limit * 100) if gas_limit > 0 else 0

    base_fee = _maybe_int(
        block.get("base_fee_per_gas_decoded")
        or block.get("baseFeePerGas")
        or block.get("baseFee")
        or block.get("base_fee_per_gas")
    )
    base_fee_gwei = base_fee / 1e9 if base_fee > 1000 else base_fee

    return {
        "number": (
            block.get("blockHeight")
            or block.get("number_decoded")
            or _maybe_int(block.get("number"))
            or block.get("height")
            or "?"
        ),
        "hash": block.get("blockHash") or block.get("hash") or "?",
        "miner": block.get("miner") or block.get("coinbase") or "",
        "timestamp": timestamp,
        "tx_count": tx_count,
        "transactions": txs if isinstance(txs, list) else [],
        "size": _maybe_int(block.get("size_decoded") or block.get("size")),
        "gas_used": gas_used,
        "gas_limit": gas_limit,
        "gas_pct": round(gas_pct, 1),
        "base_fee_gwei": round(base_fee_gwei, 3),
        "blockchain": block.get("blockchain") or block.get("chain") or "?",
    }


def _format_timestamp(value):
    """Render a mixed-format timestamp (epoch ms, epoch s, or ISO string)."""
    if value in (None, "", "_"):
        return ""
    if isinstance(value, (int, float)):
        ts = float(value)
        # Heuristic: Lukka sends epoch milliseconds. Convert to seconds.
        if ts > 10_000_000_000:
            ts /= 1000.0
        try:
            return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        except (ValueError, OSError):
            return str(value)
    s = str(value).strip()
    if s.lower().startswith("0x"):
        try:
            return datetime.fromtimestamp(int(s, 16), tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        except (ValueError, OSError):
            return s
    # Plain numeric string
    try:
        n = float(s)
        if n > 10_000_000_000:
            n /= 1000.0
        return datetime.fromtimestamp(n, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    except ValueError:
        return s


def _maybe_int(value):
    """Coerce to int, tolerating hex strings (Lukka-UDA `get_block` returns hex)."""
    if value is None:
        return 0
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float)):
        return int(value)
    s = str(value).strip()
    if not s:
        return 0
    try:
        return int(s, 16) if s.lower().startswith("0x") else int(s)
    except ValueError:
        return 0


def truncate_hash(h, n=10):
    if not h or h == "?" or len(str(h)) < 16:
        return str(h)
    s = str(h)
    return f"{s[:n]}...{s[-3:]}"


def print_block_stats(block):
    print(f"Block {block['number']} ({block['blockchain']})")
    print("=" * 40)
    print(f"Time:           {block['timestamp']}")
    print(f"Hash:           {truncate_hash(block['hash'], 12)}")
    print(f"Transactions:   {block['tx_count']}")
    if block["size"]:
        print(f"Size:           {block['size']:,} bytes")
    if block["gas_limit"]:
        print(f"Gas Used:       {block['gas_used']:,} / {block['gas_limit']:,} ({block['gas_pct']}%)")
    if block["base_fee_gwei"]:
        print(f"Base Fee:       {block['base_fee_gwei']} Gwei")


def print_sample(block, n):
    txs = block["transactions"]
    if not txs:
        print("No transaction hashes available.")
        return

    # Get hashes (might be strings or objects)
    hashes = []
    for t in txs:
        if isinstance(t, str):
            hashes.append(t)
        elif isinstance(t, dict):
            hashes.append(t.get("hash") or t.get("transactionHash") or str(t))

    sample = random.sample(hashes, min(n, len(hashes)))
    print(f"\nSample tx hashes for decode (--sample {n}):")
    for h in sample:
        print(f"  {truncate_hash(h, 12)}")


def print_range_stats(blocks):
    """Stats across multiple blocks."""
    if not blocks:
        print("No blocks found.")
        return

    total_txs = sum(b["tx_count"] for b in blocks)
    avg_txs = total_txs / len(blocks)
    max_block = max(blocks, key=lambda b: b["tx_count"])
    min_block = min(blocks, key=lambda b: b["tx_count"])

    print(f"Block Range Stats ({len(blocks)} blocks)")
    print("=" * 50)
    print(f"Block range:    {blocks[0]['number']} - {blocks[-1]['number']}")
    print(f"Total txs:      {total_txs:,}")
    print(f"Avg txs/block:  {avg_txs:.1f}")
    print(f"Max txs:        {max_block['tx_count']} (block {max_block['number']})")
    print(f"Min txs:        {min_block['tx_count']} (block {min_block['number']})")

    if blocks[0]["gas_used"]:
        avg_gas = sum(b["gas_pct"] for b in blocks) / len(blocks)
        print(f"Avg gas usage:  {avg_gas:.1f}%")

    if blocks[0]["size"]:
        avg_size = sum(b["size"] for b in blocks) / len(blocks)
        print(f"Avg block size: {avg_size:,.0f} bytes")


def main():
    parser = argparse.ArgumentParser(description="Process block data JSON from mcp__Lukka-UDA__UDA___get_block")
    parser.add_argument("file", help="JSON file (single block) or JSONL (multiple blocks)")
    parser.add_argument("--stats", action="store_true", help="Print block summary")
    parser.add_argument("--sample", type=int, help="Random N tx hashes for decode")
    parser.add_argument("--range-stats", action="store_true", help="Stats across multiple blocks (JSONL)")
    parser.add_argument("--format", choices=["table", "csv", "json"], default="table", dest="fmt")
    args = parser.parse_args()

    path = Path(args.file)
    content = path.read_text().strip()

    # Detect JSONL vs JSON
    blocks = []
    if args.range_stats or path.suffix == ".jsonl":
        for line in content.splitlines():
            line = line.strip()
            if line:
                blocks.append(parse_block(_loads(line)))
    else:
        data = _loads(content)
        if isinstance(data, dict):
            # Could be wrapper or single block
            inner = data.get("data") or data.get("block") or data
            if isinstance(inner, list):
                blocks = [parse_block(b) for b in inner]
            else:
                blocks = [parse_block(inner)]
        elif isinstance(data, list):
            blocks = [parse_block(b) for b in data]

    if not blocks:
        print("No block data found.", file=sys.stderr)
        sys.exit(1)

    print(f"# Blocks: {len(blocks)}", file=sys.stderr)

    if args.range_stats:
        print_range_stats(blocks)
    elif args.fmt == "json":
        json.dump([{"number": b["number"], "tx_count": b["tx_count"], "gas_pct": b["gas_pct"], "timestamp": b["timestamp"]} for b in blocks], sys.stdout, indent=2)
        print()
    else:
        for block in blocks:
            if args.stats or not args.sample:
                print_block_stats(block)
            if args.sample:
                print_sample(block, args.sample)
            if len(blocks) > 1:
                print()


if __name__ == "__main__":
    main()
