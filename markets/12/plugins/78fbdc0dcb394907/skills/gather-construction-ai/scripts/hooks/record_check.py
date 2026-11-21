#!/usr/bin/env python3
"""Deterministic hook: no model call. Rule P3.6 - PostToolUse hooks are command
type unless justified in writing.

Matcher: mcp__gather__getShiftRecord

Completeness check on a single shift record: missing narrative/notes, no
workers, no weather, and shift duration under 2h or over 14h. Field presence
and arithmetic only - never a model call.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _hookutil import read_input, extract_tool_response, safe_exit  # noqa: E402


def _from_form_answers(answers):
    """Tolerate a 'form answers' shape: list of {question/label, answer/value}."""
    out = {}
    for a in answers:
        if not isinstance(a, dict):
            continue
        key = a.get("question") or a.get("label") or a.get("name")
        val = a.get("answer")
        if val is None:
            val = a.get("value")
        if key:
            out[str(key).strip().lower()] = val
    return out


def _find_record(obj):
    """Dig a shift-record-shaped dict out of whatever the tool returned."""
    if isinstance(obj, dict):
        if any(k in obj for k in ("narrative", "notes", "workers", "shiftStart", "formAnswers", "form_answers", "answers")):
            return obj
        for key in ("record", "shiftRecord", "data", "result"):
            if key in obj and isinstance(obj[key], dict):
                found = _find_record(obj[key])
                if found is not None:
                    return found
    return obj if isinstance(obj, dict) else None


def _hours_between(start, end):
    """Best-effort ISO8601 duration in hours. Returns None if unparseable."""
    try:
        from datetime import datetime
        s = start.replace("Z", "+00:00")
        e = end.replace("Z", "+00:00")
        sd = datetime.fromisoformat(s)
        ed = datetime.fromisoformat(e)
        return (ed - sd).total_seconds() / 3600.0
    except Exception:
        return None


def main():
    payload = read_input()
    parsed = extract_tool_response(payload)
    record = _find_record(parsed)
    if not isinstance(record, dict):
        safe_exit([])

    # Fold in a "form answers" shape if present, without overriding real fields.
    form = record.get("formAnswers") or record.get("form_answers") or record.get("answers")
    form_fields = _from_form_answers(form) if isinstance(form, list) else ({str(k).lower(): v for k, v in form.items()} if isinstance(form, dict) else {})

    def field(*names):
        for n in names:
            if n in record and record[n] not in (None, ""):
                return record[n]
        for n in names:
            key = n.lower()
            if key in form_fields and form_fields[key] not in (None, ""):
                return form_fields[key]
            for fk, fv in form_fields.items():
                if key in fk and fv not in (None, ""):
                    return fv
        return None

    issues = []

    narrative = field("narrative", "notes", "diaryNotes", "comments")
    if not narrative or (isinstance(narrative, str) and not narrative.strip()):
        issues.append("Missing narrative/notes on this shift record.")

    workers = field("workers", "crew", "labour")
    if not workers or (isinstance(workers, list) and len(workers) == 0):
        issues.append("No workers listed on this shift record.")

    weather = field("weather", "conditions", "weather_conditions")
    if not weather or (isinstance(weather, str) and not weather.strip()):
        issues.append("No weather data recorded on this shift record.")

    duration = None
    actual_hours = field("actualHours", "hours")
    if isinstance(actual_hours, (int, float)):
        duration = float(actual_hours)
    else:
        start = field("shiftStart", "start", "start_time")
        end = field("shiftEnd", "end", "end_time")
        if isinstance(start, str) and isinstance(end, str):
            duration = _hours_between(start, end)

    if isinstance(duration, (int, float)):
        if duration < 2:
            issues.append(f"Shift duration is under 2 hours ({duration:.1f}h) - check for a data entry error.")
        elif duration > 14:
            issues.append(f"Shift duration is over 14 hours ({duration:.1f}h) - check that the recorded start and end times are correct.")

    if not issues:
        safe_exit([])

    record_id = record.get("id") or record.get("recordId") or record.get("uuid") or "record"
    date = record.get("date") or ""
    prefix = f"[shift record {record_id}{(' ' + date) if date else ''}]"
    safe_exit([f"{prefix} {issue}" for issue in issues])


if __name__ == "__main__":
    main()
