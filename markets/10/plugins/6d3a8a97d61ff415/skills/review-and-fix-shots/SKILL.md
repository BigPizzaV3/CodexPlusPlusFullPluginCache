---
name: review-and-fix-shots
description: Check a PulseJet AI project's generation progress, find shots that failed or look wrong, and fix them with the least spend, then recompile.
---

1. **Read the real state first.** `get_project` for the pipeline state, then `get_generation_progress` for per-shot status, and `get_shots` (use `summary: true` on large projects) for the detail. Report only what came back.
   When the customer asks to see a shot, call `get_shot_image` with its project and shot ids. That result displays the still and clip separately when available. A `video/mp4` URL is a video clip, not an image: do not place it in image Markdown. If the host does not show the media card, offer the separately labelled still and clip links, and do not claim the pixels or player appeared unless visible.
2. **Failed shots.** For a shot stuck in a failed state, `render_shot` re-renders it (`regenerateImage: true` also redoes the still). If it fails permanently and the customer wants to move on, `skip_shot` excludes it so the video can still compile.
3. **Wrong-looking shots.** Edit the prompt with `update_shot` (imagePrompt, negativePrompt, motionDescription) and re-render, or generate an alternative with `generate_image_candidate` and let the customer choose via `accept_image_candidate` / `reject_image_candidate`. Video alternatives use `accept_video_candidate` / `reject_video_candidate`.
4. **Use the customer's own material.** `change_shot_source` to `user_image` or `user_video`, then `upload_shot_image` or `upload_shot_video` through the presigned flow (`filename` + `contentType`, PUT to `uploadUrl`, finish with `stagingKey`). Stills must match the project's aspect ratio exactly.
5. **Order and structure.** `reorder_shots` with every shot id in the new order; `delete_shot` to remove one.
6. **Finish.** `compile_video` once every shot is rendered or skipped, then `get_project` for the download link.

Any re-render, regenerate or candidate step spends credits (compiling does not): check `get_credit_balance`, say what it costs, and get an explicit yes first. Prefer fixing one shot over re-rendering everything; `render_all_pending_videos` is the expensive path and needs its own confirmation.

## Reporting a problem

A shot that fails again after one re-render, a result the customer calls wrong, or anything in this flow that seems broken is worth reporting. If it is not clear the customer wants it passed on, offer in one sentence; read back a one-sentence summary and file it with `submit_feedback` once they agree, with their own words in `message`, the project id, the `shotId` concerned and the `errorCode` the failing call returned. Quote the ticket key from the result back to them.

If a fix is not working out, say that the problem can be reported from this conversation with `submit_feedback`; the customer does not have to go looking for a form.
