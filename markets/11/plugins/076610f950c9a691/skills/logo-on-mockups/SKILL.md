---
name: logo-on-mockups
description: Place the user's original attached logo or design on one or several real editable product mockups. Use for "put this logo on a shirt", "create a T-shirt mockup with my logo", or branding apparel, packaging and products, even without naming Artboard. Supports comparisons when requested; use the editor rather than generating a replacement image.
---

# Logo on mockups

For one product, create or use one editable Artboard project and place the original
artwork on its print surface. Do not ask the user to request Artboard explicitly
when its tools are already available. Do not generate an image as a substitute.
Use the comparison workflow below only when the user requests several products
or variants; a single T-shirt request does not authorize three or four projects.

1. **Choose.** Search with `search_mockups` and show the options visually with
   `open_artboard` (`view: "mockups"` and the same search). Agree on which ones and how
   many: each mockup becomes a project in the user's account. Create only the
   requested number of projects.
2. **Upload once, reuse after.** For the first mockup, place the attached file with
   `set_project_image` (`image`). Then call `list_my_files` and use its `file_id` for every
   other mockup. Reused files never count as uploads.
3. **For each mockup**, in turn:
   1. `open_mockup`.
   2. `get_open_project`, to find the artwork surface (`mockup-1/surface-N`).
   3. `set_project_image` on that surface with the `file_id`.
   4. Apply the same color, background and aspect ratio choices to every mockup, so the
      comparison is fair.
   5. `export_project` (`png`).

   Finish each mockup before opening the next one: edits go to the most recently opened
   view.
4. **Present** the download links with the mockup names, and say which one you would
   pick and why.

## Artwork is an editor operation
"Put this logo on the shirt" means use the actual selected Artboard project and `set_project_image`, not image generation. Resolve the print area from live project context; distinguish artwork targets from product-color surfaces. Adjust logo size/rotation/position using `style_project_surface` and the current transform, preserving aspect. Recolor the product separately. To add another product to the same composition use `add_mockup_to_project` and arrange it through `update_canvas_layer`; avoid creating unnecessary projects. User-facing replies should describe results, not tool names.


Native edits now return real rendered visual feedback. Inspect it before claiming
success; `inspect_project` captures a read-only frame without an export allowance.
Use a new `begin_project_edit` group for a multi-tool user request, and pass its
`history_group` so one undo restores that request. All three editors support
recorded native undo/redo across reopening. Exports have a persistent Download control for the original rendered file. Existing artwork placement remains a real editor
operation; native AI generation is for explicitly requested creative assets only.
