---
name: compose-stashiro-board
description: Use when Stashiro is selected or mentioned to present, plan, analyze, compare, create, save, add, edit, move, connect, or organize visual board content.
---

# Compose a Stashiro board

Stashiro organizes content as Space > Board > Card. A canvas board supports freely positioned visual cards; a list board supports a linear bento-style collection.

1. Choose the mode from the request. When Stashiro is selected for a plan, analysis, comparison, research synthesis, or another multi-item answer, the answer is the native card presentation; do any needed research first, then present it without saving instead of returning the deliverable only as prose. For an explicit create or save request, prepare the same reviewable composition and let the user confirm its destination in the Stashiro UI. Use direct write tools only for a small targeted change to an existing board.
2. Choose one primary organizing axis: time, topic, entity, workflow stage, audience, location, or another relation the user will navigate. Make one named `section` for each useful unit. A table may compare units, but does not replace sections people need separately.
3. Make each note about one subject. Keep an ordinary note under 60 words. Split independent resources, facts, decisions, or actions. A resource note describes one resource and sits with its link. Use a short overview only for synthesis that applies to the whole result.
4. Build one section at a time in reading order. Put its note, source link, native card, and action together before starting the next section. Never batch cards by type or move all links to the end. Use every card index in exactly one section.
5. For a new multi-card answer or composition, call `present_stashiro_cards` once with the final ordered cards and sections. This is the final native Stashiro answer after any research, not an intermediate reasoning step or an optional duplicate of a prose answer. It does not save until the user confirms the destination in its UI.
6. For a small direct edit or addition, use `create_card` for short headings and notes. Use `create_link_card`, `create_table_card`, `create_chart_card`, `create_flight_card`, `create_map_card`, `upload_image_card`, and `create_connector` for their native content. Prefer a table for comparable records and a chart when the visual pattern matters more than exact lookup.
7. A flight-tracking URL requires a flight card with the original URL in `sourceUrl`. Use sourced offset timestamps and live status only when provided. Never infer flight status.
8. Use an image card only for a user-requested attached or generated image. Ask which image when several candidates match. Never pass a local path or add decorative media without a request.
9. Use a connector only when direction, sequence, dependency, or another relation should remain visible after cards move. Use `arrow` for direction, `plain` for a neutral relation, and `dashed` for a tentative or indirect relation.
10. For direct canvas writes, use `layout-stashiro-board` before supplying geometry and verify the result afterward. `present_stashiro_cards` and `save_capture` preserve section grouping without model-supplied coordinates.
11. Resolve a destination only for persistent work. Use `search` for a named destination and accept a unique match only when its subject fits. Never treat the only match as relevant by default. Ask for an existing Space or permission before `create_space`. Use `create_board` with the exact Space reference. Default to `canvas`; use `list` only for a linear collection.
12. Use `update_card`, `move_card_to_board`, `reorder_cards`, or `delete_card` only for the requested direct change. Before moving a connected card, inspect its connectors and preserve only relationships that still make sense.
13. Use `show_selected_stashiro_cards` for existing identified cards that have not appeared in the current response and `show_stashiro_board` for an unfiltered board page. Return exact board links after writes.
