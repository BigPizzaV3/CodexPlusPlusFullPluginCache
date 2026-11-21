#!/usr/bin/env python3
"""shift_analytics.py — deterministic aggregator for Gather cached-report dumps.

WHY THIS EXISTS AS CODE: labour, plant-report, weather-impact, resource-analysis
and data-quality all sum the same handful of dashboard reports (dashboardResourceLabour,
dashboardResourcePlant, dashboardShiftTable, ...) in-context, row by row. For a month of
data that is ~30k tokens of table the model has to add up itself, with no guarantee two
runs of the same skill add it up the same way. This script does the addition once,
deterministically, off the exact rows the skill would otherwise paste into context, and
prints a compact summary a skill can cite instead of re-deriving.

It never fabricates: if a report or column a computation needs is missing, that computation
is reported under "unavailable" naming the missing column, rather than guessed at.

Usage:
    python3 shift_analytics.py <file.json> [<file2.json> ...] [--format json|md]
    python3 shift_analytics.py --schema
    python3 shift_analytics.py --self-check

Input: one or more JSON files, each one of:
    - a raw MCP tools/call result: {"content": [{"type": "text", "text": "<json>"}], ...}
    - a bare list of report rows (what getCachedReport returns for most report types)
    - {"rows": [...]} or {"records": [...]} (the getShiftRecords page wrapper)
Each file's report type is auto-detected from its column names; pass --report-type to
override when a file's rows don't carry enough columns to detect (e.g. a hand-trimmed
subset). Multiple files may cover different report types — they are merged by type.

Stdlib only. No network, no writes.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta

# --- Known report schemas (column names), verified against tests/harness/sample_data.json's
# getReportSchemas response. Reports named in the guide/action-plan but not present in this
# harness (so their real column names are unconfirmed) map to None — --schema reports them
# as "unknown", it never invents columns for them. Call the live getReportSchemas tool to
# confirm before relying on one of these.
SCHEMAS = {
    "dashboardShiftTable": ["recordId", "date", "supervisor", "location", "shiftStart",
                            "shiftEnd", "plannedHours", "actualHours", "weather", "crewSize"],
    "dashboardResourceLabour": ["date", "person", "role", "hours", "project"],
    "dashboardResourceMaterial": ["date", "material", "quantity", "unit"],
    "dashboardResourcePlant": ["date", "plant", "hoursOnHire"],
    "dashboardNarrative": ["date", "recordId", "supervisor", "narrative", "tags"],
    "dashboardProgress": ["date", "activity", "unit", "plannedQuantity", "actualQuantity"],
    "dashboardAccessPossession": ["id", "date", "location", "plannedStart", "actualStart",
                                  "plannedEnd", "actualEnd", "lateHandover", "reason"],
    "dashboardAccessNonPossession": ["id", "date", "location", "plannedStart", "actualStart",
                                     "delayMinutes", "reason"],
    "dashboardAccessOverview": ["totalPossessions", "onTime", "late", "lateRatePercent",
                                "averageLateMinutesWhenLate"],
    # Named in GATHER_MCP_GUIDE.md / the action plan (16 live report types; this harness's
    # mock server and sample_data.json only cover 11) but not confirmed here — unknown.
    "dashboardAllocation": None,
    "dashboardWeather": None,
    "dashboardPeopleDetail": None,
    "dashboardSubcontractorLabourDetail": None,
}

# Which computations each report type feeds, for the --schema listing.
FEEDS = {
    "dashboardResourceLabour": "labour hours by trade/role and week, headcount by day, duplicate allocations",
    "dashboardResourcePlant": "plant hours, idle days, off-hire candidates",
    "dashboardShiftTable": "weather-lost hours/day counts by type, shift coverage gaps",
}


# --- Loading ---------------------------------------------------------------------------

def _unwrap(obj):
    """Unwrap one level of MCP tools/call result or getShiftRecords-style paging wrapper
    down to a bare list of rows. Returns (rows, note) where note is None or a caveat string
    (e.g. getShiftRecords pages return only id/lastModified/tags — not enough for most
    aggregates below)."""
    if isinstance(obj, list):
        return obj, None
    if isinstance(obj, dict):
        if "content" in obj and isinstance(obj["content"], list):
            for item in obj["content"]:
                if isinstance(item, dict) and item.get("type") == "text":
                    try:
                        inner = json.loads(item["text"])
                    except (json.JSONDecodeError, TypeError):
                        continue
                    return _unwrap(inner)
            return [], "MCP content wrapper carried no parseable text payload"
        if "rows" in obj and isinstance(obj["rows"], list):
            return obj["rows"], None
        if "records" in obj and isinstance(obj["records"], list):
            return obj["records"], ("getShiftRecords page wrapper: rows are projected "
                                     "(id/lastModified/tags only) — most aggregates need the "
                                     "full report via getCachedReport instead")
        # A single dict that is itself one row (defensive; not expected in practice).
        return [obj], None
    return [], f"unrecognised input shape: {type(obj).__name__}"


def detect_report_type(rows: list) -> str | None:
    if not rows or not isinstance(rows[0], dict):
        return None
    cols = set(rows[0].keys())
    best, best_score = None, 0
    for name, schema in SCHEMAS.items():
        if not schema:
            continue
        score = len(cols & set(schema))
        # require a reasonably strong match, not just one shared column like "date"
        if score >= max(3, len(schema) - 1) and score > best_score:
            best, best_score = name, score
    return best


def load_files(paths: list, report_type_override: str | None) -> tuple[dict, list, dict]:
    """Returns (rows_by_type, warnings, counts_by_source_file)."""
    rows_by_type: dict = defaultdict(list)
    warnings: list = []
    counts: dict = {}
    for path in paths:
        with open(path, encoding="utf-8") as f:
            try:
                obj = json.load(f)
            except json.JSONDecodeError as e:
                warnings.append(f"{path}: not valid JSON ({e}) — skipped")
                continue
        rows, note = _unwrap(obj)
        if note:
            warnings.append(f"{path}: {note}")
        rtype = report_type_override or detect_report_type(rows)
        if rtype is None:
            warnings.append(f"{path}: could not auto-detect report type from columns "
                             f"{sorted(rows[0].keys()) if rows and isinstance(rows[0], dict) else '(no rows)'}"
                             " — pass --report-type")
            rtype = "unknown"
        rows_by_type[rtype].extend(rows)
        counts[path] = {"report_type": rtype, "rows": len(rows)}
    return dict(rows_by_type), warnings, counts


# --- Date helpers ------------------------------------------------------------------------

def parse_d(s: str) -> date:
    return datetime.strptime(s[:10], "%Y-%m-%d").date()


def week_of(d: date) -> str:
    monday = d - timedelta(days=d.weekday())
    return f"Week of {monday.isoformat()}"


def daterange(d0: date, d1: date):
    d = d0
    while d <= d1:
        yield d
        d += timedelta(days=1)


# --- Aggregates --------------------------------------------------------------------------

def missing_cols(rows: list, needed: list) -> list:
    if not rows:
        return needed
    have = set(rows[0].keys())
    return [c for c in needed if c not in have]


def agg_labour(rows: list) -> dict:
    need = ["date", "person", "role", "hours"]
    miss = missing_cols(rows, need)
    if miss:
        return {"unavailable": f"dashboardResourceLabour missing column(s): {miss}"}

    by_role: dict = defaultdict(float)
    by_week: dict = defaultdict(float)
    by_person_role: dict = {}
    headcount_by_day: dict = defaultdict(set)

    for r in rows:
        d = parse_d(r["date"])
        hours = float(r.get("hours") or 0.0)
        role = r.get("role") or "(unspecified)"
        person = r.get("person") or "(unspecified)"
        by_role[role] += hours
        by_week[week_of(d)] += hours
        if hours > 0:
            headcount_by_day[r["date"]].add(person)
        by_person_role.setdefault(person, role)

    return {
        "by_trade_role": {k: round(v, 2) for k, v in sorted(by_role.items(), key=lambda kv: -kv[1])},
        "by_week": {k: round(v, 2) for k, v in sorted(by_week.items())},
        "headcount_by_day": {k: len(v) for k, v in sorted(headcount_by_day.items())},
        "total_hours": round(sum(by_role.values()), 2),
    }


def agg_duplicate_allocations(rows: list) -> dict:
    need = ["date", "person"]
    miss = missing_cols(rows, need)
    if miss:
        return {"unavailable": f"dashboardResourceLabour missing column(s): {miss}"}

    seen: dict = defaultdict(list)
    for r in rows:
        seen[(r["date"], r.get("person"))].append(r)
    dupes = [{"date": k[0], "person": k[1], "row_count": len(v)}
             for k, v in seen.items() if len(v) > 1]
    dupes.sort(key=lambda x: (x["date"], x["person"]))
    return {
        "candidates": dupes,
        "note": ("Same person + same date appearing more than once in dashboardResourceLabour. "
                 "This report has no start/end time per row, so true overlapping-window "
                 "detection is not possible from it alone — these are candidates for review, "
                 "not confirmed double-bookings. Confirm against getShiftRecord for the dates "
                 "listed."),
    }


def agg_plant(rows: list, idle_threshold: int) -> dict:
    need = ["date", "plant", "hoursOnHire"]
    miss = missing_cols(rows, need)
    if miss:
        return {"unavailable": f"dashboardResourcePlant missing column(s): {miss}"}

    by_plant: dict = defaultdict(lambda: {"hours": 0.0, "dates": []})
    for r in rows:
        p = r["plant"]
        by_plant[p]["hours"] += float(r.get("hoursOnHire") or 0.0)
        by_plant[p]["dates"].append((parse_d(r["date"]), float(r.get("hoursOnHire") or 0.0)))

    summary = {}
    off_hire_candidates = []
    for plant, info in by_plant.items():
        dates_sorted = sorted(info["dates"])
        idle_dates = [d for d, h in dates_sorted if h == 0.0]
        # longest run of *consecutive recorded* idle dates (consecutive calendar days
        # among the rows present for this item, not the whole calendar).
        max_idle_run, run = 0, 0
        prev = None
        for d, h in dates_sorted:
            if h == 0.0 and (prev is None or (d - prev).days == 1):
                run += 1
            elif h == 0.0:
                run = 1
            else:
                run = 0
            if h == 0.0:
                max_idle_run = max(max_idle_run, run)
            prev = d
        summary[plant] = {
            "hours_on_hire_total": round(info["hours"], 2),
            "allocated_days": len(dates_sorted),
            "idle_days": len(idle_dates),
            "max_consecutive_idle_days": max_idle_run,
        }
        if max_idle_run >= idle_threshold:
            off_hire_candidates.append({
                "plant": plant, "max_consecutive_idle_days": max_idle_run,
                "idle_days_total": len(idle_dates),
            })
    off_hire_candidates.sort(key=lambda x: -x["max_consecutive_idle_days"])
    return {
        "by_plant": summary,
        "off_hire_candidates": off_hire_candidates,
        "idle_threshold_consecutive_days": idle_threshold,
        "note": ('"Idle day" = a row recorded for that plant item with hoursOnHire == 0 (i.e. '
                 "allocated/on site but not used). Consecutive-idle counts only the dates "
                 "present in the rows given — a genuine gap in recording looks the same as a "
                 "gap in allocation from this report alone."),
    }


def agg_weather(rows: list) -> dict:
    need = ["date", "weather", "plannedHours", "actualHours"]
    miss = missing_cols(rows, need)
    if miss:
        return {"unavailable": f"dashboardShiftTable missing column(s): {miss}"}

    durations = sorted(float(r.get("actualHours") or 0.0) for r in rows if r.get("actualHours"))
    if not durations:
        return {"unavailable": "dashboardShiftTable has no actualHours values to derive a standard shift length"}
    n = len(durations)
    standard = durations[n // 2] if n % 2 else (durations[n // 2 - 1] + durations[n // 2]) / 2.0
    if standard <= 0:
        return {"unavailable": "median actualHours is 0 — cannot classify shifts"}

    lost_by_type: dict = defaultdict(float)
    days_by_type: dict = defaultdict(int)
    classified = {"FW": 0, "FW-N": 0, "RW": 0, "NW": 0}
    total_lost = 0.0
    affected_dates = []

    for r in rows:
        actual = float(r.get("actualHours") or 0.0)
        planned = float(r.get("plannedHours") or actual)
        weather = (r.get("weather") or "").strip()
        has_weather = bool(weather) and weather.lower() not in ("clear", "none", "dry", "fine", "n/a", "")
        ratio = (actual / standard) if standard else 1.0
        lost = 0.0
        if has_weather and ratio < 0.25:
            cat = "NW"
            lost = max(planned, standard) - actual
        elif has_weather and 0.25 <= ratio <= 0.75:
            cat = "RW"
            lost = max(planned, standard) - actual
        elif has_weather:
            cat = "FW-N"  # full duration, weather merely noted — no narrative available here
                          # to detect curtailment language, so this script cannot distinguish
                          # FW-N from a narrative-curtailed RW at >75% duration (see note).
        else:
            cat = "FW"
        classified[cat] += 1
        if cat in ("RW", "NW"):
            lost_by_type[weather] += lost
            days_by_type[weather] += 1
            total_lost += lost
            affected_dates.append(r["date"])

    return {
        "standard_shift_hours": round(standard, 2),
        "classified_days": classified,
        "weather_lost_hours_by_type": {k: round(v, 2) for k, v in sorted(lost_by_type.items(), key=lambda kv: -kv[1])},
        "weather_affected_days_by_type": dict(sorted(days_by_type.items(), key=lambda kv: -kv[1])),
        "total_weather_lost_hours": round(total_lost, 2),
        "total_weather_affected_days": classified["RW"] + classified["NW"],
        "note": ("FW-N vs a narrative-curtailed RW at >75% of standard duration cannot be told "
                 "apart from dashboardShiftTable alone (that distinction needs narrative "
                 "impact-language, per the weather-impact skill) — every >75%-duration weather "
                 "day here is counted FW-N (zero lost time). Pass dashboardNarrative rows and "
                 "re-run the skill's own narrative check if that distinction matters for a claim."),
    }


def agg_coverage(rows: list, date_from: str | None, date_to: str | None) -> dict:
    need = ["date"]
    miss = missing_cols(rows, need)
    if miss:
        return {"unavailable": f"dashboardShiftTable missing column(s): {miss}"}
    if not rows:
        return {"unavailable": "no dashboardShiftTable rows to assess coverage"}

    present = {r["date"] for r in rows}
    lo = parse_d(date_from) if date_from else parse_d(min(present))
    hi = parse_d(date_to) if date_to else parse_d(max(present))
    gaps = [d.isoformat() for d in daterange(lo, hi) if d.isoformat() not in present]
    total_days = (hi - lo).days + 1
    return {
        "range": [lo.isoformat(), hi.isoformat()],
        "calendar_days_in_range": total_days,
        "days_with_records": total_days - len(gaps),
        "gap_days": gaps,
        "coverage_pct": round(100.0 * (total_days - len(gaps)) / total_days, 1) if total_days else None,
    }


# --- Orchestration -------------------------------------------------------------------------

def build_summary(rows_by_type: dict, idle_threshold: int, date_from: str | None, date_to: str | None) -> dict:
    source_counts = {rtype: len(rows) for rtype, rows in rows_by_type.items()}
    summary: dict = {"source_row_counts": source_counts, "columns_used": {}, "sections": {}}

    for rtype, rows in rows_by_type.items():
        if rows and isinstance(rows[0], dict):
            summary["columns_used"][rtype] = sorted(rows[0].keys())

    labour_rows = rows_by_type.get("dashboardResourceLabour", [])
    plant_rows = rows_by_type.get("dashboardResourcePlant", [])
    shift_rows = rows_by_type.get("dashboardShiftTable", [])

    labour = agg_labour(labour_rows) if labour_rows or "dashboardResourceLabour" not in rows_by_type else agg_labour(labour_rows)
    if not labour_rows:
        labour = {"unavailable": "no dashboardResourceLabour rows supplied"}
    summary["sections"]["labour"] = labour

    if labour_rows:
        summary["sections"]["duplicate_allocations"] = agg_duplicate_allocations(labour_rows)
    else:
        no_data = {"unavailable": "no dashboardResourceLabour rows supplied"}
        summary["sections"]["duplicate_allocations"] = no_data

    summary["sections"]["plant"] = (agg_plant(plant_rows, idle_threshold) if plant_rows
                                     else {"unavailable": "no dashboardResourcePlant rows supplied"})

    summary["sections"]["weather"] = (agg_weather(shift_rows) if shift_rows
                                       else {"unavailable": "no dashboardShiftTable rows supplied"})

    summary["sections"]["shift_coverage_gaps"] = (agg_coverage(shift_rows, date_from, date_to) if shift_rows
                                                   else {"unavailable": "no dashboardShiftTable rows supplied"})

    return summary


def render_md(summary: dict) -> str:
    out = ["# Shift analytics summary", ""]
    out.append("**Source row counts:** " +
               ", ".join(f"{k}={v}" for k, v in summary["source_row_counts"].items()) or "(none)")
    out.append("")
    for rtype, cols in summary["columns_used"].items():
        out.append(f"**Columns used ({rtype}):** {', '.join(cols)}")
    out.append("")

    def section(title, body):
        out.append(f"## {title}")
        if isinstance(body, dict) and "unavailable" in body:
            out.append(f"_Unavailable: {body['unavailable']}_")
        else:
            out.append("```json")
            out.append(json.dumps(body, indent=2, default=str))
            out.append("```")
        out.append("")

    s = summary["sections"]
    section("Labour hours by trade/role and week, headcount by day", s.get("labour"))
    section("Duplicate allocation candidates", s.get("duplicate_allocations"))
    section("Plant hours, idle days, off-hire candidates", s.get("plant"))
    section("Weather-lost hours and day counts by type", s.get("weather"))
    section("Shift coverage gaps", s.get("shift_coverage_gaps"))
    return "\n".join(out)


def print_schema() -> None:
    for name, cols in SCHEMAS.items():
        feeds = FEEDS.get(name, "")
        if cols is None:
            print(f"{name}: unknown — not confirmed live in this harness; call getReportSchemas "
                  "before relying on it")
        else:
            line = f"{name}: {', '.join(cols)}"
            if feeds:
                line += f"  [feeds: {feeds}]"
            print(line)


def self_check() -> int:
    """Exercise every aggregate against a small in-memory fixture. Used by CI / manual sanity."""
    failures = []

    def check(label, cond):
        if cond:
            print(f"PASS  {label}")
        else:
            print(f"FAIL  {label}")
            failures.append(label)

    labour_rows = [
        {"date": "2026-02-02", "person": "A", "role": "Groundworker", "hours": 10.0, "project": "P"},
        {"date": "2026-02-03", "person": "A", "role": "Groundworker", "hours": 10.0, "project": "P"},
        {"date": "2026-02-03", "person": "A", "role": "Groundworker", "hours": 2.0, "project": "P"},  # duplicate
        {"date": "2026-02-02", "person": "B", "role": "Plumber", "hours": 8.0, "project": "P"},
    ]
    lab = agg_labour(labour_rows)
    check("labour by_trade_role", lab["by_trade_role"] == {"Groundworker": 22.0, "Plumber": 8.0})
    check("labour headcount_by_day", lab["headcount_by_day"] == {"2026-02-02": 2, "2026-02-03": 1})
    dup = agg_duplicate_allocations(labour_rows)
    check("duplicate detection", dup["candidates"] == [{"date": "2026-02-03", "person": "A", "row_count": 2}])

    plant_rows = [
        {"date": "2026-02-01", "plant": "Crane", "hoursOnHire": 0.0},
        {"date": "2026-02-02", "plant": "Crane", "hoursOnHire": 0.0},
        {"date": "2026-02-03", "plant": "Crane", "hoursOnHire": 8.0},
    ]
    plant = agg_plant(plant_rows, idle_threshold=2)
    check("plant idle run", plant["by_plant"]["Crane"]["max_consecutive_idle_days"] == 2)
    check("plant off-hire candidate", plant["off_hire_candidates"][0]["plant"] == "Crane")

    weather_rows = [
        {"date": "2026-02-01", "weather": "Clear", "plannedHours": 10.0, "actualHours": 10.0},
        {"date": "2026-02-02", "weather": "Heavy rain", "plannedHours": 10.0, "actualHours": 2.0},
        {"date": "2026-02-03", "weather": "Clear", "plannedHours": 10.0, "actualHours": 10.0},
    ]
    weather = agg_weather(weather_rows)
    check("weather NW day", weather["classified_days"]["NW"] == 1)
    check("weather lost hours", weather["total_weather_lost_hours"] == 8.0)

    cov = agg_coverage([{"date": "2026-02-01"}, {"date": "2026-02-03"}], None, None)
    check("coverage gap detection", cov["gap_days"] == ["2026-02-02"])

    print(f"\n{len(failures)} failure(s)")
    return 0 if not failures else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("files", nargs="*", help="Saved getCachedReport/getShiftRecords JSON dumps")
    ap.add_argument("--report-type", choices=[k for k, v in SCHEMAS.items() if v],
                    help="Override auto-detection for files that don't carry enough columns")
    ap.add_argument("--format", choices=["json", "md"], default="json")
    ap.add_argument("--idle-threshold", type=int, default=3,
                    help="Consecutive idle days before a plant item is an off-hire candidate (default 3)")
    ap.add_argument("--from", dest="date_from", help="YYYY-MM-DD lower bound for coverage-gap check")
    ap.add_argument("--to", dest="date_to", help="YYYY-MM-DD upper bound for coverage-gap check")
    ap.add_argument("--schema", action="store_true", help="Print the columns each computation needs, per report type, and exit")
    ap.add_argument("--self-check", action="store_true", help="Run built-in aggregate sanity checks and exit")
    args = ap.parse_args()

    if args.schema:
        print_schema()
        return 0
    if args.self_check:
        return self_check()
    if not args.files:
        ap.error("at least one input file is required (or use --schema / --self-check)")

    rows_by_type, warnings, counts = load_files(args.files, args.report_type)
    summary = build_summary(rows_by_type, args.idle_threshold, args.date_from, args.date_to)
    summary["sources"] = counts
    if warnings:
        summary["warnings"] = warnings

    if args.format == "md":
        print(render_md(summary))
    else:
        json.dump(summary, sys.stdout, indent=2, default=str)
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
