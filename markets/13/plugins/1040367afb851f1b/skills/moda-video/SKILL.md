---
name: moda-video
description: >-
  Canvas motion, animation, photo slideshows, and timeline composition using
  uploaded or existing footage — including Main Edit timeline cuts,
  visual tracks, and transitions. Export editable designs as mp4/gif with
  moda-video-motion. New audio/video generation is unavailable through this
  connector.
---

# moda-video

**PREREQUISITE — `load_skill("moda-core")` once per session** (step-0, write
contract, free/metered map). Already loaded? Skip ahead. If you cannot load
it, the non-negotiables: call `moda_bootstrap` before anything; `brand_list`
before creating; revision-guarded writes use `expected_revision` from your last read.
`canvas_edit_image` captures its own target state and has no revision argument.
On `stale_revision`, re-read and retry once; send the canvas link
the moment it exists; stuck or failed? `ask_expert("<question>")` — free and
fast, never guess.

## Recipes

| Recipe | When it owns the ask |
|---|---|
| `moda-video-clip` | New audio/video generation is unavailable through this connector. |
| `moda-video-motion` | Canvas keyframes, animated type/logos, photo slideshows, existing-clip timeline compositing (cuts, visual tracks, transitions) and mp4/gif export. |

Route motion and video composition to `moda-video-motion`. Upload existing
footage or select team video files; do not promise to create missing footage.
Animate photos, text, logos and vector designs with canvas keyframes. For an
ask requiring new generated audio or video, explain that the connector cannot
do it. Cutting a large folder of LOCAL footage into a film is Moda's local
command-line footage lane, not this connector — it runs on the machine
that holds the clips (see moda.app docs: Moda for agents). A pasted canvas plus
"export as mp4/gif" uses the motion/export flow.

## Family facts

Keep text, prices and brand marks as editable canvas layers over footage.
Inspect existing clips with `media_video_frames(video='file_…')` before using
them; an empty frame list means decoding failed, not that the footage is bad.
Keyframes and clip sequencing require `canvas_create(category='animation')`;
shader fills animate on ordinary canvases too.

Export one animation page with `export(format='mp4'|'gif', page=N)`, or stitch
visible pages into one mp4 using `export(canvas_ref, format='mp4', scope='sequence')`.
A canvas with a persisted Main Edit timeline exports it with
`scope='main_edit'` (mp4 only, page-less like sequence). Stitched scopes have
no `page` argument; gif exports remain per-page. `fps` picks the capture rate
(mp4 24|30|60 default 30; gif 10|12|15|24 default 12). One mp4 film has an
**18000-frame / 600 s ceiling** (600 s at 30 fps — 60 fps halves it; gif
9000 frames / 300 s), and transitions or overlapping visual tracks lower the
composited ceiling (references/export.md). Shorten or split larger
compositions. A page without motion is refused with `no_animation`; deliver a
still and the canvas link when appropriate. Screenshots capture one frame.

Existing unmuted clip audio can be muxed into mp4; inspect export warnings for
`audio_source_dropped`. This connector cannot create audio tracks, generate
video, or perform generative video edits. See references/export.md for full
export settings and limits.

## Money

Canvas motion authoring, screenshots and mp4/gif exports are free. Iterate on
the canvas until the timing, legibility and framing work. There is no paid
video/audio generation lane through this connector.

## Delivering

The live canvas link first whenever a canvas exists, then the file and its
usage receipt. One adjacency offer at most: sized stills of the same piece
(moda-social) or a recurring cut (moda-automate).

## Errors

Any typed error → moda-core's recovery reference. `stale_revision`: re-read and
retry once — it heals.

See also: moda-core — contract, routing ladder, everything Moda can do.

## References

| Doc | Load when |
|---|---|
| references/export.md | mp4/gif rules, per-page exports, warnings |
| references/gotchas.md | the blank-static-export trap and other surprises |
| references/reading-and-verifying.md | screenshot loop, degraded verify without vision |
| references/markup.md, references/edit-code.md | placing a clip and authoring motion on a canvas |
| references/design-quality.md, references/charts.md, references/omni-and-media.md | type ladder and imagery; a data page in the cut; metered-lane semantics |
