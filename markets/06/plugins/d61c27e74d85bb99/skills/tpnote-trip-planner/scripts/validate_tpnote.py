#!/usr/bin/env python3
"""Validate a TPNote portable trip plan using the app's schema invariants."""

from __future__ import annotations

import argparse
import json
import math
import sys
import uuid
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


MAX_FILE_SIZE = 20 * 1024 * 1024
MAX_RECORD_COUNT = 100_000
CURRENT_SCHEMA_VERSION = 6
MINIMUM_SCHEMA_VERSION = 1

ENUMS = {
    "themeID": {"sakura", "ocean", "forest", "sunset", "graphite"},
    "itemType": {"Activity", "Hotel", "Flight", "Train", "Food", "Note", "Payment", "Reminder", "Custom"},
    "status": {"Idea", "Planned", "Booked", "Done", "Skipped"},
    "timelineRole": {"Scheduled Event", "Background Context"},
    "category": {"Hotel", "Food", "Activity", "Transit", "Shopping"},
    "placeProvider": {"Apple Maps", "Google Places", "Manual"},
    "provider": {"Apple Maps", "Google Places", "Manual"},
    "kind": {"Note", "Booking", "Payment", "Reminder"},
    "paymentStatus": {"Planned", "Paid", "Refunded", "Disputed"},
    "detailType": {"Note", "Checklist", "Link", "Confirmation", "Payment", "Weather", "Attachment", "Custom Text"},
    "deliveryStyle": {"Standard", "Time Sensitive"},
    "transportMode": {"Public Transit", "Walking", "Driving", "Cycling", "Flight"},
}

ROOT_ARRAYS = ("days", "items", "notes", "places", "bookings", "moneyEntries", "details")
OPTIONAL_ROOT_ARRAYS = ("reminders", "legs")
RECORD_ARRAYS = ROOT_ARRAYS + OPTIONAL_ROOT_ARRAYS

REQUIRED = {
    "plan": {"id", "title", "destinationSummary", "ownerName", "createdAt", "updatedAt"},
    "days": {"id", "date", "title", "timeZoneIdentifier", "sortIndex", "createdAt", "updatedAt"},
    "items": {
        "id", "dayID", "parentItemID", "placeID", "bookingID", "moneyEntryID", "name", "subtitle",
        "address", "startTime", "endTime", "allDay", "latitude", "longitude", "itemType", "status",
        "category", "placeProvider", "providerPlaceID", "phoneNumber", "websiteURL", "details",
        "confirmation", "amount", "sortIndex", "orderRank", "createdAt", "updatedAt",
    },
    "notes": {"id", "dayID", "parentItemID", "time", "title", "body", "kind", "sortIndex", "orderRank", "createdAt", "updatedAt"},
    "places": {"id", "name", "address", "latitude", "longitude", "provider", "providerPlaceID", "phoneNumber", "websiteURL", "category", "notes", "createdAt", "updatedAt"},
    "bookings": {"id", "itemID", "title", "provider", "confirmationNumber", "contactName", "phoneNumber", "email", "websiteURL", "startsAt", "endsAt", "notes", "createdAt", "updatedAt"},
    "moneyEntries": {"id", "itemID", "title", "amount", "currencyCode", "paymentStatus", "transactionDate", "notes", "createdAt", "updatedAt"},
    "details": {"id", "itemID", "detailType", "title", "body", "value", "orderRank", "createdAt", "updatedAt"},
    "reminders": {"id", "itemID", "minutesBefore", "isEnabled", "deliveryStyle", "createdAt", "updatedAt"},
    "legs": {"id", "dayID", "fromItemID", "toItemID", "transportMode", "createdAt", "updatedAt"},
}

# Swift's synthesized Codable encoder omits nil optionals. Accept both an
# omitted key and an explicit JSON null for portable files from any TPNote build.
OMITTABLE_NULLABLE_FIELDS = {
    "items": {"dayID", "parentItemID", "placeID", "bookingID", "moneyEntryID"},
    "notes": {"parentItemID"},
    "bookings": {"itemID", "startsAt", "endsAt"},
    "moneyEntries": {"itemID"},
    "details": {"itemID"},
}

DATE_FIELDS = {
    "plan": ("createdAt", "updatedAt"),
    "days": ("date", "createdAt", "updatedAt"),
    "items": ("startTime", "endTime", "createdAt", "updatedAt"),
    "notes": ("time", "createdAt", "updatedAt"),
    "places": ("createdAt", "updatedAt"),
    "bookings": ("startsAt", "endsAt", "createdAt", "updatedAt"),
    "moneyEntries": ("transactionDate", "createdAt", "updatedAt"),
    "details": ("createdAt", "updatedAt"),
    "reminders": ("createdAt", "updatedAt"),
    "legs": ("createdAt", "updatedAt"),
}


class Validation:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, path: str, message: str) -> None:
        self.errors.append(f"{path}: {message}")

    def warning(self, path: str, message: str) -> None:
        self.warnings.append(f"{path}: {message}")


def parse_date(value: object, path: str, result: Validation, *, nullable: bool = False) -> datetime | None:
    if value is None and nullable:
        return None
    if not isinstance(value, str):
        result.error(path, "must be an ISO 8601 string")
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        result.error(path, f"invalid ISO 8601 timestamp {value!r}")
        return None


def parse_uuid(value: object, path: str, result: Validation, *, nullable: bool = False) -> str | None:
    if value is None and nullable:
        return None
    if not isinstance(value, str):
        result.error(path, "must be a UUID string")
        return None
    try:
        return str(uuid.UUID(value)).upper()
    except ValueError:
        result.error(path, f"invalid UUID {value!r}")
        return None


def finite_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def require_fields(record: object, kind: str, path: str, result: Validation) -> dict | None:
    if not isinstance(record, dict):
        result.error(path, "must be an object")
        return None
    missing = sorted(
        REQUIRED[kind]
        - OMITTABLE_NULLABLE_FIELDS.get(kind, set())
        - record.keys()
    )
    if missing:
        result.error(path, "missing required fields: " + ", ".join(missing))
    return record


def validate_enum(record: dict, field: str, path: str, result: Validation, *, optional: bool = False) -> None:
    if field not in record and optional:
        return
    value = record.get(field)
    if value is None and optional:
        return
    if value not in ENUMS[field]:
        result.error(f"{path}.{field}", f"unsupported value {value!r}; expected one of {sorted(ENUMS[field])}")


def check_reference(record: dict, field: str, targets: set[str], path: str, result: Validation, *, nullable: bool = False) -> str | None:
    value = parse_uuid(record.get(field), f"{path}.{field}", result, nullable=nullable)
    if value and value not in targets:
        result.error(f"{path}.{field}", f"references missing record {value}")
    return value


def validate_coordinates(record: dict, path: str, result: Validation) -> None:
    latitude = record.get("latitude")
    longitude = record.get("longitude")
    if not finite_number(latitude) or not -90 <= latitude <= 90:
        result.error(f"{path}.latitude", "must be a finite number from -90 through 90")
    if not finite_number(longitude) or not -180 <= longitude <= 180:
        result.error(f"{path}.longitude", "must be a finite number from -180 through 180")


def validate(path: Path, *, app_ready: bool = False) -> Validation:
    result = Validation()
    try:
        size = path.stat().st_size
    except OSError as error:
        result.error(str(path), str(error))
        return result
    if size > MAX_FILE_SIZE:
        result.error("$", f"file is {size} bytes; maximum is {MAX_FILE_SIZE}")
        return result

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        result.error("$", f"cannot read UTF-8 JSON: {error}")
        return result
    if not isinstance(data, dict):
        result.error("$", "root must be an object")
        return result

    if data.get("format") != "tpnote-plan":
        result.error("$.format", "must equal 'tpnote-plan'")
    version = data.get("schemaVersion")
    if not isinstance(version, int) or isinstance(version, bool) or not MINIMUM_SCHEMA_VERSION <= version <= CURRENT_SCHEMA_VERSION:
        result.error("$.schemaVersion", f"must be an integer from {MINIMUM_SCHEMA_VERSION} through {CURRENT_SCHEMA_VERSION}")
    elif version < CURRENT_SCHEMA_VERSION:
        result.warning("$.schemaVersion", f"version {version} is importable, but new files should use {CURRENT_SCHEMA_VERSION}")
    parse_date(data.get("exportedAt"), "$.exportedAt", result)

    plan = require_fields(data.get("plan"), "plan", "$.plan", result)
    if plan:
        if not isinstance(plan.get("title"), str) or not plan["title"].strip():
            result.error("$.plan.title", "must be a nonblank string")
        if "themeID" in plan and plan["themeID"] is not None:
            validate_enum(plan, "themeID", "$.plan", result, optional=True)
        for field in DATE_FIELDS["plan"]:
            parse_date(plan.get(field), f"$.plan.{field}", result)

    arrays: dict[str, list] = {}
    for name in ROOT_ARRAYS:
        value = data.get(name)
        if not isinstance(value, list):
            result.error(f"$.{name}", "must be an array")
            arrays[name] = []
        else:
            arrays[name] = value
    for name in OPTIONAL_ROOT_ARRAYS:
        value = data.get(name, [])
        if value is None:
            value = []
        if not isinstance(value, list):
            result.error(f"$.{name}", "must be an array when present")
            arrays[name] = []
        else:
            arrays[name] = value

    record_count = 1 + sum(len(arrays[name]) for name in RECORD_ARRAYS)
    if record_count > MAX_RECORD_COUNT:
        result.error("$", f"contains {record_count} records; maximum is {MAX_RECORD_COUNT}")

    ids: dict[str, set[str]] = {name: set() for name in RECORD_ARRAYS}
    all_ids: dict[str, str] = {}
    if plan:
        plan_id = parse_uuid(plan.get("id"), "$.plan.id", result)
        if plan_id:
            all_ids[plan_id] = "$.plan.id"

    for kind in RECORD_ARRAYS:
        for index, raw_record in enumerate(arrays[kind]):
            record_path = f"$.{kind}[{index}]"
            record = require_fields(raw_record, kind, record_path, result)
            if not record:
                continue
            record_id = parse_uuid(record.get("id"), f"{record_path}.id", result)
            if record_id:
                if record_id in all_ids:
                    result.error(f"{record_path}.id", f"duplicates {all_ids[record_id]}")
                else:
                    all_ids[record_id] = f"{record_path}.id"
                    ids[kind].add(record_id)
            for field in DATE_FIELDS[kind]:
                parse_date(
                    record.get(field),
                    f"{record_path}.{field}",
                    result,
                    nullable=kind == "bookings" and field in {"startsAt", "endsAt"},
                )

    for index, day in enumerate(arrays["days"]):
        if not isinstance(day, dict):
            continue
        timezone = day.get("timeZoneIdentifier")
        if not isinstance(timezone, str):
            result.error(f"$.days[{index}].timeZoneIdentifier", "must be an IANA time-zone string")
            continue
        try:
            ZoneInfo(timezone)
        except ZoneInfoNotFoundError:
            result.error(f"$.days[{index}].timeZoneIdentifier", f"invalid IANA time zone {timezone!r}")

    parent_by_item: dict[str, str | None] = {}
    item_day: dict[str, str | None] = {}
    places_by_id = {
        str(place.get("id", "")).lower(): place
        for place in arrays["places"] if isinstance(place, dict)
    }
    for index, item in enumerate(arrays["items"]):
        if not isinstance(item, dict):
            continue
        path_prefix = f"$.items[{index}]"
        item_id = parse_uuid(item.get("id"), f"{path_prefix}.id", Validation())
        day_id = check_reference(item, "dayID", ids["days"], path_prefix, result, nullable=True)
        parent_id = check_reference(item, "parentItemID", ids["items"], path_prefix, result, nullable=True)
        check_reference(item, "placeID", ids["places"], path_prefix, result, nullable=True)
        place = places_by_id.get(str(item.get("placeID", "")).lower())
        if place:
            for item_key, place_key in (("latitude", "latitude"), ("longitude", "longitude"),
                                        ("address", "address"), ("phoneNumber", "phoneNumber"),
                                        ("websiteURL", "websiteURL"), ("placeProvider", "provider"),
                                        ("providerPlaceID", "providerPlaceID"), ("googlePlaceID", "googlePlaceID")):
                if (item.get(item_key) or "") != (place.get(place_key) or ""):
                    result.warning(f"{path_prefix}.{item_key}",
                                   "differs from the linked place; copy its canonical location/contact fields. "
                                   "Event category and title may differ, but location identity must agree.")
        subtitle = item.get("subtitle")
        if place and isinstance(subtitle, str) and subtitle.strip():
            place_name = place.get("name")
            if isinstance(place_name, str) and place_name.strip() != subtitle.strip():
                result.warning(f"{path_prefix}.subtitle",
                               "does not match the linked place name; subtitle is a place-name fallback, "
                               "not event or booking context. Preserve descriptive text in details when repairing.")
        check_reference(item, "bookingID", ids["bookings"], path_prefix, result, nullable=True)
        check_reference(item, "moneyEntryID", ids["moneyEntries"], path_prefix, result, nullable=True)
        validate_enum(item, "itemType", path_prefix, result)
        validate_enum(item, "status", path_prefix, result)
        validate_enum(item, "category", path_prefix, result)
        validate_enum(item, "placeProvider", path_prefix, result)
        validate_enum(item, "timelineRole", path_prefix, result, optional=True)
        validate_coordinates(item, path_prefix, result)
        if not finite_number(item.get("orderRank")):
            result.error(f"{path_prefix}.orderRank", "must be a finite number")
        start = parse_date(item.get("startTime"), f"{path_prefix}.startTime", Validation())
        end = parse_date(item.get("endTime"), f"{path_prefix}.endTime", Validation())
        if start and end and end < start:
            result.error(path_prefix, "endTime cannot be earlier than startTime")
        if item_id:
            parent_by_item[item_id] = parent_id
            item_day[item_id] = day_id

    for index, place in enumerate(arrays["places"]):
        if not isinstance(place, dict):
            continue
        path_prefix = f"$.places[{index}]"
        validate_enum(place, "provider", path_prefix, result)
        validate_enum(place, "category", path_prefix, result)
        validate_coordinates(place, path_prefix, result)

    for index, note in enumerate(arrays["notes"]):
        if not isinstance(note, dict):
            continue
        path_prefix = f"$.notes[{index}]"
        check_reference(note, "dayID", ids["days"], path_prefix, result)
        check_reference(note, "parentItemID", ids["items"], path_prefix, result, nullable=True)
        validate_enum(note, "kind", path_prefix, result)
        if not finite_number(note.get("orderRank")):
            result.error(f"{path_prefix}.orderRank", "must be a finite number")

    for kind in ("bookings", "moneyEntries", "details"):
        for index, record in enumerate(arrays[kind]):
            if not isinstance(record, dict):
                continue
            path_prefix = f"$.{kind}[{index}]"
            check_reference(record, "itemID", ids["items"], path_prefix, result, nullable=True)
            if kind == "moneyEntries":
                validate_enum(record, "paymentStatus", path_prefix, result)
            if kind == "details":
                validate_enum(record, "detailType", path_prefix, result)
                if not finite_number(record.get("orderRank")):
                    result.error(f"{path_prefix}.orderRank", "must be a finite number")

    for index, reminder in enumerate(arrays["reminders"]):
        if not isinstance(reminder, dict):
            continue
        path_prefix = f"$.reminders[{index}]"
        check_reference(reminder, "itemID", ids["items"], path_prefix, result)
        validate_enum(reminder, "deliveryStyle", path_prefix, result)
        minutes = reminder.get("minutesBefore")
        if not isinstance(minutes, int) or isinstance(minutes, bool) or minutes < 0:
            result.error(f"{path_prefix}.minutesBefore", "must be a nonnegative integer")

    for index, leg in enumerate(arrays["legs"]):
        if not isinstance(leg, dict):
            continue
        path_prefix = f"$.legs[{index}]"
        day_id = check_reference(leg, "dayID", ids["days"], path_prefix, result)
        from_id = check_reference(leg, "fromItemID", ids["items"], path_prefix, result)
        to_id = check_reference(leg, "toItemID", ids["items"], path_prefix, result)
        validate_enum(leg, "transportMode", path_prefix, result)
        if from_id and to_id and from_id == to_id:
            result.warning(path_prefix, "fromItemID and toItemID are the same")
        for endpoint, item_id in (("fromItemID", from_id), ("toItemID", to_id)):
            if day_id and item_id and item_day.get(item_id) not in {None, day_id}:
                result.warning(f"{path_prefix}.{endpoint}", "item belongs to a different day")

    for item_id in parent_by_item:
        visited: set[str] = set()
        current: str | None = item_id
        while current:
            if current in visited:
                result.error(all_ids.get(item_id, "$.items"), "parentItemID chain contains a cycle")
                break
            visited.add(current)
            current = parent_by_item.get(current)

    if app_ready:
        audit_app_ready(data, arrays, result)

    return result


def audit_app_ready(data: dict, arrays: dict[str, list], result: Validation) -> None:
    """Apply the stronger quality contract used for finished plugin output."""
    places = {
        str(place.get("id", "")).upper(): place
        for place in arrays["places"] if isinstance(place, dict)
    }
    items = {
        str(item.get("id", "")).upper(): item
        for item in arrays["items"] if isinstance(item, dict)
    }
    bookings = {
        str(booking.get("id", "")).upper(): booking
        for booking in arrays["bookings"] if isinstance(booking, dict)
    }

    for index, place in enumerate(arrays["places"]):
        if not isinstance(place, dict):
            continue
        path_prefix = f"$.places[{index}]"
        if not isinstance(place.get("name"), str) or not place["name"].strip():
            result.error(f"{path_prefix}.name", "app-ready places need a recognizable nonblank name")
        if not isinstance(place.get("address"), str) or not place["address"].strip():
            result.error(f"{path_prefix}.address", "app-ready places need a complete readable address")
        if not str(place.get("providerPlaceID") or "").strip() and not str(place.get("googlePlaceID") or "").strip():
            result.warning(
                path_prefix,
                "has no trusted provider identity; keep verified name/address/coordinates and disclose that "
                "TPNote will attempt Google Places enrichment after import",
            )

    for index, item in enumerate(arrays["items"]):
        if not isinstance(item, dict):
            continue
        path_prefix = f"$.items[{index}]"
        is_scheduled = item.get("timelineRole", "Scheduled Event") == "Scheduled Event"
        needs_place = item.get("itemType") in {"Activity", "Hotel", "Flight", "Train", "Food"}
        place_id = str(item.get("placeID") or "").upper()
        if is_scheduled and needs_place and not place_id:
            result.error(
                f"{path_prefix}.placeID",
                "app-ready in-person events must link to a canonical place",
            )
        if place_id and place_id in places:
            place = places[place_id]
            if not str(item.get("address") or "").strip():
                result.error(f"{path_prefix}.address", "linked event needs the canonical place address snapshot")
            if not str(item.get("subtitle") or "").strip():
                result.error(f"{path_prefix}.subtitle", "linked event needs the canonical place name as its subtitle")

        booking_id = str(item.get("bookingID") or "").upper()
        if booking_id and booking_id in bookings:
            linked_item_id = str(bookings[booking_id].get("itemID") or "").upper()
            if linked_item_id != str(item.get("id") or "").upper():
                result.error(
                    f"{path_prefix}.bookingID",
                    "booking relationship must be reciprocal through bookings[].itemID",
                )
        if item.get("status") == "Booked" and not booking_id:
            result.warning(
                f"{path_prefix}.bookingID",
                "booked event has no booking record; store user-provided reservation facts in bookings, not event prose",
            )

    for index, booking in enumerate(arrays["bookings"]):
        if not isinstance(booking, dict):
            continue
        path_prefix = f"$.bookings[{index}]"
        item_id = str(booking.get("itemID") or "").upper()
        if item_id and item_id in items:
            linked_booking_id = str(items[item_id].get("bookingID") or "").upper()
            if linked_booking_id != str(booking.get("id") or "").upper():
                result.error(
                    f"{path_prefix}.itemID",
                    "booking relationship must be reciprocal through items[].bookingID",
                )

    leg_pairs = {
        (str(leg.get("fromItemID") or "").upper(), str(leg.get("toItemID") or "").upper())
        for leg in arrays["legs"] if isinstance(leg, dict)
    }
    for day in arrays["days"]:
        if not isinstance(day, dict):
            continue
        day_id = str(day.get("id") or "").upper()
        scheduled = [
            item for item in arrays["items"]
            if isinstance(item, dict)
            and str(item.get("dayID") or "").upper() == day_id
            and item.get("timelineRole", "Scheduled Event") == "Scheduled Event"
        ]
        scheduled.sort(key=lambda item: (
            str(item.get("startTime") or ""),
            float(item.get("orderRank") or 0),
            int(item.get("sortIndex") or 0),
        ))
        for earlier, later in zip(scheduled, scheduled[1:]):
            earlier_place = str(earlier.get("placeID") or "").upper()
            later_place = str(later.get("placeID") or "").upper()
            if not earlier_place or not later_place or earlier_place == later_place:
                continue
            pair = (
                str(earlier.get("id") or "").upper(),
                str(later.get("id") or "").upper(),
            )
            if pair not in leg_pairs:
                result.error(
                    "$.legs",
                    f"missing commute leg from {earlier.get('name')!r} to {later.get('name')!r}",
                )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help=".tpnote files to validate")
    parser.add_argument(
        "--app-ready",
        action="store_true",
        help="also require polished places, reciprocal bookings, and commute coverage",
    )
    args = parser.parse_args()
    failed = False
    for path in args.files:
        result = validate(path, app_ready=args.app_ready)
        for warning in result.warnings:
            print(f"WARNING {warning}")
        for error in result.errors:
            print(f"ERROR {error}")
        if result.errors:
            failed = True
            label = "APP-READY INVALID" if args.app_ready else "INVALID"
            print(f"{label} {path} ({len(result.errors)} error(s), {len(result.warnings)} warning(s))")
        else:
            label = "APP-READY" if args.app_ready else "VALID"
            print(f"{label} {path} ({len(result.warnings)} warning(s))")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
