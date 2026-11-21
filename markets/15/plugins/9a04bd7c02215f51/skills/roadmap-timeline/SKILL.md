---
name: roadmap-timeline
description: Draw a roadmap, timeline, release plan, project schedule, quarterly plan or history of events on an editable Igly canvas. Use when the user lists work over time, milestones, phases, sprints or dates.
---

# Roadmap and timeline

## 1. Plan
- Choose the time unit from the input: quarters, months, weeks, sprints or dated events.
- Group items into 2 to 5 lanes (teams, themes or workstreams) when there are more than 8 items.

## 2. Create
`create_canvas` with a `title` such as "2027 product roadmap". Keep `canvas_id`. To continue an existing Igly project instead, pass its link or id as `canvas_id` (`list_projects` finds it).

## 3. Layout (one `add_elements` call)
- Title text at (0, -140), `font_size: 48`, bold.
- Time columns: one header per period, `type: "shape"`, rectangle 300 x 70 at x = 200 + i * 320, y = -40, fill `#1E1E1E`, `text_color: "#FFFFFF"`, bold, `font_family: "Inter"`.
- Lane labels: `type: "text"` at x = 0, y = 60 + lane * 260, bold, `font_size: 26`.
- Items: `type: "sticky"`, 280 x 180, placed in their period column and lane, x = 210 + i * 320, y = 50 + lane * 260 (stack a second item in the same cell 200 lower and grow the lane).
- One sticky `color` per lane: `#BFDBFE`, `#FBCFE8`, `#BBF7D0`, `#FDE68A`, `#DDD6FE`.
- Milestones: `shape: "star"` 90 x 90 at the column edge, with a short `type: "text"` caption below.
- Optional "today" marker: `type: "line"` from (x, -60) to (x, bottom), `stroke: "#E03131"`, `stroke_width: 4`, `dashed: true`.
- Tentative or stretch items: `dashed: true` on the bar so they read as not committed.
- Dependencies between bars in different lanes: `type: "arrow"` with `from_id`/`to_id` and `curve` toward the side with space so it clears other bars.
- For a single-track timeline of events, use one horizontal `type: "arrow"` from (0, 0) to (end, 0), small `ellipse` dots on it and alternating sticky notes above and below.

## 4. Check
- `get_canvas_summary`, then `arrange` with `align_top` per row or `distribute_horizontal` per lane if spacing drifted.
- Offer edits: move an item to another quarter (`update_elements` with `dx: 320`), add a lane, export a PNG.

- Check your work: when you finish building or editing, call `export_png` once and look at the preview image it returns; fix overlapping or cut-off text before you answer. In a later reply that only edits the board, call `show_canvas` once first so the user sees it change.
