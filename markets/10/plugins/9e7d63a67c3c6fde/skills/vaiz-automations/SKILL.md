---
name: vaiz-automations
description: Build and change Vaiz board automations — turn a "when X, do Y" request into conditions and actions with real ids, edit and publish automation graphs, pause or delete automations, and avoid duplicates and app-only webhook or Slack actions.
---

# Vaiz board automations

An automation belongs to one board: when a task event on that board matches its conditions, its actions run on that task. Only board managers and owners can create, change, or delete automations.

## Prerequisite

The Vaiz MCP server (`https://api.vaiz.com/mcp`) must be available through the installed Vaiz plugin and authorized with OAuth (open the Vaiz connection and complete OAuth sign-in).

Vaiz tools can appear under different names depending on how Vaiz is connected: `mcp__Vaiz__query_tasks` for a directly configured MCP server, or `mcp__codex_apps__vaiz_query_tasks` (sometimes with a longer app prefix such as `vaiz_testing_`) when Vaiz is installed as an app. Match tool names case-insensitively and by the tool suffix (`query_tasks`, `show_tasks`, …), not by an exact `Vaiz` prefix. Tools may also be loaded lazily: a Vaiz tool that is not in the current tool list is not missing — load it through tool search (for example `Vaiz get_automations`) before concluding it is unavailable. Work with Vaiz only through these tools: do not open app.vaiz.com in a browser or drive the Vaiz desktop app with Computer Use, even if the user's `@Vaiz` mention also resolves to that app.

## Before creating

1. `get_automations(boardId)` — an automation for the same trigger may already exist. Extend or re-enable it with `edit_automation` instead of adding a twin.
2. Collect real ids: columns and task types from `get_board`, people from `query_members` (they need access to the board), target boards from `list_boards` (same project only).
3. Say the automation back in plain words — "When a task moves to **Review**, assign **Anna**…" — and create it after the user agrees.

Then call `create_automation` with `boardId`, `title`, `conditions`, `actions`, and optionally `enabled: false` to create it paused.

## Conditions

The automation runs when one of the condition events happens and the task then matches all conditions. 1–10 conditions, each type once.

| Type | Fires when |
| --- | --- |
| `created` | A task is created on the board |
| `comment_added` | A comment is added |
| `complete` / `uncomplete` | A task is completed / reopened (never both in one automation) |
| `archive` | A task is archived |
| `assign` + `memberId` | The member is assigned |
| `group_change` + `groupId` | A task moves into the column |
| `type_change` + `typeId` | The type is added |
| `priority_change` + `priority` | The task gets the priority (`"0"` Low … `"4"` Urgent) |
| `code_change_linked` | A pull request (GitHub) or merge request (GitLab) is linked |
| `code_change_opened` / `code_change_merged` / `code_change_closed` | A linked PR/MR is opened or reopened / merged / closed without merging |

`code_change_*` conditions need GitHub or GitLab connected; branches and commits do not trigger them.

## Actions

Run in order, 1–10, each type once.

| Type | Does |
| --- | --- |
| `complete` | Completes the task |
| `archive` | Archives the task (it leaves the board for everyone — mention it) |
| `assign` + `memberId` | Assigns the member |
| `group_change` + `groupId` | Moves the task to a column of this board |
| `type_change` + `typeId` | Adds the type |
| `move_in_group` + `position` | Reorders it in its column: `top`, `middle`, or `bottom` |
| `duplicate_task` + `boardId` (+ `groupId`) | Copies the task to a board of the same project |

Moving a task to another board is not an automation action. An old `move_to_board` action shown by `get_automations` does nothing any more; offer to replace it with `duplicate_task` or with multihoming (`add_task_to_board`, see `vaiz-tasks`).

## Graph drafts and publication

`get_automations` also returns `draftGraph`, `publishedGraph`, `publishedVersion`, and validation issues. Only the published graph runs.

- Convert a legacy rule into a draft with `edit_automation` and `convertToGraph: true`; conversion does not publish.
- Replace the draft with `draftGraph` (version 1, nodes and edges; trigger, condition, and action nodes). Preserve existing node ids.
- Publish with `publishGraph: true` only when the user asks. Invalid or disconnected graphs cannot be published; saving a draft leaves the published graph running.
- Do not mix graph fields with legacy `conditions` / `actions` in one request. Once a graph is published, edit the graph.

## Changing and removing

- `edit_automation` — omitted fields keep their values; `conditions` and `actions` are replaced as a whole, so send the full list.
- Pause with `enabled: false` rather than deleting. `delete_automation` is permanent (tasks it already changed stay as they are); confirm first.
- Webhook and Slack actions are app-only: they cannot be created over MCP, and in an automation that has them the legacy actions cannot be replaced. Graph edits may keep those nodes only if you copy their returned items unchanged. Webhook values come back masked; never ask the user to paste secrets into the chat.

## Pitfalls

- Changes made by automation actions do not emit further automation events, so automations do not chain.
- Assigning an AI agent in an action does not start it: automations never wake agents. Agent reactions are configured in the agent's own trigger (see `vaiz-agents`).
- Changing a task over MCP runs automations the same way the app does: `edit_task` moving a column fires `group_change`, `set_task_archived` fires `archive`. Expect the extra changes and mention them to the user.

Further reading: https://vaiz.com/help/tutorials/how-to-connect-vaiz-to-mcp · https://vaiz.com
