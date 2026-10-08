#!/usr/bin/env python3
"""Create a structurally sanitized TPNote template copy for human privacy review."""

from __future__ import annotations

import argparse
import json
import re
import uuid
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

from validate_tpnote import validate


RECORD_ARRAYS = (
    "days", "items", "notes", "places", "bookings", "moneyEntries", "details", "reminders", "legs"
)
REFERENCE_FIELDS = {
    "dayID", "parentItemID", "placeID", "bookingID", "moneyEntryID", "itemID", "fromItemID", "toItemID"
}
PRIVATE_DETAIL_TYPES = {"Confirmation", "Payment", "Attachment"}
SENSITIVE_PATTERNS = (
    re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    re.compile(r"\b(?:\d[ -]?){8,}\b"),
    re.compile(r"\b(?:home|my house|residence|apartment|traveler|passenger)\b", re.IGNORECASE),
)


def sanitize(data: dict, *, keep_reminders: bool = False) -> tuple[dict, list[str]]:
    output = deepcopy(data)
    warnings: list[str] = []

    records = [output["plan"]]
    for array_name in RECORD_ARRAYS:
        records.extend(output.get(array_name, []))
    id_map = {
        record["id"]: str(uuid.uuid4()).upper()
        for record in records
        if isinstance(record, dict) and isinstance(record.get("id"), str)
    }

    for record in records:
        if not isinstance(record, dict):
            continue
        if record.get("id") in id_map:
            record["id"] = id_map[record["id"]]
        for field in REFERENCE_FIELDS:
            value = record.get(field)
            if value in id_map:
                record[field] = id_map[value]

    output["plan"]["ownerName"] = "Traveler"
    output["exportedAt"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    for item in output.get("items", []):
        item["confirmation"] = ""
        item["amount"] = ""
        item["moneyEntryID"] = None

    for booking in output.get("bookings", []):
        booking["confirmationNumber"] = ""
        booking["contactName"] = ""
        booking["phoneNumber"] = ""
        booking["email"] = ""
        booking["notes"] = ""

    output["moneyEntries"] = []
    output["details"] = [
        detail for detail in output.get("details", [])
        if detail.get("detailType") not in PRIVATE_DETAIL_TYPES
    ]
    if not keep_reminders:
        output["reminders"] = []

    for array_name in ("items", "notes", "places", "details"):
        for index, record in enumerate(output.get(array_name, [])):
            if not isinstance(record, dict):
                continue
            for field, value in record.items():
                if not isinstance(value, str) or not value.strip():
                    continue
                if any(pattern.search(value) for pattern in SENSITIVE_PATTERNS):
                    warnings.append(
                        f"{array_name}[{index}].{field} may contain personal information; review it semantically"
                    )

    return output, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", nargs="?", type=Path)
    parser.add_argument("--keep-reminders", action="store_true")
    args = parser.parse_args()

    output_path = args.output or args.source.with_name(f"{args.source.stem}-template.tpnote")
    data = json.loads(args.source.read_text(encoding="utf-8"))
    sanitized, warnings = sanitize(data, keep_reminders=args.keep_reminders)
    output_path.write_text(json.dumps(sanitized, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    validation = validate(output_path)
    for warning in warnings + validation.warnings:
        print(f"WARNING {warning}")
    for error in validation.errors:
        print(f"ERROR {error}")
    if validation.errors:
        print(f"INVALID {output_path}")
        return 1
    print(f"CREATED {output_path}")
    print("Human review is still required for free-text notes, residential locations, and traveler-specific events.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
