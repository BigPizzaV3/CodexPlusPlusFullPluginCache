#!/usr/bin/env python3
"""Process large transaction JSON from get_address_transactions.

Usage:
    python3 process_transactions.py <file.json> [options]
    python3 process_transactions.py txs.json --stats --top-senders 10
    python3 process_transactions.py txs.json --large-txs 5 --dust-threshold 0.0001
"""

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lukka_notation import load as _load, rows_to_dicts  # noqa: E402


def parse_tx(tx):
    """Normalize a transaction record.

    Lukka UDA ``get_address_transactions`` (verbose=1) returns rows with
    columns: ``value``, ``amount``, ``fee``, ``asset``, ``block``,
    ``time``, ``tx``, ``error``. It does NOT expose sender / recipient -
    those require a per-tx ``Get_transaction_for_txhash`` follow-up.
    Fields below try Lukka keys first, then legacy Etherscan-style names
    for backwards compatibility with non-hosted sources.
    """
    raw_error = tx.get("error") or tx.get("isError") or tx.get("status")
    is_error = raw_error not in (None, "", "_", "0", 0, False) and str(raw_error).lower() not in ("0", "false", "ok", "success", "none")
    return {
        "hash": tx.get("tx") or tx.get("transactionHash") or tx.get("hash") or tx.get("txHash") or "?",
        "block": tx.get("block") or tx.get("blockHeight") or tx.get("blockNumber") or "?",
        "timestamp": tx.get("time") or tx.get("timestamp") or tx.get("blockTimestamp") or "",
        "from": tx.get("from") or tx.get("sender") or tx.get("fromAddress") or "",
        "to": tx.get("to") or tx.get("recipient") or tx.get("toAddress") or "",
        "asset": tx.get("asset") or tx.get("symbol") or "",
        "value": float(tx.get("value") or tx.get("amount") or 0),
        "fee": float(tx.get("fee") or tx.get("gasFee") or 0),
        "is_error": is_error,
        "gas_used": int(tx.get("gasUsed") or tx.get("gas_used") or 0),
    }


def truncate_addr(addr, n=8):
    if not addr or addr == "?" or len(addr) < 16:
        return addr
    return f"{addr[:n]}...{addr[-4:]}"


def print_stats(txs, address, args):
    """Print statistical summary."""
    if not txs:
        print("No transactions found.")
        return

    timestamps = []
    for t in txs:
        if t["timestamp"]:
            try:
                ts = t["timestamp"]
                if isinstance(ts, (int, float)):
                    timestamps.append(datetime.fromtimestamp(ts, tz=timezone.utc).replace(tzinfo=None))
                else:
                    timestamps.append(datetime.fromisoformat(ts.replace("Z", "+00:00").replace("+00:00", "")))
            except (ValueError, OSError):
                pass

    has_counterparty_data = any(t["from"] or t["to"] for t in txs)
    addr_l = address.lower() if address else ""

    total_in = sum(t["value"] for t in txs if t["to"].lower() == addr_l) if addr_l else 0
    total_out = sum(t["value"] for t in txs if t["from"].lower() == addr_l) if addr_l else 0
    total_fee = sum(t.get("fee", 0) for t in txs)
    total_value = sum(t["value"] for t in txs)
    errors = sum(1 for t in txs if t["is_error"])
    dust_thresh = args.dust_threshold or 0.0001
    dust = sum(1 for t in txs if 0 < t["value"] < dust_thresh)

    senders = Counter()
    sender_vol = defaultdict(float)
    recipients = Counter()
    recipient_vol = defaultdict(float)

    if has_counterparty_data and addr_l:
        for t in txs:
            if t["to"] and t["to"].lower() == addr_l:
                senders[t["from"]] += 1
                sender_vol[t["from"]] += t["value"]
            if t["from"] and t["from"].lower() == addr_l:
                recipients[t["to"]] += 1
                recipient_vol[t["to"]] += t["value"]

    all_counterparties = {cp for t in txs for cp in (t["from"], t["to"]) if cp}

    addr_display = truncate_addr(address) if address else "unknown"
    print(f"Transaction Summary for {addr_display}")
    print("=" * 50)
    print(f"Total transactions: {len(txs)}")

    if timestamps:
        ts_sorted = sorted(timestamps)
        days = max((ts_sorted[-1] - ts_sorted[0]).days, 1)
        print(f"Date range:         {ts_sorted[0].strftime('%Y-%m-%d')} - {ts_sorted[-1].strftime('%Y-%m-%d')} ({days} days)")
    if has_counterparty_data and addr_l:
        print(f"Total inflow:       {total_in:.6f}")
        print(f"Total outflow:      -{total_out:.6f}")
        print(f"Net flow:           {'+' if total_in >= total_out else ''}{total_in - total_out:.6f}")
    else:
        # Lukka-UDA verbose=1 responses do not include from/to - directional
        # flow needs Get_transaction_for_txhash follow-ups.
        print(f"Total value moved:  {total_value:.6f}")
        print(f"Total fees paid:    {total_fee:.6f}")
    print(f"Error/reverted:     {errors} ({errors/len(txs)*100:.1f}%)")
    print(f"Dust txs (<{dust_thresh}):  {dust} ({dust/len(txs)*100:.1f}%)")
    if has_counterparty_data:
        print(f"Unique counterparties: {len(all_counterparties)}")
    else:
        print(f"Counterparties:     not in response - use Get_transaction_for_txhash to resolve")

    top_n = args.top_senders or 5
    if senders:
        print(f"\nTop {min(top_n, len(senders))} Senders:")
        for addr_s, count in senders.most_common(top_n):
            print(f"  {truncate_addr(addr_s):20s} {count:4d} txs   {sender_vol[addr_s]:.6f}")

    top_r = args.top_recipients or 5
    if recipients:
        print(f"\nTop {min(top_r, len(recipients))} Recipients:")
        for addr_r, count in recipients.most_common(top_r):
            print(f"  {truncate_addr(addr_r):20s} {count:4d} txs   {recipient_vol[addr_r]:.6f}")

    large_n = args.large_txs or 5
    by_value = sorted(txs, key=lambda t: -t["value"])[:large_n]
    if by_value and by_value[0]["value"] > 0:
        print(f"\nLargest Transactions (decode with Get_transaction_for_txhash):")
        for t in by_value:
            ts_str = t["timestamp"][:10] if t["timestamp"] else "?"
            print(f"  {truncate_addr(t['hash'], 10):18s} {ts_str}   {t['value']:.6f}   block {t['block']}")


def print_csv(txs):
    print("hash,block,timestamp,from,to,value,is_error")
    for t in txs:
        print(f'{t["hash"]},{t["block"]},{t["timestamp"]},{t["from"]},{t["to"]},{t["value"]},{t["is_error"]}')


def main():
    parser = argparse.ArgumentParser(description="Process transaction JSON from get_address_transactions")
    parser.add_argument("file", help="JSON file from get_address_transactions")
    parser.add_argument("--stats", action="store_true", help="Print summary statistics")
    parser.add_argument("--address", help="Target address (auto-detected if possible)")
    parser.add_argument("--top-senders", type=int, help="Top N senders")
    parser.add_argument("--top-recipients", type=int, help="Top N recipients")
    parser.add_argument("--min-value", type=float, help="Min value filter")
    parser.add_argument("--from-date", help="Filter from date (YYYY-MM-DD)")
    parser.add_argument("--to-date", help="Filter to date (YYYY-MM-DD)")
    parser.add_argument("--large-txs", type=int, help="N largest transactions")
    parser.add_argument("--dust-threshold", type=float, default=0.0001, help="Dust threshold (default: 0.0001)")
    parser.add_argument("--format", choices=["table", "csv", "json"], default="table", dest="fmt")
    args = parser.parse_args()

    data = _load(args.file)

    # Handle response shapes
    if isinstance(data, dict):
        records = data.get("data") or data.get("transactions") or data.get("results") or []
        # Lukka compact notation often wraps rows in a {cols, rows} table
        table = rows_to_dicts(records)
        if table is not None:
            records = table
    elif isinstance(data, list):
        records = data
    else:
        print("Error: unexpected JSON shape", file=sys.stderr)
        sys.exit(1)

    txs = [parse_tx(r) for r in records]

    # Auto-detect address from most common to/from
    address = args.address
    if not address and txs:
        all_addrs = Counter(t["to"] for t in txs) + Counter(t["from"] for t in txs)
        address = all_addrs.most_common(1)[0][0] if all_addrs else None

    # Filters
    if args.min_value:
        txs = [t for t in txs if t["value"] >= args.min_value]
    if args.from_date:
        txs = [t for t in txs if t["timestamp"] >= args.from_date]
    if args.to_date:
        txs = [t for t in txs if t["timestamp"] <= args.to_date]

    print(f"# Transactions: {len(txs)} (from {len(records)} total)", file=sys.stderr)

    if args.stats:
        print_stats(txs, address, args)
    elif args.fmt == "csv":
        print_csv(txs)
    elif args.fmt == "json":
        json.dump(txs, sys.stdout, indent=2)
        print()
    else:
        print_stats(txs, address, args)


if __name__ == "__main__":
    main()
