---
name: loopsii
description: Use the Loopsii MCP tools to read and update the user's freelance workspace — projects, clients, tasks, time entries, meetings, recordings and documents. Use it whenever the user asks about their work, wants to log time, create or update tasks, or asks what was said or decided in a meeting.
---

# Working with Loopsii

Loopsii is the user's own workspace. Every tool acts on their account, and every tool that returns a
`url` returns the record's page inside the app.

## Ground rules

- Finish every reply that created or changed something with the record's `url` as a link. The user is
  usually reading you with no Loopsii tab open.
- The `url` is never a public share link. Do not describe it as something the user can send to a client.
- Nothing here deletes. If the user asks to delete a record, say that deletion happens in the app.
- Use `search` first whenever the user names something you do not have an id for ("the Acme brief",
  "that invoice"), then `fetch` or the matching `get_*` tool for the full record. Narrow it with `type`,
  `project`, `client` or `since` when the user scopes the question.
- Archived projects are left out of `list_projects` unless you pass `include_archived`; a project name
  still finds an archived project when no active one matches.

## Time

- `add_time_entry` logs finished work: duration (`1h30m`, `45m`), the project, and a description of what
  was actually done. Never invent the description — take it from the user's words.
- `timer_start` starts a running timer (it stops any running one first); `timer_stop` ends it and
  reports the entry; `timer_status` says what is running.
- Ask for the project when it is ambiguous; do not guess between similarly named projects.
- `update_time_entry` files a logged entry under another project or fixes its description; take the
  entry id from `list_time_entries`.

## Tasks and projects

- `create_task` needs a title and a project; add priority, due date or milestone only if the user gave
  them. Completing a task is `update_task` with status `done`.
- `update_project` overwrites the fields you pass (stage, dates, price). Pass only what changes.
- Project stages are negotiation → planning → working → closure.
- `get_task` returns the task with its comments. `add_task_comment` posts as the user, and on a project
  shared with a client the comment shows in the client portal — post only what the user asked for,
  written the way they would write it.

## Meetings

- `list_meetings` finds the meeting; `get_meeting` gives its notes, tasks and project. Answer from the
  notes when they cover the question.
- For precise questions ("what exactly did Vlad say about the polygon budget?") call `get_meeting` with
  `include_transcript: true`. Long transcripts come in pages: while `transcriptNextOffset` is not null,
  call again with `transcript_offset` set to it.
- `update_meeting` and `update_recording` rename a meeting or recording or file it under a project. When
  a follow-up task comes from a meeting, pass `meeting` to `create_task` so the task is linked to it.

## Documents

- `create_document` takes a title, a project and markdown content; `update_document` replaces the
  content or title. `get_document` returns markdown.

## Style

- Short answers with the facts the tools returned. Quote meeting notes rather than paraphrasing
  decisions loosely.
