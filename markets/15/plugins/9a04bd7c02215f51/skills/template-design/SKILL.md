---
name: template-design
description: Make a poster, social media post, flyer, menu, invitation, quote card, infographic or thumbnail by starting from one of Igly's editable design templates and rewriting its text. Use when the user wants a designed graphic rather than a diagram.
---

# Template design

Igly has 2,400+ free, designed, editable templates. Start from one instead of drawing a layout from scratch.

## 1. Find templates
- If the user only wants to look around, or has not said what to make, call `browse_igly`: it opens templates and animations in one picker with categories.
- `list_templates` with a `query` from the request ("bakery menu", "summer sale", "wedding invitation", "quote") and/or a `category` (Posters, Social posts, Business, Food, Travel, Infographics, Video thumbnails...). Use `limit` 8 to 12.
- Match the size to the use: 1080 x 1080 or 1080 x 1350 for feed posts, 1080 x 1920 for stories, 1587 x 2245 for print posters.
- `list_templates` also opens a picker with thumbnails in the board view. If the user wants to browse, let them pick there; their pick creates the board (or adds to the current one) and you are told its `canvas_id` and template.
- Otherwise offer 2 or 3 options in one short line each, or pick the best fit if the user asked you to choose.

## 2. Create from the template
- New board: `create_canvas` with `template_id` and a `title`. Keep `canvas_id`. To continue an existing Igly project instead, pass its link or id as `canvas_id` (`list_projects` finds it).
- Board already open: `apply_template` with `canvas_id` and `template_id`. The template lands to the right of the existing content as a new page, so nothing is covered.
- `create_canvas` and `apply_template` show the user one live board that follows every later edit. In a later reply that only edits the project, call `show_canvas` once before the first edit.

## 3. Rewrite the copy
- `get_canvas_summary` to see the template's text elements, their ids and fonts. The list shortens long text: before rewriting a paragraph, call it again with `element_ids` for the full text and every style. It lists 150 elements per call; when `has_more`, call it again with `next_offset`.
- `update_elements` with new `text` for each, in one call. Keep each text about as long as the original so the layout holds; shorten headlines rather than shrinking fonts. Text boxes refit their text.
- Restyle in place with the same ids: `font_family` (any family `search_fonts` lists), `font_weight` or `bold`, `align`, `letter_spacing`, `line_height`, `uppercase`, `color` on text and `fill` on shapes, `corner_radius`, `opacity` on photos.
- If the result lists fields under "Ignored", those did not change: tell the user rather than claiming them.
- Remove parts that don't apply with `remove_elements`; add missing details (date, address, price) as `type: "text"` matching the nearby font and color.
- Need another price tag, card or row like one already there? `duplicate_elements` copies it (with its group and the arrows between copied pieces), then retext the copy.
- Swap a template photo for the user's own: `update_elements` on the photo's id with `image_url` (a public PNG, JPEG or WebP link), or, for a photo the user attached in the chat, pass the file in `attached_images` and set `attached_image: 0` (its position) on the update. Never pass a local path like `/mnt/data/...` as `image_url`. The photo keeps its box; if the result says it was stretched, set the given height or ask which crop they want. Add a new picture with `add_elements` `type: "image"` the same two ways.
- No photo from the user and the design needs one (a product shot, a scene)? `generate_image` with a specific prompt and `replace_id` set to the template photo's id (or `x`/`y`/`width` for a new picture), instead of linking a picture from the web. If it says the image is still being generated, call `get_image_job` with the same placement. `remove_background` cuts out an image element's subject so it sits on the design. Both spend the user's Igly credits: tell them what each step cost.
- Rename the project or change the page size with `update_canvas`. Resizing moves nothing; move elements that the result says now reach past the page.

## 4. Check and deliver
- When the edits are done, call `export_png` once and look at the preview image it returns (and its layout check). Fix what your edits broke, such as overlapping or cut-off text, with `update_elements` (`dx`, `dy`) or `arrange`, then export again. Point out anything else that looks wrong and offer to fix it.
- Tell the user in a sentence what the design looks like, with the PNG link from `export_png`.
- Users can open the layers panel to ungroup a template and edit one piece by hand; read the board again before your next change.
- If your app cannot pass the attached file (the tool says so), ask the user to add it with Add image in the board view or in the full editor through `open_url`, or to share a public link.
