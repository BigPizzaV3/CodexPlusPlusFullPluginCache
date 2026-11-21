---
name: log-workout
description: Log a workout in Outlift, swap a planned exercise for a similar one, and suggest weights from the previous session. Use this whenever the user wants to record sets, reps, weight or time they just did, mentions today's workout or training day, says they could not do an exercise (machine taken, injury, no equipment), asks what they lifted last time, or - as a trainer - wants to log a session for a trainee. Apply it even when the user never says "Outlift" or "log", for example "I did 3x8 squats at 60".
---

# Log a workout

Outlift keeps one log per person, training day and date. The plan comes from the trainer; this skill records what was really done, so the numbers have to be the user's, never guessed.

## Before you log anything

1. Call `whoami` once. It returns the user's role, `timezone` and `locale`. Pass the timezone as `tz` and the locale as `locale` in every later call: the timezone decides which day "today" is, and the locale keeps exercise names in the user's language.
2. Find the workout with `get_workout_draft` (it defaults to today and to the training day scheduled for that date). The draft shows each planned exercise with its `exerciseId`, the planned sets and reps, what is already logged, and `previousSets` from the last session.
3. If there is no training day for that date, say so and ask which one they trained. A trainer can list templates with `list_training_days`; a trainee can name it and you look it up from their `get_trainee_schedule`. Do not log into a training day the user did not mention.

## Record what was done

Call `log_workout` with the exercises the user reports.

- Identify exercises by `exerciseId`, taken from the draft or from `search_exercises`. Names differ between languages, so a name is only a label and a guessed id fails.
- Give each set `reps` and, when the user says so, `weight` (kg), `time` (seconds) or `rir` (reps in reserve, 0-10). Leave out what they did not say. Do not fill in a weight because the plan or last time had one.
- The call is incremental: exercises you do not mention keep what was logged before. Call it after each exercise or once at the end; both work.
- Logging an exercise again for the same date replaces that exercise's sets, so check the draft before correcting something the user already logged.
- An exercise that is not in the plan can be added: find its id with `search_exercises` and log it. It is stored as an extra exercise and never blocks the workout from counting as complete.
- Skipped exercises: pass `skipped: true` when the user says they skipped one.

After the call, tell the user what was saved and whether the workout is complete. If planned exercises are still open, name them, because completion only becomes true once every planned exercise is done or skipped.

## Swap an exercise that cannot be done

Use this when the user cannot do a planned exercise.

1. Find it in the draft. Only a planned exercise with nothing logged yet can be replaced; if sets are already saved for it, log the new exercise as an extra instead and say why.
2. Call `get_similar_exercises` with that exercise's id. It returns exercises for the same main muscle, best equipment match first. Pass `exclude` for ones already in today's workout. If the user did not name a substitute, offer two or three with their equipment and let them choose; if they named one, check it is in the list or find it with `search_exercises`.
3. Log the chosen exercise with `replaces` set to the planned exercise's id. The substitute takes the same slot and keeps the planned sets, reps and rest, so the trainer sees what was swapped and the plan itself is untouched.

## Suggest weights

When the user asks what to lift, call `get_last_sets` with the exercise id. It returns the sets from the last workout where that exercise was done, on any training day. Propose a starting point from those numbers and say they are from last time; if it returns nothing, say the exercise has no history and ask what they want to start with. Do not give medical or injury advice; for pain, suggest they talk to their trainer or a professional.

## Logging as a trainer

A trainer logs for a trainee by passing `trainee_id` (the trainee's uid from `list_my_trainees`) to `get_workout_draft`, `get_last_sets` and `log_workout`. Confirm which trainee before saving, because a log under the wrong person is hard to spot later.

## Connection and errors

Logging needs write access. If the tool says the connection is read-only, tell the user to reconnect and allow changes; do not retry in a loop. If a tool returns an error, repeat the message in plain words and ask what they want to do next. You cannot delete a log; if the user wants one removed, point them to History in the Outlift app.

## Example

User: "Machine for leg press is taken, did 3x10 hack squat at 80 instead."

1. `whoami`, then `get_workout_draft` for today. The leg press is planned with nothing logged.
2. `search_exercises` for "hack squat" to get its id (or `get_similar_exercises` for the leg press and pick it from the list).
3. `log_workout` with the hack squat id, `replaces` set to the leg press id, three sets of 10 reps at 80 kg.
4. Reply: "Saved 3x10 hack squat at 80 kg in place of the leg press. Still open today: RDL and 4 more exercises."
