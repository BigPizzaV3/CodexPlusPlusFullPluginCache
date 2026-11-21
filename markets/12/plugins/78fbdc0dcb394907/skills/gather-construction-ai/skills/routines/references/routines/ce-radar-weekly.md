## ce-radar-weekly

**Cadence:** Weekly, Mondays, 08:00 (after time-bar-sweep — the two are complementary)
**Surface:** Desktop
**Prerequisites:** `ce-register.md`; `contract-profile.md` (as-amended notification periods); `{{FOLDER}}/routine-state/ce-radar-weekly/last-run.md`
**Priority:** Recommended — the claims you were about to lose, found while they are still notifiable

**Instructions:**
```
Run $ce-radar for {{PROJECT}} over the trailing 4 weeks ending on the Sunday before this
scheduled Monday run — use that explicit end date as the review date, so the time-bar clocks
are computed against a stated date, not "today" on a late catch-up.

Use the contract profile in this folder for the as-amended notification periods; if it is
absent, keep the radar's unamended-assumed caveat visible in the reply. Cross-check every
candidate against {{FOLDER}}/ce-register.md. The distinction from time-bar-sweep: that routine
ages known candidates against the 61.3 clock; this one hunts for candidates nobody has logged —
half-filled and conflicting records graded, not skipped. An early warning is "notified", never
"raised".

Read and update {{FOLDER}}/routine-state/ce-radar-weekly/last-run.md — report only candidates
that are new or whose verdict/clock worsened since last week; a candidate already reported and
unchanged gets one carried-forward line at most.
End with ACTION AVAILABLE NOW: for each new candidate, the single next move (notify an EW,
complete the named half-filled record in Gather, obtain the weather comparison data, or run
$ce-builder). If the sweep finds nothing new, reply in three lines and stop.
```
