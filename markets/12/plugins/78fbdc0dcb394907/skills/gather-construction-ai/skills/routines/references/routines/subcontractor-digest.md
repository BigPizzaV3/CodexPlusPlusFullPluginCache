## subcontractor-digest

**Cadence:** Weekly, e.g. Fridays, 16:00 (ahead of month-end applications)
**Surface:** Desktop
**Prerequisites:** `{{FOLDER}}/routine-state/subcontractor-digest/last-run.md`; `commercial-profile.md` optional (package names only, no rates needed)
**Priority:** Standard

**Instructions:**
```
Window = Monday to Sunday of the week ending on this scheduled run date (explicit dates, not
"this week" relative to fire time).

Run $labour for {{PROJECT}} over that week, broken down by trade/subcontractor. Produce a
recorded hours/attendance baseline per subcontractor — this is the pre-agreed figure their
month-end application gets checked against later via $subcontractor-check, so state it as
a baseline, not a verdict.
Read and update {{FOLDER}}/routine-state/subcontractor-digest/last-run.md — flag only
subcontractors whose weekly hours moved by more than 20% week-on-week.
If nothing moved materially, reply in two lines and stop.
```
