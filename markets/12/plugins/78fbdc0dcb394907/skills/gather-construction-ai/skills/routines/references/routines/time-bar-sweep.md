## time-bar-sweep

**Cadence:** Weekly, Mondays, 07:30
**Surface:** Desktop
**Prerequisites:** `contract-profile.md` (amended 61.3 period); `ce-register.md`; `{{FOLDER}}/routine-state/time-bar-sweep/last-run.md`
**Priority:** Recommended starter — the most expensive QS mistake, made structurally hard to commit

**Instructions:**
```
Window = the trailing 8 weeks ending on the Sunday before this scheduled Monday run — use that
explicit end date; a late catch-up still covers the same 8-week window, not a window ending
"today".

Run $events for {{PROJECT}} over that window, using the contract profile in this folder.
Cross-check every candidate against {{FOLDER}}/ce-register.md by date and description. For any
candidate with no matching "Notified date" and an aware date 6+ weeks old, run
$nec-deadlines to compute the exact 61.3 deadline (per the contract profile if amended)
and report the specific date it falls due or has passed. An early warning is "notified", never
"raised" — do not conflate an EW with a 61.3 CE notification. Append any newly-spotted
candidates as a suggested row per this file's ce-register.md schema.
Read and update {{FOLDER}}/routine-state/time-bar-sweep/last-run.md — report only new or
worsened aged candidates since last week.
End with ACTION AVAILABLE NOW: the specific notification each aged candidate needs today.
If nothing is aged past 4 weeks, reply in three lines and stop.
```
