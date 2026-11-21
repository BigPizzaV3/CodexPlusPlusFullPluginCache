---
name: wren-notes
description: Write notes, explanations, worked solutions, summaries and figures as editable handwritten ink in the user's Wren notebook. Use when the user asks to put something in Wren or write it by hand in their notebook.
---

# Writing in the user's Wren notebook

Wren is a handwriting notebook. The tools write real, editable ink on a notebook page. It is not a document or an
image. The user can keep writing on the page by hand. Answer in chat unless the user asks for Wren, a notebook or
handwriting.

## Which tool
- Notes, an explanation, a worked solution, a summary, revision sheet, or text to copy: `write_notebook_page`.
- Several pages on one topic: `plan_notebook`, then one `write_notebook_page` per slot (`target.noteId` + `planSlot`).
- Same topic as an existing note: reuse its `noteId` (`target.noteId`), never start a second note. If the user may
  already have a notebook on the topic, call `list_recent_notebooks` first. `list_notes` and `get_note` find or read notes.
- One graph, diagram, chart or mind map on its own: `draw_figure`.
- `connect_account` if the user is not signed in; `get_profile` shows which account is linked.

## Writing a page
- Write a full page: 110-140 words in 6-8 blocks (a table or figure counts about 40 words), a heading per part.
- Mark 3-6 key terms (underline or highlight). A mark copies exact words from its own block.
- Mark every number with its unit and every formula as a math mark (keep every word in its latex).
- One accent colour. Put the takeaway in a callout (key_answer or key_idea) or a summary.
- Pick the `pageKind` that fits: worked_example, concept_summary, comparison_sheet, process_walkthrough,
  revision_sheet, or verbatim.
- When the user says "write this text", use `verbatim`: their words, unchanged and once, nothing added.
- Keep the user's own words, equations and data. Use the user's language as written.

## After a write
Reply in a sentence or two with the link the tool returned. Say it is editable ink in their Wren account that they
can keep writing on by hand. Do not redraw or re-list the page. Do not call it the user's own handwriting. Do not
say ChatGPT runs inside Wren.

## If a tool refuses
The error names what is wrong. Fix exactly that and retry once. If it still fails, tell the user plainly.
