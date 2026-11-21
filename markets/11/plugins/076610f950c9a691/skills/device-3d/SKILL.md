---
name: device-3d
description: Show the user's app screen or design on a 3D device (phone, tablet, laptop, watch) as a still image or an animated video with Artboard. Use for app store shots, product launches and device promos.
---

# Design on a 3D device

1. **Find.** Use `search_templates` with `kind: "3d"` (e.g. "iPhone", "MacBook"), and
   show options with `open_artboard` (`view: "3d"`). Open the pick with `open_template`.
2. **Screen.** Call `get_open_project`. Put the user's screenshot or design on
   `screen-1` with `set_project_image` (use more targets for multi-screen devices).
3. **Look.** These come from `get_open_project`'s lists:
   - `variant` for the device color, and `environment` for lighting.
   - Pose keys for framing: `ry` turns the device, `rx` tilts it, `fov` widens or narrows
     the lens.
   - `set_project_background` and `set_aspect_ratio`.
4. **Still image.** Make sure no keyframes fight the pose: use `clear_keyframes: true`,
   or set the pose at an existing keyframe time. Then `export_project` with `png`.
5. **Video.** Animate with keyframes. Each `update_project_settings` call with `time`
   (seconds) and pose keys sets or adds the keyframe at that time; add `ease` for the
   motion departing that keyframe. For example, for a full turn over 4 seconds:
   1. `duration: 4`
   2. `time: 0, ry: 0, ease: "linear"`
   3. `time: 4, ry: 360, ease: "linear"`

   Then `export_project` with `mp4` and wait with `check_export` if it is still rendering.
   An mp4 needs at least two keyframes or a video on a screen.

## Natural-language timeline and screen control
Use the live Artboard context to resolve the actual device, active screen, hinges, pose ranges, material variants, environments and existing keyframes. Read the project yourself only when that state is missing or stale; never ask the user for tool names or ids. `style_project_surface` controls screen color, fit/fill and artwork position/size/rotation. `edit_model_timeline` authors timed poses, easing and per-keyframe background fills in one atomic edit; use `control_project_playback` to preview, pause or scrub. For "turn once over three seconds", use two keyframes at 0 and 3 seconds with a 360-degree change and linear departure easing. Preserve unrelated pose fields. Move/remove keyframes without replacing the whole timeline unless requested. Export through the real renderer and offer the editor Download action.


Use `begin_project_edit` for a multi-tool device request and pass its `history_group`
to each edit. `undo_or_redo` now restores saved 3D authoring changes across reopening.
Inspect returned rendered previews; use `inspect_project` for a separate read-only
frame. Explicit AI retouching uses `generate_project_media` with the actual canvas
reference and a credit budget, producing a separate asset. A regular device turn
uses the editable 3D timeline, not AI video generation. Download the actual rendered MP4 and open it to verify playback; Download retries
reuse that file.


## Attached images and videos

A chat attachment can be applied to a mockup artwork surface or a 3D device screen.
Use `set_project_image` for both images and videos; its `image` file parameter is
resolved by the host to a downloadable file object. Native hosts may accept the
actual local file path through that parameter. Never send `/mnt/data/...` or a
Finder path as `image_url`: the remote Artboard server cannot open those paths.
The existing import saves validated bytes in the user's Artboard **Your files**;
reuse the returned `savedFileId` for other screens without uploading again.
Read the selected screen yourself, apply the actual media, then use fit/fill as
requested. Media placement must finish decoding before reporting it displayed.
Inspect the real render; metadata or a saved file alone is not proof of playback.

If Artboard tools are absent in the current turn, do not invent an
"Artboard-connected flow" or claim an upload succeeded. Explain the specific
host limitation and tell the user to select **Artboard Mockups** with @ in this
chat and resend the request. Opening the editor or attaching Context alone does
not prove the tools are available. Do not require another plugin installation.
