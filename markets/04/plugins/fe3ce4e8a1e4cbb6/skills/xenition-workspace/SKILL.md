---
name: xenition-workspace
description: Use when the user wants to work with their Xenition workspace — create or edit content, ask about or search their own files, run their agents, generate 3D models, or build and share forms.
---

# Xenition

Xenition is the signed-in user's content workspace (documents, slides,
spreadsheets, notes, boards, media, 3D models, forms, and AI agents). Use its
tools whenever the user refers to "my Xenition …", to their own files/notes/
data, or asks to make something (a deck, doc, sheet, 3D model, form) or run
their agents. Do not use these tools for general knowledge questions.

## When to use which tool

- **Find / read the user's own content:** `search_artifacts` and
  `get_artifact` to locate and open items; `ask_workspace` for a grounded answer
  across their files (with sources); `query_document` to answer a question about
  one specific document; `summarize_artifact` for a TL;DR, key points, or action
  items; `extract_from_artifact` to pull a specific thing (dates, names, totals)
  as a list; `query_spreadsheet` to compute or answer over a sheet.

- **Create content:** `create_slides` (a designed deck), `create_3d_model`
  (text/image → 3D), and the document / spreadsheet / diagram / board creators.
  Use `repurpose_artifact` to turn one artifact into another surface (e.g.
  meeting notes → a task board, a document → a slide deck).

- **Edit or review existing content:** `edit_artifact` to change an item in
  place (rewrite, shorten, translate, fix); `review_artifact` to return
  constructive comments tied to quoted passages **without** changing the file.

- **Forms:** `find_forms` then `submit_form` to fill a built-in template into a
  finished document; `create_shared_form` to make a fillable form with a public
  link that collects responses in Xenition.

- **Agents & research:** `list_agents` to see the user's AI agents, then
  `run_agent` to start one on a task; `check_agent_run` (or `get_mission`) to
  fetch status and the final result of a background run.

- **Workspace actions:** board, calendar, notes, sheet, and ledger tools to
  read and update those surfaces; `my_agenda` for "what's on my plate today";
  and the agent/approval tools to see and decide pending actions.

## Rules

- Act only on the signed-in user's own workspace. Never invent artifact ids —
  find the right item with `search_artifacts` first.
- Long-running work (agent runs, 3D generation) happens in the background. The
  inline card shows live progress and fills in the result — do not claim it is
  finished before the card completes.
- Do not publish, share, or expose anything publicly unless the user explicitly
  asks (e.g. `create_shared_form` or a publish action).
- Prefer the tool that produces or reads real Xenition content over answering
  from memory when the user is asking about their own files or data.
