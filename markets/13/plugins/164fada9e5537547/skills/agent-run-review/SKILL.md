---
name: agent-run-review
description: Walk through what an agent did on a task, step by step. Use when the user asks what an agent did, why a task looks the way it does, or to review agent work on a task.
---
Review agent work on task "$ARGUMENTS" (a task id or title; resolve with `query_tasks` if it's a title) in the user's project (`whoami` first).

1. `get_agent_runs` with the task_id — list the runs.
2. For the latest run (or the one the user names), show its progress steps in order.

Summarize: what the agent was asked, each step it took, the outcome, and anything that failed or was skipped. Read-only.
