---
name: list-user-tasks
description: Query tasks in the personal or team workspaces accessible to the authenticated HiNoter user. Use when the user asks to list all tasks, incomplete tasks, or tasks assigned to them; do not use for creating, modifying, or completing tasks.
---

# Query HiNoter Tasks

Use the `list_user_tasks` tool provided by the plugin MCP service to query tasks.

1. Determine `workspace_id` from a trusted `list_user_workspaces` result; the personal workspace always uses `personal`. Never guess team workspace IDs.
2. Use `status` = `all` for all tasks or `todo` for incomplete tasks; use `assignee_scope` = `my` for tasks assigned to the current user, otherwise `all`.
3. Each read covers 20 matching files by default; when `has_more` is `true`, continue reading with the same filters and an increasing `offset`, with a single `limit` no larger than 100.
4. Do not pass `user_id`, access tokens, or any other identity information. The server identifies the user from the OAuth context and validates read permission on the personal or team workspace.
5. If the tool returns `isError`, briefly restate the error and stop. Do not bypass permission checks by calling regular business APIs.

This skill only reads tasks. It never creates, updates, deletes, completes, or regenerates anything.
