---
name: video-generation
description: Generate a Clout video from text or an owned image, or transfer a verified reference video's motion to a saved AI influencer
---

# Video generation

Use for a standalone video clip or motion transfer. Read [the shared workflow](../../references/creative-workflow.md) first. Use `lip-sync` for a supplied speech performance, `ugc-product-video` for a product promotion, `faceless-story` for narrated multi-scene stories, or `cinema-sequence` for a planned film and export.

## Text or image to video

1. Capture subject, setting, movement, camera direction, duration, framing, audio preference, and any elements that must stay stable. Make motion physically coherent and keep the number of actions suitable for the chosen duration.
2. Call `clout_list_models` with `mediaType: "video"` and select a returned available model supporting the required text/image/reference inputs, duration, audio, and format. Do not advertise unsupported controls.
3. For image-to-video, use a ready owned image returned by the asset or generation library. Preserve its exact canonical URI and owning source reference. Uploaded video/audio references must be inspected and ready before use.
4. Build the final `clout_generate_media` input, estimate with `clout_quote_generation` if needed, and generate using existing credits without an extra approval.
5. Generate using existing credits and a UUID request ID and poll `clout_get_generation`. Retry uncertain operations only with the same request ID and original input.
6. Use `clout_get_download` on completed output. Preview when supported and check continuity, requested movement, duration, aspect ratio, and visible artifacts before describing the result.

## Reference motion with an influencer

1. Select a ready owned character using `clout_list_influencers` / `clout_get_influencer`. Find a public motion template with `clout_list_motion_templates` or use a ready user-uploaded video with verified duration and metadata.
2. Run `clout_prepare_motion` for the requested review-frame step using the exact owned references. Poll `clout_get_motion_generation` and show the actual review frame.
3. When the frame is ready, use `clout_render_motion` to finish the requested video. Use the server's verified reference duration; do not infer a cheaper duration from the request.
4. Render using existing credits and poll the same motion job until complete. Do not confuse a completed review frame with a completed video.

If no model supports the requested combination, explain the concrete limit and offer supported settings. Never substitute a paid model or longer clip without the user requesting that change.

Follow the shared direct-generation policy: no extra credit-approval step. Immediately show the returned Clout job with `clout_show_generation`; never substitute native ChatGPT image generation or another provider.
