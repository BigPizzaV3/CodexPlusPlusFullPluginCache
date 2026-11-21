---
name: draftt-moodboard
description: "Turn a creative brief into a curated visual direction and an editable Draftt moodboard using Explore references or the user's saved images. Use for film, commercial, music video, cinematography and art direction moodboards, including revisions to an existing board."
---

# Build a visual direction in Draftt

Use the connected Draftt MCP tools. Discover their current schemas rather than relying on a particular tool namespace. A request for reference research alone does not authorize creating a board.

## Translate the brief into choices

Identify the central feeling or story and the visual decisions it needs: for example, hard afternoon light against soft interiors, intimate framing against monumental locations, or controlled color against natural texture. Use the user's language and existing references. Ask only about a missing choice that would materially change the direction; otherwise make a small, stated assumption and proceed.

Turn abstract adjectives into visible search ideas. For "premium but human," look for tangible materials, lived-in spaces, restrained color and natural gestures, rather than searching only for "premium." Keep subject, lighting and art direction as separate search ideas when combining them would overconstrain results.

## Curate references with a purpose

- Use `search_catalog` for Explore's credited commercial, music video and film frames. Use `search_library` when the brief calls for the person's saves, uploads or existing visual vocabulary. Respect a restriction to either source.
- Start with a small set of distinct searches. Use `temperature`, `key` or a HEX query only when the brief supports that choice. Explore searches consume plan quota, so refine a promising result with `similar_to` instead of repeatedly paraphrasing the same query. Catalog similarity requires a catalog frame URL.
- Choose images for a specific transferable decision: lighting, lens impression, blocking, color, production design or composition. Describe a lens impression as interpretation unless verified technical information is available.
- Prefer complementary setups and works over many near-identical frames. A small coherent selection is stronger than filling a target count. Honor a requested count, and explain any shortfall.
- Inspect the returned images when available. Separate what is visibly present from a creative proposal. If you cannot view a result, do not claim to have visually checked it.
- Keep each selected image's returned `url`, work title, available director/DP credits and source link together. Do not invent missing credits. A saved upload may have no source. Preserve the catalog URL when placing a frame so Draftt retains its catalog association.

The selection should explain a direction, not just illustrate a topic. For each chosen reference, write a short "take this" note tied to the brief, such as "Keep the amber practicals and blue window contrast; use a quieter background for the product." Do not imply that a reference is licensed for reuse in the finished film.

## Compose the requested board

For a new board, use `create_board` with `layout: "moodboard"` when images lead. Cards can pair an image with a short source and direction note; loose images suit a more visual wall. Group by meaningful choices from this brief, not a fixed list of headings. Keep longer thinking out of image captions.

Omit `workspace_id` and `folder_id` to create in the person's own space. If they name a team, project folder or existing board, resolve the destination with `list_workspaces`, `list_folders` or `list_boards`; ask when the intended shared destination remains unclear. A team destination is visible to its members.

For an existing board, read `get_board` and `get_board_snapshot` first. Respect the selected content and the composition already there. Add or adjust only what the requested revision needs with `edit_board`; do not replace the whole board to add a few references. Use the tool's current block and operation schemas, not invented fields for credits or sections.

Inspect the completed board with `get_board_snapshot`. Use selected `node_ids` if the overview makes captions too small to judge. Correct overlaps, weak grouping or unreadable notes using the IDs from `get_board`, then inspect the affected area again. Stop after a small number of targeted corrections; explain a rendering failure rather than claiming a visual check passed.

When a write fails after some operations applied, inspect the result and current board before retrying. Retry only unapplied work; do not duplicate the board or replay a whole partial batch. Stop on permission or quota errors and explain the actionable limit.

Return the actual board link, a short statement of the visual direction and any unresolved choice. Create a separate brief document or a presentation only when requested. Generated images are a distinct workflow: use them only when requested and available, label them, and keep them distinct from real reference frames.
