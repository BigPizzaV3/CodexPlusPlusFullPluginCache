---
name: helena-video
description: Generate footage or author HTML compositions in the workspace and render them with Helena. Advanced routing and orchestration happen in the Helena web app.
---

# Create or revise a video

Capture verified product references, exact copy/dialogue, aspect ratio, duration, and audio requirements. Use `generate_video` for new footage; put supplied speech verbatim in `script`. Always pass explicit `duration` and `aspect_ratio` matching the user's request (landscape is `16:9`, portrait is `9:16`). Supported clip durations are 4, 5, 8, or 12 seconds, including reference-guided clips with up to nine images. A closing-frame image requires 5, 8, or 12 seconds. For a longer video, propose multiple clips and compose them together; do not silently shorten the user's request. Do not combine non-temporal reference images with first/last-frame anchors.

For deterministic editing, stitching, or exact text/branding, author a self-contained HyperFrames HTML composition. Save it with `write_workspace_file` under an account-relative path such as `files/video-compositions/product.html`, obtaining approval for the file write. Then call `compose_video` with `composition_path` and optional render settings. The renderer does not write HTML or accept a brief/assets payload. To revise, read the saved HTML, edit it, save to the same path, and render again.

Minimal format (replace the example copy and styling with the requested content):

```html
<!doctype html>
<html><head>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
  body { margin: 0; }
  #root { position: relative; width: 1080px; height: 1920px; overflow: hidden; background: #111; color: white; }
  .clip { position: absolute; inset: 0; display: grid; place-items: center; font: 80px sans-serif; }
</style>
</head><body>
<div id="root" data-composition-id="main" data-width="1080" data-height="1920" data-duration="5">
  <section class="clip" data-start="0" data-duration="5" data-track-index="1"><h1 id="title">Your headline</h1></section>
</div>
<script>
  const timeline = gsap.timeline({ paused: true });
  timeline.from("#title", { opacity: 0, y: 40, duration: 0.6 }, 0);
  window.__timelines = { main: timeline };
</script>
</body></html>
```

Use unitless pixel dimensions and timing in seconds, not milliseconds. Timed layers need `data-start`, `data-duration`, and numeric `data-track-index`; overlapping layers use different tracks. Media elements must be direct children of the composition root. Workspace media paths can be used in `src`; the renderer makes them fetchable. `data-media-start` selects a source offset. Video elements are muted: preserve sound using a separate root-level `<audio>` with matching source/timing, its own track, and `data-volume`. Omit audio for silent output. Do not guess source durations or speech timing; inspect supplied media with `analyze_media` and use `transcribe_media` for spoken captions. Register a paused GSAP timeline keyed by the root composition ID.

Proper routing across generation, editing, composition, and providers happens within the [Helena web app](https://agent.enrichlabs.ai). Use it for advanced or hybrid workflows instead of reconstructing internal creative playbooks in ChatGPT.

Footage generation consumes video credits; composition rendering does not. Both return a `job_id`; poll `get_operation_status` until done or error without repeating the operation. Inspect the returned URL, warnings, and any quality critique before claiming success. Fix and rerender a flagged composition rather than publishing it. Creating media does not authorize social publication; publish only through a separate tool after explicit user approval.
