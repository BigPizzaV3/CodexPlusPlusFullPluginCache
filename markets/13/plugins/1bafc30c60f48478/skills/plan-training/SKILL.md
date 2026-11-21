---
name: plan-training
description: Plan the user's training in Lifterly over any span (the next days, a week, a month, a program), one session per training day matching their weekly goal and split, around what is already planned, and add the sessions once they agree. Use when the user asks to plan their week, the next days, a month, a training schedule or a program.
---

# Plan training

The user's explicit instructions (span, days, times, split, number of
sessions) always win over these defaults. Without a span, plan the coming
week.

"Plan my week" asks for a proposal, not for saved sessions: always show the
plan in a `show_plan_proposal` card first, and add nothing until the user
agrees or adds it with the card's button.

## Gather

1. `get_training_profile`: goal, level, equipment, `workoutsPerWeekGoal`,
   weight unit.
2. `list_planned_workouts` for the span: keep what is already planned, and
   only fill the remaining days unless the user asks to replace them.
3. `list_workouts` for the last two weeks: what they trained and how often.
4. Settle the days and times. Ask once, in a single question, if the user did
   not say which days or what time they train; do not invent a schedule.

## Choose the split

- 1–2 sessions a week: `fullBody`.
- 3 sessions: `fullBody`, or `ppl` (push, pull, legs).
- 4 sessions: `upperLowerSplit` (upper, lower, upper, lower).
- 5–6 sessions: `ppl` twice, or `arnoldSplit`.
- Keep the split the user already follows when their history shows one.
- Leave at least a day between sessions that load the same muscles.

## Build each session

For each day: `search_exercises` with its `workoutType` and `splitPart`, then
`get_exercise_progress` for the candidates, and apply
[references/programming.md](references/programming.md). Vary exercises between
sessions of the same part.

Over several weeks, progress the main lifts gradually from week to week (a
small weight or rep increase on the previous week's targets, more slowly for
advanced lifters), and plan a lighter week after every three to five hard ones
when the span allows it.

## Long programs

A card and an answer have limits: propose at most about four weeks of
sessions at once. For a longer program, agree on its structure first (split,
weekly progression, lighter weeks), then propose it in blocks of up to four
weeks, one block per answer, continuing from where the last block ended.

## Show and confirm

1. Call `show_plan_proposal` once with every session of the span or block
   (each the plan `create_planned_workout` would save, `plannedAt` in the
   user's time zone, ISO 8601 with its offset). It shows them in one card,
   by week, each session opening to its exercises, with an "Add all to my
   plan" button. Never call `show_workout_proposal` once per session:
   ChatGPT keeps only the last card of an answer.
2. Summarize the plan in a few lines (days, sessions, why this split, how it
   progresses) and ask the user to confirm it.
3. If they ask for changes, adjust and call `show_plan_proposal` again.
4. When they agree in the conversation, call `create_planned_workouts` once
   with all the sessions (unless they already added them with the button:
   the tool result or the card says so), then `show_week_plan` for the first
   week.

If sessions are refused, fix what the result says for those only and add
them again; tell the user if a session could not be added.
