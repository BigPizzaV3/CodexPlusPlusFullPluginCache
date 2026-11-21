---
name: mind-map
description: Draw a mind map, brainstorm, topic cluster or idea map on an editable Igly canvas. Use when the user wants to brainstorm, explore a topic, break an idea into branches or organise notes around a central theme.
---

# Mind map

## 1. Plan
- One central topic, 4 to 6 main branches, 2 to 4 leaves per branch. Keep labels to 1 to 5 words.

## 2. Create
`create_canvas` with the topic as `title`. Keep `canvas_id`. To continue an existing Igly project instead, pass its link or id as `canvas_id` (`list_projects` finds it).

## 3. Radial layout (one `add_elements` call)
- Center: `shape: "ellipse"`, 320 x 160 at (0, 0), bold, `font_size: 28`.
- Branch i of n: angle = i * 360 / n (start at -90 so the first branch is on top). Place a 220 x 90 rounded rectangle (`corner_radius: 24`) at distance 420 from the center:
  x = 160 + 420 * cos(angle) - 110, y = 80 + 420 * sin(angle) - 45.
- Leaves of a branch: `type: "sticky"`, 170 x 120, placed 320 beyond their branch along the same angle, fanned 35 degrees apart around it (for 3 leaves: -35, 0, +35). Leaves of neighbouring branches must not touch; with 6 branches keep 3 leaves or fewer each, or increase the branch distance to 500.
- Give each branch its own `fill`, and its leaves the matching sticky `color` (branch / leaf):
  `#DBEAFE` / `#BFDBFE`, `#FCE7F3` / `#FBCFE8`, `#DCFCE7` / `#BBF7D0`, `#FEF3C7` / `#FDE68A`, `#EDE9FE` / `#DDD6FE`, `#FFE4E6` / `#FECDD3`.
- Connect center to branch and branch to leaf with `type: "line"` and `from_id`/`to_id` (lines read calmer than arrows here). A light `bend` (30 to 60) gives organic, hand-drawn branches.
- Cross-links between ideas on different branches: a `dashed: true` line with `curve` toward the outside of the map so it arcs around it.

## 4. Check
- `get_canvas_summary`; move overlapping leaves outward with `update_elements` (`dx`, `dy`).
- Offer to add more leaves to one branch, regroup branches, or export a PNG (`export_png`).
- Mention the board is editable in the chat and opens in the full editor via `open_url`.

- Check your work: when you finish building or editing, call `export_png` once and look at the preview image it returns; fix overlapping or cut-off text before you answer. In a later reply that only edits the board, call `show_canvas` once first so the user sees it change.
