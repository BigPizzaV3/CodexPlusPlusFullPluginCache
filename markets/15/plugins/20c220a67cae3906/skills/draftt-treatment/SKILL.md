---
name: draftt-treatment
description: "Create or refine a visual treatment or creative pitch in Draftt from a brief, reference board or selected images. Use for director treatments, commercial and music video pitches, and visual storytelling decks."
---

# Make a visual treatment in Draftt

Use the connected Draftt MCP tools and their current schemas. Create a new presentation only when requested; use `get_deck` and `edit_deck` for revisions. If the user only wants an outline or critique, deliver that without making a deck.

## Find the film's through-line

Read the supplied brief and any named Draftt board with `get_board`; inspect its imagery with `get_board_snapshot` when needed. For a document tile, use `get_doc` to read its contents rather than guessing from its title. For an existing treatment, read `get_deck` and inspect the relevant slides before proposing changes.

Distill one specific creative promise that connects the product or artist, the audience and the visual approach. Let that promise determine the sequence. Preserve the user's concept and selected references; do not silently substitute a different campaign because a search returned more images for it.

A treatment should make the film imaginable. Depending on the brief, useful sections may cover the opening hook, story beats, performance, camera behavior, light and color, art direction, edit rhythm, sound and the closing image. Include only what contributes to this project. Do not pad a three-slide request into a long template or reduce a detailed requested sequence to generic mood words.

Distinguish confirmed brief requirements from proposed creative decisions. Avoid inventing production commitments, locations, casting, budget, schedule, factual claims or endorsements. Keep an unresolved decision explicit instead of presenting it as approved.

## Make references carry the argument

Use the supplied board's selections first. When more images are needed, search `search_catalog` for credited Explore frames or `search_library` for the user's images, according to the requested source. Search for the missing visual decision rather than starting research again from scratch.

Match every reference to its role in the treatment: a frame may demonstrate camera distance, a color relationship, a performance register or a transition idea. Explain that role in concrete terms. Do not claim a still demonstrates an unseen camera move or editing rhythm; describe those as the proposed execution.

Place returned image URLs in the layout's `image_url` slots. Keep available work titles, director/DP credits and source links in the deck's content, using supported text or caption fields. Use an additional sources slide when the requested length allows it; otherwise integrate concise credits into the existing structure. Do not fabricate credits or treat user uploads without provenance as published film frames.

Generated images are optional and consume credits. Use available generation tools only when the user asks for generation, and distinguish the resulting concept images from reference frames. Never replace a failed reference search with generation silently.

## Build the narrative as slides

For a new deck, use `create_deck` with layout slides and their `slots`. Draftt presentations are 16:9. For an existing deck, use the actual slide IDs from `get_deck`, preserve unrelated material and work within the requested scope.

Write the slide's claim first, then choose a layout that makes it legible. `image_full` suits a visual statement with a concise `caption`; `image_text` pairs a reference with a concrete execution decision; `columns` suits parallel choices. Use `compose` when a diagram or deliberate grouping needs more structure. Use the current tool schema for slots and limits; do not force invented layout names into a payload.

Carry one palette and typography system through the deck, reflecting the brief or source board. Use fonts supported by the tool. Keep text readable against the imagery and prefer a strong reference with short copy over an essay beside a thumbnail. Preserve the specified slide count unless the user permits changing it.

For a new deck without a named destination, omit `workspace_id` and `folder_id` to use the person's own space. Resolve a named team or folder with the corresponding tools; clarify an ambiguous shared destination before creating there.

## Review what the audience will see

Read the write response, including per-slide warnings and partial failures. Fix accidental overflow, overlap and low contrast with `edit_deck`. Shorten or restructure copy before shrinking type. Respect deliberate visual choices the user requested and identify any remaining tradeoff.

Call `get_deck_snapshot` on every created or changed slide. The tool renders up to eight slides per call and uses zero-based indexes; inspect longer decks in explicit batches so the final slides are not skipped. Check cropping, text wraps, contrast, hierarchy and consistency between consecutive slides. Make targeted corrections and render those slides again. If rendering fails or a problem remains after a small number of corrections, report the limit accurately.

After a partial write or uncertain timeout, read the current deck before retrying. Retry only missing operations and avoid duplicate decks or slides. Stop on permission or quota errors rather than moving to another workspace to evade the restriction.

Return the actual deck link and a brief account of the creative through-line. Mention unresolved creative decisions or unverified rendering. Do not claim a treatment was exported, published or shared unless that action was requested and its result was verified.
