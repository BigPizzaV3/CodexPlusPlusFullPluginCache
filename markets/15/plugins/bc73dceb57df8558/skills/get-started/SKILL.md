---
name: get-started
description: Use when the user first connects Gymus or asks what Gymus can do. Shows what the connector reads and changes, and how its edits and deletes ask before writing.
---

# Getting started with Gymus

Gymus is the user's workout log. Everything the tools return belongs to the account they signed
in with, and nothing else is reachable.

When the user has just connected, or asks what Gymus can do:

1. Call `get_training_profile` and `list_workouts` to see what the account holds. A new account
   may have no workouts yet; say so plainly rather than inventing any.
2. In two or three sentences, say what you found (for example, how many sessions in the last
   two weeks) and what the user can ask for:
   - questions about their workouts, plans, schedule and weigh-ins;
   - logging a workout they describe, or several at once;
   - logging a weigh-in, today's or a past one;
   - creating a workout plan;
   - correcting or deleting a workout or plan;
   - keeping a note on an exercise.
3. Offer one example that fits what you found, such as logging today's session or reviewing
   last week.

Rules that apply to every request:

- Find exercise ids with `search_exercises` before logging a workout or creating a plan, and
  confirm the exercises, sets and dates with the user before calling `log_workouts` or
  `create_workout_plans`.
- Every edit and delete takes two calls. The first changes nothing and returns a preview with a
  `confirmationToken`; show the preview, and send the token only after the user agrees.
- Stored values are kilograms, metres and centimetres. `get_training_profile` reports the units
  the user prefers to read; convert for display.
- The schedule and the training profile are read-only here, and weigh-ins can be logged but not
  corrected or deleted. For those, the user opens the Gymus app.
- Changes reach the Gymus app the next time it syncs.
