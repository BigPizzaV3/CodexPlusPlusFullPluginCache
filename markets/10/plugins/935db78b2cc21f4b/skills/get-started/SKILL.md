---
name: get-started
description: Use Bluetab to find saved tabs, review tab groups and projects, read or add Brain Dump notes, and set reminders from the user's Bluetab browser extension.
---

# Bluetab

Bluetab is a browser tab manager. The `bluetab` tools read and change the user's own saved data:
tab groups (each with tabs), projects (sets of groups), Brain Dump notes and reminders.

## Reading

- To find a page the user saved, call `search_tabs` with words from its title or address.
- To see what is saved, call `list_groups`, then `get_group` for the tabs of one group.
- `list_projects` shows which groups belong to each project.
- `list_brain_dump` and `get_brain_dump_entry` return the user's quick notes.
- Results come from the latest snapshot uploaded by the extension. When a result has `stale: true`, mention that the data may be a few minutes old.

## Changing

- `save_tab_group`, `update_group`, `add_project`, `update_project`, `add_brain_dump`, `update_brain_dump` and `create_reminder` queue a change.
- Queued changes are applied the next time Bluetab is open in the user's browser. Tell the user the change is queued, not done.
- `create_reminder` takes `fireAt` as Unix time in milliseconds. Confirm the date and time with the user first.
- Nothing can be deleted through these tools. If the user asks to delete, explain that and point them to the Bluetab extension.

## Errors

- "Bluetab Pro is required": the user needs a Bluetab Pro subscription.
- "No snapshot available": the user should open Bluetab and turn on AI apps (MCP) in settings.
- "This connection is read-only" or a missing scope: the user connected without allowing changes.
