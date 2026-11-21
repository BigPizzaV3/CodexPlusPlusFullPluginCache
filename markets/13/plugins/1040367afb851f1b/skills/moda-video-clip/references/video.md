# Video on Moda — existing footage and editable motion

Use uploaded footage, editable canvas animation and mp4/gif export. This connector does not generate audio/video, extend or reframe footage, or upscale video. For vector motion load moda-video-motion. Inspect existing footage with media_video_frames.

## Main Edit service

Use the Edit service for deterministic cut-list changes to the Main Edit:

- `edit_read(canvas_ref)` returns compact tracks and clips with stable ids,
  links, transitions, and exact rational times. Each time carries an integer
  string `value` numerator and a positive integer `timescale` denominator.
- Plan with an array of `insert_clip`, `move_clip`, `trim_clip`, `remove_clip`,
  `reorder_clip`, `set_transition`, `remove_transition`, `create_track` (visual),
  and `remove_track` operations. Pass them to `edit_read(canvas_ref,
  operations=[…])` to validate without mutating.
- Exact examples: `move_clip` takes `clip_id`, `track_id`, and exact `start`;
  `trim_clip` takes `clip_id`, `edge`, and exact `time`; `remove_clip` takes
  `clip_id`; `reorder_clip` takes `track_id`, `clip_id`, and optional
  `before_clip_id`; `insert_clip` takes `track_id` and a composition clip
  with a new caller-chosen unique `id`, returned track/source ids, exact
  `start`, and exact `duration`. Never invent an id referring to existing
  state. Tool discovery
  exposes the full discriminated schema.
- A composition IS a canvas page: `composition_id` takes a page id — the `p_…`
  ref from `edit_read`'s `compositions` list or `canvas_read`, or the page UUID
  — never the canvas's own `cvs_` id, which fails with "references missing
  composition". `edit_read` lists every composition with its `page_uuid`.
- This connector's edit tools insert composition clips only. Placing uploaded
  video or audio files, creating audio tracks, splitting, per-clip source-audio
  changes and OpenTimelineIO import/export are not on this connector — they live
  in the Moda app and Moda's local tooling; clips authored there still read back,
  move, trim, and remove here.
- Apply atomically with `edit_apply(canvas_ref, operations=[…],
  expected_revision=REV)`. The whole batch commits or none of it does; re-read
  after `stale_revision` and retry with the new revision.

Operations are the NUDGE lane — trims, moves, one swapped source. Building or
restructuring a whole timeline here is a larger batch of the same operations.
OpenTimelineIO interchange (versioned `.otio` files, media maps for local
footage) reads and writes files on the user's own machine through Moda's
local tooling — not on this surface.

Visual tracks composite bottom to top. A supported transition covers an exact
two-clip overlap on one track; unpaired/three-way overlaps and unknown policies
still decline by name. Types: `dissolve`, `dipToBlack`, `push`, `slideOver`;
the last two require `direction: left|right|up|down`. Named easing accepts
`linear`, `easeIn`, `easeOut`, `easeInOut`, `easeInCubic`, `easeOutCubic`,
`easeInOutCubic`, `easeOutQuint`, `easeInOutQuint`, `easeOutBounce`.
Overshooting Back curves decline instead of being clamped.

```json
{"op":"set_transition","transition":{"id":"edge-new","type":"dissolve","from_clip_id":"clip-a","to_clip_id":"clip-b","easing":"linear"},"placement":{"kind":"at_cut","in_offset":{"value":"0","timescale":1},"out_offset":{"value":"1","timescale":2}}}
{"op":"remove_transition","transition_id":"edge-from-read"}
{"op":"create_track","track":{"id":"visual-new","kind":"visual"}}
```

`at_cut` borrows exact source handles without ripple; `overlap` binds an
existing overlap and accepts optional `in_offset`. Explicit hold/loop tails
can supply outgoing handles; incoming pre-roll must exist. Insufficient handles
reject atomically. Removal restores a supported edge's saved cut.

When to transition at all: the hard cut is the default — most cuts in a
finished piece stay cuts, and a piece that transitions on every edge reads
as a slideshow. Reach for a short `dissolve` (0.3–0.7 s) to mark a real
shift of time or place, or to soften the closing beat; `dipToBlack` for a
chapter break; `push`/`slideOver` only when the motion itself tells the
story (UI walkthroughs, spatially adjacent scenes). Pick one style per
piece and keep durations consistent; when in doubt, cut. Any transition
also switches the whole export to composited work-unit pricing (the export
constraints section below), so a long timeline may buy its dissolve with a
shorter ceiling.

Trim/move refuses implicit transition growth: resize with `set_transition`
first. Inspect `changed_transition_ids` and `removed_transition_ids` in each
operation confirmation for incident edges shrunk/removed by a clip edit.
Confirm destructive trim/remove operations with the user before applying them.

Create an overlay lane using `create_track` with `track.id` and `track.kind: visual`,
then insert/move into it with `ripple:false`. The last visual track cannot be removed.
Visual transitions do not add audio fades. This connector's Edit grammar
does not author standalone audio clips or fades. Respect the surface's advertised
operations and the live validator's audio/resource limits. Slow/fast motion works on media clips (forward-only;
0.25x–4x when source audio is audible). Rate-changed audible audio plays
pitch-coupled — never promise pitch-preserved slow motion. OTIO preserves supported transition
handles and visual tracks; unknown Custom effects remain fidelity-report items.
Never replace the Edit document as raw JSON: shared operations preserve fields a
newer producer may have written. Inspect an exported midpoint as well as preview.



















## Export constraints on long or composited cuts

(Local audio routing does not apply on this connector: there is no local
shell, and standalone audio generation is unavailable here. A video fill's
own audio IS muxed into mp4 exports — an `audio_source_dropped` warning
names any fill whose sound went missing.)

Long-composition exports can be DECLINED. One mp4 is at most
**600 s / 18000 frames** (so 600 s at 30 fps, 300 s at 60 fps; a gif is
300 s / 9000 frames) and at most 4K per frame. These are outer limits, not a
promise that every Main Edit fits them. Adding any transition or second
visual track switches the entire edit to compositing: each frame costs
`1 + visible layers + transition pairs` against **18000 work units** for mp4
(9000 for gif). At 30 fps, a mostly single-track edit with one dissolve fits
just under 300 s; two continuously visible tracks fit 200 s. Single-track
hard cuts retain the 600 s tier. `frame_cap_exceeded` is terminal: shorten
the edit, lower `fps` where selectable, or reduce overlapping
layers/transitions — lower resolution helps memory limits, not this work
budget. Re-running the same over-budget composition declines the same way;
when a multi-page animation canvas fits the ceiling, `scope='sequence'`
stitches all visible pages into one video in a single call.

Two placement cautions: externally UPLOADED video files can fail to place on
a canvas — route platform-generated media by `file_` ref and treat
upload-then-place as unreliable; and a clip whose placement warned
`video_poster_unavailable` renders blank in stills — deliver canvas-video
work as an mp4/gif export, never a still.

## Delivery

Deliver editable canvas motion with the live design link and an mp4/gif `export`. One video is at most **300 s / 9000 frames** (300 s at 30 fps, 150 s at 60 fps). If the export exceeds its ceiling, shorten the composition or split it across pages and export each page. A screenshot or PNG captures only one frame.
