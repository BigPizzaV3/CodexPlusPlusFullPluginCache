---
name: task-execution
description: List and create development tasks inside the signed-in user's Vibe Coding Plan projects
---

# Task Execution

Use the Vibe Coding Plan MCP tools after ChatGPT OAuth.

## Tools

- `list_projects` — the signed-in user's projects
- `get_project_tasks` — tasks for one owned project
- `create_project` — create a project, optionally generate tasks

## Workflow

1. Call `list_projects` when the user asks what they have.
2. Call `get_project_tasks` with a project id they own.
3. Call `create_project` to save a new project. Set `generate_plan` when they want tasks created.

## Rules

- Never read or write another user's projects.
- Never print env vars, API tokens, or OAuth secrets.
- Do not start GitHub automation or AI task runners from ChatGPT.
