# Hosted trailer timeline

Call `pps_plan_trailer` without spec to verify the live worker supports TrailerComposition before buying assets. Use the returned tool schema as the authority. No local render environment is required.

One spec has title, mode (cinematic or product-hype), durationFrames (150–1800 at 30 fps), aspectRatio, background, layers, audio. Times are integer frames: 30 seconds = 900 frames. Layers draw back to front in array order. Each has startFrame, durationFrames and canvas-percent x/y/width/height. All source IDs are real workspace assets at render time; plan placeholders are allowed only during planning.

Layer kinds: text, rect, ellipse, cursor, image, video. Font size is percent of canvas width; radius and borderWidth are pixels. Text is exact, editable and rendered by PPS. For precise real product UI, import a screenshot using pps_import_image and animate it; compose text/shapes/cursors only from verified UI or label the result conceptual. Avoid generated legible UI text.

Keys are local frames; first key is frame 0, strictly increasing, last before layer duration. Each key is a COMPLETE pose: x/y offsets in canvas percentages, scale, rotate in degrees, opacity, reveal (left-to-right wipe). Omitted properties reset to defaults rather than inheriting. The destination key sets ease (linear/in/out/in-out). Use identical adjacent poses for holds. Crossfade with overlapping layers and complementary opacity keys. Cut by changing layer boundaries. Video trimStartFrame picks the source in-point; default volume 1 preserves source sound.

Audio uses kind music (MusicGeneration), voiceover (NarrationGeneration), or scene-audio (SeedAudioGeneration). It has assetId, startFrame/durationFrames, trimStartFrame, volume, fadeInFrames/fadeOutFrames and local gainKeys. Place existing risers and impacts from scene-audio takes; there is no new SFX generation endpoint. Gain keys create score dips under speech. Check the actual score; no automatic beat detection is claimed.

Limits: 80 layers, 16 keys per layer, 16 audio clips, four simultaneous video layers, 5–60 seconds. Exact source lengths are checked by the worker before rendering. Do not request media past its end. The background intentionally fills uncovered frames; review every deliberate blank hold. Use fontSize and box bounds that keep all titles legible, and visually inspect the rendered result. Rendering is free; source creation uses existing quote/approval. Render with pps_render_trailer, follow pps_wait_job, deliver the MP4 Save link and preserve the editable spec.
