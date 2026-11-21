---
name: kanban-retro
description: Build a kanban board, retrospective wall, affinity map, SWOT, pros and cons or any sticky-note board on an editable Igly canvas. Use when the user wants items sorted into columns or categories, or a team board to move notes around.
---

# Kanban, retro and sticky-note boards

## 1. Pick the frame
- Kanban: To do / Doing / Done (add Blocked or Review if asked).
- Retro: Went well / To improve / Actions (or Start / Stop / Continue, or Mad / Sad / Glad).
- SWOT: 2 x 2 grid (Strengths, Weaknesses, Opportunities, Threats).
- Affinity map: cluster the user's notes into 3 to 6 themes you name.

## 2. Create
`create_canvas` with a `title` (e.g. "Sprint 14 retro"). Keep `canvas_id`. To continue an existing Igly project instead, pass its link or id as `canvas_id` (`list_projects` finds it).

## 3. Layout (one `add_elements` call)
- Title: `type: "text"` at (0, -150), `font_size: 48`, bold.
- Column i: a background lane `type: "shape"`, rectangle 360 wide, tall enough for its notes (90 + rows * 200), at x = i * 400, y = 0, `fill: "#F4F4F5"`, `stroke: null`, `corner_radius: 24`, with `name` set to the column title.
- Column header: `type: "text"` at x = i * 400 + 24, y = 20, bold, `font_size: 30`.
- Notes: `type: "sticky"`, 312 x 170, x = i * 400 + 24, y = 90 + row * 200. One sticky `color` per column, e.g. `#FDE68A`, `#BFDBFE`, `#BBF7D0`, `#FBCFE8`.
- For a 2 x 2 grid use two rows of lanes (y = 0 and y = rows * 200 + 140).
- Put the user's exact wording on notes; keep each to about 12 words.

## 4. After drawing
- Moving a note between columns: `update_elements` with `dx: 400` (or `-400`) and a new sticky `fill` if columns are colored.
- Re-pack a column: `arrange` with `distribute_vertical` and `gap: 30`.
- Summaries: read the board with `get_canvas_summary` before summarising or proposing actions.
- The board is editable in the chat; the user can drag notes too. Offer `export_png` or the `open_url`.

- Check your work: when you finish building or editing, call `export_png` once and look at the preview image it returns; fix overlapping or cut-off text before you answer. In a later reply that only edits the board, call `show_canvas` once first so the user sees it change.
