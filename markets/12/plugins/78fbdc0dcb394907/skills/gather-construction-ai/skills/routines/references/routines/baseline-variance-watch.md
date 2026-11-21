## baseline-variance-watch

**Cadence:** Weekly, e.g. Thursdays, 08:00
**Surface:** Desktop
**Prerequisites:** `programme/programme-baseline.md` with a confirmed activity mapping; `{{FOLDER}}/routine-state/baseline-variance-watch/last-run.md`
**Priority:** Standard

**Instructions:**
```
Run the Programme Advisor baseline-vs-actual comparison (Mode 2) for {{PROJECT}} over the
user-confirmed mapping: planned vs actual start/finish per mapped activity, dormancy against
the baseline window, milestone variance.

Read {{FOLDER}}/routine-state/baseline-variance-watch/last-run.md and report only activities
whose variance is new or worsened since last week, ranked with stored-critical activities
first (criticality as stored in the import at its data date — never recomputed). An activity
that is newly late AND flagged critical in the stored programme is the lead item, and it ends
with the action available now: an early warning to notify, or a re-sequence to request from
the planner. Unmapped activities are listed once, not re-litigated weekly.
If nothing changed, reply in three lines and stop. Timing language is "coincides with",
never "caused by".
```
