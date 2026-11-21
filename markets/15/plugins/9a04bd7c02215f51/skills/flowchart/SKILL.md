---
name: flowchart
description: Draw a flowchart, process map, decision tree, user flow or system diagram on an editable Igly canvas. Use when the user asks to diagram steps, a process, a pipeline, an architecture or "how X works".
---

# Flowchart

Draw the whole chart in one `add_elements` call, then check and fix it.

## 1. Plan before drawing
- List the steps (6 to 14 is ideal; group extra detail into notes).
- Pick the direction: left to right for a pipeline of 5 or fewer steps per row, top to bottom for longer flows and decision trees.
- Mark decisions (yes/no questions), start and end.

## 2. Create the board
`create_canvas` with a short `title` (e.g. "Customer onboarding"). Keep the returned `canvas_id`. To continue an existing Igly project instead, pass its link or id as `canvas_id` (`list_projects` finds it).

## 3. Lay out on a grid
- Box: 240 x 110. Column step 320 (left to right) or row step 190 (top to bottom).
- Start/end: `shape: "ellipse"`. Steps: `"rectangle"`. Decisions: `"diamond"`, 220 x 140. Inputs/outputs: `"parallelogram"`.
- Branches of a decision go to the next column/row, offset by one lane (240 + 80).
- Title: `type: "text"`, `font_size: 48`, bold, 100 above the first box.
- Give every element a readable `id` (`start`, `check_email`, `approve`...).

## 4. Connect
- `type: "arrow"` with `from_id` / `to_id`. Arrows attach to the facing edges and follow boxes when they move.
- Label decision branches with the arrow `label` ("Yes" / "No").
- Loops and back-edges (retry, "go back to step 1"): connect with `from_id`/`to_id` and add `curve` ("down", "up", "left" or "right") toward the side with empty space, usually away from the title and other rows ("down" for a loop back under a row). It curves around the boxes instead of crossing them.
- Optional or future steps: `dashed: true` on the box and on its arrow.
- Never draw arrows by coordinates between boxes; always use ids.

## 5. Style
- Default hand-drawn font suits sketches. For a clean, presentation look set `font_family: "Inter"` on every element.
- Use at most 3 fills: steps `#DBEAFE`, decisions `#FEF3C7`, start/end `#DCFCE7`. Keep text dark (`#1E1E1E`).
- Optional sticky notes (`type: "sticky"`) beside a step for caveats.

## 6. Check and finish
- `get_canvas_summary` and look for overlaps; fix with `update_elements` (`dx`/`dy`) or `arrange` (`align_middle`, `distribute_horizontal`).
- Tell the user they can edit the board directly and open it in the full editor with the canvas `open_url`.
- If they want an image, call `export_png`.
- Check your work: when you finish building or editing, call `export_png` once and look at the preview image it returns; fix overlapping or cut-off text before you answer. In a later reply that only edits the board, call `show_canvas` once first so the user sees it change.

## Example (one call)
```json
{"canvas_id":"<id>","elements":[
 {"type":"text","id":"title","x":0,"y":-110,"text":"Customer onboarding","font_size":48,"bold":true},
 {"type":"shape","id":"start","shape":"ellipse","x":0,"y":0,"width":240,"height":110,"text":"Sign up","fill":"#DCFCE7"},
 {"type":"shape","id":"verify","x":320,"y":0,"width":240,"height":110,"text":"Verify email","fill":"#DBEAFE"},
 {"type":"shape","id":"ok","shape":"diamond","x":640,"y":-15,"width":220,"height":140,"text":"Verified?","fill":"#FEF3C7"},
 {"type":"shape","id":"done","shape":"ellipse","x":940,"y":0,"width":240,"height":110,"text":"Welcome tour","fill":"#DCFCE7"},
 {"type":"shape","id":"resend","x":640,"y":220,"width":240,"height":110,"text":"Resend link","fill":"#DBEAFE"},
 {"type":"arrow","id":"a1","from_id":"start","to_id":"verify"},
 {"type":"arrow","id":"a2","from_id":"verify","to_id":"ok"},
 {"type":"arrow","id":"a3","from_id":"ok","to_id":"done","label":"Yes"},
 {"type":"arrow","id":"a4","from_id":"ok","to_id":"resend","label":"No"},
 {"type":"arrow","id":"a5","from_id":"resend","to_id":"verify","curve":"down"}
]}
```
