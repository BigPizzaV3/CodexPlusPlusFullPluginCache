---
name: notii
description: Work in the user's Notii (notes, notebooks, tasks, daily notes, Kanban boards, reminders and calendar) through the Notii connector. Use whenever the user mentions Notii or their notes, notebooks, to-dos, daily note, reminders or board, or asks to save, find or plan something they keep in Notii.
---

# Working in Notii

Notii is the user's notes app. The Notii connector acts as the user, with their access: their own notes and the notebooks (projects) people share with them.

## Which tool

| To… | Use |
| --- | --- |
| Find notes | `search` (matches words in titles, text and attachments, then notes about the same thing by meaning), then `fetch` for a note's full text |
| See recent notes, notebooks or tags | `list_notes` (by notebook or tag), `list_notebooks` (with board lanes and fields), `list_tags` |
| Write | `create_note` (Markdown), `update_note` (prefer `append_markdown`; it can also rename, retag or move), `create_notebook` |
| Work with tasks | `list_tasks` (soonest due first), `add_task` (to the daily note unless `note_id` is given), `complete_task` (`note_id` and `index` from `list_tasks`) |
| Plan days | `get_daily_note`, `get_calendar` (`from`/`to` as YYYY-MM-DD, up to three months; includes the user's subscribed calendars) |
| Remind | `set_reminder` (Notii emails the user then) |
| Track work | `update_card` (board lane, due date, owner, priority and the project's own fields), `set_project_fields` |
| Automate | `list_rules`, `create_rule`, `delete_rule` |
| Other | `create_canvas`, `share`, `save_clip` (save a web page, a selection, an image or a link) |

## Habits

- **Dates are the user's.** Pass their local date (YYYY-MM-DD) and IANA time zone (`timezone`) to `add_task`, `get_daily_note` and `set_reminder`. "Today" means the user's today.
- **Write Markdown.** Headings, lists, `- [ ]` checklists (they become real tasks), tables, fenced code and ```mermaid diagrams all turn into Notii blocks.
- **Link what you mention.** Every note has a `url`; cite notes as `[Title](url)` so the user can open them.
- **Don't duplicate.** Before making a note about something the user already keeps, `search` for it and offer to append instead.
- **Ask first** before anything that loses or sends something: `trash_note`, `update_note` with `markdown` (it replaces the whole body), `delete_rule`, and `share` (it emails the person).
- **Respect access.** Notes shared view-only can be read, not changed; if a tool says so, tell the user.
- **Keep the user's words.** When capturing, don't add facts the user didn't give; put open questions and follow-ups as tasks.
- **Not connected?** If a tool asks to connect Notii or fails to authorize, ask the user to connect (or reconnect) the Notii connector and approve it.
