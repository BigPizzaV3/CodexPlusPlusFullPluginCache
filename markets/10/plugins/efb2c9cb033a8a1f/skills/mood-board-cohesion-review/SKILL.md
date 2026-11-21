---
name: mood-board-cohesion-review
description: "Review and refine the contents of an existing Mood Board when the user asks why it feels scattered, wants a more coherent direction, or needs prioritized changes while preserving specified anchors. Use the current model-visible board and visible references. Do not use for creating unrelated concepts, spatial layout critique without a visible board image, or a designer handoff brief."
---

# Mood Board Cohesion Review

## Inputs

Use the latest board contents, the intended mood or audience, and any ingredients
the user wants to retain. Use attached images only when they are actually visible.

## Workflow

1. Read the latest model-visible `modelContent.moodBoard`. Use
   `structuredContent.moodBoard` from the latest tool result only when newer user
   edits are unavailable. If no board contents are visible, request them; do not
   claim to retrieve them through a tool.
2. State the intended direction in one sentence and identify fixed anchors such
   as exact colors, font families, references, or wording. Infer a tentative
   direction from the conversation when reasonable and label that inference.
   Ask a focused question only when a missing aim would change the review.
3. Assess palette hierarchy, typography tone, reference consistency, repetition,
   and whether notes or quotes reinforce the direction. Describe only imagery
   you can see or that the user has described. Separate observed ingredients
   from judgments about their effect.
4. Select up to three changes with the greatest benefit. Identify each target
   by its content or family name, explain the conflict, and give a concrete
   replacement, removal, or adjustment. Keep the user's anchors intact.
5. Render a revision when the user requests refinement. For a critique-only
   request, return the review without rendering. Follow the rendering rules
   below; provide precise widget edit instructions when a new rendering cannot
   preserve what the user needs.
6. After rendering, use the returned `structuredContent.moodBoard` as the new
   baseline and summarize the changes against the intended direction.

## Rendering rules

- Call `display-mood-board` with the complete `moodBoard.items`, at most ten
  items, and an optional `reason`. Follow the registered item schema and omit
  output IDs and response metadata from the input.
- Carry every retained ingredient into the complete payload. Never silently
  truncate a board that the user expanded beyond ten items in the widget;
  provide widget edit instructions or ask which subset to render.
- Treat the result as a new rendering with fresh item UUIDs. Do not promise to
  patch the existing widget, retain dragged positions, or preserve private
  upload and export bookkeeping.
- Use reusable source image URLs. If an uploaded image has no reusable source,
  guide edits within the existing widget instead of inventing a URL or assuming
  a file ID can be passed as an image URL. Do the same when the user requires
  the existing layout or uploaded-file associations to remain intact.
- Leave remote image delivery to the widget. Never call the app-only
  `resolve-mood-board-images` helper or substitute its signed delivery URLs for
  source URLs.

## Deliverable

Return the direction and retained anchors, followed by up to three prioritized
changes with their reasons. Include the revised board when requested and
representable, or concrete instructions for editing the current widget.

## Boundaries

Review semantic contents rather than hidden card geometry. Do not assume access
to `privateContent` or treat image IDs and URL names as visual evidence. Keep
layout changes, uploads, display modes, and export as widget actions. Respect
requests for text only or no tools.
