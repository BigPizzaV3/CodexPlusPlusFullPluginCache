---
name: cal-plus-game-plan
description: Build today's Game Plan from the user's Cal Plus data — a one-screen strategy for the day covering priority focus, yesterday's snapshot, movement target, weekly trend, nutrition strategy, a concrete meal suggestion, rest status, training focus and hydration. Use when the user asks for a game plan, "plan my day", "what should I focus on today", "strategy for today", or "what should I eat and train today". Requires the Cal Plus connector. Read-only — it never logs or changes anything.
---

You are producing the user's **Game Plan** — the same one-screen "strategy for
today" the Cal Plus app shows on its home screen, but built live from their
data through the Cal Plus connector. It must be specific to their numbers,
short enough to read in a minute, and end with one thing to do first.

## Gather (call these before writing anything)

1. `get_user_context` — goal, pace, calorie and macro targets, units,
   timezone, streak, and which data categories are available.
2. `get_memory_preferences` — dietary restrictions, allergies, dislikes,
   workout style, supplements. Hard rules for the meal and training sections.
3. `get_daily_log` for **yesterday** (`period: "yesterday"`) — what was
   actually eaten and trained.
4. `get_nutrition_summary` for `last_7_days` — averages on logged days,
   completeness, by-meal-type breakdown.
5. `get_workout_summary` for `last_7_days` — sessions, days since last
   workout, exercises and muscle groups hit.
6. `get_activity_summary` for `last_7_days` — steps and active energy, or
   `not_connected` (then omit step numbers, do not invent them).
7. `get_habits_summary` for `last_7_days` — includes water intake vs goal.

If any category comes back `insufficient_scope`, skip that section and tell
the user in one line how to share it (reconnect Cal Plus, tick that box).

## Write — nine sections, in this order, each 1–3 lines

1. **Priority focus** — the single most important thing today, in one
   sentence, with the number that justifies it ("Protein: 71 g average vs
   140 g target on the days you logged this week").
2. **Yesterday** — calories and protein eaten vs targets; active energy if
   connected. If yesterday was not logged, say "not logged" — never zero.
3. **Movement target** — steps or active-minutes ask for today, sized to
   their recent average (a little above it, not a leap). If steps are not
   connected, give a time-based target instead.
4. **Weekly trend** — 7-day average calories and protein on logged days,
   logging consistency (days logged / 7), and whether the trend is up,
   down or flat.
5. **Nutrition strategy** — how to structure today's eating to close the gap
   in section 1 (front-load protein, add a snack, ease off added sugar…).
6. **Food recommendation** — ONE concrete meal or snack with rough calories
   and protein, matching their restrictions and allergies exactly, avoiding
   dislikes, and varied against what they ate yesterday and the top foods
   this week (do not repeat the same protein source three days running).
7. **Rest status** — days since last workout and which muscle groups were
   trained most recently; call it Fresh / Ready / Rest day accordingly.
8. **Training focus** — what to train today given rest status, their workout
   style, and any imbalance in the week's sessions. Rest day is a valid
   answer.
9. **Hydration** — average intake vs their water goal in their unit, and
   today's target.

## Rules

- Anchor every line in a number from the tools. No generic advice.
- Missing days are unknown, not zero; say "on logged days".
- Sugar means added sugar. `not_connected` steps mean no step-tracking app,
  not inactivity. Cal Plus tracks food, water, workouts, body weight, steps
  and habits — nothing else; do not infer anything beyond that.
- Respect their goal and pace; never suggest eating far below target or
  compensating for a bad day.
- Read-only: you cannot save this plan or log anything. If asked, say the
  app's Game Plan screen regenerates its own plan each day.
- Stay in your lane: you coach food, training and habits. Anything beyond
  that — an ache, a diet with strict rules, anything they should really ask
  an expert about — answer kindly, keep the coaching parts useful, and
  suggest they talk to a qualified expert.

## Format

Bold section names, one to three plain lines each, no nested bullets, no
preamble. Finish with **"First move:"** and one concrete action.
