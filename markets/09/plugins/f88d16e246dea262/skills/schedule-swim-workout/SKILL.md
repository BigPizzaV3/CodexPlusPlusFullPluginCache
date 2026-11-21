---
name: schedule-swim-workout
description: Turn a user-approved pool swim into a structured Lion Lift workout. Use when the user asks to schedule a swim; confirm the exact session and local date/time before creating it.
---

# Schedule a swim workout

Create the pool swim the user approved using Lion Lift's structured swim scheduling tool. A proposal from `propose-swim-workout` is useful but not required.

## Prepare the workout

- Resolve the user's local calendar date and start time, warm-up, every work and recovery step, repeat counts, strokes, targets, and cool-down. Ask for missing details needed to preserve the intended session. Do not infer what “today” or “tomorrow” means near a date or time-zone boundary.
- Check Lion Lift's current scheduling schema before constructing the call. The present `schedule_pool_swim_workout` tool requires a distinctive `display_name`, local `scheduled_for` in `YYYY-MM-DDTHH:MM` format, and at least one block with `work`, optional `recovery`, and `iterations`. `warmup` and `cooldown` are optional single steps. Use each step's `display_name` for its stroke or purpose.
- Current goal types are open, time (seconds), distance (meters), energy (kilocalories), and `poolSwimDistanceWithTime` (both meters and seconds must be met). Convert units carefully. A conventional swim send-off may need explicit recovery or a different representation; do not assume the combined distance-and-time goal behaves like a send-off. If the desired timing cannot be represented faithfully, explain the limitation and ask the user to approve a concrete alternative.
- Current alerts support heart rate, power, and stroke cadence, but no pool pace alert. Use only supported targets the user approved. The scheduling tool has no pool-length parameter; the swimmer sets pool length in the Watch workout. It does not support open-water swim scheduling.
- Preserve the intended sequence. A repeated work/recovery pair can include recovery after its final repetition; if the plan ends on work, represent that explicitly. Do not silently add or remove rest or change the total distance.

## Confirm and create

Before the write, show the complete workout in plain language: local date/time, title, warm-up, every set and repeat count, strokes, targets, recovery, cool-down, and any unit conversion or representation change. Obtain the user's explicit confirmation of that exact session. If details changed since the proposal, confirm the revised version.

After confirmation, call the scheduling tool once. If the result is uncertain, inspect the swim-workout list for a matching record before retrying; avoid duplicates. Report the created title, scheduled local time, and returned status. The record is pending until the user opens Lion Lift and uses **Workouts → Swim → Sync Workouts** to put it in Apple Fitness/on the Watch. If the write fails, state the failure without implying that the workout was scheduled.
