---
name: get-started
description: Use when the user first connects PeerBie or asks what PeerBie can do in ChatGPT.
---

# Getting started with PeerBie

PeerBie holds the user's work: tasks, projects, goals (OKRs), meeting notes, the workspace feed, workflows and colleagues.

When the user starts:
1. If they belong to several workspaces and the connection is not limited to one, call `list_workspaces` and ask which one to use.
2. Offer three useful starting points: what is overdue or due this week (`my_tasks`), which goals are at risk (`goals_status`), and the latest meeting notes (`search_meeting_notes`).
3. Before any change (`create_task`, `update_task`, `add_task_comment`, `okr_check_in`, `create_note`), repeat the details and wait for the user's confirmation.

If a tool answers that the connection may only read PeerBie, tell the user to reconnect PeerBie and allow changes. Nothing can be deleted through PeerBie in ChatGPT.
