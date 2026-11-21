# Product video workflow

## Brief and scope

Choose promotion, UGC or close-up based on the requested deliverable. Capture the product, supported benefit, audience, duration, ratio, copy language and exact CTA where applicable. Preserve the user's references and required style. Identify the role of each attachment: product appearance, style reference, presenter reference or motion reference.

If only planning is requested, produce the requested concept, script or shot plan in the conversation using supplied facts, with no generation calls. For an actual production request with a complete brief, proceed without another mandatory planning approval. If critical inputs are missing, ask a concise question; do not run a second extensive interview alongside the Designkit agent.

## Submit and follow the real task

`designkit_create_task` is the unified image and video generation entrypoint. Use it for requested video production rather than looking for a separately named video generator or exporter. `designkit_get_profile` contains identity only and cannot establish the supported media types. Account or generation failures are operational failures, not evidence that Designkit lacks video capability.

Use `designkit_prepare_upload` only for actual accessible local media that can be uploaded through the host. Follow its returned upload contract. Never claim an unuploaded chat attachment reached the server. Pass confirmed public media URLs to `designkit_create_task` with their true `media_type`. A text-to-video fictional concept can have no attachments when the server accepts that workflow.

Put the requested preset, product facts, narrative, shots, duration, ratio, language, audio requirements and references into the ordinary task `message`. Use only live-schema arguments and a unique idempotency key. The existing MCP has no dedicated video-model selector or standalone voice-cloning tool. Do not invent those fields or promise unsupported editing operations.

Save the actual room and task IDs. Poll `designkit_get_artifacts` with the returned incremental sequence. Answer returned questions with `designkit_answer_task` using trusted request/card context. Preserve user choices already supplied, but do not guess option IDs. For revisions to this video, use `designkit_update_task` in the same room and identify the desired change.

## Completion and delivery

Inspect both task state and returned media. A script, storyboard image, cover, or queued task is not a completed video. For a video artifact, retain the actual media URL, MIME type or format, title and cover when returned. Share user-openable playback and download links supported by the host. Do not send an MP4 URL to `designkit_show_images`; use that tool only for actual image artifacts such as a returned storyboard or cover.

Open the returned video using an available host-supported player to check playback when possible. Confirm a download only after an actual file is obtained, and describe unverified playback/download honestly when the host cannot perform it. Do not invent duration, resolution, sound, presenter identity or product continuity from a thumbnail.

Use only a cover returned for that artifact as its preview. If none is available, provide the actual video link without a replacement thumbnail; do not search for or display stock imagery as the generated result. Requested duration and a script's shot timings are not measurements of the completed file. State a measured duration only when the player or file metadata supplies it; otherwise leave the duration unverified.

If login or entitlements fail, preserve the room context if any and explain the real recovery step. Do not retry creation under a new key or spend more credits to obtain a preview. If no playable video is returned, state the missing deliverable and offer the real returned material or room link. Do not claim completion or automatic notification.
