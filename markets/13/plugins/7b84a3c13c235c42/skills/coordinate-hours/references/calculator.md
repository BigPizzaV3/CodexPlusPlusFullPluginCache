# Overlap calculator

Requires Python 3.9+ and a host IANA time-zone database (`zoneinfo`). Run bundled `../scripts/overlap.py` with one UTF-8 JSON file path. Use safe argument passing. The calculator reads the file, prints JSON, makes no network calls, and writes no files. Failure produces an error on stderr with exit status 2. Do not install dependencies automatically if time-zone data is absent.

## Input
- `start_date`, `end_date`: inclusive ISO dates, ascending, at most 93 days. These identify the anchor participant's local work-window start dates.
- `anchor`: exact unique participant name.
- `participants`: 2–10 objects with `name`, `zone` (IANA name), `start`, `end` (24-hour HH:MM); optional `weekdays` (0 Monday through 6 Sunday), default Monday–Friday. Every participant has one continuous window per selected weekday.
- `minimum_minutes`: integer 1–1440, default 60; disclose when this default is used.

End earlier than start means an overnight shift. Equal start/end is rejected, not treated as a full day. Weekdays apply to each person's local shift start, so a Friday overnight shift may extend into Saturday. Dates displayed for the other participants can differ from the anchor date. Intervals are start-inclusive and end-exclusive.

## Method and limitations
Convert each local work boundary to UTC with the host time-zone database. Reject ambiguous and nonexistent boundaries around clock changes. Intersect the anchor shift with the other shifts at one-minute resolution. Output all common continuous spans, duration, and whether each meets the minimum. Adjacent valid minutes form a span; disconnected spans cannot be combined to satisfy the minimum. Every output date has a sufficient-overlap flag; never omit zero-overlap days from a summary.

A shift may contain a repeated/skipped hour internally; UTC duration reflects elapsed minutes. Ambiguous endpoints require user-selected unambiguous windows. Holidays, PTO, lunch breaks, split shifts, and calendar conflicts are not automatically known. For split shifts, run each set of continuous windows separately and do not double-count shared intervals. Historic/sub-minute offsets and future rule changes need separate verification. This is availability within supplied windows, not access to calendars.

See `../assets/example-input.json` for a fictional Rome/Chicago scenario around their differently timed 2026 DST transitions. A calendar event is not created.
