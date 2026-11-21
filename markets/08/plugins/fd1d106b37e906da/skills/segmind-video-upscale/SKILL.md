---
name: segmind-video-upscale
description: >
  Upscale or enhance the resolution of an existing video with Segmind. Use when
  the user wants a video made sharper, bigger, higher-resolution, 2x/4K, cleaned
  up, or "enhanced" — including a clip they just generated that came out too
  soft. Do not use for images (that is segmind-generate-image), for generating
  new video, or for reformatting, trimming, or re-encoding a video without
  changing its resolution.
---

# Upscale a video with Segmind

Read [pixelflow-contract](references/pixelflow-contract.md) and
[inference-contract](references/inference-contract.md) first.

## Use `bria-increase-video-resolution`

Priced at **$0.05 per video-second of *input***, so a 10s clip is ~$0.50 — quote
that before running.

### Always pass `desired_increase: 4`

Because the price is per **input** second, the multiplier is free. Measured on
the same 3.57s clip:

| `desired_increase` | Output | Cost | Inference |
|---|---|---|---|
| 2 | 2048x1024 | $0.1785 | 25.0s |
| **4** | **4096x2048** | **$0.1785** | 44.6s |

Same bill, 16x the pixels. The only cost is ~20s more wall-clock. So **4 is the
default** — drop to 2 only when the user explicitly wants a smaller file, or
when the output feeds a downstream model with a resolution ceiling.

The model does **not** default to 4 (its default is 2), so pass it explicitly
every time.

Two routes, same model:

- **The Pixelflow** `video-enhancer` — inputs `video`, `scale` (2 or 4),
  `format`; output `video_out`. Use it when the enhance is a step in a bigger
  flow, or when you want the format conversion for free.
- **The model directly** via `submit_inference("bria-increase-video-resolution",
  {"video_url": ..., "desired_increase": 4})` — fewer moving parts for a one-off.

`output_container_and_codec` accepts `mp4_h264` (default), `mp4_h265`,
`webm_vp9`, `mov_h265`, `mov_proresks`, `mkv_*` and `gif` — so the format
conversion is free here rather than a separate `video-editor-agent` call.

Either way this is a slow model: **submit, then poll `check_*` in the same turn
until it is done.** Never `run_inference`, and never end the turn on "queued".

## Do not use these — they are broken

| Model / flow | What happens |
|---|---|
| `esrgan-video-upscaler` | Fails **every** call with `image not found` — including with its own documented sample video. Dead. |
| `ai-video-enhancer`, `runway-4k-upscaler`, `kling-1.6-4k-upscaler` | All three published flows chain `esrgan-video-upscaler`, so all three fail. |
| `topaz-video-upscale` | Fails with `Could not read the input video's metadata` — it is billed on input duration and the probe it needs is missing in production. |
| `flux-3-draft-enhance` | Not a general upscaler; it only takes a `draft_cache` handle from its own generation. |

If the user names one of these, say plainly that it is currently broken and
offer Bria instead. Do not "try it anyway" — a failed run still costs the wait,
and in a Pixelflow it can bill the earlier nodes in the chain.

## Workflow

1. **Get a URL for the source video.** A local file goes through
   `upload_media` first (contract rule 4); a video from an earlier Segmind step already
   has an `images.segmind.com` URL that feeds straight in.
2. **Quote the price.** $0.05 x the clip's length in seconds. Confirm anything
   over $0.50.
3. **Submit**, then poll on the returned hint until terminal — in this turn,
   not by asking the user to check back.
4. **Deliver** the `images.segmind.com` output URL, and say the new dimensions
   if the user cares about the exact size.

## Rules

1. **Duration is the only cost lever — resolution is free.** A 60s clip is $3
   whether you upscale it 2x or 4x. Check the length before submitting; if the
   user only needs a section, trim first with `segmind-video-edit` ($0.30 flat,
   so it pays for itself on anything over ~7 seconds of trimmed material).
2. **Upscale last.** In a chain, run generation and any editing at the working
   resolution, then upscale once at the end — upscaling early makes every
   downstream model slower and dearer for no visible gain.
3. **Never `run_inference`.** Submit, then poll in-turn until terminal.
4. **Do not silently substitute a model** if Bria fails. Say which model failed
   and what its error was.
