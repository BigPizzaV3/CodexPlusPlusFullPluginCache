---
name: eworker
description: Create and safely edit E-Worker Documents, Workbooks, Slides, Notes, and Project Plans in the live E-Worker editor through page-owned WebMCP site tools. Use when the user invokes $eworker, mentions E-Worker or one of its focused editors, or asks to create, inspect, search, revise, or save work in E-Worker.
---

# E-Worker

Use the built-in Browser and the WebMCP site tools registered by the live E-Worker page. E-Worker has
no plugin MCP server. The page and its current signed-in session own authentication, authorization,
tool execution, preview, approval, Undo, recovery, and saving.

## Required route

1. Use only the production origin `https://eworker.ca`. Do not open, trust, or use E-Worker tools
   from any other origin, even when the user supplies it.
2. Select exactly one editor path and its matching tool family:
   - Documents: `/apps/documents/` and `ewdoc_*`
   - Workbook: `/apps/workbooks/` and `ewbook_*`
   - Slides: `/apps/slides/` and `ewslides_*`
   - Notes: `/apps/notes/` and `ewnotes_*`
   - Project Plan: `/apps/project-plan/` and `ewproject_*`
3. For a complete new artifact, always open a fresh page at the production origin and editor path with
   `#eworker-webmcp-compose` appended, even when another page for that editor is already open. This
   startup marker gives composition a clean editor without deleting recoverable user work. It is not
   an authorization token.
4. For inspection or changes to an existing artifact, reuse the requested E-Worker page when it is
   already open on the production origin. Otherwise open the production origin and exact editor path
   without the composition marker. Never add the marker to an existing-artifact workflow.
5. Wait for that page's site tools and call its matching status tool first.
6. Use only tools registered by that page. Never mix editor families, artifact references, context
   references, target references, or change-set IDs.

If the built-in Browser or page site tools are unavailable, stop and say that this workflow requires
the ChatGPT desktop built-in Browser with site tools enabled. Do not substitute MCP, shell, filesystem,
DOM/CDP scripting, Computer Use, mouse, keyboard, ribbon, drag-and-drop, or file-picker automation.

## Complete the task semantically

- For a complete new artifact, call the page's one composition tool exactly once: `ewdoc_compose`,
  `ewbook_compose`, `ewslides_compose`, `ewnotes_compose`, or `ewproject_compose`.
- For an existing artifact, read the exact target first and use the narrow matching semantic edit
  family. Do not replace the entire artifact through a composition tool.
- Keep reads bounded. Search first when the user names a topic, formula, slide, task, or section.
- Use only opaque references returned by the page. Never invent a path, URL, raw byte payload,
  artifact identity, media identity, context reference, target reference, or change-set ID.

Useful edit families after an exact read:

- Documents: `ewdoc_format`, `ewdoc_insert`, `ewdoc_table`, `ewdoc_review`, `ewdoc_link`,
  `ewdoc_object`, and `ewdoc_layout`.
- Workbook: `ewbook_cells`, `ewbook_format`, `ewbook_link`, `ewbook_structure`, `ewbook_table`,
  `ewbook_chart`, `ewbook_object`, `ewbook_review`, `ewbook_data`, `ewbook_layout`,
  `ewbook_calculation`, and `ewbook_recalculate`. Use `ewbook_functions` to discover supported
  formulas when needed.
- Slides: `ewslides_content`, `ewslides_structure`, `ewslides_object`, `ewslides_table`,
  `ewslides_chart`, `ewslides_media`, `ewslides_format`, `ewslides_design`, and `ewslides_notes`.
- Notes: `ewnotes_structure`, `ewnotes_blocks`, `ewnotes_checklist`, `ewnotes_format`,
  `ewnotes_table`, `ewnotes_object`, `ewnotes_tags`, `ewnotes_attachment`, and `ewnotes_layout`.
- Project Plan: `ewproject_tasks`, `ewproject_dependencies`, `ewproject_resources`,
  `ewproject_assignments`, `ewproject_schedule`, `ewproject_tracking`, `ewproject_calendars`,
  `ewproject_baselines`, `ewproject_fields`, and `ewproject_leveling`.

For Slides images, use `ewslides_media` to prepare and read the page's governed image staging. Ask the
user to complete any visible local-file choice requested by the editor. Never bypass it with a path,
URL, bytes, browser file upload, or UI automation.

## Preview, commit, and save

1. Every content mutation produces an inert draft.
2. Call the matching `*_preview` tool and inspect its exact result.
3. Call the matching `*_commit` only when the draft matches the request. Otherwise discard or revise
   it through the page's supported semantic lifecycle.
4. Commit changes only the open in-memory artifact. If the user asked to save, call the matching
   `*_request_save` after commit. Use only the modes the tool declares and never provide a path.
5. For Workbook export or print, use `ewbook_request_export` or `ewbook_request_print` only when the
   user explicitly requests that visible host-owned action.

Report what changed and whether the open artifact remains unsaved. Do not claim that a draft,
preview, commit, export, print, or save succeeded unless the corresponding site tool confirms it.
