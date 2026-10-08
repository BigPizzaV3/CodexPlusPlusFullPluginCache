#!/usr/bin/env python3
"""Privacy-preserving local telemetry ingestion and aggregation for delivery evidence."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path


ALLOWED = {"app_launch", "navigation", "save_success", "save_failure", "integration_failure", "role_test"}


def main():
    parser = argparse.ArgumentParser(description="Store or summarize privacy-safe app events")
    sub = parser.add_subparsers(dest="command", required=True)
    ingest = sub.add_parser("ingest"); ingest.add_argument("event", type=Path); ingest.add_argument("--store", type=Path, required=True)
    summary = sub.add_parser("summary"); summary.add_argument("--store", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "ingest":
        event = json.loads(args.event.read_text(encoding="utf-8"))
        if event.get("eventType") not in ALLOWED or any(key in event for key in ("token", "password", "prompt", "fieldValue", "email")):
            raise SystemExit("Event rejected by privacy policy")
        safe = {"eventType": event["eventType"], "timestamp": event.get("timestamp", dt.datetime.now(dt.timezone.utc).isoformat()), "role": event.get("role", "unknown"), "feature": event.get("feature", "unknown"), "actorHash": hashlib.sha256(str(event.get("actor", "anonymous")).encode()).hexdigest()[:16]}
        args.store.parent.mkdir(parents=True, exist_ok=True)
        with args.store.open("a", encoding="utf-8") as file: file.write(json.dumps(safe, ensure_ascii=False) + "\n")
        print("accepted")
    else:
        events = [json.loads(line) for line in args.store.read_text(encoding="utf-8").splitlines()] if args.store.exists() else []
        counts = {}
        for event in events: counts[event["eventType"]] = counts.get(event["eventType"], 0) + 1
        print(json.dumps({"events": len(events), "byType": counts}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
