#!/usr/bin/env python3
"""Deterministic hook: no model call. Rule P3.6 - PostToolUse hooks are command
type unless justified in writing.

Matcher: mcp__gather__getShiftRecords

Replaces the two prompt hooks previously on this matcher. getShiftRecords
returns summary rows (UUID, date, supervisor, tags, and sometimes a title or
narrative field) rather than full shift records, so this script does two
cheap, page-scoped checks:

  (a) keyword scan over any text fields present, using the keyword
      categories from Pattern 10 -
      shared/patterns/10-contractual-event-keywords.md -
      copied below as constants (keep in sync - update both in the same
      commit), with the same false-positive exclusion rule;
  (b) duplicate check: the same supervisor + date + location appearing more
      than once on this page.

Prints at most one short note per check, per page. Silent otherwise.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _hookutil import read_input, extract_tool_response, safe_exit  # noqa: E402

# Keep in sync with Pattern 10 (10-contractual-event-keywords.md).
KEYWORD_CATEGORIES = {
    "access/possession": ["no access", "access denied", "access restricted", "late possession",
                          "possession not given", "could not access", "waiting for access"],
    "instructions/changes": ["instruction", "variation", "scope change", "design change",
                             "redesign", "additional work", "omission", "rework", "abortive"],
    "standing/delay": ["standing time", "standing", "stood down", "idle", "waiting",
                       "unable to proceed", "delay", "delayed", "disruption", "held up",
                       "no work available"],
    "physical conditions": ["unforeseen", "unexpected ground", "contamination", "asbestos",
                            "utilities found", "services found"],
    "third party": ["statutory undertaker", "utility company", "other contractor", "interference"],
    "information": ["waiting for information", "drawing not issued", "design incomplete",
                    "rfi", "query outstanding"],
    "weather": ["weather", "rain", "wind", "storm", "flood", "snow", "ice", "fog"],
}

# False-positive rule: routine mentions that happen to contain a keyword.
EXCLUSIONS = [
    "waiting for concrete to cure",
    "toolbox talk instruction",
    "delivery delayed",
]

TEXT_FIELDS = ("narrative", "notes", "title", "summary", "description", "comments")


def _rows_from(parsed):
    if isinstance(parsed, list):
        return parsed
    if isinstance(parsed, dict):
        for key in ("shiftRecords", "records", "rows", "data", "results"):
            v = parsed.get(key)
            if isinstance(v, list):
                return v
        for v in parsed.values():
            if isinstance(v, list):
                return v
    return []


def _excluded(text_lower):
    return any(ex in text_lower for ex in EXCLUSIONS)


def _keyword_scan(rows):
    for row in rows:
        if not isinstance(row, dict):
            continue
        text_parts = [str(row[f]) for f in TEXT_FIELDS if row.get(f)]
        if not text_parts:
            continue
        text = " ".join(text_parts)
        text_lower = text.lower()
        if _excluded(text_lower):
            continue
        for category, keywords in KEYWORD_CATEGORIES.items():
            for kw in keywords:
                if kw in text_lower:
                    date = row.get("date", "")
                    return (
                        f"Potential contractual event detected in {date} shift record - "
                        f"'{kw}' ({category}). Consider /gather:events for a full analysis or "
                        f"/gather:ce-builder to prepare a submission. Note: notification "
                        f"deadlines may apply (NEC: 8 weeks, FIDIC: 28 days)."
                    )
    return None


def _duplicate_scan(rows):
    seen = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        key = (row.get("supervisor"), row.get("date"), row.get("location"))
        if not any(key):
            continue
        if key in seen:
            return (
                f"Possible duplicate allocation in the records just fetched - "
                f"same supervisor/date/location ({row.get('supervisor')}, {row.get('date')}, "
                f"{row.get('location')}). Run /gather:data-quality [project] [period] duplicates "
                f"for the full sweep."
            )
        seen[key] = True
    return None


def main():
    payload = read_input()
    parsed = extract_tool_response(payload)
    rows = _rows_from(parsed)
    if not rows:
        safe_exit([])

    lines = []
    kw_note = _keyword_scan(rows)
    if kw_note:
        lines.append(kw_note)
    dup_note = _duplicate_scan(rows)
    if dup_note:
        lines.append(dup_note)

    safe_exit(lines)


if __name__ == "__main__":
    main()
