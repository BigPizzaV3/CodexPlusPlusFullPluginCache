# Media Inputs, Edits And Reuse

Use PixVerse's offline Create contracts and the wrapper's actual supported parameters
for image/video/audio generation. Use FFmpeg/ffprobe for local media inspection,
extraction and editing. Read only the input family needed by the current request.

## Media Roles And Job Lifecycle

Keep local file, provider media path, upload ID and generation job ID distinct.
Use documented role mappings, ordered image/video/audio arrays and current limits.
An endpoint image is not a general style reference. Audio input does not imply an
output-audio toggle. Reuse accepted assets through provider paths and receipts;
record parameters actually returned. Recover uncertain submissions by ID.

## Reference Information

Use available reference information to guide the requested creative work.

### Video Reference Information

For a supplied file or a link the user asks to work from, use `./reference-breakdown.md`:
probe, frames, word-labelled contact sheets, cut candidates, local transcription and
timecoded notes (`ANALYSIS.md`, `TIMELINE.md`). The remake workflow rebuilds the piece from
those notes; other workflows consume them for scripts, boards and adaptation.

Reuse available information about mood, pacing, camera choices, text, sound and the moments
the user wants to preserve or change. Keep observed details distinct from creative
assumptions; do not claim to have watched footage based on a link or summary alone.
A complete shot-by-shot report is not required to begin planning from sufficient reference
information. For exact source-preserving edits, obtain usable footage before editing.

### Image Reference

Classify it:

- identity anchor: preserve subject
- brand anchor: preserve logo/packaging/visual system
- style reference: preserve aesthetic only
- layout reference: preserve composition
- raw asset: use directly or upload

If the image is an identity/brand anchor, pass it to PixVerse as an image reference instead of only describing it.

### Storyboard Boards And Dossier Images

When a generated board contains panels, labels, arrows, column headers, frame numbers, borders, or split-screen layout, treat that board furniture as reference-only. The video prompt should say the model should read those elements for identity, sequence, composition, and motion intent, not reproduce the literal grid.

A multi-panel board usually means sequential beats over time. If several subjects must appear together, describe one cohesive frame or space; do not ask the video model to render a panel collage unless the user explicitly wants a split-screen graphic.

## Image And Video Edits

- Image edits and refinements use Sunburst 2K/high. Bind the accepted image, state the
  specific change and protect its identity, composition, aspect and unchanged text.
- Localized video edits need the actual source video, the requested change and any
  reference frame's exact source time. Use only roles supported by the selected video
  mode. A still-image edit alone does not change the corresponding video frames.
- Crop, contain-fit, letterboxing, trims and graphic overlays use FFmpeg. Preserve
  chronology and accepted audio. Outpainting requires a supported generative mode;
  a crop does not reveal unseen pixels.
- Continue or modify motion using the actual source video and supported edit/extend
  mode. Keep source timing, reference authority and the intended start/end state.
- For character continuity, use accepted images and the separate identity, expression,
  wardrobe and scene roles in `../skills/pixverse-character-sheet/references/identity.md`.

## Reusable Creative Inputs

Store the accepted creator, product, brand, hook, setting and ad reference in local
project memory. Record exact spelling, real product/packaging images, dimensions,
visible features, supplied claims and source files. Keep a hook distinct from a style
image or product reference. Reuse a canonical product/brand record across outputs.

Select the concrete workflow by the requested result: creator UGC, product showcase,
try-on, unboxing, tutorial or cinematic ad. Reference-led work uses reference information
already obtained by Codex or supplied by the user; Codex chooses how to acquire and
understand the source. A fresh concept starts from its chosen hook and setting.

## Sound

Use voiceover for exact spoken copy, music generation for a requested soundtrack,
and video-native sound for visible synchronized events. Existing sound effects can
be extracted, trimmed or mixed with FFmpeg. Use a standalone generation mode only
when the current CLI contract exposes that media type; preserve the actual output
role rather than calling a music bed an isolated sound effect.

Specialized multi-shot prompts retain all shot, voice and reference instructions.
Shared descriptions can be concise; prompt budgets do not remove required events.
