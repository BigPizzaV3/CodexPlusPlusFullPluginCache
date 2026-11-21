---
name: tasks
description: List tasks matching a filter, e.g. "/writesonic-agents:tasks high priority open" or "/writesonic-agents:tasks assigned to me".
disable-model-invocation: true
---
`whoami` first. Interpret "$ARGUMENTS" as a filter (priority, status, assignee, keyword) and call `query_tasks` view="list" with the matching filters (default: open tasks). Show title, assignee, status, priority, due date. Read-only.
