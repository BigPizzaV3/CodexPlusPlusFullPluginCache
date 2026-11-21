---
name: vaiz-safe-changes
description: Remove, archive, restore, or delete things in Vaiz without losing work — archive instead of delete wherever Vaiz has an archive, know what each irreversible tool takes down with it, confirm before destructive or bulk changes, restore archived items, and handle read-only spaces.
---

# Safe changes in Vaiz

Your mistakes must stay reversible. Vaiz over MCP mirrors the app: where the app has an archive, MCP archives; deleting exists only where the app deletes too.

## Prerequisite

The Vaiz MCP server (`https://api.vaiz.com/mcp`) must be available through the installed Vaiz plugin and authorized with OAuth (open the Vaiz connection and complete OAuth sign-in).

Vaiz tools can appear under different names depending on how Vaiz is connected: `mcp__Vaiz__query_tasks` for a directly configured MCP server, or `mcp__codex_apps__vaiz_query_tasks` (sometimes with a longer app prefix such as `vaiz_testing_`) when Vaiz is installed as an app. Match tool names case-insensitively and by the tool suffix (`query_tasks`, `show_tasks`, …), not by an exact `Vaiz` prefix. Tools may also be loaded lazily: a Vaiz tool that is not in the current tool list is not missing — load it through tool search (for example `Vaiz set_task_archived`) before concluding it is unavailable. Work with Vaiz only through these tools: do not open app.vaiz.com in a browser or drive the Vaiz desktop app with Computer Use, even if the user's `@Vaiz` mention also resolves to that app.

## "Remove it" means archive

| Entity | Tool | What happens |
| --- | --- | --- |
| Task | `set_task_archived` | Leaves boards and lists; history, comments, and links are kept |
| Milestone | `set_milestone_archived` | Leaves the board and milestone lists; its tasks stay |
| Project | `set_project_archived` | Leaves the project list for everyone; boards, tasks, and documents are kept |
| Board | `set_board_archived` | Hidden from its project; tasks and milestones are kept |
| Document | `set_document_archived` | Leaves the doc tree together with its sub-documents |
| Memory entry | `set_memory_archived` | Hidden from reads and search; status unchanged |
| Automation | `edit_automation` with `enabled: false` | Stops running, stays in the list |
| Member | `set_member_deactivated` | Loses access and frees a seat; their work stays |

All of these are restored by the same tool with `archived: false` (or `enabled: true`, `deactivated: false`) and are idempotent: a repeated call reports `changed: false`.

- A task that lives on more than one board cannot be archived: remove it from the extra boards first (`remove_task_from_board`).
- Archiving a task runs the board's "archived" automations, as in the app.
- Archived projects, boards, milestones, and documents reject edits until they are restored.

## Irreversible tools

Call these only when the user explicitly asked to delete, and confirm first, naming exactly what goes away. If the user only wants something out of sight, archive instead.

| Tool | What is lost |
| --- | --- |
| `delete_board` | The board **with all its tasks and milestones**; nothing goes to the archive |
| `delete_document` | The document; its direct sub-documents move up one level |
| `delete_comment` | Your own comment; shown as deleted in the thread |
| `delete_automation` | The automation; tasks it already changed stay as they are |
| `delete_time_entry` | Your own time entry, from the task log and reports |

Before `delete_board`, tell the user how many tasks and milestones it holds (`query_tasks` and `query_milestones` with `boardId`). There is no MCP tool to delete a task, milestone, project, or member — archive or deactivate instead and say so rather than looking for a workaround.

## Restoring

List tools do not return archived projects, boards, milestones, or documents, so keep the id from the archiving call or ask the user for a link or id. Archived tasks are found with `query_tasks(includeArchived: true)`.

- Task: `set_task_archived` with `archived: false`; `groupId` optionally picks the column of its main board.
- Document: `set_document_archived` with `archived: false`; `parentDocumentId` and `index` choose where it goes back (by default the end of the top level).

## Bulk changes

"Clean up the old tasks" is still a decision per item for the user. Show what matches first (`show_tasks` with the filters), get a yes for that set, then act. Report what changed and what was skipped.

## Side effects that reach other people

- Changing a task's column, assignees, priority, dates, or completion, adding comments, and creating or editing milestones can start AI agents and board automations (see `vaiz-agents` and `vaiz-automations`).
- `invite_members`, `set_member_role`, and `set_member_deactivated` change who can see the space; confirm the people and the role first.

## Read-only space

When a space's trial has ended without a subscription, every write tool fails with "This space is read-only…". Reading still works, and so do `select_space` and `invite_members`. Do not retry or look for another tool: tell the user a space owner can upgrade the plan in Vaiz.

Further reading: https://vaiz.com/help/tutorials/how-to-connect-vaiz-to-mcp · https://vaiz.com
