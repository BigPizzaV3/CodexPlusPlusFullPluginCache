---
name: segmind-anime-video
description: >
  Generate anime, manga, or cartoon-styled video with Segmind — a cel-shaded
  clip from a prompt, an anime-style ad, a stylised animation from a reference
  image or character. Use when the user asks for anime, manga, cartoon,
  cel-shaded, or hand-drawn animation as the *look* of a video. Do not use for
  photoreal video (that is segmind-generate-video), for still anime images, or
  for restyling existing footage.
---

# Anime video with Segmind

Read [inference-contract](references/inference-contract.md) first. For the
Pixelflow route also read [pixelflow-contract](references/pixelflow-contract.md).

## Use the `anime-maker` flow, or the model directly

`anime-maker` — inputs `prompt`, `duration`, `aspect_ratio`, `resolution`;
output `video_out`. Single node, so it fails legibly.

Underneath it is `wan3.0-video`, which you can also call directly:

**Measured working:** a 5s 720P clip completed in **159s for $0.50**.

```
submit_inference("wan3.0-video", {
  "prompt": "anime style, ...",
  "resolution": "720P",
  "duration": 5,
  "aspect_ratio": "16:9"
})
```

Optional: `image` (first frame), `last_frame`, `reference_images` (character
consistency across shots), `audio_url`, `negative_prompt`, `prompt_extend`
(defaults true — it rewrites your prompt upstream; set false when you have
written a precise one and want it respected).

**`@` is rejected by wan3.0 specifically.** Strip `@` from prompts; sibling
models tolerate it, so a prompt that worked elsewhere can fail here for that
one character.

Alternatives at other price points: `wan2.7-t2v` (text-to-video),
`wan-2.2-i2v-fast` (~$0.18, ~40s) when a still already sets the look.

## The published anime flows

`anime-style-ad-wan-3` passes the chain check — every model it uses is live —
and **still fails**: measured, it ran for **10 minutes and returned
`COMPLETED` with a null video**, billing the nodes that did run. Do not offer it.

`ai-cartoon-avatar-video-creation-nano-banana-veo-3-1-fast` and
`cartoon-style-dance-animation-creation-kling-motion-control-nano-banana-pro`
pass the chain check but are unverified. Treat them as untested and say so.

`indie-anime-video-wan2.2-qwen-image` also passes, but it is a **fifteen-node**
graph that runs `llama4-scout-instruct-basic` six times — the same node measured
returning 400 inside `qwen-image-edit-virtual-try-on` (see `segmind-fashion`).
Do not reach for it.

The general lesson, which the contract states and this use case proves twice:
**a live chain is not a working flow.** When a single model can do the job, the
model is the more reliable route.

## Getting the look

The style lives in the prompt — there is no "anime" parameter.

- Name the medium and the technique: *cel-shaded, hand-drawn 2D animation, flat
  colour with hard shadow edges, visible line art*. "Anime" alone drifts toward
  3D-render.
- Name the era or register if it matters: *90s OVA*, *modern TV anime*,
  *studio-quality film animation*, *chibi*.
- Describe motion in animation terms: *animated on twos*, *held frame with a
  camera pan*, *speed lines*.
- Put camera and light in the prompt too — they read as strongly here as in
  photoreal work.
- **Never name a real studio or franchise.** Describe the look instead; a named
  studio is both a legal problem and a weaker instruction than an actual
  description.

For a consistent character across several clips, generate the character sheet
once as a still (`segmind-generate-image`), then pass it via `image` or
`reference_images` on every clip rather than re-describing them each time.

## Workflow

1. Write the prompt with an explicit style block (above). Strip any `@`. If the
   user supplied a reference or first-frame image as a file, upload it with
   `upload_media` first (contract rule 4) — the model takes a URL, not a path.
2. Quote the cost — $0.50 for 5s at 720P — and confirm.
3. **Submit, then poll in this same turn** until it finishes — ~160s is
   normal. Do not use `run_inference`, and do not hand the turn back saying it
   is queued.
4. **One clip first.** Get the look agreed before generating a sequence.
5. Deliver the `images.segmind.com` URL. To cut, caption or join clips, hand off
   to `segmind-video-edit`; to sharpen, `segmind-video-upscale`.

## Rules

1. **`wan3.0-video` direct, not the anime Pixelflows.** The flagship flow
   silently returns nothing.
2. **No `@` in a wan3.0 prompt.**
3. **No real studio or franchise names.**
4. **One clip, then the sequence.**
5. **Never `run_inference` for this** — 160s exceeds the blocking budget. Poll
   `check_inference` in-turn instead.
6. **Segmind models only.**
