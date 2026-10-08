---
name: ai-video-editor-projects
description: |
  Build cohesive multi-scene AI videos as editable editor projects through the doublespeed MCP: generate scene clips with available credits, add an ElevenLabs voiceover track, add word-timed captions, and save it all as an /editor project the user can open and edit on the timeline. Use when the user wants an AI video assembled in the editor, a narrated multi-scene video, or MCP-driven video production that stays editable (not a one-shot render).
---

# AI Video Editor Projects

Assemble multi-scene AI videos as real editor projects instead of one-shot renders. Every layer lands on the `/editor` timeline as its own editable item: each scene clip is a video item, the voiceover is an audio item, and captions are caption items with word-accurate timing. The user (or you) can then rearrange, retrim, restyle, and export from the editor, or render via MCP.

Read `doublespeed://skills/ai-video-generation` first for model selection and credits safety; this skill covers the assembly pipeline on top of it.

## Pipeline

1. **Setup**: `whoami`, `set_product` if needed, `context_get_rules`. All steps below are scoped to the active product.
2. **Plan scenes**: agree on scene count, per-scene prompts, and duration with the user before spending credits. Default 9:16 (1080x1920), ~5s clips, 3-6 scenes. For visual continuity across scenes, use image-to-video from a shared reference image or generate each scene's prompt from one consistent style description; models do not carry state between generations.
3. **Generate scenes**: `list_models` for pricing, then `generate_video` per scene (parallel is fine) and poll `check_generation_status` until every clip has a hosted URL. Never switch products to chase credits. Existing footage: `import_media_url` for a direct file URL (mp4/mov/jpg; watch pages like YouTube or TikTok are not downloaded), or `prepare_media_upload` + `commit_media_upload` for local files (both take a `files` batch). Then `import_media_url` with `probe_only: true` for the real duration and dimensions.
4. **Voiceover**: `generate_voiceover` with the narration script (use `list_voices: true` to pick a voice first). Returns a hosted `audioUrl`.
5. **Captions**: `generate_captions` with the voiceover's `audioUrl`. Returns word-level `{ word, start, end }` timings.
6. **Save the project**: `save_editor_project` with the ordered scenes (`video_url` plus `duration_ms` or `trim_ms` each; optional `start_ms`, geometry, `fit`), any `text_items` (native editable headlines), the voiceover, and the caption words. Returns a lean `projectId`, `editorUrl`, and an `items` index (ids + timing) for follow-up patches. Pass `include_composition: true` only when you need the raw composition.
7. **Hand off**: give the user the `editorUrl` as a markdown link. Opening it loads the full composition on the editor timeline.
8. **Check a frame (optional)**: `render_video` with `project_id` and `still_at_ms` returns a PNG of that moment; cheap way to verify layout and text before a full render.
9. **Iterate**: `patch_editor_project` with the item id from `items` to retrim or move one scene, change a headline, swap a motion clip's HTML, or replace captions without resending everything. An open editor tab picks the change up live.
10. **Export (optional)**: call `render_video` with `project_id`; no need to resend the composition. For anything over ~20s or `quality: "high"`, add `background: true`: it returns a `jobId` at once, and `check_generation_status` with `render_job_ids` reports progress and the final `videoUrl` (a synchronous call that outlasts your client's tool timeout reads as a failure even though the render finishes). Or let the user export from the editor after their edits.

## Details that matter

- Scene clips are placed back-to-back in order unless a scene sets `start_ms`. `trim_ms: { from, to }` picks which part of the source file plays (independent of timeline position); `duration_ms` alone means "play the first N ms". Pass `source_duration_ms` (from the probe) so trims past the end of the file are rejected instead of producing black frames.
- Scenes fill the canvas by default (`fit: "cover"`). Use `fit: "contain"` or `"blur-fill"` with `source_width`/`source_height` for mismatched aspect ratios, or set `top`/`left`/`width`/`height` for picture-in-picture layouts.
- `text_items` are native editor text layers (font, size, color, position); prefer them over baking text into video for anything the user may want to reword.
- The voiceover defaults to spanning the whole video from 0. Pass `duration_ms` when the narration is shorter than the scenes so it does not get stretched on the timeline.
- Captions group words into items of 4 by default (`max_words_per_caption` to change). Presets: `stroke` (white text, black outline) and `boxed` (white text on a dark box); override font, size, color, `position` (top/center/bottom) or explicit geometry. Both stay editable per item in the editor.
- Caption `timing` defaults to `timeline` (word times are project times, e.g. from a voiceover). Use `timing: "source"` with `source_url` when the words were transcribed from the scene footage itself: they are then mapped through each scene's trim and placement, so reordering or retrimming scenes keeps captions in sync.
- Update instead of duplicating: pass `project_id` to `save_editor_project` to overwrite an existing project after feedback.
- Preview before showing the user: `render_video_preview` with the returned composition catches pacing and caption-timing problems cheaply.

## Best practices

- Write the narration script first and generate scenes to fit it, not the other way around; timing a script to existing clips almost always needs manual editing.
- Keep narration inside the total scene duration. A 5-scene x 5s video holds roughly 60-70 spoken words.
- Check guardrails (`context_get_rules`, `context_check_content`) before queueing or publishing anything built from the project.
