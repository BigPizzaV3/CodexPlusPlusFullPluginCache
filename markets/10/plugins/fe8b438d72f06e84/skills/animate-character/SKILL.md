---
name: animate-character
description: Animate a character image with the motion from a reference video using RTST (rtst.ai) motion transfer — make a person, mascot or illustration perform a dance, gesture or movement taken from another clip. Use when the user wants their character or photo to copy the moves in a video, and when an RTST card button picks a motion reference video or asks for another motion transfer.
---

# Motion transfer with RTST

Tools: `motion_transfer`, `estimate_cost`, `list_videos`, `job_status`.

1. **The model is fixed.** `motion_transfer` always runs RTST's Wan motion-transfer
   model. Never ask the user to pick a motion model and never list models for this.
2. **Character image** — a hosted https URL. Use `use-my-media` for the user's own
   photo (a new request opens the uploader again; reuse an earlier upload only if the
   user points to it), or an image they pick from their library (`list_images`).
3. **The motion.** Either:
   - `reference_video_url`: a hosted https video the **user** chose: one of their RTST
     videos or a public https video URL. If they have not said which, show their videos
     with `list_videos` and **wait**: in ChatGPT they pick one with the card's **Use this
     motion** button. Never choose a reference video yourself. Videos cannot be uploaded
     through this plugin; `media_upload` and `media_import_url` take images only.
   - `template_id`: only if the user already has an RTST motion template id.
4. **Mode.** Leave `mode` out (standard). Send `"pro"` only if the user asks for higher
   quality.
5. **Quote.** Call `estimate_cost` with `type: "motion"` and the reference clip's
   `duration` in seconds if you know it; otherwise give the per-second rate. Tell the
   user it is an estimate, and get a yes before submitting.
6. **Submit** with `motion_transfer`, once. In ChatGPT the card follows the job: do not
   call `job_status`. Elsewhere call `job_status` with `kind: "motion"` and
   `sync: true`, and report the result URL when it finishes.
7. Finished transfers are listed by `list_videos` with `kind: "motion"`.

## Messages sent by RTST card buttons

- "Use this video as the motion reference for my rtst.ai motion transfer: …" → that URL
  as `reference_video_url`. If there is no character image yet, get one with
  `use-my-media`; then quote and wait for a yes.
- "Make another motion transfer like this one with rtst.ai: …" → same inputs and model,
  or the change the user asks for; quote again.
