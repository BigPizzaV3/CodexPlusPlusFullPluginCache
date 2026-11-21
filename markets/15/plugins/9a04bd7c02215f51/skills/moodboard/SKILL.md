---
name: moodboard
description: Build a moodboard, style direction, brand board, color palette, type pairing or layout grid on an editable Igly canvas. Use when the user explores a look and feel, brand direction, visual theme, campaign concept or design system basics.
---

# Moodboard and style board

## 1. Define the direction
From the brief, decide: 3 to 5 keywords (e.g. "calm, earthy, premium"), a 5-color palette with hex codes, a heading/body font pairing, and 3 to 6 content ideas. Explain choices in a sentence each.

## 2. Create
`create_canvas` with the direction name as `title`. Keep `canvas_id`. To continue an existing Igly project instead, pass its link or id as `canvas_id` (`list_projects` finds it).

## 3. Layout (one `add_elements` call)
- Title at (0, -160): `type: "text"`, `font_size: 64`, bold, in the heading font.
- Keywords row at y = -60: `type: "shape"` rectangles with `corner_radius: 40`, 200 x 60, fill from the palette, keyword as `text`.
- Palette at y = 40: five squares 180 x 180 (`corner_radius: 16`), x = i * 200, `fill` = the color, and a `type: "text"` caption below with the hex code and role ("Primary #2F3E46").
- Type specimen at y = 300: heading sample (`font_size: 72`, `font_family` = heading font) and body sample (`font_size: 20`, `width: 560`).
- Concept tiles to the right (x >= 1100): sticky notes or rounded rectangles 300 x 220 describing imagery, textures and references in words.
- Layout grid (if asked): a frame rectangle and thin `type: "line"` column guides (`stroke: "#ADB5BD"`, `stroke_width: 1`).
- `font_family` takes any family from Igly's font list, the same list as the Igly editor (e.g. "Playfair Display", "DM Sans", "Space Grotesk", "Fraunces", "Caveat"; the hand-drawn default is "Kalam"). `search_fonts` finds them; an unknown name fails with close matches. Pair one display face with one plain sans.

## 4. Variants and finish
- For 2 or 3 directions, repeat the block side by side (x offset 1800) with its own title so the user can compare.
- `get_canvas_summary` to check, `arrange` to tidy, `export_png` to share.
- Real photos or brand assets: `add_elements` `type: "image"` with `image_url` (a public PNG, JPEG or WebP link), or, for images the user attached in the chat, the files in `attached_images` and `attached_image: <position>` on each image element; give a `width` and the height keeps the picture's shape. If your app cannot pass attachments, the user adds them with Add image in the board view or in the full editor through `open_url`. For a photo or illustration nobody supplied, `generate_image` makes one with Igly's image model and places it (it spends the user's Igly credits; say what it cost).
- `duplicate_elements` repeats a tile or a palette swatch; `update_canvas` renames the board.

- Check your work: when you finish building or editing, call `export_png` once and look at the preview image it returns; fix overlapping or cut-off text before you answer. In a later reply that only edits the board, call `show_canvas` once first so the user sees it change.
