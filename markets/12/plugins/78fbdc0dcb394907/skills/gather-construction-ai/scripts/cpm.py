#!/usr/bin/env python3
"""cpm.py — deterministic CPM engine for the Gather plugin.

Forward/backward pass over an imported programme network (the JSON sidecar written by
scripts/parse_programme.py), with working-time calendars (weekly patterns + dated
exceptions), constraint handling, in-progress roll-forward to a status date, and fragnet
insertion for impact runs.

WHY THIS EXISTS AS CODE: the plugin's Pattern 15 forbids presenting model-arithmetic as a
schedule. This engine is deterministic, unit-tested (tests/unit/test_cpm.py runs in CI), and
every consumer labels its output INDICATIVE — the stored programme remains the only source
for "the Accepted Programme says…". The engine never writes to the sidecar.

Usage:
    python3 cpm.py <sidecar.json> [--impact <impact.json>] [--status-date ISO] [--self-check]

Input sidecar schema (subset relevant here):
    calendars: {id: {hours_per_day, week: [7 floats, Mon..Sun hours], exceptions:
                     [{date: "YYYY-MM-DD", hours: float}]}}
    tasks: [{id, name, type: "task"|"milestone", duration_hours, remaining_hours?,
             pct_complete?, actual_start?, actual_finish?, calendar_id?,
             constraint?: {type, date}, stored: {start, finish, total_float_hours?,
             critical?}}]
    links: [{pred, succ, type: "FS"|"SS"|"FF"|"SF", lag_hours}]

Impact spec schema:
    {"changes": [{"task_id": str, "delay_hours"?: float, "new_duration_hours"?: float}],
     "fragnet": {"tasks": [...same as tasks...], "links": [...same as links...]}}

Output (JSON to stdout): per-task early/late start/finish (ISO minutes), total_float_hours,
critical flag, project finish, and — with --self-check — a comparison of computed vs stored
dates with a match percentage (the per-file trust calibrator).

Constraint types (MSPDI names; parser maps P6 codes onto these):
    ASAP (default), SNET (start no earlier), SNLT (start no later), FNET (finish no
    earlier), FNLT (finish no later), MSO (must start on), MFO (must finish on).

Stdlib only. No network, no writes.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, time, timedelta

ISO_MIN = "%Y-%m-%dT%H:%M"

DEFAULT_WEEK = [8.0, 8.0, 8.0, 8.0, 8.0, 0.0, 0.0]  # Mon..Sun
WORK_DAY_START = time(8, 0)  # nominal in-day anchor; affects display, not durations


class Calendar:
    """Working-time calendar: weekly hour pattern + dated exceptions (hours override)."""

    def __init__(self, spec: dict | None):
        spec = spec or {}
        week = spec.get("week")
        if not week or len(week) != 7:
            hpd = float(spec.get("hours_per_day", 8.0) or 8.0)
            week = [hpd, hpd, hpd, hpd, hpd, 0.0, 0.0]
        self.week = [float(h) for h in week]
        self.exceptions = {}
        for ex in spec.get("exceptions", []) or []:
            self.exceptions[ex["date"]] = float(ex.get("hours", 0.0) or 0.0)
        if all(h == 0 for h in self.week) and not any(self.exceptions.values()):
            # A calendar with no working time would loop forever; treat as standard week.
            self.week = list(DEFAULT_WEEK)

    def day_hours(self, d: date) -> float:
        key = d.isoformat()
        if key in self.exceptions:
            return self.exceptions[key]
        return self.week[d.weekday()]

    def is_working(self, d: date) -> bool:
        return self.day_hours(d) > 0.0

    def add_hours(self, start: datetime, hours: float) -> datetime:
        """Advance start by `hours` of working time. Position within a day is tracked in
        hours-worked-so-far-today, derived from the anchor time."""
        if hours <= 0:
            return self.roll_forward(start)
        cur_day = start.date()
        # hours already consumed today before `start`
        day_len = self.day_hours(cur_day)
        consumed = min(max((start - datetime.combine(cur_day, WORK_DAY_START)).total_seconds() / 3600.0, 0.0), day_len)
        remaining = hours
        while True:
            avail = self.day_hours(cur_day) - consumed
            if avail > 0:
                if remaining <= avail + 1e-9:
                    return datetime.combine(cur_day, WORK_DAY_START) + timedelta(hours=consumed + remaining)
                remaining -= avail
            cur_day = cur_day + timedelta(days=1)
            consumed = 0.0

    def sub_hours(self, finish: datetime, hours: float) -> datetime:
        """Step back by `hours` of working time from `finish`."""
        if hours <= 0:
            return self.roll_back(finish)
        cur_day = finish.date()
        day_len = self.day_hours(cur_day)
        consumed = min(max((finish - datetime.combine(cur_day, WORK_DAY_START)).total_seconds() / 3600.0, 0.0), day_len)
        remaining = hours
        while True:
            if consumed > 0:
                if remaining <= consumed + 1e-9:
                    return datetime.combine(cur_day, WORK_DAY_START) + timedelta(hours=consumed - remaining)
                remaining -= consumed
            cur_day = cur_day - timedelta(days=1)
            consumed = self.day_hours(cur_day)

    def roll_forward(self, dt: datetime) -> datetime:
        """Snap to the next instant with working time available (for zero-duration moves)."""
        cur_day = dt.date()
        day_len = self.day_hours(cur_day)
        consumed = max((dt - datetime.combine(cur_day, WORK_DAY_START)).total_seconds() / 3600.0, 0.0)
        while day_len <= 0 or consumed >= day_len:
            cur_day = cur_day + timedelta(days=1)
            consumed = 0.0
            day_len = self.day_hours(cur_day)
        return datetime.combine(cur_day, WORK_DAY_START) + timedelta(hours=consumed)

    def roll_back(self, dt: datetime) -> datetime:
        cur_day = dt.date()
        consumed = max((dt - datetime.combine(cur_day, WORK_DAY_START)).total_seconds() / 3600.0, 0.0)
        while self.day_hours(cur_day) <= 0 or consumed <= 0:
            cur_day = cur_day - timedelta(days=1)
            consumed = self.day_hours(cur_day)
        return datetime.combine(cur_day, WORK_DAY_START) + timedelta(hours=min(consumed, self.day_hours(cur_day)))

    def working_hours_between(self, a: datetime, b: datetime) -> float:
        """Signed working hours from a to b (negative if b < a)."""
        if b < a:
            return -self.working_hours_between(b, a)
        total = 0.0
        cur_day = a.date()
        while cur_day <= b.date():
            day_len = self.day_hours(cur_day)
            day_anchor = datetime.combine(cur_day, WORK_DAY_START)
            lo = max((a - day_anchor).total_seconds() / 3600.0, 0.0) if cur_day == a.date() else 0.0
            hi = min(max((b - day_anchor).total_seconds() / 3600.0, 0.0), day_len) if cur_day == b.date() else day_len
            lo = min(lo, day_len)
            total += max(hi - lo, 0.0)
            cur_day += timedelta(days=1)
        return total


def parse_dt(s: str | None) -> datetime | None:
    if not s:
        return None
    s = s.strip()
    for fmt in (ISO_MIN, "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(s.replace("Z", ""), fmt)
            if fmt == "%Y-%m-%d":
                dt = datetime.combine(dt.date(), WORK_DAY_START)
            return dt
        except ValueError:
            continue
    raise ValueError(f"unparseable date: {s!r}")


class Task:
    def __init__(self, spec: dict, calendars: dict):
        self.id = str(spec["id"])
        self.name = spec.get("name", self.id)
        self.milestone = spec.get("type") == "milestone"
        self.duration = 0.0 if self.milestone else float(spec.get("duration_hours", 0.0) or 0.0)
        self.remaining = spec.get("remaining_hours")
        self.remaining = float(self.remaining) if self.remaining is not None else None
        self.pct = float(spec.get("pct_complete", 0.0) or 0.0)
        self.actual_start = parse_dt(spec.get("actual_start"))
        self.actual_finish = parse_dt(spec.get("actual_finish"))
        self.cal = calendars.get(spec.get("calendar_id") or "", calendars.get("", None)) or Calendar(None)
        c = spec.get("constraint") or {}
        self.cstr_type = (c.get("type") or "ASAP").upper()
        self.cstr_date = parse_dt(c.get("date"))
        self.stored = spec.get("stored") or {}
        # results
        self.es = self.ef = self.ls = self.lf = None
        self.float_hours = None
        self.critical = False

    def working_duration(self, status: datetime | None) -> float:
        """Working content to schedule. WITHOUT a status date the engine runs in
        reproduction mode — full durations, so computed dates are comparable with the
        file's stored schedule (the self-check depends on this). WITH a status date it
        runs in roll-forward mode — remaining work resumes at the status date."""
        if self.actual_finish:
            return 0.0
        if status is None:
            return self.duration
        if self.remaining is not None:
            return self.remaining
        if self.actual_start and self.pct > 0:
            return self.duration * max(0.0, 1.0 - self.pct / 100.0)
        return self.duration


def topo_order(tasks: dict, preds: dict) -> list:
    indeg = {tid: 0 for tid in tasks}
    succs = {tid: [] for tid in tasks}
    for tid, plist in preds.items():
        for (p, _t, _l) in plist:
            if p in tasks:
                indeg[tid] += 1
                succs[p].append(tid)
    queue = sorted([t for t, d in indeg.items() if d == 0])
    order = []
    while queue:
        n = queue.pop(0)
        order.append(n)
        for s in sorted(succs[n]):
            indeg[s] -= 1
            if indeg[s] == 0:
                queue.append(s)
    if len(order) != len(tasks):
        cyc = sorted(set(tasks) - set(order))
        raise SystemExit(json.dumps({"error": "logic loop detected", "tasks_in_cycle": cyc}))
    return order


def schedule(data: dict, impact: dict | None = None, status_date: str | None = None) -> dict:
    calendars = {cid: Calendar(cspec) for cid, cspec in (data.get("calendars") or {}).items()}
    if "" not in calendars:
        calendars[""] = Calendar(None)

    task_specs = {str(t["id"]): dict(t) for t in data.get("tasks", [])
                  if t.get("type") != "summary"}
    links = [dict(l) for l in data.get("links", [])]

    # Apply impact spec: duration changes/delays and fragnet insertion.
    applied_changes = []
    if impact:
        for ch in impact.get("changes", []) or []:
            tid = str(ch["task_id"])
            if tid not in task_specs:
                raise SystemExit(json.dumps({"error": f"impact change targets unknown task {tid}"}))
            spec = task_specs[tid]
            if "new_duration_hours" in ch:
                spec["duration_hours"] = float(ch["new_duration_hours"])
                spec.pop("remaining_hours", None)
                applied_changes.append(f"{tid}: duration set to {ch['new_duration_hours']}h")
            if "delay_hours" in ch:
                base = float(spec.get("remaining_hours") if spec.get("remaining_hours") is not None
                             else spec.get("duration_hours", 0.0) or 0.0)
                if spec.get("remaining_hours") is not None:
                    spec["remaining_hours"] = base + float(ch["delay_hours"])
                else:
                    spec["duration_hours"] = base + float(ch["delay_hours"])
                applied_changes.append(f"{tid}: +{ch['delay_hours']}h")
        frag = impact.get("fragnet") or {}
        for t in frag.get("tasks", []) or []:
            task_specs[str(t["id"])] = dict(t)
            applied_changes.append(f"fragnet task {t['id']} inserted")
        links.extend(dict(l) for l in frag.get("links", []) or [])

    tasks = {tid: Task(spec, calendars) for tid, spec in task_specs.items()}

    preds: dict = {tid: [] for tid in tasks}
    succs_map: dict = {tid: [] for tid in tasks}
    for l in links:
        p, s = str(l["pred"]), str(l["succ"])
        if p in tasks and s in tasks:
            entry = (p, (l.get("type") or "FS").upper(), float(l.get("lag_hours", 0.0) or 0.0))
            preds[s].append(entry)
            succs_map[p].append((s, entry[1], entry[2]))

    order = topo_order(tasks, preds)
    status = parse_dt(status_date) if status_date else None

    default_start = None
    for t in tasks.values():
        st = parse_dt((t.stored or {}).get("start"))
        if st and (default_start is None or st < default_start):
            default_start = st
    if status and (default_start is None or status > default_start):
        project_open = status
    else:
        project_open = default_start or datetime.combine(date.today(), WORK_DAY_START)

    # ---- forward pass ----
    for tid in order:
        t = tasks[tid]
        cal = t.cal
        if t.actual_finish:
            t.es, t.ef = t.actual_start or t.actual_finish, t.actual_finish
            continue
        cands = []
        for (p, ltype, lag) in preds[tid]:
            pt = tasks[p]
            if ltype == "FS":
                cands.append(cal.add_hours(pt.ef, lag) if lag else pt.ef)
            elif ltype == "SS":
                cands.append(cal.add_hours(pt.es, lag) if lag else pt.es)
            elif ltype == "FF":
                fin = cal.add_hours(pt.ef, lag) if lag else pt.ef
                cands.append(cal.sub_hours(fin, t.working_duration(status)))
            elif ltype == "SF":
                fin = cal.add_hours(pt.es, lag) if lag else pt.es
                cands.append(cal.sub_hours(fin, t.working_duration(status)))
        es = max(cands) if cands else project_open
        if t.actual_start and not t.actual_finish:
            es = max(t.actual_start, status or t.actual_start)
            if status and t.actual_start <= status:
                es = status  # remaining work resumes at the status date
        # constraints (forward-pass side)
        if t.cstr_type in ("SNET",) and t.cstr_date:
            es = max(es, t.cstr_date)
        if t.cstr_type in ("MSO",) and t.cstr_date:
            es = t.cstr_date
        if t.cstr_type in ("FNET",) and t.cstr_date:
            es = max(es, cal.sub_hours(t.cstr_date, t.working_duration(status)))
        if t.cstr_type in ("MFO",) and t.cstr_date:
            es = cal.sub_hours(t.cstr_date, t.working_duration(status))
        if t.working_duration(status) > 0:
            es = cal.roll_forward(es)
            t.es = es
            t.ef = cal.add_hours(es, t.working_duration(status))
        else:
            # Zero-duration (milestones): attach at the driving instant — do not roll a
            # milestone past its predecessor's finish onto the next working morning; the
            # planning tools place it on the same day. Roll only off fully non-working days.
            if not cal.is_working(es.date()):
                es = cal.roll_forward(es)
            t.es = es
            t.ef = es

    project_finish = max((t.ef for t in tasks.values()), default=project_open)

    # ---- backward pass ----
    for tid in reversed(order):
        t = tasks[tid]
        cal = t.cal
        if t.actual_finish:
            t.lf, t.ls = t.ef, t.es
            t.float_hours = 0.0
            continue
        cands = []
        for (s, ltype, lag) in succs_map[tid]:
            st = tasks[s]
            if ltype == "FS":
                cands.append(cal.sub_hours(st.ls, lag) if lag else st.ls)
            elif ltype == "SS":
                start_bound = cal.sub_hours(st.ls, lag) if lag else st.ls
                cands.append(cal.add_hours(start_bound, t.working_duration(None)))
            elif ltype == "FF":
                cands.append(cal.sub_hours(st.lf, lag) if lag else st.lf)
            elif ltype == "SF":
                start_bound = cal.sub_hours(st.lf, lag) if lag else st.lf
                cands.append(cal.add_hours(start_bound, t.working_duration(None)))
        lf = min(cands) if cands else project_finish
        if t.cstr_type in ("FNLT", "MFO") and t.cstr_date:
            lf = min(lf, t.cstr_date)
        if t.cstr_type in ("SNLT",) and t.cstr_date:
            lf = min(lf, t.cal.add_hours(t.cstr_date, t.working_duration(None)))
        t.lf = lf
        t.ls = cal.sub_hours(lf, t.working_duration(None)) if t.working_duration(None) > 0 else lf
        t.float_hours = round(t.cal.working_hours_between(t.es, t.ls), 2)
        t.critical = t.float_hours <= 0.005

    # ---- output ----
    out_tasks = {}
    for tid, t in tasks.items():
        out_tasks[tid] = {
            "name": t.name,
            "early_start": t.es.strftime(ISO_MIN),
            "early_finish": t.ef.strftime(ISO_MIN),
            "late_start": t.ls.strftime(ISO_MIN),
            "late_finish": t.lf.strftime(ISO_MIN),
            "total_float_hours": t.float_hours,
            "critical": t.critical,
            "constraint": t.cstr_type if t.cstr_type != "ASAP" else None,
        }
    result = {
        "engine": "gather-cpm",
        "indicative": True,
        "banner": ("INDICATIVE recalculation performed outside the planning tool - not the "
                   "Accepted Programme; verify in P6/MSP/Asta before relying on it."),
        "status_date": status.strftime(ISO_MIN) if status else None,
        "applied_changes": applied_changes,
        "project_finish": project_finish.strftime(ISO_MIN),
        "tasks": out_tasks,
    }
    return result


def self_check(data: dict, result: dict) -> dict:
    """Compare engine-computed dates against the file's stored dates: the per-file trust
    calibrator. A high match means the sidecar's network model explains the stored programme;
    mismatches usually mean calendars/constraints the export carries but the model lacks."""
    rows, matched = [], 0
    for t in data.get("tasks", []):
        tid = str(t["id"])
        if t.get("type") == "summary" or tid not in result["tasks"]:
            continue
        stored = t.get("stored") or {}
        ss, sf = stored.get("start"), stored.get("finish")
        if not ss or not sf:
            continue
        cs = result["tasks"][tid]["early_start"][:10]
        cf = result["tasks"][tid]["early_finish"][:10]
        ok = (cs == ss[:10]) and (cf == sf[:10])
        matched += ok
        rows.append({"id": tid, "stored": [ss[:10], sf[:10]], "computed": [cs, cf], "match": ok})
    total = len(rows)
    return {
        "compared": total,
        "matched": matched,
        "match_pct": round(100.0 * matched / total, 1) if total else None,
        "verdict": ("network model reproduces the stored programme" if total and matched == total
                    else "stored dates diverge from the modelled network - calendars/constraints "
                         "not captured in the sidecar are likely driving the difference; treat "
                         "indicative results with that caveat"),
        "mismatches": [r for r in rows if not r["match"]][:25],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("sidecar")
    ap.add_argument("--impact")
    ap.add_argument("--status-date")
    ap.add_argument("--self-check", action="store_true")
    args = ap.parse_args()

    with open(args.sidecar, encoding="utf-8") as f:
        data = json.load(f)
    impact = None
    if args.impact:
        with open(args.impact, encoding="utf-8") as f:
            impact = json.load(f)

    result = schedule(data, impact=impact, status_date=args.status_date)
    if args.self_check:
        result["self_check"] = self_check(data, result)
    json.dump(result, sys.stdout, indent=2)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
