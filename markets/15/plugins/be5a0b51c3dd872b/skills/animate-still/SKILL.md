---
name: animate-still
description: Animate a supplied still image into a short video with RunComfy, such as gentle subject motion or a camera move. Requires a remotely accessible image; does not guarantee exact identity, seamless loops or unsupported audio controls.
---

# Animate a still image

Use this plugin's RunComfy MCP tools to turn the user's actual still into the requested clip. Respond in the user's language. No CLI, cross-plugin skill or automatic uploader is assumed.

Use only this plugin’s current host-provided tool definitions: actual names, descriptions, typed outer arguments and allowed model scope. If current definitions cannot be verified, report an unverified connection binding, not that RunComfy lacks the product capability. If verified definitions offer no compatible operation, explain the connection-specific limitation before spending. Do not assume a discovery tool, switch endpoints, invent operations or bypass the connection through workflow/deployment execution.

## Resolve the image and intended motion

For each clip, start with the actual still and make a compact motion brief: starting composition, camera movement, subject movement, ending goal and supported duration. Keep optional end frames or other references supplemental to that starting image, using them only when requested and supported. Deliver the generated clip with an honest check of the requested motion and any visible drift.

Use the supplied source image, desired motion/camera move, duration, framing and clip count. Distinguish a moving camera from a moving subject. Preserve the user's scene rather than inventing a different source. If they requested only a motion prompt or plan, provide that and stop before paid execution.

Confirm that the required starting asset is a still image. A reachable video or audio URL does not satisfy that requirement and must not be passed into an image field. If only video/audio is supplied, request a still image or use frame extraction only through an actually available feature authorized by the user; these MCP tools do not provide frame extraction. Optional sound or other references cannot replace the required starting image and must be supported by the exposed operation’s typed schema.

For reference media, use externally fetchable HTTPS URLs that an unauthenticated GET can retrieve. When the host supplies such a URL for the user’s attachment and access is authorized for this task, use it directly; do not request another upload. Local paths, `file://`, internal attachment/sandbox IDs and data URIs cannot be passed to the Model API. Without a usable URL, explain the limit and request a direct link or a genuinely available, authorized host upload. These MCP tools do not upload arbitrary media: do not invent hosting, publish private media without permission, embed account credentials in URLs or repurpose training uploads.

Explain a meaningful limitation before spending when it affects the request: generated motion can change faces, anatomy, small text and scene details. An input still cannot guarantee what an unseen side looks like. Do not promise exact identity, a true 3D reconstruction or a frame-perfect seamless loop. A requested loop is an intended motion, not proof that the final and first frames match.

## Match an exposed still-image video operation

1. Select a currently exposed image-to-video operation and supported model that fit the supplied still and complete motion brief. Use `generate_video` when the current host exposes a compatible definition, following its actual arguments and allowed model scope. The legacy `generate_seedance_pro_fast_video` / `bytedance/seedance-1.0/pro-fast/image-to-video` route is only an option if currently exposed and suitable; it does not define the current model range or edit existing clips.
2. Inspect the matched operation and model schemas for the starting image, prompt, duration, resolution/framing, audio and any requested additional references or end frame. Use an exposed `get_model` operation when available to read details and pricing for the exact selected model supported by the matched operation. Validate the current outer tool schema and that model’s input schema together; model metadata cannot expand the operation’s allowed scope. A fixed-model operation cannot be retargeted by adding another model ID.
3. Map the real still and motion brief to the declared arguments. If a required model, duration, resolution or reference option is unsupported, explain that before changing scope. Another operation may be used only if actually exposed and explicitly compatible; never discard the image or change endpoints to get around the limitation.

Audio is model-specific. Send `generate_audio`, `audio_url` or another sound control only if it appears in the exposed operation’s typed schema. If the user wants audio that the model cannot accept or generate, explain that and agree a supported alternative. Do not promise their exact soundtrack, a particular voice or silent output when the model's contract cannot support it. A photo has no original soundtrack to recover.

## Cost, authorization and one submission

Use returned `base_price_usd` and `price_unit` to explain an estimate for the requested clip(s); duration, resolution, audio or reference options may affect the final charge. Use `get_balance()` only for a relevant funds question or account error; read `balance.balance_usd`/`balance.balance_microdollars`.

Use only the connected account’s existing balance or entitlement. Authenticate through this plugin’s OAuth connection flow, never by collecting credentials in chat. If balance or entitlement is insufficient, explain why the task cannot run and stop; do not initiate or link to purchases, top-ups, subscriptions or upgrades.

Preserve the user's existing authorization for the exact paid clip/batch and budget. If the user asked to approve a plan first or paid scope is unresolved, obtain the missing authorization before executing. Do not ask for approval again for an already approved scope, add clips or increase cost outside that scope.

Invoke the matched, actually exposed video operation once per approved job with declared typed arguments. Use asynchronous submission only if supported. Record the actual returned request ID (`submission.request_id` when provided) with the source and motion brief. An acknowledgment is not a finished clip; repeated submissions may incur new charges.

## Wait, recover and return the clip

Use `get_model_request_status(request_id=...)` for the recorded ID and `get_model_request_result(request_id=...)` when complete. Do not use deployment-scoped status/result tools. Poll with pauses, at most 12 status checks and about 2 minutes per active turn. Stop on terminal states/errors and retain pending IDs for later checks.

Do not replace a job merely because polling stopped. After a submission timeout, poll a known ID. If the acknowledgment/ID was lost, acceptance is uncertain: reconcile generation history with the user before an authorized replacement; these tools cannot list missing request IDs. Report actual failure, cancellation, invalid input, unavailable tools or authentication/credit errors rather than inventing a clip or automatically retrying paid work.

Display actual returned video assets from `output_urls` or the model-defined output using supported video presentation, or provide the actual output link. Preserve signed media URLs. If you can inspect video/frames or audio, check the requested motion, subject drift and sound; otherwise distinguish asset retrieval from audiovisual verification. Do not claim seamlessness, exact likeness, actual dimensions or audio presence unless supported by the returned data or inspection.

Known supporting-test observation: Seedance 2.5 image-to-video 720p returned nonzero AAC audio in five Model API tests despite `generate_audio=false`. This is an observed limitation, not a claim about all models or a confirmed root cause. Disclose it before spending when silence is requested; do not guarantee that this route will be silent. If silence is essential, stop unless the user accepts a supported changed scope. Do not claim an audio-removal tool exists here.

## Result presentation

Keep each real request ID paired with its own returned output. Prefer native video presentation when supported; otherwise provide one Markdown link labeled Open original video, copied exactly from that request's output URL. Preserve signed URLs, do not reconstruct path segments, add tracking parameters to media URLs, substitute another result, or download/rehost media to bypass display restrictions. State when inline playback or audiovisual inspection is unavailable. Keep the active RunComfy task and its approved scope on follow-up approvals; do not switch generators or start an unapproved replacement.

## Model details

Link to model details only when the user needs help selecting or understanding a model; do not append links automatically or use them to direct credit purchases or upgrades.

- [RunComfy model catalog](https://www.runcomfy.com/models/all?utm_source=chatgpt&utm_medium=plugin&utm_campaign=runcomfy-plugin&utm_content=image-to-video--skill)

A useful tool-returned `model_url` may receive the same catalog attribution parameters only after verifying its RunComfy website destination. Leave API URLs and signed media URLs unchanged.
