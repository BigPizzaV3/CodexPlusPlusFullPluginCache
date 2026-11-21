---
name: get-started
description: Use when the user first connects Lucy or asks what Lucy can do in ChatGPT.
---

# Getting started with Lucy

Lucy is the user's personal assistant app: tasks with deadlines and reminders, notes from meetings and lectures they recorded, a private notes pad, routines, and the calendar they connected.

When the user starts, offer three useful starting points: what is due today or overdue (`my_tasks`), the action items from their latest recording (`search_meeting_notes`, then `get_meeting_notes`), and their routines (`list_routines`).

Before any change (`create_task`, `update_task`, `create_note`, `create_routine`, `pause_routine`), repeat the details and wait for the user's confirmation.

If a tool answers that the connection may only read, tell the user to reconnect Lucy and allow changes. Nothing can be deleted through Lucy in ChatGPT.
