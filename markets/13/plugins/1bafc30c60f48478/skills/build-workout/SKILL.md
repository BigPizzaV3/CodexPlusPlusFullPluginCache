---
name: build-workout
description: Build one strength-training session in Lifterly from the user's real profile, equipment, history and results, show it, and add it to their plan once they agree. Use when the user asks for a workout, a session for today or a given day, or a session targeting given muscles or a split part.
---

# Build a workout

Follow the user's explicit instructions first; this workflow fills in what they
did not specify.

## Gather

1. `get_training_profile` for goal, level, equipment, weekly goal and weight
   unit. If the user has no profile, say so and ask about their goal and
   equipment instead of guessing.
2. `list_workouts` (last two weeks) to see what they trained recently.
3. Decide the workout type and split part: from the user's words, otherwise
   the next part in their usual rotation, otherwise `fullBody`.
4. `search_exercises` with that `workoutType` and `splitPart`.
5. `get_exercise_progress` for the exercises you are considering, to set
   weights from their results.

Ask one short question instead of guessing when the day, the time available or
the muscles to train are unclear and matter.

## Build

Apply [references/programming.md](references/programming.md): exercise choice,
sets, weights in kg, rest in seconds, session length.

## Show and confirm

1. Call `show_workout_proposal` with the complete plan (the same input
   `create_planned_workout` takes). It shows the session with an
   "Add to my plan" button; nothing is saved yet.
2. Explain the choice in two or three sentences, weights in the user's unit.
3. If the user asks for changes, adjust and show the proposal again.
4. When they agree in the conversation, call `create_planned_workout` with the
   same plan (unless they already added it with the button: the tool result
   says so), then `show_planned_workout` with its id.

## Do not

- Invent exercise ids or results.
- Save anything before the user agrees.
- Plan through injuries the user mentioned; leave the affected exercises out
  and suggest `ban_exercises` if the limitation is lasting.
