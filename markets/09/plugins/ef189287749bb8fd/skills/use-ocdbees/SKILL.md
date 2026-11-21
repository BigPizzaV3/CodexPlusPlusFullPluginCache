---
name: use-ocdbees
description: Use OCDBees MCP tools when the user asks about Clients, Projects, or Tasks in their Tenant.
---

# Use OCDBees

FIRE means Urgency Pants on Fire. HOLD means Progress Hold. They are not one status.

Reads (no writes): `list_capabilities`, `list_tasks`, `list_projects`, `report_completed`, `report_fire`, `report_overdue`, `personal_priorities`, `search`, `list_operations`, `import_schema`, `import_dry_run`.

A Client inventory is `list_projects` for the Client code, then `list_tasks` for that Client, following `next_cursor` until the pages end. Search may resolve the Client code. `search`, `report_fire`, `report_overdue`, and `report_completed` do not supply the inventory. If `list_projects` or `list_tasks` is not callable, say the Client inventory is unavailable. Do not fill it from search or those reports.

Summarize with Project status, Task Progress, Urgency, end date, and assignees. Progress Complete stays in that inventory.

Enumerate Progress Complete by paging `list_tasks`. If that count is over 100, say a single archive preview is blocked and do not call `update_tasks_preview` on the first page of ids. If it is 100 or fewer, call `update_tasks_preview` and wait for the user before confirm. If the list tools are callable and `update_tasks_preview` is not, return the inventory and say the archive preview is unavailable. Do not walk Tasks through `update_task_preview`.

Writes are preview, then confirm. Show the preview, then call the matching confirm tool with `confirm_token`:

- `create_project_preview` / `create_project_confirm`
- `add_tasks_preview` / `add_tasks_confirm` (`client_code` plus `project_title` names that Client's Project; if several match, pass `project_id`)
- `update_task_preview` / `update_task_confirm` (one Task; no confirm when nothing would change)
- `update_tasks_preview` / `update_tasks_confirm` (one shared change on a set; task ids or a Client/Project filter, not both; no confirm for a no-op or more than 100 Tasks)
- `assign_task_preview` / `assign_task_confirm`
- `add_task_note_preview` / `add_task_note_confirm`
- `import_preview` / `import_confirm` (Tenant Admin only)

Tools only touch the authenticated User's Tenant. Attachment results are metadata and deep links, not file bytes. Search does not include file contents. Do not invent task dependencies or capacity calendars. Do not claim a write succeeded until the confirm tool returns success.
