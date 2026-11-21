---
name: plan-training
description: Build and organise training in Outlift as a trainer - create or edit training days, add custom exercises (with Polish translations or photos), set up supersets and circuits, and put training days on a trainee's weekly schedule. Use this whenever a trainer talks about programming, templates, a client's week, adding or changing exercises, sets, reps, rest or tempo, or scheduling a training day, even if they never say "Outlift". Not for logging a workout that was already done.
---

# Plan training

Trainers build training days (templates of exercises) and put them on a trainee's weekly schedule. Everything here is a change to real data that trainees will follow, so look first, change what was asked, and say what changed.

## Start

Call `whoami`. Only trainers (and admins) can plan; for a trainee, explain that their trainer plans the week and offer to show it with `get_trainee_schedule` instead. Use `list_my_trainees` to get a trainee's uid.

## Exercises come from the library

Every planned exercise is an `exerciseId`, never a name. Names differ between languages, and a wrong id puts the wrong exercise in a client's plan.

1. Search the library with `search_exercises` before anything else. Reuse a match instead of creating a duplicate, and tell the trainer which exercises matched. When two candidates could be the same exercise, ask.
2. Use `get_exercise` when you need the full details (muscles, difficulty, video) to choose between options.
3. Create an exercise only when nothing fits. `create_exercise` takes a name and optional body part, equipment, muscle groups, description and translations (`en` and `pl`). Do not set it public unless the trainer asks: a public exercise becomes visible to all trainers.
4. Fix an exercise the trainer created with `update_exercise` (name, description, muscle groups, difficulty, translations). Only change the fields they asked about; omitted fields stay as they are. Shared library exercises belong to Outlift and only admins can change them.
5. Photos: `set_exercise_photo` takes a public https link or base64 image data (JPG, PNG or GIF under 600 KB). Only use images the trainer supplied, and only when it is clear which exercise it shows.

## Create and edit training days

Read `references/training-day-fields.md` for the exercise fields (sets, reps ranges, rest, tempo, reps in reserve, warm-ups, supersets) before building one with more than the basics.

- `create_training_day` takes a title, an ordered list of exercises and an optional description. Keep the trainer's own numbers exactly; if sets or reps are unclear, ask rather than choose.
- `update_training_day` edits one the trainer owns. Omitted fields stay as they are; `exercises` replaces the whole list in order; `add_exercises` appends. Before replacing a list, read the day with `get_training_day` so nothing is lost by accident, and tell the trainer what was removed.
- To make a superset or circuit, give two or more consecutive exercises the same `group_id`. Rest applies once, after the last exercise of the group.
- Afterwards, summarize the saved day (title, exercises in order with sets and reps) so the trainer can spot a mistake right away.

## Put training days on the week

`set_weekly_schedule` replaces the trainee's whole week. Anything you leave out disappears from the active schedule (the old version stays in history), so never send only the new day.

1. Read the current week with `get_trainee_schedule` for that trainee.
2. Build the full list of assignments: every existing day the trainer wants to keep, plus the change. Each assignment is a `trainingDayId` and `dayOfWeek`, where 0 is Sunday, 1 is Monday and 6 is Saturday. Note that the schedule view lists days Monday first by name, so convert carefully.
3. State the result before saving when it removes something ("this moves Nogi from Wednesday to Thursday and keeps the rest"), then call it, then confirm the new week.
4. A trainer plans their own week by passing their own uid. Use `get_schedule_history` to see or explain earlier versions of a trainee's schedule.

## What you cannot do

You cannot delete training days, exercises or schedules, and you cannot add or remove trainees. Say so and point to the Outlift app. If a tool says the connection is read-only, ask the trainer to reconnect and allow changes; do not retry in a loop. For other errors, repeat the message in plain words and say what you can still do.

## Example

Trainer: "Create Upper A: bench 4x8-10 with 2 minutes rest, then a superset of pull-ups and dips 3x10, and put it on Mondays for Anna."

1. `whoami`, `list_my_trainees` (Anna's uid), `search_exercises` for bench press, pull-ups and dips.
2. `create_training_day` with bench (`sets` 4, `reps` "8-10", `rest_seconds` 120), then pull-ups and dips (`sets` 3, `reps` 10) sharing a `group_id`.
3. `get_trainee_schedule` for Anna; build the week with her current assignments plus Upper A on Monday (`dayOfWeek` 1); `set_weekly_schedule`.
4. Reply with the saved day and Anna's full week.
