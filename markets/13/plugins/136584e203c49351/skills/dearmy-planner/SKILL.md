---
name: dearmy-planner
description: Read and manage the user's DearMY planner (tasks, categories, special dates, daily briefing, diary drafts, re-plan) through the DearMY MCP tools.
---

# DearMY Planner

Use the DearMY tools when the user asks about their plans, tasks, schedule, special dates, diary draft or re-planning.

## Rules
- Start with `get_planner_context` (or `get_today_briefing` for "today") before answering schedule questions.
- Read tools (`get_planner_context`, `list_planner_categories`, `list_planner_tasks`, `get_today_briefing`, `list_special_dates`, `get_replan_options`) need no confirmation.
- Write tools (`create_planner_task`, `update_planner_task`, `complete_planner_task`, `save_diary_draft`, `apply_replan`, `undo_replan`) must only run after the user clearly confirms the exact change. Pass `confirmed: true`, a fresh unique `request_key`, and the latest `expected_revision`.
- On a revision conflict, re-read, show the user what changed, and ask again.
- `save_diary_draft` saves a draft only; diary entries cannot be read back. Never claim you read the diary.
- Nothing can be deleted through this connector. Do not offer deletion.
- Do not reveal tokens or internal ids unless asked; summarize in plain language.
