# Structured workouts

Before drafting, obtain the user's goal and target date, available days and approximate time, activity and workout preferences, recent training context, current readiness, and any injuries, symptoms, or medical restrictions.

Create a batch of proposed operations, then call `validate_structured_workout_batch`. If valid, call `preview_structured_workout_batch` and show the returned dates, titles, activity types, recurrence, replacements, deletions, warnings, and before-and-after diff.

Use the exact names exposed by the connected tool catalog. For one new workout, call `preview_structured_workout_create` with `{ "payload": { ...workoutFields } }`. For a schedule, validation accepts `{ "operations": [...] }`; preview accepts `{ "payload": { "operations": [...] } }`. Each create operation is `{ "action": "create", "workout": { ...workoutFields } }`. There is no `preview_structured_workout_change` tool. If a tool is unavailable, refresh discovery and choose the matching create, update, delete, or batch tool before reporting that saving is unavailable.

The preview is not permission to mutate. Ask for explicit confirmation after showing it. Only then may `apply_structured_workout_batch` be called with the unchanged action fields and confirmation token. If the revision or proposal changes, preview again and ask again.

Structured workouts are date-based; do not invent a time-of-day field.
