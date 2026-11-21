# `export` — deliverable files

```
export(canvas_ref, format='pdf'|'pptx'|'png'|'jpeg'|'mp4'|'gif',      # mp4/gif REQUIRE page
       scope='page'|'sequence'|'main_edit', page=N, pixel_ratio=1..4,  # …unless a stitched scope
       flatten=…, video_quality='standard'|'high'|'max',               # mp4 only
       video_codec='h264'|'h265', fps=N)          # fps: mp4 24|30|60, gif 10|12|15|24
```

- **Export is ASK-FIRST.** The live link (share/editor URL) is the handoff,
  always — run it only when the user named a file or format ("a PDF
  one-pager", "PPTX", "send me a file" — their format words win, and
  platform-implied files like the LinkedIn-carousel PDF count) or accepted
  the single brief offer at handoff. Never auto-export as ceremony. Share
  the link BEFORE any export — the link never depends on the export
  succeeding.
- **Shader fills and animations freeze in static exports** (png/jpeg/pdf/
  pptx) — they render live in-app. The motion-preserving exports are
  `format='mp4'` and `format='gif'` (one page's animation per file, or one
  stitched film of every page with `scope='sequence'` — next bullet; a page
  with NO animation rejects typed `no_animation` — that is the honest
  answer, deliver a still + the live link). When an animated canvas gets a
  static-file request, offer the motion file too.
- **A multi-scene sequence (an animated storyboard) becomes ONE stitched mp4
  with `scope='sequence'`** — mp4 only, multi-page animation canvases only:
  every visible page in canvas order, page transitions included, one video,
  no `page`. The whole stitched film shares the single-page mp4 ceiling
  (18000 frames / 600 s TOTAL, so 600 s at mp4's 30 fps), so a long storyboard rejects
  typed `animation_budget_exceeded` — shorten pages or split the export.
  A canvas with no animation timelines rejects `no_animation`; gif has no
  stitched form (export gifs page-by-page). The editor's export panel has the
  same MP4 "sequence" mode when the user wants to drive it interactively.
  A canvas with a persisted Main Edit timeline (the NLE-style edit) renders
  it with `scope='main_edit'` — mp4 only, page-less like sequence, fine on a
  single-page canvas; no persisted edit rejects typed `no_animation`.
  Without a stitched `scope` it is one page of animation per mp4/gif
  (`page=N`). `fps` picks the capture rate (mp4 24|30|60, default 30;
  gif 10|12|15|24, default 12) — the frame ceiling is rate-independent and
  per-format (mp4 18000 frames / 600 s, gif 9000 frames / 300 s), so 60 fps
  halves the longest exportable mp4 timeline (300 s); pixel ratio (1–4)
  is the resolution lever; mp4/gif default to 1 (page resolution). Any
  transition or second visual track makes a Main Edit export composited:
  each frame costs `1 + visible layers + transition pairs` against 18000
  work units (mp4), so a mostly single-track edit with one dissolve fits
  just under 300 s at 30 fps and single-track hard cuts keep the 600 s tier;
  over budget rejects terminal `frame_cap_exceeded` — shorten the edit,
  lower `fps`, or reduce overlaps (lower resolution does not help).
- **mp4 has two encode knobs, both optional and both mp4-only.**
  `video_quality='standard'|'high'|'max'` (default `standard`) buys sharpness
  with encode time and file size; nothing about the render changes, so a
  re-export at a higher tier costs only the encode. `video_codec='h264'|'h265'`
  (default `h264`) picks the codec inside the same `.mp4` container: `h265`
  (HEVC) is much smaller on detailed footage but needs a modern player — hand
  it to someone only when they asked for a smaller file or named HEVC. Either
  argument on a non-mp4 format is rejected, never ignored.
- **A page bigger than 4K still exports.** MP4 is capped at 3840px on the
  longest side (and a 4K pixel budget); an oversized page is scaled down to
  fit and the result carries an `mp4_downscaled_to_fit` warning naming the
  delivered dimensions. Relay it — the file is smaller than the page.
- **Sound in a page or sequence mp4 is exactly the unmuted video fills' own
  audio, muxed server-side — nothing else.** The PAGE timeline has no
  standalone audio track, so on those scopes export muxes no voiceover or
  music: standalone audio generation is unavailable on this connector.
  `scope='main_edit'` is the exception — the Main Edit's audio tracks (music
  beds and VO placed as `media-stream` clips, with their gain, pan and fades)
  mux into the file alongside unmuted visual-clip audio.
- **The hero claim, stated verbatim:** PDF exports carry real text layers, embedded fonts and clickable hyperlinks — a link on the page is a live link in the file; PPTX exports are native editable shapes and text — not screenshots pasted into a deck. **PDF exports need `flatten=false`** — the server default (`flatten=true`) rasterizes the PDF; pass `flatten=false` on every PDF export unless the user explicitly wants a flat raster file.
- **Read the `warnings[]` on a completed export.** Quality caveats about a file that still succeeded — `pptx_shape_rasterized` (some images baked into the slide rather than editable shapes), `pptx_content_dropped` (elements missing from the deck entirely), `pdf_pages_dropped` (pages missing from the document), `pdf_page_rasterized` (a page shipped as pixels — it looks right and its links still work, but its text is not selectable or searchable), `pdf_page_reduced_quality` (an oversized page rendered below the DPI you asked for), `audio_source_dropped` (an mp4 shipped without one video fill's audio — the message names the source and why). Relay the caveat honestly when you hand over the file. A warning is usually not a reason to re-run the export — the pptx and pdf rendering degradations are deterministic, an identical re-run degrades identically — and never a reason to withhold the file. Two exceptions are worth a re-run: `pdf_pages_dropped` means pages are genuinely ABSENT from the document, so say so plainly and try again rather than handing over an incomplete file; and an `audio_source_dropped` whose message names a fetch failure or timeout is transient-shaped and MAY succeed on a later export of an edited canvas (a plain re-run of the same version returns the cached file). Treat an unrecognized code as informational and pass its message along.
- Export is deterministic-lane: **zero metered credits on every plan** (`usage.metered_credits: 0` on the response). Export rate is plan-quota enforced server-side; a throttle surfaces as a typed error with a retry hint.
- A render that outlasts the wait budget returns a job handle — poll `task_status` (its `retry_after_seconds` says when); re-calling `export` reuses the same job, it never renders twice.
- Never poll with sleeps longer than 60 seconds; follow `task_status`'s `retry_after_seconds`. If export fails with the same typed code twice, deliver the share link + screenshots and note the export failure honestly.
- The result carries a short-lived download link — hand it to the user in your reply promptly (it expires).
- **Multi-page png/jpeg arrives as ONE zip of per-page images** — the response's `delivered_format` says `zip`. That zip is the deliverable for image carousels; don't call it a png.
- `page=N` exports a single 1-indexed page (there is no range selection); omit it for all pages. A multi-page png/jpeg export arrives as one `.zip` of per-page files.
- **`format='webp'` is rejected with a typed error** — it has no server lane. Say so plainly instead of retrying; the supported stills are pdf, pptx, png, jpeg.

Typical closes:

```
export(canvas_ref, format='pptx')   # after a deck build
export(canvas_ref, format='pdf')    # after a document build
```

Pair the file with the canvas link (`canvas_share` mints a share URL; `editor_url` rides every mutation result) — the deliverable is both: the artifact file and the live, editable canvas.
