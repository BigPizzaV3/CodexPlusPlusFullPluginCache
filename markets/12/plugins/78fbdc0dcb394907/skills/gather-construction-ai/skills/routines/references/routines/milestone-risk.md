## milestone-risk

**Cadence:** Weekly, e.g. Wednesdays, 08:00
**Surface:** Cloud ☁ or Desktop
**Prerequisites:** `{{FOLDER}}/routine-state/milestone-risk/last-run.md` (Desktop only); `contract-profile.md` optional
**Priority:** Standard

**Instructions:**
```
Window = the trailing 8 weeks of run-rate data ending on this scheduled run date (explicit date;
a late catch-up keeps the same window, not "today").

Run $programme for {{PROJECT}} over that window — schedule-risk ranking from current run
rates (not critical path; no logic data available from the API). If a contract profile is
present in this folder, cross-check its key_dates against the forecast and flag any date the
run-rate no longer supports.
Read and update {{FOLDER}}/routine-state/milestone-risk/last-run.md — report only milestones
whose risk band changed since last week. (Running stateless with no prior file: report the full
ranking once.)
If nothing changed, reply in three lines and stop.
```
