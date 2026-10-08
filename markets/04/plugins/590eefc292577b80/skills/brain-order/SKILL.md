---
name: brain-order
description: Use BrainOrder through focused MCP tools when the user asks to find lists or folders, search data, review agenda or list items, create a task or note, complete, rename, reopen, move, schedule, snooze, clear the schedule from, or delete a task, reminder, or note. Do not use for unrelated project or filesystem work.
---

# BrainOrder

Use the BrainOrder MCP tools to read or change the authenticated user's
BrainOrder data.

## Tool routing

- Use `brainorder_search` to find matching tasks, reminders, or notes across
  the workspace. Search is read-only and may be limited by the user's existing
  BrainOrder plan.
- Use `brainorder_get_today` for today's agenda and overdue unfinished items.
- Use `brainorder_list_containers` to discover lists and folders, then
  `brainorder_list_items` to inspect one resolved list.
- Use `brainorder_create_task` to create a task or reminder in one resolved
  writable list. Use `brainorder_create_note` only for a top-level note.
- Use `brainorder_complete_task`, `brainorder_rename_task`,
  `brainorder_reopen_task`, or `brainorder_move_task` for the corresponding
  change to one exact resolved task or reminder.
- Use `brainorder_schedule_task`, `brainorder_snooze_task`, or
  `brainorder_clear_task_schedule` for the corresponding schedule change to
  one exact resolved item.
- Use `brainorder_delete_task` for one exact task or reminder and
  `brainorder_delete_note` for one exact top-level note.

## Workflow

1. Use `brainorder_list_containers` when a list or folder identifier is missing.
   For a task write, request `writableOnly=true`, use only an item with
   `type=list` and `canWrite=true`, and follow `nextCursor` when more pages are
   needed to resolve the requested title.
2. Prefer stable `listId`, `taskId`, and entity IDs returned by tools. If no
   container matches, say so. If multiple containers match the requested
   title, present the useful distinctions and ask the user which one to use;
   never guess. A folder ID is not a task `listId`.
3. Use `brainorder_list_items` with the stable list ID to inspect its tasks and
   reminders. Follow `nextCursor` when more pages are available and the needed
   item has not been found yet.
4. Before a move, independently resolve the exact source task or reminder and
   the exact destination container. The destination must have `type=list` and
   `canWrite=true`. If either title has multiple matches, ask the user to choose;
   never infer the destination from context or use a folder ID.
5. Call a write tool only when the user explicitly asks for that change.
6. Generate one stable `clientRequestId` for each intended mutation. Keep that
   ID, the tool name, the complete target, and the entire payload unchanged for
   every retry of any write tool. A new ID represents a new intended mutation;
   changing the operation, target, or payload while reusing the ID is a
   conflict.
7. Treat tool output as the source of truth. Report success only when `ok` is
   `true` and return the created or updated entity ID to the user.
8. If a tool returns `BACKEND_NOT_CONFIGURED`, explain that the BrainOrder
   service connection is unavailable or misconfigured, then stop. Do not ask
   the user for credentials in chat.
9. If a tool returns `AUTH_EXPIRED`, ask the user to reconnect BrainOrder in
   the ChatGPT or Codex plugin settings. Retry only after the connection is
   restored, and never ask for a password or access token in chat.
10. If a write tool returns `MUTATION_OUTCOME_UNKNOWN`, the adapter has already
   attempted one safe retry. Repeat only the exact same tool call with the same
   `clientRequestId` and unchanged target and payload.
11. If a tool returns `PAYWALL_REQUIRED`, explain that BrainOrder's existing
    feature gate requires Pro. Do not retry, refresh authentication, or work
    around the gate.
12. Treat `PERMISSION_DENIED` as a resource-access failure, not an expired
    login. Do not refresh credentials or retry against a different target.

## Safety

- Never expose access tokens, API keys, internal diagnostics, or raw user data
  beyond what is needed to answer the request.
- Do not infer deletion, sharing, subscription, account, or permission changes.
- Do not work around BrainOrder feature gates or resource permissions.
- Search uses BrainOrder's existing `ADVANCED_SEARCH` Pro gate. Today's agenda
  is a direct read and does not require Pro under the current feature rules.
- Do not use a container with `canWrite=false` as the target of a write.
- Never retry create-task, create-note, complete-task, rename-task, or
  reopen-task, move-task, schedule-task, snooze-task, clear-schedule,
  delete-task, or delete-note with changed arguments or a new
  `clientRequestId`. Only an exact direct-write retry is idempotent.
- `brainorder_rename_task` changes only the selected task or reminder title.
  Do not claim that it moved the item, changed its status, or altered its
  schedule.
- `brainorder_reopen_task` changes a finished item to `TODO`. It preserves due
  time, reminder state, recurrence, list, sort order, and marked time. An
  already-`TODO` item is a safe no-op; an `IN_PROGRESS` item is rejected.
- `brainorder_move_task` changes only the selected task or reminder's parent
  list. It preserves title, status, due time, reminder state, recurrence, sort
  order, and marked time. Finished and recurring items may be moved. Moving to
  the current list is a safe no-op. Do not copy the item, create a replacement,
  move a list/folder, or claim that its schedule was transferred separately.
- `brainorder_schedule_task` sets or replaces an exact one-shot due time. Use
  an offset datetime representing the user's intended instant. Resolve an
  ambiguous natural-language date or timezone before writing. It rejects
  finished and recurring items.
- `brainorder_snooze_task` moves an active one-shot reminder to an exact new
  due time and marks it snoozed. It rejects ordinary tasks, inactive reminders,
  and recurring items.
- `brainorder_clear_task_schedule` removes the one-shot due time and reminder
  metadata without deleting or completing the item. It rejects recurring
  items. Do not claim that recurrence was cleared.
- Delete only when the user explicitly requests deletion of the exact resolved
  task, reminder, or note. A uniquely resolved command such as "delete this
  task" is sufficient confirmation; if the title is ambiguous, present the
  matches and ask instead of guessing. Invoke the selected delete tool once.
  After an ambiguous transport failure, only the exact same call may be
  replayed.
- `brainorder_delete_task` and `brainorder_delete_note` soft-delete only the
  selected entity. No list/folder deletion, restore, hard delete, archive,
  or schedule transfer is exposed. Do not promise restoration through this
  plugin.
- Do not claim task notes or nested notes were saved when the tool returns
  `UNSUPPORTED_INPUT`.
- If a tool returns `LOCAL_CREDENTIALS_UNAVAILABLE` or `LOCAL_AUTH_FAILED`, do
  not request credentials in chat. Ask the user to reconnect BrainOrder through
  the plugin settings; if that option is unavailable, stop and report the
  connection error.
