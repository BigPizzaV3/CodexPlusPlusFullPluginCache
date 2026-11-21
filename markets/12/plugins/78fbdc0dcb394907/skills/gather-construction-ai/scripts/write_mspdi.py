#!/usr/bin/env python3
"""write_mspdi.py — deterministic MSPDI (MS Project XML) writer for the Gather plugin.

Two jobs:
1. FULL WRITE (default): emit a draft programme as MSPDI from a sidecar-schema JSON
   (tasks/links/calendars — the same schema scripts/parse_programme.py produces and
   scripts/cpm.py consumes). Powers /gather:programme-create: MS Project opens the file
   natively; P6 and Asta Powerproject import it. The draft is a SKELETON for a planner to
   own — the file's Title carries a DRAFT marker and the writer refuses to overwrite an
   existing file without --force.
2. ACTUALS UPDATE (--actuals-only): emit the monthly round-trip subset — UID, Name,
   ActualStart, ActualFinish, PercentComplete per task — for the planner to import over
   the live programme instead of re-keying a month of progress by hand. No planned dates,
   no logic, nothing that could disturb the network.

Self-consistency is tested in CI (tests/unit/test_mspdi_roundtrip.py): a written file
re-parsed by parse_programme.py must reproduce the input fields. That proves
writer/parser agreement — opening the file in real MS Project/P6/Asta remains the
external validation to run on a customer machine.

Usage:
    python3 write_mspdi.py <input.json> --out <file.xml> [--title "..."] [--actuals-only] [--force]

Stdlib only. Writes only the --out path.
"""

from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

NS = "http://schemas.microsoft.com/project"

LINK_TYPE_CODES = {"FF": "0", "FS": "1", "SF": "2", "SS": "3"}
CONSTRAINT_CODES = {None: "0", "ALAP": "1", "MSO": "2", "MFO": "3",
                    "SNET": "4", "SNLT": "5", "FNET": "6", "FNLT": "7"}


def el(parent, tag, text=None):
    e = ET.SubElement(parent, f"{{{NS}}}{tag}")
    if text is not None:
        e.text = str(text)
    return e


def iso_dt(s: str | None) -> str | None:
    if not s:
        return None
    s = s.strip().replace("Z", "")
    if len(s) == 10:
        s += "T08:00:00"
    elif len(s) == 16:
        s += ":00"
    return s


def pt_duration(hours: float) -> str:
    h = int(hours)
    m = int(round((hours - h) * 60))
    return f"PT{h}H{m}M0S"


def tenths_of_minutes(hours: float) -> int:
    return int(round(hours * 600))


def build(data: dict, title: str, actuals_only: bool) -> ET.ElementTree:
    ET.register_namespace("", NS)
    root = ET.Element(f"{{{NS}}}Project")
    el(root, "Name", title)
    el(root, "Title", title)
    prov = data.get("provenance") or {}
    if prov.get("data_date"):
        el(root, "StatusDate", iso_dt(prov["data_date"]))

    if not actuals_only:
        cals_el = el(root, "Calendars")
        calendars = data.get("calendars") or {}
        if not calendars:
            calendars = {"1": {"hours_per_day": 8.0}}
        for cid, spec in calendars.items():
            cal_el = el(cals_el, "Calendar")
            el(cal_el, "UID", cid or "1")
            el(cal_el, "Name", spec.get("name") or f"Calendar {cid or '1'}")
            el(cal_el, "IsBaseCalendar", "1")
            week = spec.get("week")
            if not week:
                hpd = float(spec.get("hours_per_day", 8.0) or 8.0)
                week = [hpd] * 5 + [0.0, 0.0]
            wds = el(cal_el, "WeekDays")
            for day_type in range(1, 8):           # MSPDI: 1=Sunday .. 7=Saturday
                mon_index = (day_type + 5) % 7     # to Mon..Sun list
                hours = week[mon_index]
                wd = el(wds, "WeekDay")
                el(wd, "DayType", day_type)
                el(wd, "DayWorking", "1" if hours > 0 else "0")
                if hours > 0:
                    wts = el(wd, "WorkingTimes")
                    wt = el(wts, "WorkingTime")
                    el(wt, "FromTime", "08:00:00")
                    end_h = 8 + int(hours)
                    end_m = int(round((hours - int(hours)) * 60))
                    el(wt, "ToTime", f"{end_h:02d}:{end_m:02d}:00")
            for ex in spec.get("exceptions", []) or []:
                # 2007+ exception block
                exs = cal_el.find(f"{{{NS}}}Exceptions")
                if exs is None:
                    exs = el(cal_el, "Exceptions")
                x = el(exs, "Exception")
                working = float(ex.get("hours", 0) or 0) > 0
                el(x, "DayWorking", "1" if working else "0")
                tp = el(x, "TimePeriod")
                el(tp, "FromDate", f"{ex['date']}T00:00:00")
                el(tp, "ToDate", f"{ex['date']}T23:59:59")
                if working:
                    wts = el(x, "WorkingTimes")
                    wt = el(wts, "WorkingTime")
                    el(wt, "FromTime", "08:00:00")
                    el(wt, "ToTime", f"{8 + int(float(ex['hours'])):02d}:00:00")

    tasks_el = el(root, "Tasks")
    links_by_succ: dict = {}
    for l in data.get("links", []) or []:
        links_by_succ.setdefault(str(l["succ"]), []).append(l)

    for i, t in enumerate(data.get("tasks", []) or [], start=1):
        if t.get("type") == "summary":
            continue
        task_el = el(tasks_el, "Task")
        uid = str(t["id"])
        el(task_el, "UID", uid)
        el(task_el, "ID", i)
        el(task_el, "Name", t.get("name") or uid)
        if actuals_only:
            if t.get("actual_start"):
                el(task_el, "ActualStart", iso_dt(t["actual_start"]))
            if t.get("actual_finish"):
                el(task_el, "ActualFinish", iso_dt(t["actual_finish"]))
            el(task_el, "PercentComplete", int(round(float(t.get("pct_complete", 0) or 0))))
            continue
        stored = t.get("stored") or {}
        start = iso_dt(t.get("start") or stored.get("start"))
        finish = iso_dt(t.get("finish") or stored.get("finish"))
        if start:
            el(task_el, "Start", start)
        if finish:
            el(task_el, "Finish", finish)
        el(task_el, "Duration", pt_duration(float(t.get("duration_hours", 0) or 0)))
        el(task_el, "DurationFormat", "7")  # days display; content is exact PT hours
        el(task_el, "Milestone", "1" if t.get("type") == "milestone" else "0")
        if t.get("wbs"):
            el(task_el, "WBS", t["wbs"])
        cstr = t.get("constraint") or {}
        ctype = cstr.get("type")
        if ctype and not str(ctype).startswith("UNKNOWN"):
            el(task_el, "ConstraintType", CONSTRAINT_CODES.get(ctype, "0"))
            if cstr.get("date"):
                el(task_el, "ConstraintDate", iso_dt(cstr["date"]))
        if t.get("calendar_id"):
            el(task_el, "CalendarUID", t["calendar_id"])
        if t.get("actual_start"):
            el(task_el, "ActualStart", iso_dt(t["actual_start"]))
        if t.get("actual_finish"):
            el(task_el, "ActualFinish", iso_dt(t["actual_finish"]))
        if t.get("pct_complete"):
            el(task_el, "PercentComplete", int(round(float(t["pct_complete"]))))
        for l in links_by_succ.get(uid, []):
            pl = el(task_el, "PredecessorLink")
            el(pl, "PredecessorUID", str(l["pred"]))
            el(pl, "Type", LINK_TYPE_CODES.get((l.get("type") or "FS").upper(), "1"))
            lag = float(l.get("lag_hours", 0) or 0)
            if lag:
                el(pl, "LinkLag", tenths_of_minutes(lag))
                el(pl, "LagFormat", "7")
    return ET.ElementTree(root)


def indent(tree: ET.ElementTree):
    if hasattr(ET, "indent"):
        ET.indent(tree, space=" ")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input_json")
    ap.add_argument("--out", required=True)
    ap.add_argument("--title")
    ap.add_argument("--actuals-only", action="store_true")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    with open(args.input_json, encoding="utf-8") as f:
        data = json.load(f)

    out = Path(args.out)
    if out.exists() and not args.force:
        raise SystemExit(json.dumps({"error": f"{out} exists — pass --force to overwrite"}))

    default_title = ((data.get("provenance") or {}).get("project_name") or "Programme")
    if args.actuals_only:
        title = args.title or f"{default_title} — actuals update"
    else:
        title = args.title or f"DRAFT — {default_title} (Gather plugin skeleton for planner review)"

    tree = build(data, title, args.actuals_only)
    indent(tree)
    out.parent.mkdir(parents=True, exist_ok=True)
    tree.write(out, encoding="UTF-8", xml_declaration=True)
    n_tasks = sum(1 for t in data.get("tasks", []) if t.get("type") != "summary")
    json.dump({"written": str(out), "mode": "actuals-only" if args.actuals_only else "full",
               "title": title, "tasks": n_tasks,
               "note": ("import over the live programme in the planning tool" if args.actuals_only
                        else "a DRAFT skeleton — the planner owns it from here")},
              sys.stdout, indent=2)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
