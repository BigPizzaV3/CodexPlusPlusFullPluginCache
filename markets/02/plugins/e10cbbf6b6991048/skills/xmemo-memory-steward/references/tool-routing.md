# XMemo public tool routing

Use only tools available in the connected XMemo plugin. Never substitute a
nonexistent legacy or full-profile tool.

## Connection and memory lifecycle

| Intent | Tool |
| --- | --- |
| Check connection or account identity | `get_mcp_identity` |
| Save a new durable concept | `remember` |
| Correct or revise an existing concept | `update_memory` |
| Soft-delete by default or explicitly hard-delete an exact target | `forget` |
| Restore an eligible soft-deleted memory | `restore_memory` |
| Explain why a memory exists or matched | `explain_memory` |

## Recall and analysis

| Intent | Tool |
| --- | --- |
| Quick recall | `recall` |
| Exact or scoped memory search | `search_memory` |
| Bounded multi-memory or resume context | `recall_context` |
| Aggregate memory statistics or activity | `memory_overview` |
| Analyze supplied text before deciding what deserves memory | `analyze_memory_text` |

## Progress and structured work

| Intent | Tool |
| --- | --- |
| Save or replace resumable working state | `update_state` |
| Record a completed milestone, decision occurrence, or handoff event | `record_event` |
| Create, update, complete, or list action items | `todo` |
| Manage transactions or subscriptions | `ledger` |
| Create or mutate an authorized project entity | `project` |

Formal project creation requires:

```text
project(entity="project", action="create", name="<project name>")
```

Omit `project_id` during project creation. For later project mutations, use the
authorized project identifier required by the selected action. Existing
`Projects / <name> / ...` memory paths attach to the formal project; a path must
not silently create one.

## Visual and project surfaces

| Intent | Tool |
| --- | --- |
| Open the interactive TODO Board | `open_todo_board` |
| Open the interactive Ledger workspace | `open_ledger` |
| Get a short project status or next-action answer | `get_project_summary` |
| Open Project Workspaces Home or one project workspace | `open_project_workspace` |

Visual tools are for opening interactive UI. Do not call them when the user
only needs a concise text answer.

## Public-surface boundary

The ChatGPT public tool surface does not expose a dedicated restart-snapshot
restore operation. Reconstruct a resumed session from `recall_context`,
`get_project_summary`, relevant TODOs, and recorded events. Do not claim that
XMemo can reopen the original ChatGPT thread.
