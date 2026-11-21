"""Encode the existing Timely v4 link format using only Python's standard library."""

import base64
from datetime import date, datetime, time, timedelta, timezone
import json
import re
import sys
import unicodedata
from uuid import UUID, uuid4
from zoneinfo import ZoneInfo


THEMES = {"blue", "purple", "green", "orange", "pink"}


def checked_text(value, label, maximum):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a nonempty string")
    value = value.strip()
    if len(value.encode("utf-8")) > maximum:
        raise ValueError(f"{label} exceeds {maximum} UTF-8 bytes")
    if any(unicodedata.category(character) == "Cc" for character in value):
        raise ValueError(f"{label} contains a control character")
    return value


def encode_countdown(fields, now=None):
    if not isinstance(fields, dict):
        raise ValueError("Input must be a JSON object")
    allowed = {"title", "emoji", "theme", "id", "deadline", "allDayDate", "timeZone"}
    unknown = fields.keys() - allowed
    if unknown:
        raise ValueError("Unsupported fields: " + ", ".join(sorted(unknown)))
    now = now or datetime.now(timezone.utc)
    title = checked_text(fields.get("title"), "title", 512)
    emoji = checked_text(fields.get("emoji"), "emoji", 64)
    theme = checked_text(fields.get("theme"), "theme", 64)
    if theme.lower() in THEMES:
        theme = theme.lower()
    else:
        raise ValueError("Choose a stock colour: blue, purple, green, orange, or pink")
    identifier = str(UUID(fields["id"])) if "id" in fields else str(uuid4())
    payload = {"v": 4, "i": identifier, "t": title, "e": emoji, "c": theme}
    exact = "deadline" in fields
    all_day = "allDayDate" in fields
    if exact == all_day:
        raise ValueError("Supply exactly one of deadline or allDayDate")
    if all_day:
        raw_day = fields["allDayDate"]
        if not isinstance(raw_day, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw_day):
            raise ValueError("allDayDate must use YYYY-MM-DD")
        day = date.fromisoformat(raw_day)
        if not isinstance(fields.get("timeZone"), str):
            raise ValueError("An IANA timeZone is required for all-day dates")
        zone = ZoneInfo(fields["timeZone"])
        if day < now.astimezone(zone).date():
            raise ValueError("The all-day countdown has expired")
        deadline = datetime.combine(day, time(12), tzinfo=zone)
        payload.update(p="allDay", a=raw_day)
    else:
        raw_deadline = fields["deadline"]
        if not isinstance(raw_deadline, str) or "T" not in raw_deadline:
            raise ValueError("deadline must be an ISO 8601 timestamp with an offset")
        deadline = datetime.fromisoformat(raw_deadline.replace("Z", "+00:00"))
        if deadline.utcoffset() is None:
            raise ValueError("deadline requires an explicit UTC offset")
        if deadline <= now:
            raise ValueError("The countdown deadline has passed")
        if "timeZone" in fields:
            zone = ZoneInfo(fields["timeZone"])
            if deadline.astimezone(zone).utcoffset() != deadline.utcoffset():
                raise ValueError("deadline offset does not match timeZone at that instant")
    payload["d"] = deadline.timestamp()
    data = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    if len(data) > 768:
        raise ValueError("Payload exceeds 768 bytes; shorten the title")
    encoded = base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")
    url = "https://www.timelycountdown.com/c?data=" + encoded
    if len(url.encode("utf-8")) > 1500:
        raise ValueError("Link exceeds 1500 bytes; shorten the title")
    return {"url": url, "id": identifier, "payload": payload}


def main():
    try:
        result = encode_countdown(json.load(sys.stdin))
    except (ValueError, TypeError, KeyError, OverflowError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
