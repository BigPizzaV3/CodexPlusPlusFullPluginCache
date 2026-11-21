---
name: habit-tracker
version: 1.0.0
description: Open Habit Tracker to track habits, check off today's routines, and see streaks, completion rates and a year heatmap.
---

# Habit Tracker

Use this skill when the user asks to open, show, or use their habit tracker, or wants to track habits, routines or streaks.

## How to open it

Call the `show_habit_tracker` tool from the `habit-tracker` MCP server. It renders the interactive tracker in the chat.

If the tool is unavailable, direct the user to the hosted app:

https://habit-tacker.host.safrow.com/

## What it does

- Daily, specific-weekday and times-per-week habits
- Yes/no habits and count habits (for example, 8 glasses of water)
- Skip days that keep the streak
- Current and best streaks, 30-day completion rate, year heatmap
- Undo/redo, JSON export/import, CSV export

## Behavior

When the user says things such as "show my habit tracker", "track my habits", "add a habit", "check off my workout", or "how is my streak", open the tracker.

The user edits habits directly in the tracker. Their data stays in their browser, so you cannot see or change it. Do not claim to have added, checked off, skipped, edited or deleted a habit, or quote streaks or stats, unless the user tells you or the app reports it. You can suggest habits, targets and schedules for the user to enter.

If the tracker shows "Not saved", the chat blocked storage; suggest using Export to keep a backup.
