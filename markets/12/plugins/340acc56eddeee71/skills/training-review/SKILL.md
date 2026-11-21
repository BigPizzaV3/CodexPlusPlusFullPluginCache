---
name: training-review
description: Use when someone asks about their workouts, runs, rides, steps, strength progress or fitness test results in Gyroscope, or wants to log a workout that no device tracked.
---

# Reviewing and logging training

If no Gyroscope tools are available, follow the connect-gyroscope skill
instead.

## Reviewing

- Call `gyroscope_status` once for the member's timezone, then use explicit
  YYYY-MM-DD dates.
- Sessions: `load_workouts` for the dates. Steps: `load_steps`.
- Lifts over time: start with `load_lift_progress`, which lists each
  exercise with its sessions and best, first and latest estimated one-rep
  max. Name an exercise ("bench") for one line per session: the top set,
  the estimated max and the volume. Use `load_strength_history` only when
  they want every set.
- Fitness tests and brain games from the app: `load_benchmarks` gives each
  test's latest, previous and best result with its score out of 100, and the
  tests they have not taken yet. Name a test for every run of it.
- Totals over weeks or months: `load_trend` with metric `workouts` or `steps`.
- Their current program: `load_workout_state`, which you can see but not
  change.
- Lead with the change that matters (heavier, longer, more often), backed by
  their numbers, and line it up with their sleep or weight when they ask.

## Logging a workout

- Manual sessions (`save_workout`, `save_run`, `save_bike`) are only for what
  no device tracked. Check `load_workouts` for that day first, and never save
  over a session that is already there.
- Ask for the one missing detail, such as duration or start time, rather than
  guessing it.
- Lifts go on an existing workout with `add_strength_training_details`, using
  its id from `load_workouts`. Show them the sets you are about to log first.
- Confirm in one line what was logged and when. The connection cannot edit or
  delete anything, so changes are done in the Gyroscope app.
