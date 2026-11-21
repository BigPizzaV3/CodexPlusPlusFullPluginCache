#!/usr/bin/env python3
"""Convert returned fixture timestamps into dated local start times."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


TIMESTAMP_PATTERN = re.compile(
    r"\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2}"
    r"(?:\.\d{1,6})?(?:Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)?"
)


def parse_gmt_timestamp(value: str) -> datetime:
    if not TIMESTAMP_PATTERN.fullmatch(value):
        raise ValueError("Expected a complete ISO calendar date and time.")

    timestamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
    # CricketData's GMT field also carries UTC timestamps without an offset.
    if timestamp.tzinfo is None:
        timestamp = timestamp.replace(tzinfo=timezone.utc)
    return timestamp.astimezone(timezone.utc)


def load_time_zones(names: list[str]) -> list[ZoneInfo]:
    zones = []
    for name in dict.fromkeys(names):
        try:
            zones.append(ZoneInfo(name))
        except (ZoneInfoNotFoundError, ValueError) as error:
            raise ValueError(f"Unknown or unavailable IANA time zone: {name}") from error
    return zones


def convert_fixture(fixture: dict, zones: list[ZoneInfo]) -> dict:
    result = {
        "id": fixture.get("id"),
        "name": fixture.get("name"),
        "date": fixture.get("date"),
        "dateTimeGmt": fixture.get("dateTimeGmt"),
        "timingStatus": "missing",
        "utcStart": None,
        "localStarts": [],
    }
    source = fixture.get("dateTimeGmt")
    if source is None or (isinstance(source, str) and not source.strip()):
        result["reason"] = "No start timestamp was supplied."
        return result
    if not isinstance(source, str):
        result.update(timingStatus="invalid", reason="Start timestamp must be a string.")
        return result

    try:
        utc_start = parse_gmt_timestamp(source.strip())
        local_starts = []
        for zone in zones:
            local_start = utc_start.astimezone(zone)
            local_starts.append(
                {
                    "timeZone": zone.key,
                    "dateTime": local_start.isoformat(),
                    "abbreviation": local_start.tzname(),
                    "dateShiftDays": (local_start.date() - utc_start.date()).days,
                }
            )
    except (ValueError, OverflowError) as error:
        result.update(timingStatus="invalid", reason=str(error))
        return result

    result.update(
        timingStatus="known",
        utcStart=utc_start.isoformat().replace("+00:00", "Z"),
        localStarts=local_starts,
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="JSON fixture array")
    parser.add_argument(
        "--timezone", required=True, action="append", help="Destination IANA time zone"
    )
    args = parser.parse_args()

    try:
        zones = load_time_zones(args.timezone)
        fixtures = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(fixtures, list) or any(
            not isinstance(fixture, dict) for fixture in fixtures
        ):
            raise ValueError("Input must be a JSON array of fixture objects.")
    except (OSError, ValueError) as error:
        parser.error(str(error))

    print(json.dumps([convert_fixture(fixture, zones) for fixture in fixtures], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
