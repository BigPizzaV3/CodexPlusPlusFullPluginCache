---
name: artboard-mockups
description: Create editable mockup projects, place attached logos or designs on T-shirts, apparel, packaging and devices, make 3D device animations, and edit or export them in Artboard. Use for "create a tshirt mockup", "put this video on the phone", and follow-ups to the open Artboard project such as "make the shirt navy", "make the artwork smaller", "change the background", "undo", "play" or "export", even without another Artboard mention. Also use for Artboard account limits, subscriptions or plan-purchase questions, and requests directed at Artboard to create custom 3D meshes or access another person's private projects.
---

# Working with Artboard

Artboard is a mockup studio. Its editor opens inside ChatGPT (the Artboard view), and you
work it through the Artboard tools the way the user would with clicks. Users speak naturally; you select the internal tools and parameters. Always use the
tools; never browse to Artboard addresses.

## Account access and purchase requests

Artboard Mockups does not sell subscriptions, credits or products, or process
payments inside ChatGPT. For "buy me Artboard Pro", "upgrade my plan" or similar
requests, explain that the purchase cannot be performed here and that no purchase
has occurred. Do not invoke Artboard tools for the purchase, quote prices, promote
an upgrade, provide billing/checkout instructions, recommend a plan, or link to
pricing or checkout. This applies even when the user explicitly asks to buy.
You may offer the normal account page only as informational navigation:
[Open Artboard account](https://artboard.studio/editor). Do not describe that link
as an upgrade path or add instructions to select a paid plan and complete checkout.

For an actual denied design action, use the exact returned restriction and account
link, explain what remains available, and do not claim the blocked action succeeded.

The editor customizes existing catalog mockups, 3D device models and motion
templates. It does not author arbitrary 3D meshes from scratch. Clarify that
boundary before invoking tools for a custom-model request; offer an existing
template only if the user wants that alternative. Only projects of the selected
authorized Artboard account are available. Do not search another person's private
account, request their credentials or imply cross-account access.

## Choose the editable workflow first

When Artboard is selected or its tools are available, a request to create a mockup,
create a project, put a logo on a product, or put media on a device means an editable
Artboard project. Do not start ChatGPT image generation for those requests. This
applies even when the user does not repeat Artboard's name or @mention it again.
Keep follow-up requests in the same project unless the user asks for a new one.
This also applies after exporting a PNG: the export is a snapshot of the editable
project. For "make the shirt navy, make the artwork 20% smaller, and change the
background to light gray", read the existing project, recolor its product surface,
scale the existing artwork around its center, and change its native background.
Do not send the exported image to image generation as a substitute for those edits.

For "create a new project for a tshirt mockup, put this logo on it", search the
T-shirt catalog, open one suitable accessible mockup once, read its artwork targets,
and place the original attachment on the print surface. If the user has not asked
to choose between options, select a suitable match and proceed. Do not replace the
logo with generated artwork or stop after displaying catalog options. Report the
saved project only after the editing tools confirm the change.

Image generation is a separate workflow for an explicitly requested new creative
asset or ad; follow `product-ad` when appropriate. If Artboard tools are unavailable,
explain that limitation rather than generating a substitute mockup or claiming a
project was created. Skill instructions cannot enable tools that the host has not
made available in this turn.

## Find and show

- Flat product and scene mockups (apparel, packaging, print, devices in photos):
  `search_mockups`. Rotatable 3D models: `search_templates` with `kind: "3d"`. Motion
  templates: `search_templates` with `kind: "animation"`.
- **Image links do not display in chat.** To let the user see options, call
  `open_artboard` with `view` (`mockups`, `3d` or `animations`) and the same `search`
  text. It shows the library with real thumbnails, and the user can click one to open it.
  In your reply, list names only; do not embed thumbnail URLs.
- The user's existing work: `list_projects`, then `open_project` with its `openPath`.
  For a public project link, use the returned `openUrl` exactly; `openPath` is an
  internal editor route, not a website URL. Never prepend the website origin to it.
  The list tool opens the real Projects view with saved-design thumbnails. Do not
  embed thumbnail image links in chat or substitute catalog images for the user's
  design. List names and public links in your reply; thumbnails belong in that view.
- The user's uploaded images: `list_my_files`.

## Open

- `open_mockup` or `open_template` creates a new project each time and opens it. Open only
  what the user picked, once. To come back to it later, use `open_project`.
- Opening tools provide `openUrl` for the exact public project link. Use it
  verbatim; their `path` is only an internal editor route.
- `create_blank_project` makes an empty project; for 3D or animation, pick its template with
  `change_template`.
- For mockups, `get_open_project` reads the saved project and `set_project_image` saves
  artwork without needing the Artboard view to load first. Do not stop logo placement
  just because the panel has not opened yet. The panel renders the saved result when it opens.
- Other edits and exports currently require a connected Artboard view. A saved mockup
  description does not prove that the renderer is connected. Do not claim an export
  finished until `export_project` returns the real rendered file.
- If a tool says no editor is open, do not retry uploads, edits or exports. Reopen the
  existing project with `open_project` **at most once**, then call `get_open_project`
  using its new `editor_context`. If that fails, stop and tell the user to open the
  Artboard view and check its connection. Additional permission approvals cannot
  fix a missing editor. Do not create replacement projects or generate a substitute
  mockup. Resume only after the editor connects and `get_open_project` succeeds.

## Edit

Pass the `editor_context` returned by the latest opening tool in this chat to every
editor tool. It identifies this project in the conversation; never reuse a handle from another
chat. If it is missing, reopen the project to obtain it.

Use the latest live Artboard model context and selection when present. It includes the conversation-scoped `editor_context`, project, layers, surfaces, full 3D keyframes, playback and settings. Edits also return `projectState`. If context is missing, stale or insufficient, call `get_open_project` yourself. Never ask the user to type command names, parameter keys or ids. It says which editor is open (mockup, 3D or animation),
lists the image targets, and gives every setting with its range or options. Use only
targets and keys it lists.

- **Images:** `set_project_image` with a `target` and exactly one source:
  - `image`: a file the user attached in this chat.
  - `file_id`: one of their files from `list_my_files`. Reusing a file never counts as an
    upload, so prefer it for an image you already placed once.
  - `image_url`: a public PNG, JPEG or WebP link.

  If you don't have the user's artwork, ask them to attach it. Don't invent a stand-in logo
  unless they agree to one.
- Targets: mockups `mockup-N/surface-M` (artwork surfaces), 3D models `screen-N`,
  animations `card-N` (omit the target to add a card).
- **Look:** `set_project_background` (color, gradient or image) and `set_aspect_ratio`.
  Mockups support 16:9, 4:3, 1:1, 3:4 and 9:16; 3D and animation also support 4:5.
- **Settings:** `update_project_settings`, several keys at once.
  - Mockups: `"<surface>.color"` for product colors, `"<surface>.fit"` (`fit` or `fill`)
    and `"<mockup>.shadow"`.
  - 3D: pose keys, `variant`, `environment`, `duration`, and `time` with pose keys to set
    or add a keyframe.
  - Animation: motion fields such as direction, step time and easing.
- `clear_project_image`, `change_template` (3D and animation) and `undo_or_redo` (all three canvases).

Describe what you changed in a sentence or two; the user sees the editor update live.

## Export

`export_project` renders with Artboard's own renderer: png, jpeg or webp for images; mp4
for 3D and animation; mp4 or webm for mockups with video on a surface. The editor first requests a native host download. If unsupported, it displays a persistent **Download** action. Prefer this action or a clickable link; never make the user copy/paste a raw URL. `hostDownloadAccepted` is a host acknowledgement, not independent proof the user saved the file. The result has:

- A download link for the user. It expires 10 minutes after it is first opened.
- The original full-resolution image in the tool result when
  `originalReference.availableInToolResult` is true (up to 3 MiB); otherwise a
  reduced preview for inspection, never the generation reference.
- When the host supports it, the original image is also attached to the user's
  message box (up to 4 MiB). A composer-only image reaches you with their next message.
- `hostImageReference`, when present, identifies the actual PNG uploaded to ChatGPT
  and registered for the next user message. Wait for that message before using it.
  An MCP image visible to the assistant does not prove the image generator received
  an input image; never invent a generator image ID or substitute a description.

If the export is still rendering, call `check_export` with its `export_id`.

## Creative based on the current canvas

For a poster, ad, banner or an image-generation request based on the current canvas,
follow `product-ad`. Keep the existing project and all requested edits; export a fresh
PNG with the real renderer. Send the original PNG as the image model's reference,
never a catalog thumbnail, preview or text reconstruction. Generate the surroundings,
then use `compose_product_ad` to retain the original canvas as a protected image layer.
A preservation prompt alone cannot guarantee unchanged product details. An image
attached to the composer is available to the model only after the user sends it.
These Artboard tools work in Chat; do not require a Work handoff merely to use them.
The final composed PNG opens in Artboard's existing Preview dialog. Native generated
image variations can be wrong and are not that completed artifact.


## Complete design control

Interpret requests like "make this larger", "put my logo on the shirt", "rotate
the phone once over three seconds", "put the second image first", "pause at two
seconds", and "export it". Use the selected project and target, not a newly
created replacement. For attached-logo placement, ALWAYS use the real Artboard
editor; image generation is for a separately requested creative asset or ad.
Do not expose underscore commands in instructions to the user.

- `select_project_target`: select a mockup layer/surface or a 3D screen.
- `add_mockup_to_project`: add a catalog mockup to the existing composition.
- `add_project_media`: add an image/video as a free mockup layer or motion card.
  To print artwork ON a product or screen, use `set_project_image` instead.
- `update_canvas_layer`: change canvas position, dimensions, scale, rotation or
  name. Use `duplicate_canvas_layer`, `reorder_canvas_layer` or `align_canvas_layer`
  for those specific operations. Prefer stable ids from context; aliases are
  positional and can change after reorder/remove. Position 1 is back.
- `remove_canvas_layer` and `remove_motion_card`: remove the explicitly requested
  object/card; do not delete its uploaded file or the whole project.
- `style_project_surface`: product/screen color, mockup gradient/opacity/blending,
  fit/fill and artwork transforms. Pixels for left/top, factors for scaleX/Y,
  degrees for angle. Preserve aspect unless the user requests stretching. Use
  current transform to calculate relative requests such as 20% smaller.
- `style_project_background`: fit/fill, repeating, scale, rotation, offsets and
  anchor of an already placed image/video background. Gradient stops in
  `set_project_background` can have individual offsets; hex colors can carry alpha.
- `control_canvas_view`: mockup zoom, reset, hand mode and content-fit frame.
- `control_project_playback`: play/pause or scrub the actual motion/3D timeline;
  seeking pauses it. Mockup video surfaces support play/pause of the selected video.
- `edit_model_timeline`: author 3D keyframes, change duration, move/remove frames,
  easing and keyframe backgrounds atomically. Use the live pose ranges; never
  invent axes, hinges, screens or variants. `replace=true` replaces an existing
  animation only when the user's request calls for that. A turn is 0 to 360
  degrees with linear easing; make sure there are at least two timed keyframes.
- `update_motion_card`: rename a motion card or set its media fit. Use
  `reorder_motion_card` or `duplicate_motion_card` for those specific operations.
  Procedural motion types have no pose keyframes: change their motion settings
  with `update_project_settings`, and switch templates with `change_template`.

After every requested batch, compare the returned `projectState` with the user's
requested result before claiming success. If it is missing, read the project.
Duplicating uses the editor's native offset; follow it with explicit transforms
for a requested layout. Canvas x/y are center positions in frame percentages;
width/height are displayed frame percentages. For equal 30%-wide objects side by
side, use matching widths, y=50, and separated centers such as x=30 and x=70.
Report actual values if native limits prevent the request. A render-ready tool
result is not visual proof of a layout; inspect the available preview too.

After changing the native frame or card count, read the returned actual duration.
An added card need not extend a looping clip because the engine can repeat cards.
To specify total motion duration, use the `duration` setting alone; do not also
set stepTime/hold in that batch. Native limits may prevent an exact requested time;
state the actual duration rather than claiming an impossible value.

`undo_or_redo` restores recorded native authoring changes on all three canvases,
including template swaps. History survives closing/reopening a project. It retains
20 changes for seven days; availability is returned in `projectState.history`.
It never restores an unrelated account or overwrites an unrecorded external change.
Deleted/missing media can make a history step unavailable. Undo reverses project
edits; AI job deletion and credit refunds follow their own native rules.
Do not ask for permission again for routine reversible changes already requested;
respect the host's approval controls and confirm ambiguous/deleting-project requests.

## Plans and access

Access follows the user's Artboard account. Items with `isFree: false` need a paid plan.
Free accounts have a lifetime allowance of three surface media uploads. Deleting
files does not restore this allowance; never suggest deleting files to free up
upload capacity. Reuse an existing owned file when it is the requested media.
If something is not included, say so plainly. Never quote prices, offer upgrades, or point
to checkout; plans are managed on artboard.studio.

## Confirm before

Deleting a project. Opening many mockups at once also creates many projects, so confirm
the number first.

## Verify, group and recover

Every completed native edit supplies fresh `projectState` and, when the renderer
is ready, a `visualPreview` image. Inspect it before claiming visual success.
Compare the requested arrangement with both the returned geometry and the image.
If `visualCheckPending` is true, use `inspect_project` once; if capture still fails,
report that the edit saved but its visual result is unverified. Never invent a
preview or use this reduced image as an original generation/export reference.
Inspection is read-only and consumes no export allowance.

For one request needing several tools, call `begin_project_edit`, then carry its
`history_group` on each editing tool so contiguous changes undo as one step.
Start a new group for each new user request; do not reuse a group from another
request or chat. `update_canvas_layers`, `duplicate_canvas_layers` and
`reorder_canvas_layers` each validate their entire batch before committing once.
Use `select_canvas_group` to select several native Fabric objects,
`transform_canvas_group` to transform them around their shared center,
`align_canvas_group` to align their edges, or `distribute_canvas_group` for equal
edge gaps. Group transforms use frame percentages for position, a relative scale
factor, and degrees for rotation. Resolve stable ids before reorder. A request
combining different operations uses the matching tools with one history group;
each tool applies atomically, and contiguous changes undo together. The group
selection is native canvas selection, not a new named saved layer.

If a native save rejects an edit, the view restores its previous local checkpoint.
Read its state before retrying; do not claim success from the first local render.
Project switches close the old editor scope so queued work cannot edit the new view.

## Native Artboard AI

For explicit generation or retouching, use the native AI tools in this same app.
For placing an existing logo, changing colors, or animating an editable 3D/motion
project, use the native design controls instead of a generated replacement.

1. `get_project_ai_options` gives eligibility and the actual credit cost. Honor the
   user's budget; `max_credits` caps one generation or retry. Do not buy credits or
   change subscriptions. Credit exhaustion is a boundary, not permission to bypass.
2. `generate_project_media` runs the existing Artboard image-editing or image-to-video
   workflow. Retouching the current design uses `include_canvas=true` and captures
   the actual renderer. One image reference is allowed; video allows first/last
   frames. References can be current canvas, existing `reference_file_ids`, or
   ChatGPT `reference_images`. Choose `include_canvas=false` when attachments/files
   supply the requested references. Count all references together.
3. Prompt-only attachments are read transiently and optimized as inline references;
   they are not imported into Convex storage or Your files. Use actual attachment
   metadata, never invented file ids or URLs. Image output resolutions are
   0.5K/1K/2K/4K; video uses 720p/1080p, 4s/6s/8s, and auto/16:9/9:16.
4. `list_project_generations` reports real job states. Pending is not completed.
   Poll the job list while work is queued/processing; do not start duplicate jobs.
   `retry_project_generation` is for failed jobs, with original output settings and
   current explicitly chosen references. It needs its own credit budget.
5. `show_project_generation` opens the actual image/video in the existing Artboard
   Preview dialog. `apply_project_generation` reuses that completed asset on a
   surface/screen, as a background, free mockup layer, or motion card. It does not
   run generation again. The original editable project remains intact until an
   asset is deliberately applied. Outputs are raster/video assets, not new editable
   3D models or fabricated native layers. `delete_project_generation` uses native
   deletion only for an explicitly selected result.

Exports show a persistent **Export ready** card with **Download**. Open the saved
file to verify the original rendered output, including video playback. Download retries
reuse the captured file and renew an expired temporary link without rerendering or
charging another export. Host acknowledgement is not proof of a saved local file.


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
