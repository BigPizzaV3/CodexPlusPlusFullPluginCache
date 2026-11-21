---
name: routine-midday-check
description: Midday check routine. Use when setting up or running the optional scheduled midday check that preps afternoon meetings and flags what changed since the morning.
---

# Routine: midday check (optional)

**Default schedule:** weekdays 13:00. Meeting-by-meeting triggers are not possible because scheduled tasks are time-based, so this is the closest pre-meeting nudge.

## Run instruction

> Run my Delegent midday check. Use Delegent[, and my <calendar/mail app>].
> 1. For each client meeting this afternoon: a short brief (objective, what changed, open actions, sources).
> 2. What changed since this morning: new emails expecting my reply, new Delegent Inbox items, and tasks due today still open.
> Keep it under one minute to read. Save nothing. List decisions for me under "Needs you".

## How to run it

A short `prep-me` per afternoon meeting, plus `delegent_find_follow_ups` (days: 1), `delegent_list_inbox_items` and `delegent_list_my_tasks` (due today).
