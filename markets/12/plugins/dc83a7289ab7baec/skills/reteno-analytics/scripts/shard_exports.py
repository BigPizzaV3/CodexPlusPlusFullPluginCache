#!/usr/bin/env python3
"""Plan inclusive organization-local date shards and summarize additive message exports."""
from __future__ import annotations

import argparse
import csv
from datetime import date, timedelta
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))
from transfer import atomic_write


def days_between(start, end):
    first, last = date.fromisoformat(start), date.fromisoformat(end)
    if first > last or (last - first).days > 3660:
        raise ValueError("Date range must be ordered and at most ten years")
    return [first + timedelta(days=offset) for offset in range((last - first).days + 1)]


def plan(start, end, shard_days=1):
    if not 1 <= shard_days <= 366:
        raise ValueError("Shard days must be 1..366")
    days = days_between(start, end)
    return {"dateFrom": start, "dateTo": end, "dateSemantics": "inclusive organization-local days",
            "shards": [{"dateFrom": days[offset].isoformat(),
                        "dateTo": days[min(offset + shard_days - 1, len(days) - 1)].isoformat(),
                        "status": "pending"} for offset in range(0, len(days), shard_days)]}


def summarize(manifest, directory):
    requested = set(days_between(manifest["dateFrom"], manifest["dateTo"]))
    covered, complete, ids = set(), set(), set()
    sends, rows, failed = 0, 0, []
    for shard in manifest["shards"]:
        days = set(days_between(shard["dateFrom"], shard["dateTo"]))
        if days & covered or not days <= requested:
            raise ValueError("Shards overlap or extend beyond the requested window")
        covered |= days
        if shard.get("status") != "complete":
            failed.append({"dateFrom": shard["dateFrom"], "dateTo": shard["dateTo"],
                           "reason": shard.get("error", "not completed")})
            continue
        source = directory / shard["path"]
        with source.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            fields = reader.fieldnames or []
            metric = "sent" if "sent" in fields else "sends" if "sends" in fields else None
            if not metric or "message_id" not in fields:
                raise ValueError("Message export needs message_id and sent/sends columns")
            for row in reader:
                if None in row or row.get(metric) is None:
                    raise ValueError("Malformed CSV row")
                value = row[metric].strip()
                if not value.isdecimal():
                    raise ValueError("Send counts must be nonnegative integers")
                sends += int(value)
                rows += 1
                message_id = row["message_id"].strip()
                if message_id:
                    ids.add(message_id)
        complete |= days
    missing = sorted(day.isoformat() for day in requested - covered)
    return {"complete": complete == requested, "partial": complete != requested,
            "dateFrom": manifest["dateFrom"], "dateTo": manifest["dateTo"],
            "uniqueMessageIds": len(ids), "sends": sends, "rows": rows,
            "completedDates": sorted(day.isoformat() for day in complete),
            "failedShards": failed, "missingDates": missing}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    planner = commands.add_parser("plan")
    planner.add_argument("--from", dest="start", required=True)
    planner.add_argument("--to", dest="end", required=True)
    planner.add_argument("--days", type=int, default=1)
    planner.add_argument("--output", type=Path, required=True)
    summarizer = commands.add_parser("summarize")
    summarizer.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "plan":
            value = plan(args.start, args.end, args.days)
            atomic_write(args.output, (json.dumps(value, indent=2) + "\n").encode())
        else:
            value = summarize(json.loads(args.manifest.read_text()), args.manifest.parent)
        print(json.dumps(value))
    except (ValueError, OSError, KeyError, TypeError) as exc:
        parser.exit(1, f"Export recovery failed: {exc}\n")


if __name__ == "__main__":
    main()
