---
name: ai-video-generation
description: Generate AI videos with EzUGC catalog models (Veo, Kling, Runway, MiniMax, LTX, Seedance, and more). Use when the user wants text-to-video, image-to-video, a specific model, or "generate a video". Talking-head UGC ads use the ugc-generation skill instead.
---

# AI Video Generation

Generate cinematic, product, or b-roll videos with EzUGC's catalog models through this plugin's MCP tools.

The plugin is already connected through OAuth. Call `whoami`, then `get_usage`, before generating. If `whoami` fails, tell the user to reconnect the EzUGC plugin. Never use app cookies or a browser session.

Never mention USD, provider cost, or credit-to-dollar rates. Quota is remaining videos this billing cycle (`get_usage`).

## Quick start

1. Call `whoami`, then `get_usage`. Stop on auth failure.
2. Call `list_video_models`. Use a model with `available: true` and a duration from its `durations`. Do not invent an id.
3. Call `generate_video`. Prefer `wait: true`.
4. Report the real video URL from the job. If the job is still running, give the job id and poll `get_job`. Never invent a result.

Example:

```json
{
  "prompt": "Handheld vertical clip of a skincare bottle catching window light on a bathroom counter",
  "model": "google:3@3",
  "duration": 8,
  "aspectRatio": "9:16"
}
```

## Tool

Call **`generate_video`**.

| Arg | Required | Notes |
| --- | --- | --- |
| `prompt` | yes for text-to-video | Concrete visual brief. |
| `model` | no | Id from `list_video_models`. Omit to use the default. |
| `imageUrls` | no | Public https images for image-to-video: a start frame and an optional end frame. |
| `referenceImageUrls` / `referenceVideoUrls` / `referenceAudioUrls` | no | Only on models that accept references (Seedance 2.0 / 2.5, MiniMax H3). Cannot be combined with `imageUrls`. |
| `duration` | no | Seconds; snapped to the nearest option the model supports. |
| `aspectRatio` | no | `9:16`, `16:9`, or `1:1`. |
| `resolution` | no | Explicit size like `1280x720`. |
| `generateAudio` | no | Only if the chosen model supports audio. |
| brand refs | no | `brandId` / `brandSlug` / `useDefaultBrand`. |
| `wait` | no | Default true. |

## Picking a model

Call `list_video_models` and map the user's ask onto a live id. Common ids (verify they are still `available: true`):

- Veo 3.1: `google:3@2` · Veo 3.1 Fast: `google:3@3` (8s)
- Kling 2.5 Turbo Pro: `klingai:6@1` · Runway Gen-4.5: `runway:1@2`
- MiniMax H3: `minimax:h3@0` · LTX 2.3 Fast: `lightricks:ltx@2.3-fast`

Seedance models count against the plan's separate Seedance allowance. If the response carries a `notice` (for example, a retired model routed to its replacement), tell the user. Lip-sync, avatar, and OmniHuman models are not on this API.

## Format

- **Cinematic / product / b-roll / animation**: this skill (`generate_video`).
- **Spokesperson talking to camera (UGC ad)**: `ugc-generation` (`generate_ugc_video`).

If the brief is ambiguous, ask once, then generate.

## On-brand clips

If they want it for a saved brand: `list_brands`, then `create_brand { websiteUrl }` if needed, then pass `useDefaultBrand: true` (or `generate_brand_video` for a talking-head UGC ad).

## Hard rules

- Never invent a job or video URL.
- Only request models returned as `available: true`.
- Do not dump provider names, task ids, or raw upstream errors to the user.
- Do not post videos to Instagram, TikTok, or other public platforms.
