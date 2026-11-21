---
name: curate-mood-board-references
description: "Select, organize, and explain supplied visual references for Mood Board when the user asks which images to keep, wants to reduce a crowded reference collection, or needs a purposeful image-led board. Identify motifs, remove redundancy, and explain each selection. Do not use for open-ended image search, image generation, literal color extraction, or a general board critique."
---

# Curate Mood Board References

## Inputs

Use supplied images, current model-visible image and gallery items, or explicit
image descriptions, together with the project purpose and must-keep references.
Separate visual evidence from the availability of a reusable rendering URL.

## Workflow

1. Inventory the available references. Give them short labels such as R1 and R2
   in the conversation, and retain their known source URLs or user descriptions.
   Describe only images that are actually visible or described. If neither is
   available, request the references rather than inferring imagery from filenames
   or URL paths.
2. Identify each reference's useful signal: palette, material, lighting,
   composition, typography, or mood. Connect that signal to the brief and note
   any required ingredients the collection does not cover.
3. Select a small set with distinct roles, usually a main reference and a few
   supporting details. Preserve must-keep references. Remove redundant or
   conflicting references with concrete reasons tied to the intended direction.
4. Explain the keep and omit decisions before organizing the board. Distinguish
   an aesthetic judgment from an unknown reference that needs inspection.
5. When a board is requested, use `image` items for individual references,
   `gallery` items for related references, and concise `note` items for their
   roles. Submit the full `moodBoard.items` through `display-mood-board`, with at
   most ten items and an optional `reason`. Follow the registered schema;
   conversation labels and captions are not additional image item fields.
6. Read the returned `structuredContent.moodBoard` when rendering succeeds.
   Summarize the chosen references and the remaining reference gaps. Suggest
   specific subjects for missing references rather than inventing image links.

## Source handling

- Supply reusable public HTTP(S) image URLs, not webpage links, file IDs, or
  invented hosted sources. Keep original source URLs; allow the widget to resolve
  delivery URLs through its app-only `resolve-mood-board-images` helper.
- If selected attachments have no reusable URLs, deliver the curation first.
  Guide the user to upload those images into image or gallery cards. If they
  requested a fresh canvas, `display-mood-board` can render an empty `items`
  array or concrete note items to support that manual upload workflow.
- When working from an existing board, prefer its latest model-visible contents
  over earlier tool output. New renderings receive fresh UUIDs and do not carry
  private upload mappings or saved positions; use widget edit guidance when
  those must be retained.
- Apply the ten-item tool limit to a rerendered board even if the user has added
  more items manually. Never silently discard retained ingredients to fit.

## Deliverable

Return the selected references with their roles and reasons, a brief account of
omitted references, and any missing subjects. Include a curated widget when
requested and sources permit, or exact upload and organization steps.

## Boundaries

Treat image search and generation as separate capabilities, used only when
available and relevant to an additional request. Do not claim Mood Board can
find images, inspect unseen URLs, measure palette colors, recover private file
mappings, or arrange cards programmatically. Respect requests for text only.
