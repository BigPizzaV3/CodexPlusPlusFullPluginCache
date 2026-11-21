## dormancy-watch

**Cadence:** Weekly, e.g. Mondays or Fridays, 08:00
**Surface:** Desktop
**Prerequisites:** `{{FOLDER}}/routine-state/dormancy-watch/last-run.md`; no profiles needed
**Priority:** Standard

**Instructions:**
```
Window = the trailing 8 weeks ending on this scheduled run date (explicit date, not "today" —
catch-up runs keep the same window).

Run $asbuilt-programme for {{PROJECT}} over that window in dormancy-detection mode:
list activities with no recorded output for 5+ working days, with the last-active date for
each. These are early-warning candidates before they harden into delay entries — say so plainly
for any new dormancy since last run.
Read and update {{FOLDER}}/routine-state/dormancy-watch/last-run.md — report only newly-dormant
or newly-reactivated activities.
If nothing has changed since last week, reply in two lines and stop.
```
