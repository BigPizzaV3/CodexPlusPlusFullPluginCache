---
name: wireframe
description: Sketch a low-fidelity wireframe or mockup of a web page, landing page, dashboard, form or mobile app screen on an editable Igly canvas. Use when the user wants to plan a layout, page structure or UI before designing it.
---

# Wireframe

Low fidelity: grey boxes, real labels, no images. Use the clean font so it reads like a UI.

## 1. Pick the frame
- Desktop page: frame 1440 wide. Mobile screen: 390 x 844. Dashboard: 1440 x 900.
- List the sections top to bottom (nav, hero, features, pricing, FAQ, footer...) or the screen regions (sidebar, header, cards, table).

## 2. Create
`create_canvas` with `title` (e.g. "Pricing page wireframe") and, for a single screen, `width`/`height` of the frame. Keep `canvas_id`. To continue an existing Igly project instead, pass its link or id as `canvas_id` (`list_projects` finds it).

## 3. Elements (one `add_elements` call; set `font_family: "Inter"` on everything)
- Frame: rectangle at (0, 0), frame size, `fill: "#FFFFFF"`, `stroke: "#1E1E1E"`, `stroke_width: 2`, `corner_radius: 0` (mobile: 40).
- Blocks: rectangles `fill: "#F1F3F5"`, `stroke: "#ADB5BD"`, `corner_radius: 8`, with the section name as `text`, `text_color: "#495057"`.
- Image placeholders: rectangle `fill: "#E9ECEF"` plus two `type: "line"` diagonals (corner to corner, `stroke: "#ADB5BD"`).
- Headings and copy: `type: "text"`, `color: "#1E1E1E"`, headline `font_size: 44` bold, body 18 with a `width` to wrap.
- Buttons: rectangle 180 x 52, `corner_radius: 26`, `fill: "#1E1E1E"`, `text_color: "#FFFFFF"`. Secondary: white fill, dark stroke.
- Inputs: rectangle 360 x 48, white, `stroke: "#ADB5BD"`, placeholder `text` left-aligned (`align: "left"`).
- Spacing: 24 inner padding, 80 between sections on desktop, 16 / 32 on mobile.
- Annotate decisions with `type: "sticky"` notes outside the frame, connected by `type: "arrow"` with `to_id` the block they explain.

## 4. Check
- `get_canvas_summary`; align columns with `arrange` (`align_left`, `distribute_vertical` with `gap`).
- Offer a second variant beside the first (x + frame width + 200) for comparison, or `export_png`.

- Check your work: when you finish building or editing, call `export_png` once and look at the preview image it returns; fix overlapping or cut-off text before you answer. In a later reply that only edits the board, call `show_canvas` once first so the user sees it change.
