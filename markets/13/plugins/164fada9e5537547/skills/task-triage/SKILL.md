---
name: task-triage
description: Triage the task list — open task counts grouped by assignee, then the high-priority tasks that aren't done. Use when the user asks about open tasks, workload, who has what, or what's high priority.
---
Triage tasks in the user's Writesonic Agents project (call `whoami` first; if several projects, use the one named in "$ARGUMENTS" or ask).

1. `query_tasks` with view="counts", group_by="assignee_id" — open tasks per person.
2. `query_tasks` with view="list" filtered to high priority and not-done statuses — the list that needs attention.

Present counts as a table, then the high-priority list with title, assignee, status, due date. Read-only; do not modify tasks unless asked.
