---
name: schedule-bike-workout
description: Turn a user-approved ride into a structured Lion Lift cycling workout. Use when the user asks to schedule a bike workout; confirm the exact session and local date/time before creating it.
---

# Schedule a bike workout

Create the ride the user approved using Lion Lift's structured bike scheduling tool. A proposal from `propose-bike-workout` is useful but not required.

## Prepare the workout

- Resolve the user's local calendar date and start time, warm-up, every work and recovery step, repeat counts, targets, and cool-down. Ask for missing details needed to preserve the intended session. Do not infer what “today” or “tomorrow” means near a date or time-zone boundary.
- Check Lion Lift's current scheduling schema before constructing the call. The present `schedule_bike_workout` tool requires a distinctive `display_name`, local `scheduled_for` in `YYYY-MM-DDTHH:MM` format, and at least one block with `work`, optional `recovery`, and `iterations`. `warmup` and `cooldown` are optional single steps. Use each step's `display_name` to clarify its purpose.
- Current goal types are open, time (seconds), distance (miles), and energy (kilocalories). Convert units carefully. Current alerts support heart-rate zones or ranges, speed thresholds or ranges, power zones or ranges or thresholds, and pedal cadence thresholds or ranges in RPM. Include only supported targets the user approved and can reasonably measure; do not invent FTP, zones, or sensor availability. For road rides, account for terrain and traffic before encoding a speed target.
- The scheduling tool has no indoor/outdoor parameter. The rider chooses trainer or road when starting the workout on the Watch. Preserve the intended sequence: a repeated work/recovery pair can include recovery after its final repetition, so represent a plan ending on work explicitly. Do not silently add or remove recovery.

## Confirm and create

Before the write, show the complete workout in plain language: local date/time, title, warm-up, every block and repeat count, targets, recovery, cool-down, and any unit conversion or representation change. Mention that trainer versus road is chosen on the Watch. Obtain the user's explicit confirmation of that exact session. If details changed since the proposal, confirm the revised version.

After confirmation, call the scheduling tool once. If the result is uncertain, inspect the bike-workout list for a matching record before retrying; avoid duplicates. Report the created title, scheduled local time, and returned status. The record is pending until the user opens Lion Lift and uses **Workouts → Bike → Sync Workouts** to put it in Apple Fitness/on the Watch. If the write fails, state the failure without implying that the workout was scheduled.
