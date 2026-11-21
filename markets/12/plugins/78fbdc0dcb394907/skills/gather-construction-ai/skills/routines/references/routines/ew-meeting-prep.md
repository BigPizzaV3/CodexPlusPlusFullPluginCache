## ew-meeting-prep

**Cadence:** Scheduled to the project's early-warning-meeting cadence, {{MEETING_DAY}} before each meeting, morning
**Surface:** Desktop
**Prerequisites:** `{{FOLDER}}/routine-state/ew-meeting-prep/last-run.md` (required — "since last meeting" is the whole point); `contract-profile.md` optional
**Priority:** Standard

**Instructions:**
```
Read {{FOLDER}}/routine-state/ew-meeting-prep/last-run.md for the date of the last EW meeting —
if absent, treat the trailing 4 weeks as the window and say so.

For {{PROJECT}}, covering that window to {{MEETING_DAY}}: run $events for new candidate
events since the last meeting, $asbuilt-programme for any newly-dormant activities, and
list open risks still unresolved from the last meeting's notes (if recorded in the state file).
Use "notified" for any early warning, never "raised" — this agenda drafts itself from what's
actually open, not from a template. Group by: new since last meeting / still open / closed since
last meeting.
Update {{FOLDER}}/routine-state/ew-meeting-prep/last-run.md with this meeting's date and the
still-open items for next time.
If nothing is new or open, reply in three lines: no agenda items this cycle.
```
