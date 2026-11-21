#!/usr/bin/env python3
"""parse_programme.py — deterministic programme parser for the Gather plugin.

Parses an MS Project MSPDI XML or Primavera P6 XER export into the structured JSON sidecar
(`programme/programme-baseline.json`) that scripts/cpm.py and the consuming skills read.
Replaces in-context parsing for anything beyond small files: real programmes run thousands
of task rows, and a deterministic parser is the only honest way to handle them.

Fidelity rules (from the programme capability review):
- P6 target dates are CURRENT planned dates, NOT a baseline. Baseline presence is only
  reported when real baseline evidence exists (bl_/baseline fields, or a second linked
  project). "Target dates present" never reads as "baseline present".
- Calendars: weekly patterns and dated exceptions parsed where the export carries them
  (MSPDI WeekDays/Exceptions; XER clndr_data best-effort) — fallback to hours_per_day with
  an explicit warning, never silently.
- Constraints parsed and mapped to the engine's names; unknown codes surfaced verbatim in
  warnings, never dropped.
- Multi-project XER: refuses to pick silently — lists projects, requires --project.
- Encoding: UTF-8 first, Windows-1252 fallback (P6's default), stated in provenance.
- Everything the parser could not read is listed in provenance.warnings.

Usage:
    python3 parse_programme.py <export-file> [--project <proj_id>] [--out <sidecar.json>]
    python3 parse_programme.py <export-file> --list-projects   # multi-project XER inspection

Stdlib only. Writes only the --out path (default: programme/programme-baseline.json).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cpm import Calendar, parse_dt  # noqa: E402  (sibling module; shares calendar semantics)

MSPDI_NS = "{http://schemas.microsoft.com/project}"

MSPDI_CONSTRAINTS = {
    "0": None,          # As Soon As Possible (default)
    "1": "ALAP",        # As Late As Possible — engine treats as ASAP with a warning
    "2": "MSO", "3": "MFO", "4": "SNET", "5": "SNLT", "6": "FNET", "7": "FNLT",
}
MSPDI_LINK_TYPES = {"0": "FF", "1": "FS", "2": "SF", "3": "SS"}

XER_CONSTRAINTS = {
    "CS_MSOA": "SNET", "CS_MSOB": "SNLT", "CS_MEOA": "FNET", "CS_MEOB": "FNLT",
    "CS_MSO": "MSO", "CS_MEO": "MFO", "CS_MANDSTART": "MSO", "CS_MANDFIN": "MFO",
    "CS_ALAP": "ALAP",
}
XER_LINK_TYPES = {"PR_FS": "FS", "PR_SS": "SS", "PR_FF": "FF", "PR_SF": "SF"}


def read_text(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    try:
        return raw.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        return raw.decode("cp1252"), "cp1252 (P6 default; UTF-8 decode failed)"


# --------------------------------------------------------------------------- MSPDI

def mspdi_duration_hours(s: str | None, warnings: list, ctx: str) -> float:
    """MSPDI durations are ISO-8601-ish PT#H#M#S strings."""
    if not s:
        return 0.0
    m = re.fullmatch(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s.strip())
    if not m:
        warnings.append(f"unparseable duration {s!r} on {ctx} — treated as 0")
        return 0.0
    h = int(m.group(1) or 0) + int(m.group(2) or 0) / 60.0 + int(m.group(3) or 0) / 3600.0
    return round(h, 4)


def mspdi_slack_hours(v: str | None) -> float | None:
    """TotalSlack/LinkLag are in tenths of minutes."""
    if v is None or v == "":
        return None
    return round(float(v) / 10.0 / 60.0, 4)


def parse_mspdi_calendars(root, warnings: list) -> dict:
    cals = {}
    for cal in root.findall(f"{MSPDI_NS}Calendars/{MSPDI_NS}Calendar"):
        uid = (cal.findtext(f"{MSPDI_NS}UID") or "").strip()
        week = [0.0] * 7  # Mon..Sun
        exceptions = []
        found_pattern = False
        for wd in cal.findall(f"{MSPDI_NS}WeekDays/{MSPDI_NS}WeekDay"):
            day_type = (wd.findtext(f"{MSPDI_NS}DayType") or "").strip()
            working = (wd.findtext(f"{MSPDI_NS}DayWorking") or "0").strip() == "1"
            hours = 0.0
            for wt in wd.findall(f"{MSPDI_NS}WorkingTimes/{MSPDI_NS}WorkingTime"):
                ft, tt = wt.findtext(f"{MSPDI_NS}FromTime"), wt.findtext(f"{MSPDI_NS}ToTime")
                if ft and tt:
                    fh = int(ft[:2]) + int(ft[3:5]) / 60.0
                    th = int(tt[:2]) + int(tt[3:5]) / 60.0
                    hours += max(th - fh, 0.0)
            if day_type == "0":
                # An exception day definition (pre-2007 style): TimePeriod carries the dates.
                tp = wd.find(f"{MSPDI_NS}TimePeriod")
                if tp is not None:
                    fd = (tp.findtext(f"{MSPDI_NS}FromDate") or "")[:10]
                    td = (tp.findtext(f"{MSPDI_NS}ToDate") or fd)[:10]
                    if fd:
                        d0, d1 = date.fromisoformat(fd), date.fromisoformat(td or fd)
                        cur = d0
                        while cur <= d1:
                            exceptions.append({"date": cur.isoformat(),
                                               "hours": hours if working else 0.0})
                            cur += timedelta(days=1)
            elif day_type in {"1", "2", "3", "4", "5", "6", "7"}:
                found_pattern = True
                # MSPDI DayType: 1=Sunday .. 7=Saturday. Our week list is Mon..Sun.
                mon_index = (int(day_type) + 5) % 7
                week[mon_index] = hours if working else 0.0
        for ex in cal.findall(f"{MSPDI_NS}Exceptions/{MSPDI_NS}Exception"):
            tp = ex.find(f"{MSPDI_NS}TimePeriod")
            working = (ex.findtext(f"{MSPDI_NS}DayWorking") or "0").strip() == "1"
            hours = 0.0
            for wt in ex.findall(f"{MSPDI_NS}WorkingTimes/{MSPDI_NS}WorkingTime"):
                ft, tt = wt.findtext(f"{MSPDI_NS}FromTime"), wt.findtext(f"{MSPDI_NS}ToTime")
                if ft and tt:
                    hours += max((int(tt[:2]) + int(tt[3:5]) / 60.0) - (int(ft[:2]) + int(ft[3:5]) / 60.0), 0.0)
            if tp is not None:
                fd = (tp.findtext(f"{MSPDI_NS}FromDate") or "")[:10]
                td = (tp.findtext(f"{MSPDI_NS}ToDate") or fd)[:10]
                if fd:
                    d0, d1 = date.fromisoformat(fd), date.fromisoformat(td or fd)
                    cur = d0
                    while cur <= d1:
                        exceptions.append({"date": cur.isoformat(),
                                           "hours": hours if working else 0.0})
                        cur += timedelta(days=1)
        spec = {"exceptions": exceptions}
        if found_pattern and any(h > 0 for h in week):
            spec["week"] = week
        else:
            spec["hours_per_day"] = 8.0
            if uid:
                warnings.append(
                    f"calendar {uid}: no usable weekly pattern in export — 8h/day Mon–Fri assumed")
        cals[uid] = spec
    return cals


def parse_mspdi(text: str, warnings: list) -> dict:
    root = ET.fromstring(text)
    if root.tag != f"{MSPDI_NS}Project":
        raise SystemExit(json.dumps({"error": f"not an MSPDI file (root {root.tag})"}))

    status_date = (root.findtext(f"{MSPDI_NS}StatusDate") or
                   root.findtext(f"{MSPDI_NS}CurrentDate") or "")[:16]
    calendars = parse_mspdi_calendars(root, warnings)

    numbered_baselines = set()
    tasks, links = [], []
    for task in root.findall(f"{MSPDI_NS}Tasks/{MSPDI_NS}Task"):
        uid = (task.findtext(f"{MSPDI_NS}UID") or "").strip()
        if uid == "0":
            continue  # project summary row
        summary = (task.findtext(f"{MSPDI_NS}Summary") or "0").strip() == "1"
        milestone = (task.findtext(f"{MSPDI_NS}Milestone") or "0").strip() == "1"
        manual = (task.findtext(f"{MSPDI_NS}Manual") or "0").strip() == "1"
        name = task.findtext(f"{MSPDI_NS}Name") or f"task {uid}"
        ctype_raw = (task.findtext(f"{MSPDI_NS}ConstraintType") or "0").strip()
        ctype = MSPDI_CONSTRAINTS.get(ctype_raw)
        if ctype_raw not in MSPDI_CONSTRAINTS:
            warnings.append(f"unknown ConstraintType {ctype_raw!r} on task {uid} — surfaced, not mapped")
            ctype = f"UNKNOWN:{ctype_raw}"
        if ctype == "ALAP":
            warnings.append(f"task {uid} is As-Late-As-Possible — engine schedules it ASAP and flags it")
        cdate = (task.findtext(f"{MSPDI_NS}ConstraintDate") or "")[:16] or None
        critical_el = task.find(f"{MSPDI_NS}Critical")
        slack = mspdi_slack_hours(task.findtext(f"{MSPDI_NS}TotalSlack"))
        # numbered baselines (Baseline0 = the default one we surface as baseline)
        bl_start = bl_finish = None
        for bl in task.findall(f"{MSPDI_NS}Baseline"):
            num = (bl.findtext(f"{MSPDI_NS}Number") or "0").strip()
            if num == "0":
                bl_start = (bl.findtext(f"{MSPDI_NS}Start") or "")[:16] or None
                bl_finish = (bl.findtext(f"{MSPDI_NS}Finish") or "")[:16] or None
            else:
                numbered_baselines.add(num)
        if bl_start is None:
            bl_start = (task.findtext(f"{MSPDI_NS}BaselineStart") or "")[:16] or None
            bl_finish = (task.findtext(f"{MSPDI_NS}BaselineFinish") or "")[:16] or None

        t = {
            "id": uid,
            "name": name,
            "type": "summary" if summary else ("milestone" if milestone else "task"),
            "wbs": task.findtext(f"{MSPDI_NS}WBS") or None,
            "outline_level": int(task.findtext(f"{MSPDI_NS}OutlineLevel") or 0),
            "manual": manual,
            "duration_hours": mspdi_duration_hours(task.findtext(f"{MSPDI_NS}Duration"), warnings, f"task {uid}"),
            "remaining_hours": mspdi_duration_hours(task.findtext(f"{MSPDI_NS}RemainingDuration"), warnings, f"task {uid}") or None,
            "pct_complete": float(task.findtext(f"{MSPDI_NS}PercentComplete") or 0),
            "actual_start": (task.findtext(f"{MSPDI_NS}ActualStart") or "")[:16] or None,
            "actual_finish": (task.findtext(f"{MSPDI_NS}ActualFinish") or "")[:16] or None,
            "calendar_id": (task.findtext(f"{MSPDI_NS}CalendarUID") or "").strip() or None,
            "constraint": {"type": ctype, "date": cdate} if ctype else None,
            "stored": {
                "start": (task.findtext(f"{MSPDI_NS}Start") or "")[:16] or None,
                "finish": (task.findtext(f"{MSPDI_NS}Finish") or "")[:16] or None,
                "total_float_hours": slack,
                "critical": (critical_el.text.strip() == "1") if critical_el is not None and critical_el.text else None,
                "baseline_start": bl_start,
                "baseline_finish": bl_finish,
            },
        }
        if manual:
            warnings.append(f"task {uid} is manually scheduled — its stored float/critical values "
                            f"are not engine-driven in MS Project either; treat with caution")
        tasks.append(t)
        for pl in task.findall(f"{MSPDI_NS}PredecessorLink"):
            pred = (pl.findtext(f"{MSPDI_NS}PredecessorUID") or "").strip()
            ltype = MSPDI_LINK_TYPES.get((pl.findtext(f"{MSPDI_NS}Type") or "1").strip(), "FS")
            lag = mspdi_slack_hours(pl.findtext(f"{MSPDI_NS}LinkLag")) or 0.0
            links.append({"pred": pred, "succ": uid, "type": ltype, "lag_hours": lag})

    if numbered_baselines:
        warnings.append(
            f"export carries additional numbered baselines ({', '.join(sorted(numbered_baselines))}) "
            f"beyond Baseline0 — only Baseline0 is written to the sidecar")

    # Some exporters omit <Duration>. Derive it from the stored dates via the task's own
    # calendar — warned, never silent — so the engine has real work content to schedule.
    derived = 0
    for t in tasks:
        if t["type"] == "task" and not t["duration_hours"]:
            st, fn = t["stored"].get("start"), t["stored"].get("finish")
            if st and fn:
                cal = Calendar(calendars.get(t.get("calendar_id") or "", None))
                hours = cal.working_hours_between(parse_dt(st), parse_dt(fn))
                # A date-only (or midnight/anchor-time) finish means "through the end of that
                # day" — working_hours_between measured to the day's 08:00 anchor, so the
                # finish day's own hours must be added to make the duration inclusive.
                if "T" not in fn or fn[11:16] in ("00:00", "08:00"):
                    hours += cal.day_hours(parse_dt(fn).date())
                t["duration_hours"] = round(max(hours, 0.0), 2)
                derived += 1
    if derived:
        warnings.append(f"<Duration> absent on {derived} task(s) — derived from stored start/finish "
                        f"via the task calendar (inclusive of the finish day where the export "
                        f"carries date-only finishes)")

    resources = {}
    for res in root.findall(f"{MSPDI_NS}Resources/{MSPDI_NS}Resource"):
        rid = (res.findtext(f"{MSPDI_NS}UID") or "").strip()
        resources[rid] = res.findtext(f"{MSPDI_NS}Name") or f"resource {rid}"
    n_assign = 0
    task_index = {t["id"]: t for t in tasks}
    for a in root.findall(f"{MSPDI_NS}Assignments/{MSPDI_NS}Assignment"):
        tid = (a.findtext(f"{MSPDI_NS}TaskUID") or "").strip()
        rid = (a.findtext(f"{MSPDI_NS}ResourceUID") or "").strip()
        units = a.findtext(f"{MSPDI_NS}Units")
        if tid in task_index and rid in resources:
            task_index[tid].setdefault("resources", []).append(
                {"name": resources[rid], "units": float(units) if units else None})
            n_assign += 1

    baseline_present = any(t["stored"].get("baseline_start") for t in tasks)
    return {
        "provenance": {
            "format": "MSPDI",
            "project_name": root.findtext(f"{MSPDI_NS}Name") or root.findtext(f"{MSPDI_NS}Title"),
            "data_date": status_date or None,
            "data_date_source": "StatusDate" if root.findtext(f"{MSPDI_NS}StatusDate") else "CurrentDate",
            "baseline_present": baseline_present,
            "resource_assignments": n_assign,
        },
        "calendars": calendars,
        "tasks": tasks,
        "links": links,
    }


# --------------------------------------------------------------------------- XER

def xer_tables(text: str) -> dict:
    tables: dict = {}
    current, fields = None, []
    for line in text.splitlines():
        if line.startswith("%T"):
            current = line.split("\t")[1].strip() if "\t" in line else line[2:].strip()
            tables[current] = []
            fields = []
        elif line.startswith("%F") and current:
            fields = [f.strip() for f in line.split("\t")[1:]]
        elif line.startswith("%R") and current and fields:
            vals = line.split("\t")[1:]
            row = {fields[i]: (vals[i].strip() if i < len(vals) else "") for i in range(len(fields))}
            tables[current].append(row)
    return tables


def xer_dt(s: str) -> str | None:
    if not s:
        return None
    s = s.strip()
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})(?:\s+(\d{2}):(\d{2}))?", s)
    if not m:
        return None
    if m.group(4):
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}T{m.group(4)}:{m.group(5)}"
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"


def parse_xer_calendar_data(clndr_data: str, warnings: list, cal_id: str) -> dict:
    """Best-effort parse of P6's packed clndr_data blob: weekly DaysOfWeek pattern and
    dated exceptions (Excel-serial dates, epoch 1899-12-30). Anything unparsed is warned."""
    spec: dict = {}
    week = None
    m = re.search(r"DaysOfWeek\(\)(.*?)(?:\(0\|\|(?:VIEW|Exceptions)|$)", clndr_data, re.S)
    if m:
        week = [0.0] * 7
        # entries look like (0||1()( ... f|s|<start>|f|<finish> ... )) where 1=Sunday..7=Saturday
        for day_m in re.finditer(r"\(0\|\|([1-7])\(\)\((.*?)\)\)", m.group(1), re.S):
            day_num = int(day_m.group(1))          # 1=Sun..7=Sat
            body = day_m.group(2)
            hours = 0.0
            for t_m in re.finditer(r"s\|(\d{2}):(\d{2})\|f\|(\d{2}):(\d{2})", body):
                fh = int(t_m.group(1)) + int(t_m.group(2)) / 60.0
                th = int(t_m.group(3)) + int(t_m.group(4)) / 60.0
                hours += max(th - fh, 0.0)
            week[(day_num + 5) % 7] = hours        # to Mon..Sun
    exceptions = []
    exc_m = re.search(r"Exceptions\(\)(.*)$", clndr_data, re.S)
    if exc_m:
        for e_m in re.finditer(r"\(0\|\|(\d{4,6})\(\)\((.*?)\)\)", exc_m.group(1), re.S):
            serial = int(e_m.group(1))
            d = date(1899, 12, 30) + timedelta(days=serial)
            body = e_m.group(2)
            hours = 0.0
            for t_m in re.finditer(r"s\|(\d{2}):(\d{2})\|f\|(\d{2}):(\d{2})", body):
                hours += max((int(t_m.group(3)) + int(t_m.group(4)) / 60.0)
                             - (int(t_m.group(1)) + int(t_m.group(2)) / 60.0), 0.0)
            exceptions.append({"date": d.isoformat(), "hours": hours})
    if week and any(h > 0 for h in week):
        spec["week"] = week
    if exceptions:
        spec["exceptions"] = exceptions
    if not spec:
        warnings.append(f"calendar {cal_id}: clndr_data present but no weekly pattern/exceptions "
                        f"recovered — day_hr_cnt fallback used")
    return spec


def parse_xer(text: str, warnings: list, project_filter: str | None, list_only: bool) -> dict:
    tables = xer_tables(text)
    projects = tables.get("PROJECT", [])
    real_projects = [p for p in projects if p.get("proj_short_name")]
    if list_only:
        return {"projects": [{"proj_id": p.get("proj_id"), "name": p.get("proj_short_name"),
                              "data_date": xer_dt(p.get("last_recalc_date", ""))} for p in real_projects]}
    if len(real_projects) > 1 and not project_filter:
        raise SystemExit(json.dumps({
            "error": "XER contains multiple projects — rerun with --project <proj_id>",
            "projects": [{"proj_id": p.get("proj_id"), "name": p.get("proj_short_name")} for p in real_projects],
        }))
    proj = real_projects[0] if not project_filter else next(
        (p for p in real_projects if p.get("proj_id") == project_filter), None)
    if proj is None:
        raise SystemExit(json.dumps({"error": f"proj_id {project_filter!r} not found in this XER"}))
    proj_id = proj.get("proj_id")

    calendars = {}
    for c in tables.get("CALNDR", tables.get("CALENDAR", [])):
        cid = c.get("clndr_id", "")
        spec: dict = {}
        if c.get("day_hr_cnt"):
            try:
                spec["hours_per_day"] = float(c["day_hr_cnt"])
            except ValueError:
                pass
        if c.get("clndr_data"):
            spec.update(parse_xer_calendar_data(c["clndr_data"], warnings, cid))
        if not spec:
            spec = {"hours_per_day": 8.0}
            warnings.append(f"calendar {cid}: no day_hr_cnt/clndr_data — 8h/day assumed")
        calendars[cid] = spec

    # WBS paths
    wbs_rows = {w.get("wbs_id"): w for w in tables.get("PROJWBS", [])}

    def wbs_path(wbs_id: str) -> str | None:
        parts, cur, hops = [], wbs_rows.get(wbs_id), 0
        while cur and hops < 20:
            nm = cur.get("wbs_name") or cur.get("wbs_short_name")
            if nm:
                parts.append(nm)
            cur = wbs_rows.get(cur.get("parent_wbs_id"))
            hops += 1
        return " / ".join(reversed(parts)) if parts else None

    # Activity codes
    code_types = {ct.get("actv_code_type_id"): ct.get("actv_code_type") for ct in tables.get("ACTVTYPE", [])}
    code_values = {cv.get("actv_code_id"): (code_types.get(cv.get("actv_code_type_id"), "code"),
                                            cv.get("short_name") or cv.get("actv_code_name"))
                   for cv in tables.get("ACTVCODE", [])}
    task_codes: dict = {}
    for ta in tables.get("TASKACTV", []):
        pair = code_values.get(ta.get("actv_code_id"))
        if pair:
            task_codes.setdefault(ta.get("task_id"), {})[pair[0]] = pair[1]

    # Resources
    rsrc_names = {r.get("rsrc_id"): (r.get("rsrc_name") or r.get("rsrc_short_name")) for r in tables.get("RSRC", [])}
    task_rsrc: dict = {}
    for tr in tables.get("TASKRSRC", []):
        if tr.get("proj_id") and tr.get("proj_id") != proj_id:
            continue
        nm = rsrc_names.get(tr.get("rsrc_id"))
        if nm:
            task_rsrc.setdefault(tr.get("task_id"), []).append({"name": nm, "units": None})

    baseline_evidence = False
    tasks, links = [], []
    hours_warn_emitted = False
    for row in tables.get("TASK", []):
        if row.get("proj_id") and row.get("proj_id") != proj_id:
            continue
        tid = row.get("task_id", "")
        ttype = row.get("task_type", "TT_Task")
        if ttype == "TT_WBS":
            continue
        milestone = ttype in ("TT_Mile", "TT_FinMile")
        cal_id = row.get("clndr_id") or ""
        if cal_id not in calendars and not hours_warn_emitted:
            warnings.append("one or more tasks reference calendars not present in the export — "
                            "8h/day assumed for those tasks")
            hours_warn_emitted = True
        cstr_raw = (row.get("cstr_type") or "").strip()
        constraint = None
        if cstr_raw:
            mapped = XER_CONSTRAINTS.get(cstr_raw)
            if mapped is None:
                warnings.append(f"unknown XER constraint code {cstr_raw!r} on task {tid} — surfaced, not mapped")
                mapped = f"UNKNOWN:{cstr_raw}"
            if mapped == "ALAP":
                warnings.append(f"task {tid} is As-Late-As-Possible — engine schedules it ASAP and flags it")
            constraint = {"type": mapped, "date": xer_dt(row.get("cstr_date", ""))}
        if row.get("cstr_type2"):
            warnings.append(f"task {tid} carries a secondary constraint ({row['cstr_type2']}) — "
                            f"recorded in warnings only; engine applies the primary constraint")
        for bl_field in ("bl_start_date", "bl1_start_date", "base_start_date"):
            if row.get(bl_field):
                baseline_evidence = True

        remain = row.get("remain_drtn_hr_cnt")
        target = row.get("target_drtn_hr_cnt")
        duration = float(target) if target else 0.0
        tasks.append({
            "id": tid,
            "code": row.get("task_code"),
            "name": row.get("task_name") or tid,
            "type": "milestone" if milestone else "task",
            "wbs": wbs_path(row.get("wbs_id", "")),
            "activity_codes": task_codes.get(tid) or None,
            "duration_hours": duration,
            "remaining_hours": float(remain) if remain else None,
            "pct_complete": float(row.get("phys_complete_pct") or 0),
            "pct_type": "physical",
            "status": row.get("status_code"),
            "actual_start": xer_dt(row.get("act_start_date", "")),
            "actual_finish": xer_dt(row.get("act_end_date", "")),
            "calendar_id": cal_id if cal_id in calendars else None,
            "constraint": constraint,
            "resources": task_rsrc.get(tid) or None,
            "stored": {
                "start": xer_dt(row.get("target_start_date", "")),
                "finish": xer_dt(row.get("target_end_date", "")),
                "total_float_hours": float(row["total_float_hr_cnt"]) if row.get("total_float_hr_cnt") else None,
                "critical": (float(row["total_float_hr_cnt"]) <= 0) if row.get("total_float_hr_cnt") else None,
                "criticality_source": "derived: total_float_hr_cnt <= 0 (P6 exports carry no explicit critical flag)",
            },
        })
    for row in tables.get("TASKPRED", []):
        links.append({
            "pred": row.get("pred_task_id", ""),
            "succ": row.get("task_id", ""),
            "type": XER_LINK_TYPES.get(row.get("pred_type", "PR_FS"), "FS"),
            "lag_hours": float(row.get("lag_hr_cnt") or 0),
        })

    if not baseline_evidence:
        warnings.append(
            "NO BASELINE in this XER: target_start/end are P6's CURRENT planned dates, not a "
            "baseline. A real P6 baseline needs bl_* fields or an attached baseline project — "
            "neither is present. Do not present these dates as 'the baseline'.")

    # Sparse exports may omit target_drtn_hr_cnt — derive from stored dates (inclusive of a
    # date-only finish day), warned, exactly as the MSPDI path does.
    derived = 0
    for t in tasks:
        if t["type"] == "task" and not t["duration_hours"]:
            st, fn = t["stored"].get("start"), t["stored"].get("finish")
            if st and fn:
                cal = Calendar(calendars.get(t.get("calendar_id") or "", None))
                hours = cal.working_hours_between(parse_dt(st), parse_dt(fn))
                if "T" not in fn or fn[11:16] in ("00:00", "08:00"):
                    hours += cal.day_hours(parse_dt(fn).date())
                t["duration_hours"] = round(max(hours, 0.0), 2)
                derived += 1
    if derived:
        warnings.append(f"target_drtn_hr_cnt absent on {derived} task(s) — duration derived from "
                        f"target start/finish via the task calendar")

    return {
        "provenance": {
            "format": "P6 XER",
            "project_name": proj.get("proj_short_name"),
            "proj_id": proj_id,
            "projects_in_file": len(real_projects),
            "data_date": xer_dt(proj.get("last_recalc_date", "")),
            "data_date_source": "last_recalc_date",
            "baseline_present": baseline_evidence,
            "stored_dates_are": "current planned dates (target_*)" if not baseline_evidence else "current planned dates; baseline fields also present",
        },
        "calendars": calendars,
        "tasks": tasks,
        "links": links,
    }


# --------------------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("export_file")
    ap.add_argument("--project", help="proj_id to import from a multi-project XER")
    ap.add_argument("--out", default="programme/programme-baseline.json")
    ap.add_argument("--list-projects", action="store_true")
    args = ap.parse_args()

    path = Path(args.export_file)
    if path.suffix.lower() in (".mpp", ".pp"):
        raise SystemExit(json.dumps({"error": f"{path.suffix} is a binary planning-tool format and "
                                              f"is never parsed — export XML/XER first"}))
    text, encoding = read_text(path)
    warnings: list = []

    if path.suffix.lower() == ".xer" or text.startswith("ERMHDR"):
        result = parse_xer(text, warnings, args.project, args.list_projects)
        if args.list_projects:
            json.dump(result, sys.stdout, indent=2)
            print()
            return 0
    else:
        result = parse_mspdi(text, warnings)

    result["provenance"]["source_file"] = path.name
    result["provenance"]["encoding"] = encoding
    result["provenance"]["parser"] = "gather-parse-programme v1"
    result["provenance"]["warnings"] = warnings
    result["provenance"]["task_count"] = sum(1 for t in result["tasks"] if t["type"] != "summary")
    result["provenance"]["milestone_count"] = sum(1 for t in result["tasks"] if t["type"] == "milestone")
    result["provenance"]["link_count"] = len(result["links"])

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        json.dump(result, f, indent=1, ensure_ascii=False)
    summary = {k: result["provenance"].get(k) for k in
               ("format", "project_name", "data_date", "baseline_present", "task_count",
                "milestone_count", "link_count", "encoding")}
    summary["warnings"] = warnings
    summary["sidecar"] = str(out)
    json.dump(summary, sys.stdout, indent=2, ensure_ascii=False)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
