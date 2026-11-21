---
name: get-started
description: Use when the user wants to plan their day, capture tasks or review habits in DoStreak. Explains what the DoStreak tools do and how to use them well.
---

# Getting started with DoStreak

DoStreak is a planner app with tasks, a time-blocked day plan and daily habits. The connected tools read and change the user's own DoStreak data; changes appear in the app within seconds.

## Good first steps
- Call `get_day` before planning so you know existing tasks, time blocks, habits and free gaps.
- Use `add_tasks` to turn notes, emails or lists into tasks (with steps, dates and lists).
- Use `plan_day` / `plan_days` to place time blocks into free gaps. Fixed appointments are never moved.
- Use `shift_blocks` when the user is running late, `review` for habit statistics, `list_habits` + `check_habit` / `skip_habit` to check off habits, `create_habit` / `update_habit` to manage them.

## Rules
- Ask before deleting anything; only delete tasks the user named explicitly.
- Every change can be undone for 24 hours with `undo_last_change` – offer it after larger changes.
- The journal is private and not available through these tools.
