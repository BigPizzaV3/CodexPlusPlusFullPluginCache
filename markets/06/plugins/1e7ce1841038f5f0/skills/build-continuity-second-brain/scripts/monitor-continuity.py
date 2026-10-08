#!/usr/bin/env python3
"""Compare an approved continuity inventory with a current workspace.

The script is read-only with respect to the monitored root. It never follows
symlinks and reads file contents only when --hash is explicitly selected. It
writes reports only to explicit --json or --markdown paths; otherwise JSON is
printed to stdout. Detected deltas are review items, not approved updates.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


def load_inventory_module():
    module_path = Path(__file__).with_name("inventory-continuity.py")
    spec = importlib.util.spec_from_file_location("continuity_inventory", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load inventory helper: {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamp requires timezone")
    return parsed.astimezone(timezone.utc)


def compare_files(baseline: dict, current: dict) -> list[dict]:
    baseline_files = {item["path"]: item for item in baseline.get("files", [])}
    current_files = {item["path"]: item for item in current.get("files", [])}
    rows: list[dict] = []

    for path in sorted(baseline_files.keys() | current_files.keys()):
        before = baseline_files.get(path)
        after = current_files.get(path)
        if before is None:
            status = "NEW"
            method = "path absent from baseline"
        elif after is None:
            status = "REMOVED_OR_INACCESSIBLE"
            method = "path absent from current observation"
        else:
            before_hash = before.get("sha256")
            after_hash = after.get("sha256")
            if before_hash and after_hash:
                status = "UNCHANGED" if before_hash == after_hash else "CHANGED"
                method = "sha256"
            elif before.get("size_bytes") == after.get("size_bytes") and before.get("modified_utc") == after.get(
                "modified_utc"
            ):
                status = "UNCHANGED"
                method = "size and modified timestamp"
            else:
                status = "POSSIBLY_CHANGED"
                method = "metadata only; hash proof unavailable"
        rows.append(
            {
                "path": path,
                "status": status,
                "comparison_method": method,
                "baseline": before,
                "current": after,
                "requires_review": status != "UNCHANGED",
            }
        )
    return rows


def compare_symlinks(baseline: dict, current: dict) -> list[dict]:
    key = lambda item: (item.get("path"), item.get("kind"))
    before = {key(item): item for item in baseline.get("symlinks", [])}
    after = {key(item): item for item in current.get("symlinks", [])}
    rows: list[dict] = []
    for item_key in sorted(before.keys() | after.keys()):
        old = before.get(item_key)
        new = after.get(item_key)
        if old is None:
            status = "NEW"
        elif new is None:
            status = "REMOVED_OR_INACCESSIBLE"
        elif old.get("target") != new.get("target"):
            status = "CHANGED"
        else:
            status = "UNCHANGED"
        rows.append(
            {
                "path": item_key[0],
                "kind": item_key[1],
                "status": status,
                "baseline_target": old.get("target") if old else None,
                "current_target": new.get("target") if new else None,
                "requires_review": status != "UNCHANGED",
            }
        )
    return rows


def evaluate_freshness(records: list[dict], now: datetime) -> list[dict]:
    results: list[dict] = []
    for record in records:
        record_id = record.get("id") or record.get("record_id") or "UNKNOWN"
        try:
            verified = parse_timestamp(str(record["last_verified"]))
            max_age_days = int(record["max_age_days"])
            warning_days = int(record.get("warning_days", min(7, max_age_days)))
            if max_age_days < 0 or warning_days < 0:
                raise ValueError("age thresholds must be non-negative")
            due = verified + timedelta(days=max_age_days)
            warning = due - timedelta(days=warning_days)
            if now >= due:
                state = "STALE"
            elif now >= warning:
                state = "DUE_SOON"
            else:
                state = "CURRENT"
            results.append(
                {
                    "id": record_id,
                    "state": state,
                    "last_verified": verified.isoformat(),
                    "due_utc": due.isoformat(),
                    "owner": record.get("owner"),
                    "criticality": record.get("criticality"),
                    "error": None,
                }
            )
        except (KeyError, TypeError, ValueError) as exc:
            results.append(
                {
                    "id": record_id,
                    "state": "INVALID",
                    "last_verified": record.get("last_verified"),
                    "due_utc": None,
                    "owner": record.get("owner"),
                    "criticality": record.get("criticality"),
                    "error": str(exc),
                }
            )
    return results


def build_report(baseline: dict, current: dict, freshness: list[dict], generated: datetime) -> dict:
    file_deltas = compare_files(baseline, current)
    symlink_deltas = compare_symlinks(baseline, current)
    counts: dict[str, int] = {}
    for item in file_deltas + symlink_deltas:
        counts[item["status"]] = counts.get(item["status"], 0) + 1
    freshness_counts: dict[str, int] = {}
    for item in freshness:
        freshness_counts[item["state"]] = freshness_counts.get(item["state"], 0) + 1
    review_count = sum(1 for item in file_deltas + symlink_deltas if item["requires_review"])
    review_count += sum(1 for item in freshness if item["state"] != "CURRENT")
    return {
        "schema": "continuity-monitor-report-v1",
        "generated_utc": generated.isoformat(),
        "baseline_generated_utc": baseline.get("generated_utc"),
        "root_name": current.get("root_name"),
        "interpretation_boundary": "Detected deltas require review and do not update the approved baseline.",
        "summary": {
            "file_and_symlink_status_counts": counts,
            "freshness_status_counts": freshness_counts,
            "review_items": review_count,
            "current_scan_errors": current.get("summary", {}).get("errors", 0),
        },
        "file_deltas": file_deltas,
        "symlink_deltas": symlink_deltas,
        "freshness": freshness,
        "current_inventory": current,
    }


def markdown_report(data: dict) -> str:
    lines = [
        "# Continuity monitoring report",
        "",
        f"- Generated: {data['generated_utc']}",
        f"- Baseline: {data.get('baseline_generated_utc') or 'unknown'}",
        f"- Root: `{data.get('root_name') or 'unknown'}`",
        f"- Review items: {data['summary']['review_items']}",
        f"- Boundary: {data['interpretation_boundary']}",
        "",
        "## Detected file changes",
        "",
        "| Path | Status | Comparison |",
        "|---|---|---|",
    ]
    for item in data["file_deltas"]:
        if item["requires_review"]:
            lines.append(f"| `{item['path']}` | {item['status']} | {item['comparison_method']} |")
    if not any(item["requires_review"] for item in data["file_deltas"]):
        lines.append("| — | No file delta detected | — |")

    lines.extend(["", "## Detected symlink changes", ""])
    changed_links = [item for item in data["symlink_deltas"] if item["requires_review"]]
    if changed_links:
        for item in changed_links:
            lines.append(
                f"- `{item['path']}`: {item['status']} "
                f"(`{item.get('baseline_target')}` → `{item.get('current_target')}`)"
            )
    else:
        lines.append("- None")

    lines.extend(["", "## Freshness review", "", "| Record | State | Due UTC | Owner | Error |", "|---|---|---|---|---|"])
    if data["freshness"]:
        for item in data["freshness"]:
            lines.append(
                f"| {item['id']} | {item['state']} | {item.get('due_utc') or '—'} | "
                f"{item.get('owner') or '—'} | {item.get('error') or '—'} |"
            )
    else:
        lines.append("| — | No freshness register supplied | — | — | — |")
    lines.extend(["", "## Required action", "", "Review every non-unchanged or non-current item before reconciling controlled records.", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Detect continuity workspace drift without applying changes")
    parser.add_argument("baseline", type=Path, help="Approved inventory JSON produced by inventory-continuity.py")
    parser.add_argument("root", type=Path, help="Current workspace root to observe")
    parser.add_argument("--freshness-json", type=Path, help="JSON list or {'records': [...]} with freshness controls")
    parser.add_argument("--json", dest="json_path", type=Path)
    parser.add_argument("--markdown", dest="markdown_path", type=Path)
    parser.add_argument("--hash", action="store_true", help="Read regular files and calculate SHA-256 for stronger proof")
    parser.add_argument("--max-hash-bytes", type=int, default=100_000_000)
    parser.add_argument("--exclude", action="append", default=[], help="Additional exact name to skip")
    args = parser.parse_args()

    baseline = load_json(args.baseline)
    if baseline.get("schema") != "continuity-inventory-v1":
        raise ValueError("Baseline must use schema continuity-inventory-v1")

    inventory_module = load_inventory_module()
    current = inventory_module.inventory(
        args.root,
        args.hash,
        args.max_hash_bytes,
        inventory_module.DEFAULT_EXCLUDES | set(args.exclude),
        False,
    )
    freshness_records: list[dict] = []
    if args.freshness_json:
        raw = load_json(args.freshness_json)
        freshness_records = raw.get("records", []) if isinstance(raw, dict) else raw
        if not isinstance(freshness_records, list):
            raise ValueError("Freshness JSON must be a list or an object containing a records list")

    now = datetime.now(timezone.utc)
    report = build_report(baseline, current, evaluate_freshness(freshness_records, now), now)
    json_text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.json_path:
        args.json_path.parent.mkdir(parents=True, exist_ok=True)
        args.json_path.write_text(json_text, encoding="utf-8")
    if args.markdown_path:
        args.markdown_path.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_path.write_text(markdown_report(report), encoding="utf-8")
    if not args.json_path and not args.markdown_path:
        print(json_text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
