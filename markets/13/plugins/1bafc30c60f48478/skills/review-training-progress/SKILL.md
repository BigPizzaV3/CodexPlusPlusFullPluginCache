---
name: review-training-progress
description: Review the user's recent training in Lifterly: sessions done against their weekly goal, progress and records on their main lifts, stalled exercises, and what to do next. Use when the user asks how their week, month or training is going, about their progress, records, consistency or a plateau.
---

# Review training progress

## Gather

1. `get_training_profile` for the goal, `workoutsPerWeekGoal` and weight unit.
2. `list_workouts` for the period the user asks about (default: the last four
   weeks; use `from` and `to`).
3. Pick the main lifts: the exercises done most often in that period. Call
   `get_exercise_progress` with up to ten of them.
4. `list_planned_workouts` for the coming days, to connect the review to what
   is next.

## Analyze

- Consistency: sessions per week against `workoutsPerWeekGoal`, missed planned
  sessions, longest gap.
- Progress: for each main lift, the best weight (with its reps) and whether
  recent top sets went up, held or went down. Estimate a one-rep max only when
  asked (Epley: weight × (1 + reps / 30)) and say it is an estimate.
- Balance: muscle groups or split parts trained much less than others.

## Report

- Start with one sentence on the big picture, then short sections:
  consistency, progress (biggest wins first), what stalled, next steps.
- Weights in the user's unit, exercise names, dates as the user would say them.
- Use `show_exercise_progress` for the one or two lifts that tell the story.
- Next steps are concrete: a weight to aim for, a session to add, an exercise
  to swap (`find_exercise_alternatives`), a rest week if they trained hard.

Base every statement on the data; say so when there is too little to judge.
Do not give medical advice; for pain or injury suggest seeing a professional.
