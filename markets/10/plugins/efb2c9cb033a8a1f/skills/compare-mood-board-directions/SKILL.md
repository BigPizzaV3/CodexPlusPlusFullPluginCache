---
name: compare-mood-board-directions
description: "Compare two or three creative directions in Mood Board when the user wants alternative visual routes, help choosing an aesthetic, or a structured comparison before committing to a board. Hold shared requirements constant and deliver comparable boards plus tradeoffs. Do not use for a single straightforward board request, a cohesion review, or widget layout changes."
---

# Compare Mood Board Directions

## Inputs

Use the project brief, audience, intended impression, fixed ingredients, and any
supplied references. Use the latest model-visible board contents when the user
is exploring alternatives to an existing board.

## Workflow

1. Establish the shared brief and the criteria for choosing a route. Retain
   fixed colors, references, wording, and other stated constraints across all
   alternatives. Ask a focused question if a missing constraint would materially
   change the routes; otherwise state reasonable assumptions.
2. Develop two routes by default, or three when requested. Give each a name and
   a one-sentence idea. Make the alternatives differ in at least two meaningful
   ingredients, such as palette, typography, imagery, or materials.
3. Use the same ingredient categories and a similar item count for each route
   so the comparison is fair. Target four to six items per route. Include a
   `note` naming the route and its defining idea; add a palette, font previews,
   and any relevant references that have reusable image sources.
4. Render one complete board per route through `display-mood-board`, using the
   registered schema, at most ten `moodBoard.items` per call, and an optional
   `reason`. Omit output IDs and unsupported title, grouping, or position fields.
   Use the note card to identify each route and the returned
   `structuredContent.moodBoard` to describe what was rendered.
5. Compare the routes in a short table against the shared criteria. Explain
   their audience fit, strongest benefit, and practical tradeoff. Recommend the
   route that best fits the user's priorities without inventing numerical scores.
6. Ask the user to choose a route or a specific combination when the choice is
   still open. If they already chose one, refine that route directly while
   retaining the fixed anchors and using the latest visible contents.

## Image and state handling

- Use source URLs rather than signed delivery URLs. Describe references only
  when visible or described by the user. If imagery is unavailable, represent
  the intended imagery in a note and render concrete palette and font items.
- For attachments without reusable image URLs, guide the user to upload the
  selected images into the route's widget. Never fabricate a hosted source or
  pass file IDs as URL arguments.
- Use separate search or generation tools only when available and appropriate
  to an additional user request. Do not present them as Mood Board capabilities.
- Treat route boards as separate renderings with fresh item UUIDs. Do not
  promise an in-place update, retained positions, transferred private upload
  mappings, persistent versions, or a side-by-side comparison interface.
- Leave the app-only `resolve-mood-board-images` helper to the widget. Do not
  assume access to `privateContent` or inspect unseen imagery from URL names.

## Deliverable

Provide the named route boards, the compact comparison, and one recommendation
with its reason. Preserve a text-only comparison when the user requests text
only or no tools; do not render solely because this skill was selected.
