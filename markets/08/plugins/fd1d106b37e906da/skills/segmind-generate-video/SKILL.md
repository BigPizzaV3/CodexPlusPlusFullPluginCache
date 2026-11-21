---
name: segmind-generate-video
description: >
  Generate or edit video with Segmind. Use when the user wants a clip made from
  a prompt or from a still image — a product or brand ad, a cinematic shot, an
  animated photo, a talking avatar, a reference-consistent character clip — or
  wants an existing video changed: extended, restyled, background removed,
  objects erased, lip-synced, or subtitled. Do not use for still images, for
  audio-only output, or when the user only wants a model recommendation.
---

# Generate video with Segmind

Video is the slow path and the expensive one. Both facts drive the whole
workflow: **never `run_inference` it, always price it first, and poll it out
within your own turn rather than handing back a queued job.** Read
[inference-contract](references/inference-contract.md) before any tool call.

## The one rule that matters

**Video always goes through `submit_inference` + `check_inference`. Never
`run_inference`.**

`run_inference` holds one request open and its wait is capped at 50 seconds, so
that the call fits inside the MCP client's own request timeout. Video models run
far past that — `seedance-2.0` averages ~200s, `kling-3-pro-image2video` ~160s.
A `run_inference` on any of them ends in a `pending` handle at best, and burns a
minute of the user's time doing nothing. Submit, then poll.

## Workflow

### 1. Price it before you spend it

Video is where a careless run costs real money. `seedance-2.0` averages ~$1.55 a
render; `kling-3-pro-image2video` ~$1.47. Shortlist with `list_models`, then
**`compare_models` on the shortlist** — the listing's `average_cost` is observed
spend, not a price, and for video the spread between them is wide because
`duration`, `resolution` and `generate_audio` all move the bill.

Then say the number and get a yes:

> "Seedance 2.0 at 5s/1080p with audio is about $1.60 and usually takes a few
> minutes. Want me to run it?"

**Worked example of why the listing row is not enough.** A measured
`seedance-1.5-pro` run at 5s/720p with `generate_audio: true` billed **$0.261**
against a listing `average_cost` of **$0.1195** — 2.2x. Nothing was broken: the
row's `price_drivers` said `["generate_audio"]`, and `compare_models` gives the
reason outright:

| Token Type | Price |
| --- | --- |
| Output tokens (without audio) | $1.2 per million tokens |
| Output tokens (with audio) | $2.4 per million tokens |

Audio doubles the rate, and `average_cost` blends in every audio-off run ever
made. Read `price_drivers`, then read the `pricing` table **at the settings the
user actually wants** — never quote the average.

Check `get_account()` first if nothing has been run this session — it also
names whether a personal or a team balance is about to pay.

### 2. Choose from what the user actually has

| Starting from | Category | Reasonable defaults |
|---|---|---|
| A prompt only | `textToVideo` | `kling-o3-text2video`, `wan2.7-t2v`, `minimax-h3-text-to-video` |
| One still image | `imageToVideo` | `seedance-1.5-pro` (cheap, ~$0.14), `wan-2.2-i2v-fast` (~$0.17, ~40s), `seedance-2.0` (premium) |
| Reference images of a character/product | `imageToVideo` | `wan2.7-r2v`, `grok-imagine-video-1.5-reference-to-video`, `minimax-h3-reference-to-video` |
| An existing clip to change | `videoToVideo` | `wan2.7-videoedit`, `kling-o3-video2video-edit`, `veed-subtitles`, `bria-erase-video` |
| A photo that should talk | `imageToVideo` | `veed-fabric-1.0`, `heygen-avatar-iv`, `p-video-avatar` |

`seedance-1.5-pro` is the value default for image-to-video: ~$0.14 and ~80s
against ~$1.55 and ~200s for `seedance-2.0`. Reach for the premium tier when the
user asks for multi-shot narrative, 30-second length, or 1080p+ with audio — not
by default.

### 3. Submit, then poll on the hint

```
submit_inference(slug="seedance-1.5-pro", params={...})
→ request_id, poll_after_seconds
```

Wait `poll_after_seconds`, then `check_inference(request_id)`. Repeat while the
result is `pending`. The hint is derived from the model's observed latency —
honour it. Polling a 200-second model every 5 seconds is forty pointless calls
and it does not make the render finish sooner.

**Never quote the catalog's `latency` as an ETA.** It is a long-run average, not
a bound on one render — a `seedance-1.5-pro` job with an advertised `latency` of
71.6s was measured still `PROCESSING` past ten minutes when the provider was
backed up. Tell the user a range and that it can run several times longer under
load ("usually a couple of minutes, sometimes much more"), then keep polling. A
job that has not reached a terminal state has not failed.

If a job is still running after ~15 minutes, say so and hand the user the
`request_id` rather than polling in silence — the result stays collectable with
`check_inference` for about an hour, so they can walk away and come back.

If a poll errors transiently, poll again — the job is still running. Results stay
available for about an hour after they finish.

### 4. Get the video parameters right

Read `get_model_spec(slug)` and set explicitly, every time:

- **`duration`** — costs scale with it; do not let a default of 5s stand when the
  user asked for 10.
- **`aspect_ratio`** — `9:16` for Reels/TikTok/Shorts, `16:9` for YouTube and
  landscape ads, `1:1` for feed. Video models do **not** infer this from the
  input image; an unset ratio is how a vertical ad comes back letterboxed.
- **`resolution`** — 720p unless the user needs 1080p. It is a price driver.
- **`generate_audio`** — on for ads and narrative, off when the clip will be cut
  under an existing track. On some models audio is free; on others it is a price
  driver. `compare_models` says which.
- **First frame** — the image input. **Its parameter name is different on every
  model**, so read the spec and never carry a name over from another model:

  | Model | Image parameter |
  |---|---|
  | `seedance-1.5-pro`, `seedance-2.x` | `first_frame_url` (+ optional `last_frame_url`) |
  | `wan-2.2-i2v-fast`, `wan2.7-i2v` | `image` |
  | `veed-fabric-1.0` | `image_url` |
  | `kling-3-pro-image2video` | `start_image_url` (**required**; `end_image_url` sets the last frame, `elements` is a separate array of reference subjects) |
  | Reference-to-video models | `reference_images` (an array) |

  Guessing the wrong name does not error — the model silently renders
  text-to-video and ignores the image, and the user is billed for a clip that
  has nothing to do with their photo. The value must be a URL: a still from
  `segmind-generate-image` already has one, and a file on the user's disk gets
  one from `upload_media` (contract rule 4) — upload it rather than asking them
  for a link.

### 5. Deliver

Hand back the `https://images.segmind.com/...` URL and the `cost` from
`metrics`. One clip, one URL — do not promise a stitched edit the plugin cannot
produce.

## Rules

1. **`submit_inference` for every video model. No exceptions.**
2. **Price before you spend**, and confirm anything over $0.50. Six silent
   renders at $1.58 is a $9 bill the user did not agree to.
3. **Never resubmit a `pending` job.** It is running and it is billed. Poll it.
4. **One clip first.** Get the look approved on a single short render before
   spending on length, resolution, or a set.
5. **Pass `aspect_ratio` explicitly**, every call.
6. **Assembly is a separate Segmind model, not a local tool.** Trimming,
   concatenating, reformatting and captioning generated clips is
   `segmind-video-edit` (`video-editor-agent`, `veed-subtitles`) — never a local
   ffmpeg and never a non-Segmind service.
