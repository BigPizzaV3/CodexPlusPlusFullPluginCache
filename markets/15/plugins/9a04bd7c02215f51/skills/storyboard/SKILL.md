---
name: storyboard
description: Lay out a storyboard or shot list for a video, ad, reel, explainer, presentation or comic as frames with scene notes on an editable Igly canvas. Use when the user plans scenes, shots, beats or slides in sequence.
---

# Storyboard

Frames are sketch boxes with scene descriptions, not finished pictures. Draw simple stick-figure style hints with paths only if the user asks for sketches.

## 1. Plan the beats
- 4 to 12 scenes. For each: number, what we see, dialogue or voiceover, duration, camera or transition.
- Choose the frame ratio from the format: 9:16 vertical (reels, TikTok, shorts) 270 x 480; 16:9 (YouTube, slides) 480 x 270; 1:1 (feed) 360 x 360.

## 2. Create
`create_canvas` with the project as `title`. Keep `canvas_id`. To continue an existing Igly project instead, pass its link or id as `canvas_id` (`list_projects` finds it).

## 3. Layout (one `add_elements` call)
- Grid of 4 per row (3 for 16:9). Column step = frame width + 60; row step = frame height + 260.
- Frame: rectangle at (x, y), `fill: "#FFFFFF"`, `stroke: "#1E1E1E"`, `stroke_width: 3`, `corner_radius: 12`, `text` = a short visual description centered in the frame (`font_size: 20`).
- Scene number: `type: "text"` above the frame, bold, `font_size: 26` ("1  Hook  0-3s").
- Notes under the frame: `type: "sticky"`, frame width x 180, `color: "#FEF3C7"`, with voiceover/dialogue and camera direction.
- Flow: `type: "arrow"` from each frame to the next frame in the same row, with `from_id`/`to_id`; label transitions ("cut", "zoom", "swipe") with `label`. Do not draw an arrow from the last frame of a row to the first of the next row (it cuts across the board); the scene numbers already carry the order.
- Optional quick sketch inside a frame: one or two `type: "path"` strokes (e.g. a horizon line, a circle head) with `stroke: "#1E1E1E"`.

## 4. Check
- `get_canvas_summary`; fix spacing with `arrange` (`align_top`, `distribute_horizontal` with `gap: 60`).
- Offer to reorder scenes (swap positions with `update_elements`), tighten copy to the target length, or `export_png` for sharing.

- Check your work: when you finish building or editing, call `export_png` once and look at the preview image it returns; fix overlapping or cut-off text before you answer. In a later reply that only edits the board, call `show_canvas` once first so the user sees it change.
