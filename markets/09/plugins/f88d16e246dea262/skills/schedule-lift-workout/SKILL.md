---
name: schedule-lift-workout
description: Turn a user-approved lift into a scheduled Lion Lift session. Use when the user asks to schedule a lift; confirm the date and every exercise's exact sets, weights, and reps before creating it.
---

# Schedule a lift workout

Create the lift the user approved using Lion Lift's lift scheduling tool. A proposal from `propose-lift-workout` is useful but not required.

## Prepare the workout

- Resolve the user's local calendar date, exercise order, every set's reps and weight, and any notes. The present tool schedules by date, not start time. Confirm ambiguous “today” or “tomorrow” near a date or time-zone boundary.
- Check Lion Lift's current scheduling schema. Call `list_known_exercises` before `schedule_lift` and use familiar catalog names where they match the intended movements. Do not silently substitute a different exercise; the app permits free-text names when needed.
- The present `schedule_lift` tool requires `scheduled_date` (`YYYY-MM-DD`) and `lifts`, each with a name and sets of numeric `weight` and `reps`; `notes` is optional. Weight is in pounds, with no separate unit field. Convert any other units carefully and show the converted values before confirmation.
- Resolve proposal ranges or effort cues into exact set values before scheduling. Do not invent loads from an effort target or use zero to represent bodyweight without confirming what the user wants logged. If a requested element, such as timed holds or rest periods, cannot be encoded as sets of weight and reps, explain the limitation and agree on a faithful notes-based representation or leave it out.

## Confirm and create

Before the write, show the exact calendar date, each exercise and every set's weight in pounds and reps, plus the notes that will be saved. Obtain explicit confirmation of that complete record. If details changed since the proposal, confirm the revised version.

After confirmation, call `schedule_lift` once. If the result is uncertain, inspect the relevant scheduled lift records before retrying; avoid duplicates. Report the scheduled date and returned status. If the write fails, state the failure without implying that the workout was scheduled.
