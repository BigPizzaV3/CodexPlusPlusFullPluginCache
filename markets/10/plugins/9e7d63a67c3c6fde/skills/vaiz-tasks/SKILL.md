---
name: vaiz-tasks
description: Find, show, read, create, and update Vaiz tasks — show task lists as a widget or query them as data, inspect a task with its comments and history, create tasks with Markdown descriptions, edit fields, move between columns and boards, archive and restore, and manage blockers and followers.
---

# Vaiz tasks

Tasks live on boards; boards belong to projects. A task is identified either by its 24-character database id or by its human-readable id (HRID) such as `PRJ-123`. Every task tool accepts both.

## Prerequisite

The Vaiz MCP server (`https://api.vaiz.com/mcp`) must be available through the installed Vaiz plugin and authorized with OAuth. If tools are missing or return an authorization error, open the Vaiz connection and complete OAuth sign-in.

Vaiz tools can appear under different names depending on how Vaiz is connected: `mcp__Vaiz__query_tasks` for a directly configured MCP server, or `mcp__codex_apps__vaiz_query_tasks` (sometimes with a longer app prefix such as `vaiz_testing_`) when Vaiz is installed as an app. Match tool names case-insensitively and by the tool suffix (`query_tasks`, `show_tasks`, …), not by an exact `Vaiz` prefix. Tools may also be loaded lazily: a Vaiz tool that is not in the current tool list is not missing — load it through tool search (for example `Vaiz query_tasks`) before concluding it is unavailable. Work with Vaiz only through these tools: do not open app.vaiz.com in a browser or drive the Vaiz desktop app with Computer Use, even if the user's `@Vaiz` mention also resolves to that app.

## Finding tasks: `show_tasks` or `query_tasks`

Both tools take the same filters and return the same rows. Pick by who needs the rows:

- **The user wants to see the list** ("show my tasks", "what is in Review") → `show_tasks`. On hosts with MCP Apps the list is rendered as an interactive widget and the rows are **not** returned to you.
- **You need the rows** to resolve an id, count, compare, answer a question in words, or prepare another call → `query_tasks`. It never renders a widget.

Filters combine with AND. Useful patterns:

- my open tasks: `assignees: [myMemberId], completed: false`
- a board column by name across all boards: `groupLabel: "In Progress"`
- epics in a project: `projectId, typeLabel: "Epic"`
- unassigned: `assignees: "empty"`; no deadline: `dueDate: "empty"`; no milestone: `milestones: "empty"`
- overdue: `dueBefore: <today>T00:00:00Z, completed: false`
- include archived: `includeArchived: true`
- next page: `skip: 50, limit: 50` (max `limit` is 100)

Prefer `groupLabel` and `typeLabel` when you know names but not ids; use `groupId` / `types` when you already have ids from `get_board`. When the user narrows a shown list ("only Anna's"), call `show_tasks` again with the matching filters instead of describing the subset in text.

To count, put every condition into the filters and read "Found N" from the result (`limit: 1` is enough). When all matches fit on one page, the "Exact counts" line splits them by assignee, priority, column, and status. Never count rows yourself. Due dates come as calendar days (`YYYY-MM-DD`); do not shift them into the user's timezone.

Other ways to find a task:

- `search_space` with `entityType: "task"` — keyword search over names and content when you do not know the HRID.
- `get_task_context` — compact decisions, problems, risks, recent Devlogs, and code links for a task (see the `vaiz-memories` skill).

Find your own member id with `get_current_user`; resolve other people with `query_members`.

## Response protocol for `show_*` lists

The first text block (and `structuredContent.instruction`) tells you how the result was delivered:

- "rendered for the user in an interactive widget" — the user already sees the rows. Do not repeat them as a table or list, not even a subset; reply with one short sentence or answer the specific question.
- "rows follow as JSON in the next content block" — there is no widget; present the rows yourself as a concise table.

If neither phrase is present: `structuredContent` without a `data` array means a widget was rendered; with `data` means you present it. Edits the user makes inside the widget (column, priority, assignees, types, due date) are already saved in Vaiz — do not repeat them.

## Reading a task

- `get_task` — full task by id or HRID. `board` / `group` are the main board; `boards` lists every board the task lives on with role `main` or `secondary`. Custom field values are omitted unless `includeCustomFields: true`.
- `get_task_comments` — comment thread.
- `get_task_history` — change log.
- `get_board` — board structure: columns (`groups`), task types (`typesList`), custom fields. Read it before creating tasks on an unfamiliar board.
- `get_automations` — automations configured on a board, useful to understand why a task moved or changed automatically (see `vaiz-automations`).

## Creating a task

`create_task` takes a `data` object. Required: `name` and `boardId`. Optional: `groupId` (defaults to the first column), `description` in Markdown, `priority` (`"0"` Low, `"1"` General, `"2"` Medium, `"3"` High, `"4"` Urgent — names are accepted too), `assignees`, `followers`, `dueStart`, `dueEnd` (ISO 8601), `parentTask` for a subtask, `milestones` (not allowed on subtasks), `types` from the board's `typesList`, and `customFields`.

Mentions in Markdown use `@[label](kind:id)` where kind is `user`, `task`, `document`, `milestone`, `project`, or `board`.

Before creating: search for an existing task on the same topic with `query_tasks` or `search_space`, and read `get_board` to pick a valid column and type. To create a whole project with boards, milestones, and starter tasks at once, use `setup_space` instead (see `vaiz-projects-milestones`).

## Editing a task

`edit_task` takes a `data` object with `taskId` plus only the fields to change: `name`, `assignees` (replacement list; `[]` unassigns everyone), `completed` (`true` to close, `false` to reopen), `dueStart` / `dueEnd` (`null` clears), `priority`, `types`, `milestones` (replacement lists), `group` to move to another column, `parentTask` (id to nest, `null` to detach), `coverUrl`, `customFields`. It always works on the task's main board.

Moving a column is not a silent edit: the board's "moved to column" automations run and AI agents watching the board may start. `completed` is a separate flag — set it explicitly when the user says the task is done.

To change the description, use `replace_document_fragment` or `edit_document_content` with the task's document id (from `get_task`); see the `vaiz-documents` skill. To discuss rather than change, add a comment with `create_comment` (`entityType: "task"`).

## Boards: main and secondary

A task has one main board and can also appear on secondary boards.

- Show the task on another board too → `add_task_to_board` (optional `groupId`, first column by default).
- Take it off one of its boards → `remove_task_from_board`; the task is not deleted.
- Move it to another board → `add_task_to_board` on the target, then `remove_task_from_board` on the old one. There is no separate move tool. When the main board is removed, the task is rehomed onto the first remaining board; check `boards` in the response and tell the user which board is now main.

Re-adding a board restores the task's previous column and milestones there. Types, custom fields, and milestones belong to a board: after a move, check them on the new main board.

## Connections between tasks

| Relationship | Use |
| --- | --- |
| Part of a bigger task | `edit_task` `parentTask` (`null` detaches) |
| Must be done before / after | `set_task_blocker` |
| Related, no order | The board's relations custom field via `edit_task` `customFields` |
| Should hear about changes | `set_followers` with `entityType: "task"` |

`set_task_blocker` toggles a link: `direction` is relative to `taskId` — `"blockers"` means `blockerTaskId` blocks `taskId`; `"blocking"` means `taskId` blocks `blockerTaskId`. Calling it again with the same arguments removes the link. Assignees are notified anyway; add followers only for people who are not assigned.

## Archiving

"Remove" or "delete" a task means `set_task_archived` with `archived: true`; there is no tool that deletes a task. Restore with `archived: false` (optional `groupId` picks the column). A task on several boards cannot be archived — remove the extra boards first. Find archived tasks with `query_tasks(includeArchived: true)`. See `vaiz-safe-changes` before bulk changes.

## AI agents

Members with `isAgent: true` are AI agents, not people. Assigning one in `create_task` / `edit_task` starts an agent run that may change the task and spends AI credits. Tell the user it is an agent and confirm first, then report `agentInvocations` from the response (see the `vaiz-agents` skill). Never pick an agent as a fallback assignee.

## Good habits

- Confirm the space with `get_space_info` when the user has several spaces; switch with `select_space` if needed.
- Do not create tasks for things that belong in Space Memory (decisions, conventions) — use the `vaiz-memories` skill instead.
- Link code to the task with `link_code_entity` when a branch, pull request, or merge request exists (see `vaiz-code-links`).

Further reading: https://vaiz.com/help/tutorials/how-to-connect-vaiz-to-mcp · https://vaiz.com
