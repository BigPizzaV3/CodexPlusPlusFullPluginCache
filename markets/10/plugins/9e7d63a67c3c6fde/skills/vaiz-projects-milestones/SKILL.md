---
name: vaiz-projects-milestones
description: Navigate and build the Vaiz workspace structure — list projects and boards, set up a project with boards from templates in one call, configure board columns, types, and custom fields, inspect project activity, and show, query, create, edit, or archive milestones.
---

# Vaiz projects, boards, and milestones

A Vaiz space contains projects; each project contains boards; boards hold tasks and milestones. Use this skill to orient yourself in a space, to create or reshape its structure, and to plan work at the milestone level.

## Prerequisite

The Vaiz MCP server (`https://api.vaiz.com/mcp`) must be available through the installed Vaiz plugin and authorized with OAuth (open the Vaiz connection and complete OAuth sign-in).

Vaiz tools can appear under different names depending on how Vaiz is connected: `mcp__Vaiz__query_tasks` for a directly configured MCP server, or `mcp__codex_apps__vaiz_query_tasks` (sometimes with a longer app prefix such as `vaiz_testing_`) when Vaiz is installed as an app. Match tool names case-insensitively and by the tool suffix (`query_tasks`, `show_tasks`, …), not by an exact `Vaiz` prefix. Tools may also be loaded lazily: a Vaiz tool that is not in the current tool list is not missing — load it through tool search (for example `Vaiz query_tasks`) before concluding it is unavailable. Work with Vaiz only through these tools: do not open app.vaiz.com in a browser or drive the Vaiz desktop app with Computer Use, even if the user's `@Vaiz` mention also resolves to that app.

## Orientation

Start here when you do not yet know the ids you need:

1. `get_space_info` — current space, your permissions.
2. `list_projects` — all projects in the space with their ids.
3. `list_boards` — all accessible boards, or `list_boards(projectId)` for one project. Board ids are required by `create_task` and `create_milestone`.
4. `get_project` — details of one project.
5. `get_board` — columns (`groups`), task types, custom fields of one board.
6. `search_space` with `entityType: "project"` or `"board"` — when you only know a name.

## Setting up structure

- **A project with boards (and optionally milestones and starter tasks)** → one `setup_space` call. It is atomic, accepts up to 20 boards, 30 milestones, and 100 tasks, and needs Manager rights. Prefer it over a chain of `create_project` / `create_board` / `create_milestone` / `create_task`.
- **One empty project** → `create_project` (`slug` is the HRID prefix, e.g. `MKT` → `MKT-1`). A project needs at least one board before it can hold tasks.
- **One board in an existing project** → `create_board` with a `templateId` or custom `groups`, `typesList`, and `customFields`.
- **Templates** → `get_board_templates` lists built-in boards (scrum, kanban, team templates, …). Talk to the user in template titles, never ids.

`setup_space`, `create_board`, and `configure_board` write immediately. Before calling them, ask about anything missing — team size and roles, kinds of work, the stages a task goes through, the current version or milestone — then propose the plan in plain words and wait for an explicit yes. Add starter tasks only when the user asked for content, not just structure. Report the created entities with the links from the response.

## Changing a board or project

- `configure_board` — rename a board, add or edit columns, add/edit/remove task types, add/edit custom fields, in one batch. Call `get_board` first and send operations on top of the current state, never the whole structure. Columns and custom fields cannot be deleted — hide them with `hidden: true`. Custom-field options cannot be edited; offer a new field instead.
- `reorder_board` — new order of columns and/or custom fields; pass every id exactly once.
- `edit_project` — rename or change description, color, icon. The slug cannot change.
- Archive a project or board with `set_project_archived` / `set_board_archived`. `delete_board` is permanent and takes all its tasks and milestones with it — see `vaiz-safe-changes` first. Projects cannot be deleted.
- Board automations ("when a task moves to Review, assign Anna") are covered by the `vaiz-automations` skill.

## Project history

`get_project_history(projectId)` returns activity across the project: task changes, comments, document edits, and more. Narrow it with `dateRangeStart` / `dateRangeEnd` (ISO dates), `entityTypes`, `taskIds`, `boardIds`, `createdBy`, or event `keys` / `excludeKeys`. Paginate with `limit` and the `page.nextCursor` value from the previous response.

Use it for "what happened in this project this week" style questions instead of reading every task.

## Milestones

- `show_milestones` — the user wants to see milestones; renders a widget, rows are not returned to you. Follow the widget response protocol from `vaiz-tasks`: do not repeat rows the user already sees.
- `query_milestones` — you need the rows (resolve a name to an id, compare progress, answer a question). Both take optional `boardId` or `projectId`.
- `get_milestone(milestoneId)` — one milestone with its document and linked tasks.
- `create_milestone` — requires `name` and `boardId`. Optional `description` is a **short plain-text summary** (not Markdown). `dueStart` / `dueEnd` are ISO 8601 dates.
- `edit_milestone` — change `name`, `description`, `dueStart`, `dueEnd`; only passed fields change, `null` clears a date.
- `set_milestone_archived` — the way to remove a milestone; its tasks stay on the board. Restore with `archived: false` (archived milestones reject edits until restored).

To give a milestone rich content, call `edit_document_content` or `replace_document_fragment` with the milestone's `documentId` (see the `vaiz-documents` skill). To attach tasks to a milestone, pass the milestone id in `milestones` when calling `create_task` or `edit_task` (see `vaiz-tasks`). Subtasks cannot carry milestones.

Comments on a milestone go through `create_comment` with `entityType: "milestone"`. Creating or editing a milestone can start AI agents watching the board; see `vaiz-agents`.

## Good habits

- Resolve names to ids once, then reuse the ids for the rest of the session.
- Check `query_milestones` before creating one to avoid duplicates.
- Record planning decisions that outlive the milestone in Space Memory (see `vaiz-memories`).

Further reading: https://vaiz.com/help/tutorials/how-to-connect-vaiz-to-mcp · https://vaiz.com
