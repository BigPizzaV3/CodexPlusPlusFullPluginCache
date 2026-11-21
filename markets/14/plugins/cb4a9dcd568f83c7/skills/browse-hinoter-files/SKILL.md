---
name: browse-hinoter-files
description: Browse the workspaces, files, and tasks accessible to the authenticated HiNoter user. Use when the user asks to view all workspaces, list files, find files by workspace, or query tasks; do not use for modifying, deleting, or generating file content.
---

# Browse HiNoter Workspaces and Files

Use the plugin MCP service tools `list_user_workspaces`, `list_workspace_files`, and `list_user_tasks` to browse the current user's data scope.

1. Call `list_user_workspaces` once first. Do not pass `user_id`, access tokens, or any other identity information. The server identifies the user from the OAuth context and returns only the personal workspace and the team workspaces where the current user has an active membership.
2. When files are needed, call `list_workspace_files` for the target workspace using the `id` from the workspace results; the personal workspace always uses `personal`. The default page size is 50; when `has_more` is `true` in the results, continue reading with the same `workspace_id` and an increasing `offset`, with a single `limit` no larger than 100.
3. The file list contains only metadata and the `has_summary` flag — no transcriptions, summary content, images, todos, storage paths, or sharing credentials. When the user wants a summary, use `get_user_file_summary` with an explicit `id` from the list.
4. When the user wants tasks, use `list_user_tasks` with the workspace `id`; the optional `status` accepts `all` or `todo`, and the optional `assignee_scope` accepts `all` or `my`.
5. If the workspace, file, or task tool returns `isError`, briefly restate the error and stop. Do not try other workspace IDs and do not bypass permission checks by calling regular business APIs.
6. When the corresponding MCP tools are not available in the current task, do not interpret it as "no workspaces or files". Explain that the HiNoter MCP is not loaded in the current task, give the following troubleshooting order, then stop:
   - In the Codex plugin settings, confirm HiNoter is enabled; from the command line, use `codex plugin list` to confirm both `installed` and `enabled` are `true` for `hinoter`.
   - After installing, updating, or enabling the plugin, start a new task (restart Codex if necessary); existing tasks do not hot-load new MCP tools.
   - If a new task still has no tools, check that the MCP URL in the plugin `mcp.json` is reachable and that the protected resource metadata and authorization server metadata return JSON. The server must have `mcp.issuer`, `mcp.resource_uri`, and `mcp.token_hmac_key` configured; production also requires `mcp.web_login_url` with test authorization disabled.
   - Do not fall back to unauthorized network requests, and do not assume the user's identity or manually pass `user_id` or access tokens.

This skill only reads workspace, file, and task data. It never creates, updates, or deletes anything, never generates summaries, and never reads transcriptions.
