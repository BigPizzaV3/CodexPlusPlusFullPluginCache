## eac-drift

**Cadence:** Monthly, the 1st (or shortly after month-end-close), 08:00
**Surface:** Desktop
**Prerequisites:** `{{FOLDER}}/routine-state/eac-drift/last-run.md` (required — this routine exists specifically to diff against it)
**Priority:** Standard

**Instructions:**
```
Run $cost-to-complete for {{PROJECT}} to date. Read
{{FOLDER}}/routine-state/eac-drift/last-run.md for the previous estimate-at-completion figure —
if the file doesn't exist yet, save this run's EAC as the baseline and stop (nothing to compare
yet).
Compare this run's EAC to the saved figure. Speak only if the forecast moved by more than 10% in
either direction — state the old figure, the new figure, and the single largest driver of the
move. Update {{FOLDER}}/routine-state/eac-drift/last-run.md with this run's EAC regardless.
If the move is 10% or less, reply in one line: "EAC stable — no material drift." and stop.
Silence is the feature here, not a shortfall.
```
