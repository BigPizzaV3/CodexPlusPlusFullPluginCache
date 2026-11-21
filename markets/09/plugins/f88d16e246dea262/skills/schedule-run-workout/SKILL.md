---
name: schedule-run-workout
description: Turn a user-approved run into a structured Lion Lift workout. Use when the user asks to schedule a run; confirm the exact session and local date/time before creating it.
---

# Schedule a run workout

Create the run the user approved, using Lion Lift's structured run scheduling tool. A proposal from `propose-run-workout` is useful but not required; the user may supply their own session.

## Prepare the workout

- Resolve the user's local calendar date and start time, indoor or outdoor setting, warm-up, every work and recovery step, repeat counts, targets, and cool-down. Ask for any missing detail needed to create the intended session. Do not infer what “today” or “tomorrow” means near a date or time-zone boundary.
- Check Lion Lift's current scheduling tool schema before constructing the call. For the present `schedule_interval_run` tool, use a distinctive `display_name`, local `scheduled_for` in `YYYY-MM-DDTHH:MM` format, `location`, optional `warmup` and `cooldown`, and at least one block with `work`, optional `recovery`, and `iterations`.
- The current goal types are open, time (seconds), distance (miles), and energy (kilocalories). Convert units carefully. Available alerts include heart-rate, pace, power, and cadence targets. Use only targets the user approved and that the tool supports. Outdoor GPS is required for pace alerts; for indoor runs, omit pace alerts or use an approved heart-rate or cadence alert.
- Preserve the intended sequence. A repeated work/recovery pair can include recovery after its final repetition; if the user's plan ends on a work step, represent that explicitly with an appropriate final block. Do not silently add or remove recovery.

## Confirm and create

Before the write, show the complete workout in plain language: local date/time, title, location, warm-up, every block and repeat count, targets, recovery, and cool-down. Obtain the user's explicit confirmation of that exact session. A general request to schedule or approval of a different proposal is insufficient if these details have changed.

After confirmation, call the scheduling tool once. If the result is uncertain, inspect the run-workout list for a matching record before retrying; avoid duplicates. Report the created title, scheduled local time, and returned status. The record is pending until the user opens Lion Lift and uses **Workouts → Run → Sync Workouts** to put it in Apple Fitness/on the Watch. If the write fails, state the failure without implying that the workout was scheduled.
