---
name: create-video
description: Create videos with RTST (rtst.ai) on the user's account — text-to-video, animating an image (first/last frame), reference images and optional audio, on any RTST video model, always quoting the credit cost first. Use when the user asks RTST to make, animate or remix a video or clip, and when an RTST card button asks to animate an image, make another take, a longer or higher-resolution version, a remix, or to use a video model.
---

# Create a video with RTST

Tools: `get_model`, `list_models`, `estimate_cost`, `generate_video`, `job_status`,
`enhance_prompt`, `balance`. Bringing in the user's own image is the `use-my-media` skill.

1. **Pick the model.** If the user named one, call `get_model` with their wording
   (`type: "video"`) and use the exact `name` it returns. Otherwise choose one yourself
   from `list_models` (`type: "video"`, no card) by `description`, and tell the user
   which model you picked and why. Call `show_models` only if they ask to see the
   models. Never invent one.
2. **Take every setting from that model's entry.** `aspect_ratio` and `duration` from its
   lists (most models require both); `resolution` from `resolutions`; `audio: true` only
   if `is_audio_supported`; images only if `is_image_supported`, and a `last_frame` only
   if `supported_frames` allows it.
3. **Write the prompt** — at least 10 words, describing subject, motion, camera move,
   setting and mood. If it is shorter, offer `enhance_prompt` and show the result.
4. **Images in** (hosted https URLs, from `use-my-media`):
   - Animate an image: `first_frame` (and optionally `last_frame`).
   - Subject, style or scene references: `reference_images`, cited in the prompt as
     `{{img1}}`, `{{img2}}`… in array order.
   - Seedance 2.x takes frames **or** references in one job, never both.
5. **Always quote first.** Video always costs credits. Only the `estimate_cost` number may
   be quoted: `credits_per_second` is a base rate that resolution and audio change either
   way (480p can cost less than half of 1080p), and Seedance 2.x has no rate at all
   (`pricing`, token-priced). Never work a price out from a rate. Call `estimate_cost` with
   `type: "video"` and the same arguments you will generate with. Tell the user the
   credits and the settings you chose (duration, aspect ratio, resolution, audio), then
   **stop and wait**: submit only after the user says to go ahead, or changes a setting
   (quote again). If `can_afford` is false, do not submit: show `balance` and point to
   https://rtst.ai/pricing.
6. **Generate** with `generate_video`, once, after the go-ahead. The video is private to the user's library;
   send `private: false` only if the user asks to publish it.
7. **Follow the job.** Videos take about 1–3 minutes. In ChatGPT the card follows the
   job and plays the video when it is done: do not call `job_status`, just tell the user
   it is rendering. Elsewhere call `job_status` with `kind: "video"` and `sync: true`,
   and again when asked or after `poll_after_seconds`. Never resubmit a running job.
8. **Reply.** With a card, do not repeat URLs; summarize model, length and cost and
   offer a next step. Without one (Codex, Claude Code), give the video URL and `web_url`.

If a job is refused for safety, say so and suggest a different prompt; do not switch
models to get around a safety filter.

## Messages sent by RTST card buttons

- "Animate this image into a short video with rtst.ai: …" → that URL as `first_frame`.
- "Generate another take of that video with rtst.ai, same prompt, different seed/motion."
  → same model, prompt and settings; quote again.
- "Make a longer or higher-resolution version of that video with rtst.ai — estimate the
  cost first." → a longer `duration` or higher `resolution` the model offers; quote it.
- "Make another video like this one with rtst.ai: …" → reuse that prompt, then quote.
- "Use the … (…) video model on rtst.ai for my next video — estimate the cost first."
  → `get_model` for its settings, then quote.
- "Check the status of my rtst.ai … job …" (the card could not refresh itself) →
  `job_status` with that id and kind, then report the result with its URL: no card
  shows it.
