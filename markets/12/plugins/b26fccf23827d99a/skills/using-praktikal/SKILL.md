---
name: using-praktikal
description:
  Create interactive learning materials, student worksheets, quizzes, lessons
  and presentations with Praktikal. Use when teachers want to build classroom
  activities, find and adapt teaching materials, or practise with interactive
  questions through the connected Praktikal MCP tools.
---

# Using Praktikal

Use the connected Praktikal account's materials and permissions. Choose tools
from the current MCP catalog; available actions depend on the granted scopes. If
the connection is unavailable, explain what needs connecting before claiming to
have found or changed account content.

## Choose the content structure

The Repository contains reusable learning objects. Choose a container by
purpose:

- **Lesson:** one teaching session, divided into modules containing worksheets,
  slides, and other content. Tool names use `lecture`; lesson search uses
  `node_types: ["sblesson"]`.
- **Collection:** a sequence of lessons, such as a unit or course.
- **Book:** chapters of reading and reference material.
- **Worksheet:** an activity containing content and questions, reusable across
  lessons. Inserting an existing worksheet by reference shares later edits.
- **Slideshow:** delivery of content as a live session or assignment. Creating
  lesson content alone does not start a session or assign it to learners.

## Load the relevant playbook

Use `list_skills` to discover the account's available guidance. Load a returned
skill with `read_skill`, for example:

```json
{ "target": { "kind": "skill", "skill_id": "authoring-playbook" } }
```

Load the relevant server playbook before its workflow:

| Task                                                           | Playbook             |
| -------------------------------------------------------------- | -------------------- |
| Create or adapt lessons, choose content types, reuse materials | `authoring-playbook` |
| Compose and position native presentation slides                | `slide-composition`  |
| Draw an editable diagram or concept map                        | `canvas-authoring`   |
| Create a chart with axes, series, and data                     | `chart-spec`         |
| Create an HTML interactive activity or simulation              | `artifact-slides`    |

Read supporting references when the loaded playbook requires them, using
`read_skill` with `target.kind: "reference"` and its returned `reference_id`.
The live tool schemas govern arguments if an older playbook uses a retired name.
If a playbook is unavailable, use the exposed descriptions and schemas; explain
any missing guidance that prevents completing the task reliably.

## Find, read, and adapt materials

When a request names a book, lesson, or collection, first find that container
with `search_nodes`. Then search within its returned ID using `in_tree`. Use
`read_node` in structure mode to inspect its outline and full mode to read the
relevant content. Base summaries and suggestions on the returned material. For
an empty search, report the result and offer a useful search adjustment.

Before creating a lesson, search for an existing match. `create_lecture` returns
the lesson root and an initial module; use that returned module ID when adding
worksheets or slides. Inspect the relevant node-type schema before authoring
questions or unfamiliar content. Add related new siblings together when the
current `create_node` schema supports it.

Read existing content and its revision before editing. Use the dedicated editor
for the requested operation, such as `edit_slide`, `edit_canvas`, `edit_table`,
or `edit_html_artifact`; `update_node` edits ordinary fields directly, without a
`patch` dispatcher. Supply the tool's required revision preconditions. After a
conflict, read the latest content and reconcile the intended change before
retrying. Distinguish edits to a shared original from creating a separate copy.

## Practice with interactive questions

Resolve actual question IDs with `read_node`, or use `read_slideshow_content`
for a supported Praktikal slideshow link. Call `view_node` to display the
original interactive question. Respond to the learner's submitted answer and
continue with the next question when appropriate. Showing a card is not proof
that an answer was submitted or stored.

## Finish with evidence

Read back created or changed content to verify the requested outcome. Return the
actual user-facing `url` supplied by the tools. Keep signed `embed_url` values
inside the widget. State any incomplete steps or permission limits. Use
delivery, sharing, publishing, and results tools only when available and within
the user's request; an authoring request does not imply publishing or inviting
learners. Retrieve student results only for the authorized task and include only
the information needed to answer it.
