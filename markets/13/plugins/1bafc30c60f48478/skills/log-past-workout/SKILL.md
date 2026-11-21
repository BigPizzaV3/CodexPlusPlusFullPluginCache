---
name: log-past-workout
description: Record in Lifterly a workout the user did without the app, from their description of exercises, sets, reps and weights. Use when the user says what they trained ("I did 5x5 squats at 100 kg this morning") and wants it in their history.
---

# Log a past workout

## Understand the session

1. Get from the user's words: when it happened, each exercise, and each set's
   reps, weight and duration. "5x5 at 100" is five sets of five reps at 100;
   "3x10" without weight is bodyweight unless the user says otherwise.
2. Weights: convert to kg from the user's unit (`get_training_profile` →
   `weightUnit`) when they did not say the unit; 1 lb = 0.4536 kg.
3. Find each exercise: `search_exercises` with `query` set to its name (try a
   shorter name or the main muscle if nothing matches). If several match,
   pick the obvious one or ask.
4. If it carried out a planned session, `list_planned_workouts` around that
   date and pass its id as `plannedWorkoutId`.

Ask one question for anything missing that matters (the day, an exercise you
cannot identify, a weight). Never invent sets, reps or weights.

## Confirm and save

1. Repeat the session back in the user's unit: date, exercises and sets.
2. After the user confirms, call `log_workout` with a short name, the
   `workoutType` and `splitPart` that fit, `startedAt` (and `completedAt` if
   known) with the user's time zone offset.
3. Tell the user it is in their history, and mention a record when
   `get_exercise_progress` shows they beat their best weight.
