---
name: workout-progress
description: Use when the user asks how their wall Pilates is going or wants their history erased ('how many workouts did I do this week?', 'what's my streak?', 'delete my Wallform progress'). Shows sessions, streak and program days, or erases them.
---

Wallform keeps the user's finished sessions under ChatGPT's anonymous user ID; their name and what they type are not stored. The user's own instructions come first.

## Flow

1. `get_progress` shows the sessions this week and this month, the streak, the finished Wallform 28 days and the `next_program_day`. It counts finished sessions only: a session is saved when the timed player reaches its end.
2. When the user asks to erase their history, `delete_my_progress` permanently removes their saved sessions, streak and finished days, and Wallform 28 starts again at day 1.

## Scope

- There is no account to sign in to; progress stays with the user's ChatGPT account.
- Progress is a count of finished sessions, with no claims about fitness results.
