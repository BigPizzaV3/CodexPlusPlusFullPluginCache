---
name: actions-and-follow-up
description: Turn findings into tracked actions in CitationLab and keep their status current. Use when the person wants to save a recommendation, create a task, see open actions or recommendations, or record that something was done.
---

# Actions and follow-up

Every action has a key such as `ELNO-142`; use that key when you mention an action, never its numeric id.

## See what is open

- `list_actions` with `projectId` and optionally `status`, `search` or `assignee`. Show key, title, status, priority and due date.
- `get_action` for one action's full record, `list_action_comments` for its discussion.
- `list_recommendations` / `get_recommendation` for the improvements CitationLab has found for the project, with their business case.

## Create

`create_action` with `projectId`, `title`, a `description` and `priority` (`low`, `medium`, `high`, `critical`). Optional: `dueDate` (YYYY-MM-DD), `assignee`, `tags[]`.

- Write the description as HTML: `<h3>` headings, short `<p>` paragraphs, `<ul><li>` lists. Include why (the finding and its numbers), what to do, and how success is measured.
- One action per distinct piece of work. Before creating several, list them and get a yes.

## Update

`update_action` with `actionId` (the key), `projectId`, and `status` together with a `comment` that explains the change. `add_action_comment` adds a note without changing anything else. A comment never replaces a status:

- `done` — finished and verified
- `waiting` / `on_hold` — blocked; name on whom or what
- `deferred` — postponed; say until when
- `in_progress` — work resumes now
- `cancelled` — only when the person decided to drop it

If the response carries `statusCheck`, the status was not changed — settle it before moving on.
