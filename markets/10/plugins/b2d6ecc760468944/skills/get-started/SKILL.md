---
name: cuecall-get-started
description: How to answer questions about a theater (theatre) production with the CueCall connector's tools, and what the connector will not do.
---

# Working with CueCall

CueCall is theater production management. A **production** (show) holds
**scenes**, a **roster** of cast and crew, **characters**, a **schedule** of
rehearsals and performances, department-tagged **notes**, **tasks**, **cues**,
**files** (scripts, sides, documents) and an **inventory** of costumes, props,
set pieces and equipment. Scenes are the spine: a scene lists who is in it and
what it needs.

## Start with the production

Call `whoami` first. It returns the account and every production it can open,
with the role held on each. Most tools take a `showId` from that list. If the
person has one production, use it without asking. If they have several and the
request does not say which, ask.

## Reading

- `get_show` gives an overview: dates, the account's role and permissions,
  features the production has turned off, and counts of scenes, roster and
  upcoming events.
- `list_scenes` gives the running order with readiness. `get_scene` gives one
  scene's people, characters, inventory, cues and notes.
- `list_people` is the roster. Email and phone appear only when the account's
  role may see them. If they are absent, say that the role does not include
  contact details. Do not guess them.
- `list_events` defaults to now onward, across every production unless you
  pass `showId`. Pass `from`/`to` for a range and `includePast: true` for
  history. Times are UTC instants, so convert to the person's time zone when
  you answer.
- `list_notes` filters by scene, department or unresolved only. `list_tasks`
  filters by status, department, assignee or overdue, across every production
  unless you pass `showId`.
- `list_inventory` and `get_scene_inventory` cover costumes, props and sets.
  Costs appear only for roles that may see them.
- `list_files` then `read_file` returns a script or document as text. A long
  document is clipped, so raise `maxChars` to read further. Audio, video and
  images are described, never returned.
- `read_script_page` reads the production's script a few pages at a time,
  with the cues and notes already on each page. Pages are numbered as the PDF numbers
  them, which may differ from the number printed on the page.
- `search` finds anything by words, and `fetch` opens a search result by id.

## Writing

Write tools appear only on a connection the person allowed to make changes,
and each one is still refused unless their role could do it in the app.
Before writing, confirm the production, the scene (if any) and the exact
wording. Afterwards, report what was created or changed.

- `create_note`, `update_note`, `resolve_note`. Give `create_note` a script
  page and the line it is about to put the note on that page of the script.
- `create_task`, `update_task`
- `create_event`, `update_event`
- `create_scene`, `update_scene`
- `create_announcement` (it is posted in the app, and nobody is emailed)
- `create_cue` adds a tech cue to a scene. Give the script page and the line
  that calls it, copied exactly, and the cue is pinned beside that line.
  Read the page with `read_script_page` first.
- `update_cue` changes a cue's number, description, trigger, mics,
  characters, song, timing or page. A new page or trigger line pins it again.
  Cues are not deleted here; that is done in the app.
- `create_inventory_item`, `update_inventory_item`
- `assign_inventory_to_show`, `assign_inventory_to_scene`,
  `assign_inventory_to_character`, and their `remove_inventory_from_show`,
  `remove_inventory_from_scene` and `remove_inventory_from_character`
  counterparts. Removing takes the item off. It does not delete the item from
  the library.
- `submit_feedback` sends a bug report or idea to the CueCall team. Use it
  only when the person asks to send feedback, in their words, without other
  people's contact details. A confirmation is emailed to the person's own
  address.

Every record a tool returns carries a `url` that opens it in CueCall. When you
mention or change something, give the person that link. Never build one.

Nothing here deletes a record, emails anyone else, uploads a file, invites
anyone, changes anyone's access or runs CueCall's AI generators. If asked to do one of
those, say the connector cannot and point to the CueCall app.

## Permissions

The connector sees exactly what the signed-in account sees. A result that is
empty or refused reflects the account's permissions, not a fault, so say that
plainly. Never infer or state anyone's age, guardian, medical or measurement
details.
