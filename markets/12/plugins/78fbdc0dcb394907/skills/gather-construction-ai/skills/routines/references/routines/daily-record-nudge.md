## daily-record-nudge

**Cadence:** Daily, weekday mornings, 08:00
**Surface:** Desktop
**Prerequisites:** `{{FOLDER}}/routine-state/daily-record-nudge/last-run.md`; no profile needed
**Priority:** Recommended starter (3rd) — fixes gaps while memory is fresh

**Instructions:**
```
Target date = the calendar day before this task's most recently scheduled weekday slot (08:00
Mon–Fri) — if this run is a late catch-up after a skipped day, cover the missed target date
specifically, do not shift to literal "yesterday" relative to whenever this actually fires.

Run $data-quality for {{PROJECT}} covering only the target date, including the
duplicate check — the same person on two overlapping shifts, or the same shift entered twice,
is flagged as a candidate pair while whoever entered it still remembers which is right. List
missing narratives/photos per supervisor by name. Read
{{FOLDER}}/routine-state/daily-record-nudge/last-run.md first — if the same supervisor appears
for a 3rd+ consecutive day, flag it as a coaching pattern, not just today's gap. Save today's
findings back to that file at the end.
If the record set is clean (no missing narratives, no missing photos), reply in two lines and
stop.
```
