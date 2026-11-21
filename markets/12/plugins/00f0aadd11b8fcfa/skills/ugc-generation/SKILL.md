---
name: ugc-generation
description: Create AI UGC video ads with EzUGC, meaning talking-head creator ads with script, avatar, voiceover, and captions. Use when the user wants UGC, a UGC ad, a TikTok/Reels product review, or "create a UGC video". Cinematic or silent product clips use ai-video-generation instead.
---

# UGC Generation

Use this skill when the user wants an **AI UGC ad**: a creator talking to camera about a product, with a script, avatar, voiceover, and captions.

The plugin is already connected through OAuth. Call `whoami`, then `get_usage`, before generating. If `whoami` fails, tell the user to reconnect the EzUGC plugin. Never use app cookies or a browser session.

Never mention USD, provider cost, or credit-to-dollar rates. Quota is remaining videos this billing cycle (`get_usage`).

## Quick start

1. Call `whoami`, then `get_usage`. Stop on auth failure. Report remaining videos this cycle.
2. Call `generate_ugc_video`. Prefer `wait: true`.
3. Report the real video URL from the job. A UGC render takes a few minutes; if the job is still running, give the job id and poll `get_job` until it completes. Never invent a result.

Example:

```json
{
  "prompt": "15s Reels ad for a vitamin C serum. Hook on dull skin, show the bottle, end on a shop-now CTA.",
  "platform": "instagram_reels",
  "duration": 15,
  "aspectRatio": "9:16"
}
```

## Tool

Call **`generate_ugc_video`**.

| Arg | Required | Notes |
| --- | --- | --- |
| `prompt` | yes | Creative brief (product, audience, hook, CTA). |
| `script` | no | Exact spoken words. Omit to auto-write the script. |
| `productImageUrls` | no | Public https product photos. |
| `platform` | no | e.g. `instagram_reels`, `tiktok`, `youtube_shorts`. |
| `duration` | no | Target seconds. Keep spoken pacing around 2.5 words per second if a script is supplied. |
| `aspectRatio` | no | `9:16` (default for UGC), `16:9`, `1:1`. |
| brand refs | no | `brandId` / `brandSlug` / `useDefaultBrand`. |
| `wait` | no | Default true. |

If they want it on-brand and have a website: `list_brands`, then `create_brand` if needed, then pass `useDefaultBrand: true` (or `generate_brand_video`).

## Ambiguous briefs

If they might mean a silent product clip instead of a talking-head UGC ad, ask once.

- Talking-head UGC ad: this skill.
- Cinematic / b-roll / named model (Veo, Kling, Runway): `ai-video-generation`.

## Script guidance

- Keep spoken pacing around 2.5 words per second unless they ask otherwise.
- If the requested runtime and script length conflict, flag it before sending the job.
- Keep prompts concrete: product, audience, hook, proof, CTA.

## Hard rules

- Never invent a job or video URL.
- Do not dump provider names, task ids, or raw upstream errors to the user.
- Write **Nano Banana** with a space if an image step comes up.
- Do not post videos to Instagram, TikTok, or other public platforms.
