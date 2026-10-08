---
name: create-demo-video
description: Create a demo from new or existing footage, with captions, zooms, privacy masks, and optional cursor animations or input badges.
---

# Create a demo video

Use Cirro to turn a recording into a product demo. Keep the original recording and write
generated files outside tracked repository paths.

When footage is needed, use [Capture Demo Video](../capture-demo-video/SKILL.md).

Follow [Set up Cirro](../setup/SKILL.md) to prepare its launcher before editing. The
examples use the macOS/Linux launcher; pass the same arguments on Windows.
If setup fails, report the blocker; do not substitute another editing pipeline.
Use Cirro to validate and render the final screenplay, fixing validation errors
before delivering the video.

## Inspect the recording

Cirro produces VP9/WebM video without audio and can also read supported MP4 recordings.

```sh
sh /absolute/path/to/setup/scripts/cirro.sh schema
sh /absolute/path/to/setup/scripts/cirro.sh inspect /absolute/path/recording.webm --json
```

Read the schema and [editing guide](references/screenplay-contract.md). Check the
recording's dimensions, duration, interface states, and frames around important
transitions. Before choosing the trim, identify the outcomes the user's request or
session summary says the demo should show, then locate their evidence in the footage.
Keep the setup and result for those outcomes. A short demo can compress pauses without
reducing a multi-step walkthrough to its last interaction. For a failure and retry,
let the viewer recognize the failure, retained work, and eventual result.

Show the starting state, interaction, response, and result. Use short captions to
explain what's happening.

For cursor animations and input badges, use actual event logs with coordinates in
recording pixels and timestamps in milliseconds from the first video frame. Keep drag
endpoints and button metadata; map tool names only when their meaning is known.

Omit `recording.events` when logs are unavailable. The renderer then keeps any cursor in
the recording and adds no cursor animation or input badges. If the recording already has
a cursor, omit pointer events to avoid drawing a second one; reliable keyboard events
can still produce input badges. Use cursor-free footage when supplying pointer events.
Never invent events from screenshots.

Summarize ordinary typing by count. Protected typing must contain neither its value nor
its length. Review the visible interactions as well as the finished file.

## Edit the video

Keep one continuous section of the recording. Trim the beginning or end and speed up
idle time instead of adding gaps, repeats, freezes, or invented actions. Keep enough of
the opening to establish where the viewer is and what will change. Keep important
actions and their visible results, including the final success or failure, readable.
Compress idle waits aggressively, but preserve time to recognize each new state.
The renderer shows a double-chevron icon during
fast-forward and adds elapsed source time after ten seconds.

Start at full-frame zoom 1. Use a zoom only when it reveals a detail the viewer would
otherwise miss. Use a short, deliberate transition, then hold the same framing through
the action and result. Avoid a slow zoom throughout a scene or an immediate zoom-out
that competes with the action. Keep the cursor, target, and relevant result inside the
frame; show enough context to follow scrolling and movement between controls.

Highlight visible results sparingly. Inspect the target's bounds in the actual frame;
use balanced padding that separates the annotation from the UI without covering nearby
controls. Start the highlight after its target appears and end it before the target
moves or disappears. Map source times through speed changes before timing overlays.

Use ASD-STE100-inspired language for captions: short sentences, active voice, familiar
words, and one idea per caption. Explain the action or result and give each caption
enough reading time. Keep captions and input badges from overlapping each other or the important UI;
omit redundant annotations. If annotations obscure the evidence, simplify or remove
them before adding camera motion to make room. A clear, complete static edit is a
better starting point than a decorated edit that needs repeated repairs.
Recorded click events animate the cursor. Use
`edit.style.reduced_motion` when requested.

Set `edit.style.accent` to `#4a8fff` for an ordinary demonstration, `#ef6b73`
for a bug reproduction, or `#58c98a` for a verified fix. Use the video's actual
outcome to choose the color; an unresolved bug is not a verified fix.

Use `edit.cover.at_ms` to choose a frame that shows what the viewer should notice. The
cover is the first video frame; the complete story follows. Overlay and camera times
refer to the story, so do not offset them for the cover. Derive duration from clip
ranges and speeds; validate to get the exact mapped event times.

Cover private information with opaque masks in every affected frame, including the cover
and zooms. If masks would hide the behavior being demonstrated, request a clean
recording instead of sharing it.

## Validate and render

```sh
sh /absolute/path/to/setup/scripts/cirro.sh validate /absolute/path/screenplay.json --json
sh /absolute/path/to/setup/scripts/cirro.sh render /absolute/path/screenplay.json -o /absolute/path/demo.webm --json
sh /absolute/path/to/setup/scripts/cirro.sh frame /absolute/path/screenplay.json --at-ms 2000 -o /absolute/path/review.png
```

Start with 60 fps and a width near 1440 pixels, adjusted for the source dimensions and
aspect ratio. Upscaling does not add source detail. Wait for encoding to finish.

## Verify and deliver

Watch the finished video. Check that the actions and results are easy to follow. Check
frames around clicks, zooms, speed changes, masks, and the final result. Watch the opening
and ending without relying on the prompt: the viewer should understand the setup and
see the outcome, not just the last click. Make sure the cover and captions match what happened and private content stays covered. The renderer
decodes the output to check VP9/yuv420p WebM, dimensions, frame count, and timing. That
does not establish that the demo shows the task or is easy to follow.

When the user is working on a pull request, include the video in that PR using
[Share Demo Video](../share-demo-video/SKILL.md). Otherwise, show the final video using
its absolute file path. Mention any limitations in the footage.
