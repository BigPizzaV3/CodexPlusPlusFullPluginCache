---
name: whiteboard-layout
description: Arrange and tidy diagrams on Whiteboard by Lumin with readable spacing, alignment, groups, and connectors. Use for crowded boards, flowcharts, system diagrams, and visual organization; preserve the meaning and scope of existing content.
---

# Layout and organization

Follow [Whiteboard operations](../whiteboard/SKILL.md) before changing a file. Use [Visual storytelling](../whiteboard-storytelling/SKILL.md) if the message or diagram structure is still undecided.

## Arrange the content

Read the current elements and their bounds first. For an addition, find nearby empty space and preserve existing positions. For a requested cleanup, keep related IDs and relationships intact while moving the smallest useful group. Do not reorder steps merely for symmetry.

Pick one main reading direction. Align items that play the same role; use consistent dimensions for comparable nodes. Group related items with proximity first, then a section heading or subtle container when needed. Let whitespace separate groups. A container goes behind its contents in element order; group IDs help move a set together but do not replace connector or text bindings.

As a starting point at normal zoom, use 20–24 px labels, approximately 20 px internal padding, and 48–80 px between nodes. Adapt to content and the existing scale. Wrap labels at meaningful phrases and enlarge boxes before reducing text size. Handwritten text needs room, particularly inside diamonds. Avoid one enormous board with tiny text when a few clearly separated sections would read better.

## Connect the relationships

Route connectors through whitespace and attach them at the appropriate edges. Keep the main flow direct; send return loops and exceptions around the outside. Label decision exits with their conditions. Use arrowheads only when direction has meaning, and avoid lines crossing labels or unrelated shapes.

Excalidraw line/arrow `points` are offsets from that element's `x` and `y`, not absolute canvas positions. For new skeleton arrows, supported `start: {id: "source-id"}` and `end: {id: "target-id"}` bindings keep connections attached as nodes move. IDs must resolve to actual shapes. For existing native arrows, preserve and update their native bindings and the connected shapes' `boundElements`; do not replace native records with skeleton shortcuts. Moving a bound text container also requires moving its text. Keep existing valid bindings whenever possible.

## Inspect at two scales

At fit-to-content, check the starting point, grouping, balance, and stray elements that make everything look tiny. At normal reading zoom, check label wrapping, collisions, connectors, and margins. Use a supported editor or render preview if available; do not claim a visual inspection from JSON alone. Fit the view for presentation when useful, but preserve the user's zoom and pan during an ordinary incremental edit. Do not move content merely to compensate for the current viewport.
