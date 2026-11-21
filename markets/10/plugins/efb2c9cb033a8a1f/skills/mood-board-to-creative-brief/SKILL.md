---
name: mood-board-to-creative-brief
description: "Turn an existing or edited Mood Board into a concise creative brief when the user asks for a designer handoff, a written art direction, or a summary of the board's design decisions and constraints. Ground the brief in model-visible contents and visible references. Do not use for generating a fresh board, a cohesion critique, or a photography shot list."
---

# Mood Board to Creative Brief

## Inputs

Use the latest board, the project and audience, the intended use, and any known
constraints or approved decisions. Distinguish established requirements from
ideas that still need a decision.

## Workflow

1. Prefer the latest model-visible `modelContent.moodBoard` over an earlier
   `structuredContent.moodBoard` tool result. If no contents are available,
   request them. Do not claim that the app exposes a board retrieval tool.
2. Extract exact palette values, font family names, note text, quote attribution,
   and reference sources. Describe image contents only when the image is visible
   or the user supplied a description. Leave undocumented details undecided.
3. Connect each ingredient to the project purpose. Label suggested color roles,
   typography roles, and imagery principles as proposals unless already
   established by the user. Preserve fixed anchors verbatim.
4. Write a concise, copy-ready brief with the following sections, omitting
   sections that have no useful evidence:
   - Project objective, audience, and intended deliverable.
   - Direction in one sentence and three defining characteristics.
   - Palette with exact hex values and established or proposed roles.
   - Typography with family names and established or proposed roles.
   - Imagery, materials, and styling principles tied to visible references.
   - Concrete do and avoid guidance grounded in the board.
   - Fixed constraints and unresolved production decisions.
5. Identify the few questions that would materially affect execution. Do not
   invent budget, measurements, deadlines, asset ownership, or approval status.
6. When the user needs a visual attachment, guide them to click **Export**, then
   **View**, in the widget. Describe the export as a JPEG. Treat export completion
   and the downloadable file as unknown unless the user provides them.

## App use

Consume existing board state without rerendering merely to write the brief.
Use `display-mood-board` only if the user also requests an annotated board.
In that case, submit the full `moodBoard.items` with at most ten items, an optional
`reason`, and only registered input fields. Read the returned
`structuredContent.moodBoard` and account for fresh UUIDs.

For annotations that need the original positions or uploaded-file associations,
give instructions for adding or editing a note within the existing widget.
Never drop retained ingredients to fit the tool limit or assume private upload
mappings transfer to a new rendering. Leave `resolve-mood-board-images` to the
widget; it is app-only.

## Deliverable

Return the brief in the conversation, ready to copy into a handoff. Make
established choices, proposals, and unresolved decisions easy to distinguish.
Include the short Export and View instructions only when useful for the handoff.

## Boundaries

Do not assume access to private layout, export file IDs, or export URLs. Do not
claim to export, upload, send, or attach the brief through the app. Avoid
inventing PDF or document-generation capabilities. Respect text-only requests
and keep external sharing subject to the user's explicit instructions.
