---
name: launchscene-reference
description: Turn a real launch video reference from Launchscene into a frame-numbered REFERENCE.md and BRIEF.md before building a Remotion or HyperFrames scene. Use when the user wants to plan a launch video, product reveal or shot "like" a reference, or asks for timing, entrances, holds or frame numbers taken from an existing launch film. Requires the Launchscene MCP server.
---

# Launchscene reference brief

Plan a shot from measured references instead of scrubbing a video frame by frame. Launchscene has already measured the scenes, on-screen text, text entrances, camera moves and audio cues of reviewed launch videos. This skill turns one of them into the two files a motion build needs.

## Before you start

- The Launchscene MCP server must be connected (`/api/mcp` on launchscene.app). If its tools are missing, say so and stop; do not guess measurements.
- Ask for anything missing: the product, the one action to show, the viewer, the composition size and frame rate (default 1080x1080, 30 fps), the target duration, and the assets the user can supply.

## 1. Pick the reference

- If the user gave a Launchscene link (`/v/<slug>?t=...`), use the slug, and the scene at that time from `get_video`.
- Otherwise call `search_scenes` with the role and techniques that match the brief (for example `role: "demo"` or `"feature_reveal"`). Offer two or three contrasting cards and let the user choose. Do not pick the most common pattern as if it were the best.

## 2. Get the measured reference

Call `reference_brief` with the chosen `scene_id` (or `video_slug` plus `start_ms`/`end_ms` for a window up to 120 s) and `target_fps` set to the user's composition frame rate.

Save the returned `markdown` unchanged as `REFERENCE.md`. Do not edit the measured sections.

## 3. Check the uncertain frames

For each item in `verify_frames`, call `get_frames` with its `scene_id` and `at: [at_scene_ms]`, then look at the images. Under a heading `## Frame checks` appended to REFERENCE.md, write one line per frame: what it confirms or contradicts (landing position, overshoot, transition length). Use the returned `frame_ms`, not the requested time.

## 4. Write BRIEF.md

Use global, inclusive frame numbers at the user's frame rate. Keep these sections:

```plaintext
GOAL
What the film demonstrates, the viewer, opening copy (max eight words), closing action.

DELIVERY AND ASSETS
Composition name, size, fps, total frames. Assets under public/. Missing assets.

LAYOUT
Canvas origin top-left, pixels. Background, text and accent colors. Outer margin.
Headline box, product card box, layer order.

SCENE: FRAMES a THROUGH b   (one block per scene)
Each key frame and its event: entrance, landing, cursor move, press, reveal, reading hold, cut.
Curves (spring or easing) and offsets. What stays fixed into the next scene.

IMPLEMENTATION AND REVIEW
Drive values from useCurrentFrame; expose timing constants.
Stills to render first, and the frames to inspect after approval.
```

Rules:

- Label every number as `measured` (from REFERENCE.md), `derived` (server arithmetic such as readable hold) or `proposed` (your choice). Never present a proposed value as measured.
- Adapt the timing to the user's copy and product. A reference hold of 60 frames for four words does not transfer to twelve words.
- Fonts, colors, exact curves, overshoot, cursor actions and transition lengths are not measured by Launchscene. Propose them and say so.
- Do not reuse the reference brand's footage, logo, fonts, music or copy.

## 5. Check the copy before motion

Call `readability_check` with each planned text: `in_ms`/`out_ms` from your frames (`ms = frame * 1000 / fps`), `box` as fractions of the canvas, `line_height_pct` as font size divided by canvas height times 100, and colors if known. Report each returned question next to the scene it concerns. Shorten copy or extend a hold when the reading demand is in the upper quarter; do not silently change the plan.

## 6. Stop for approval

Return REFERENCE.md, BRIEF.md, the readability questions and the list of missing assets. Wait for the user before implementing. After approval, build the opening scene first and render its stills (see the `launchscene-timing-check` skill).
