---
name: layout-stashiro-board
description: Use whenever a Stashiro canvas operation must choose, verify, or change card coordinates, dimensions, spacing, alignment, or layers; when adding or editing near existing content; when repeated additions may overlap; or when asked to arrange, distribute, tidy, or stop cards from hiding each other.
---

# Layout a Stashiro board

Use this skill for direct canvas geometry. Content skills decide what to create or change; this skill decides where it fits and verifies the result. A reviewed multi-card composition saved through `save_capture` already uses its semantic sections for collision-free placement. List boards use distribution order instead.

1. Before supplying or changing `x`, `y`, `width`, or `height`, call `list_cards` on the destination board and follow `cursor` until `isDone` is true. Use every non-connector card's returned geometry as an occupied rectangle.
2. Identify the content groups and their reading order before choosing coordinates. Preserve an established grouping when editing. Give every time period, topic, entity, stage, or other independently useful unit its own bounding area; do not substitute a card-type row for those groups.
3. Lay out one complete group before the next. Mix card types inside it: put each source link beside or below the note, comparison, map, or action it supports. Keep alternatives with their comparison. Never create a board-wide link row, note row, image row, or table row unless card type is itself the subject.
4. Keep 40 to 64 pixels between cards in one group and at least 112 pixels between groups. Use a short text heading when a group boundary would otherwise be unclear. Preserve user-supplied coordinates unless they hide another card or break an explicit group.
5. When dimensions are absent, estimate a conservative footprint: text 240 x 48, note 220 x 220, link 400 x 280, image 320 x 240, table 440 x 240, chart 440 x 300, and flight 460 x 280. Size cards for readable content and consistent peers. Do not shrink a card to force it into a gap.
6. Never reuse a generic origin or board-center position without checking collisions. Continue an existing group for repeated additions. Place a new group beside or below occupied board bounds without moving unrelated cards.
7. After each group and again after the full write, call `list_cards` through completion. Fail the layout when cards overlap substantially, one card hides another, a group mixes unrelated subjects, or a supporting card is visually closer to unrelated content than to its subject. Also fail when cards were arranged by type instead of by meaning.
8. Fix a failed layout by moving or resizing new and modified cards first. Preserve unrelated positions and `stackIndex` values. Use `reorder_cards` only when layer order is part of the requested arrangement. Recheck until cards are readable and the spatial grouping matches the content structure.
