---
name: graphics
description: "Add and animate titles, shapes, stickers, masks and effects in Donkey Cut. Use when the user asks for on-screen text, graphics, motion or layered composites."
---

# Titles, graphics and motion
Use add_title or add_text_sequence for words, add_shape for geometry, add_sticker for an imported image, and add_effect for a treatment over a time range. Each tool's schema lists the supported styles and parameters. set_background sets the project's background color. Use ids and fonts reported by inspect_project.
update_overlay changes text, position, size, color and other element fields, and accepts ids for changes shared by several elements. Layout coordinates are frame fractions. Keep text inside the project's reported safe zones and check legibility with capture_frame.
set_overlay_keyframes and set_clip_keyframes animate poses at exact times. set_group_camera moves one camera over a group of elements, and blur and motion blur soften what the camera is not on. set_overlay_animation supplies entrances, exits, loops, word motion, a typing caret and a one-shot press at a chosen moment. set_mask clips a layer to a shape and can animate the reveal. track_motion keys a mask or a pose to a hand, a head or a person in the footage, frame by frame. set_clip_effects treats one clip alone, inside its mask. Read text-videos for timed text and text-creativity for design choices.
Build composite effects as layers: add_overlay_video for copies of footage, masks for visible regions, shapes for bands, and text for labels. Match source trims so copied footage stays synchronized. Work out geometry and timing, build one representative piece, capture_frame to check it, then repeat and check the whole composition. create_sticker generates a new sticker and spends credits when the user requests it.
