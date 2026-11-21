---
name: motion-showcase
description: Turn the user's images into an animated showcase (carousel, stack, orbit, marquee or bento) with Artboard and export an MP4. Use for portfolio reels, product galleries and social video.
---

# Animated showcase

1. **Find.** Use `search_templates` with `kind: "animation"`, and show options with
   `open_artboard` (`view: "animations"`). Open the pick with `open_template`. To swap
   styles later, use `change_template`; it keeps the images.
2. **Images.** Each `set_project_image` without a target adds a card, in order. Use
   `card-N` to replace a card, and `clear_project_image` with `card-N` to remove one.
   Reuse earlier uploads with `file_id` from `list_my_files`.
3. **Motion.** Call `get_open_project` to see this template's settings, then change several
   at once with `update_project_settings`. Common ones are `direction`, `style` (snap or
   continuous), `stepTime`, `hold` and `easing`. The native engine derives duration from the cards and timing, and can repeat
   cards to meet its cycle minimum. Use the returned duration.
4. **Format.** Use `set_aspect_ratio`: 9:16 for stories and reels, 1:1 or 4:5 for feeds,
   16:9 for sites. Set the background with `set_project_background`.
5. **Export.** Call `export_project` (mp4). Longer videos may report still rendering; call
   `check_export` until the link is ready.

## Complete procedural motion control
Users ask naturally; map their intent to the actual template settings in live context. Manage image/video cards with `update_motion_card`, `reorder_motion_card`, `duplicate_motion_card`, `remove_motion_card` and `add_project_media`; stable card ids survive reorder. `control_project_playback` plays/pauses/scrubs the native timeline. Set total clip time via the `duration` setting, or adjust stepTime/hold separately; report the returned native duration. These templates are procedural (Carousel, Stack, Orbit, Marquee, Bento), not 3D pose-keyframe tracks. Use `change_template` for a different motion type, preserving the user's media. Every sidebar setting is available in the description with its allowed options and bounds. Never ask the user to operate the timeline or type internal commands.


Group multi-tool requests with `begin_project_edit` and carry `history_group`.
Motion authoring changes now support persistent `undo_or_redo`, including card
order and template swaps. Inspect the rendered feedback image and actual duration.
Use `inspect_project` without exporting to check a frame. Native AI may generate
an explicitly requested asset from real canvas/file/attachment references; apply a
completed result as a card or background. Keep template animation editable. The
persistent export card previews the actual MP4 and retries Download without a new
render or export charge.
