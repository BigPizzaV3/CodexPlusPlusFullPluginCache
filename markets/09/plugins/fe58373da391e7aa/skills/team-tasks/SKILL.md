---
name: team-tasks
description: Manage projects, tasks, steps, attachments, assignments, and authorized agent workflows in Team Tasks.
---

Use the connected Team Tasks MCP tools; do not guess project IDs, users, statuses, or permissions.

At the start of a new workflow, use `get_current_context` when available to understand the authenticated identity, whether it is a personal or independent agent, company timezone, and granted scopes. Use `get_effective_permissions` before sensitive or ambiguous actions. Respect company, project, role, and OAuth scope boundaries.

Find the relevant project with `list_projects`, or search tasks with `search_tasks` for cross-project requests. Inspect `get_project_overview` when project statuses, categories or members matter. Use `list_company_members` only when member selection is necessary and authorized. Do not invent email addresses. External invitations are not supported by `add_project_member`.

Before changing a task, call `get_task` and pass the returned current `version` to `update_task`. For a step, use its version from `get_task` with `update_step`. Older steps may legitimately start at version 0. On version conflict, reread instead of overwriting.

For a new workflow, use `create_project` or `create_task` only on explicit user request, then `create_step` for ordered steps. `reorder_steps`, `copy_tasks`, and `copy_project` change data: confirm scope, source, destination, and intent. Before retrying a failed create operation, check whether the object was actually created to avoid duplicates.

Completion evidence and uploaded files are distinct. `add_comment` may provide a comment proof when requested. `upload_attachment` creates an instruction (`guide`) or work result (`result`), **not** completion evidence; it cannot satisfy required image, video or document completion proofs. Such proofs must be provided through the Team Tasks app. Check `get_upload_rules` before uploads; observe permitted formats and size limits. Use `list_attachments` to inspect purpose and `get_attachment_file` only when necessary. `delete_attachment` is restricted to eligible guide files and must only be used on explicit request.

Respect server-side completion requirements: do not claim a task or step is done if it still has open steps or missing required proof. Read `get_task_history` for audit questions and `list_notifications` for notifications. Use `list_tasks` with `include_archived=false` for active tasks and `true` for completed archive results.

Independent agents may use `claim_task`, `renew_claim` and `release_claim` to coordinate work only on eligible, directly assigned tasks. Do not claim or perform a task unless authorized and intended; release claims when abandoning work. Do not assume that a personal assistant is an independent team member.

When project, task, step, assignee or requested change remains ambiguous after looking up available data, ask the user. Never claim success when a tool reports failure. Minimize personal data in responses and never expose access tokens, secrets or internal diagnostics.
