---
name: swap-exercise
description: Replace an exercise the user cannot or does not want to do (injury, missing equipment, dislike) with a fitting alternative in a planned Lifterly workout, and optionally stop it from being suggested again. Use when the user asks for a substitute, an alternative, or to avoid or remove an exercise.
---

# Swap an exercise

1. Identify the exercise and where it is: `list_planned_workouts` when it is
   in a planned session, otherwise `search_exercises` with `query`.
2. `find_exercise_alternatives` with the exercise id, the session's
   `workoutType` and `splitPart`, and the other exercises of the session as
   `otherExerciseIds`.
3. Choose the alternative that best keeps the session's intent (same main
   muscle and movement pattern) and respects the reason given. With an
   injury, prefer exercises that avoid loading the painful area, and suggest
   seeing a professional for pain.
4. Set its sets from `get_exercise_progress` for the alternative, or a
   conservative starting weight. When the user wants to see how to do it,
   call `show_exercise_details` with its id.
5. Show the change and, once the user agrees, call `update_planned_workout`
   with the session's complete new `exercises` list (it replaces them all;
   keep the other exercises and their sets unchanged).
6. If the reason is lasting (injury, no equipment, strong dislike), offer
   `ban_exercises` so Lifterly stops suggesting it; call it only if the user
   agrees.

Never change other exercises of the session without saying so.
