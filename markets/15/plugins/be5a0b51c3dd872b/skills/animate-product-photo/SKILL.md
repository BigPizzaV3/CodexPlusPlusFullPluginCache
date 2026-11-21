---
name: animate-product-photo
description: Create short product-motion clips from supplied product photos with RunComfy, including gentle push-ins or restrained scene motion. Use for requested product animation; does not guarantee exact SKU details, unseen geometry, true 360-degree views or seamless loops.
---

# Animate a product photo

Generate the requested clip from the user's actual product photo through this plugin's MCP tools. Respond in the user's language. This skill needs no CLI, other plugin skill or assumed uploader.

Use only this plugin’s current host-provided tool definitions: actual names, descriptions, typed outer arguments and allowed model scope. If current definitions cannot be verified, report an unverified connection binding, not that RunComfy lacks the product capability. If verified definitions offer no compatible operation, explain the connection-specific limitation before spending. Do not assume a discovery tool, switch endpoints, invent operations or bypass the connection through workflow/deployment execution.

## Source product and motion brief

Build a still-to-motion brief around the supplied product image: camera movement, any explicitly requested product movement, scene movement, ending goal and supported duration. Keep the product checklist attached to that clip. The deliverable is the requested animation and observed temporal/product drift, not a newly invented product scene or reconstructed hidden geometry.

Identify the actual source reference and, where supplied, its intended SKU/variant, color, label/logo/text, silhouette, proportions, material and important parts. A generated or illustrative source is a visual reference, not proof that a physical product or genuine SKU exists. A SKU name alone is not evidence of an unseen product's appearance. Resolve conflicting product references instead of blending them or substituting a generic item.

Use the requested camera move, scene motion, duration, aspect ratio and clip count. For a restrained product-stability brief, favor a motion description matching that request, such as a gentle push-in with the product stationary. Do not add a spin, lid opening, new label or physically different product action that the user did not request.

Preservation is a goal to inspect, not a guarantee. Motion models can warp edges, change labels or color and invent unseen surfaces. Do not certify catalog accuracy, exact logo text, measured geometry or identity throughout every frame. A single photo does not provide a true 3D model: explain the limitation before a requested exact 360-degree product rotation, rather than promising a faithful view of hidden sides. Do not guarantee seamless loops or an exact first/last-frame match.

## Reachable file and exposed operation

Confirm that the starting product reference is a still image. A product video or audio URL is not a valid substitute for the required image input. If the user supplied only a clip, request a still or use frame extraction only through an actually available, user-authorized feature; these MCP tools do not provide frame extraction. Any optional sound/reference input must be supported by the chosen model and cannot replace the starting product image.

For reference media, use externally fetchable HTTPS URLs that an unauthenticated GET can retrieve. When the host supplies such a URL for the user’s attachment and access is authorized for this task, use it directly; do not request another upload. Local paths, `file://`, internal attachment/sandbox IDs and data URIs cannot be passed to the Model API. Without a usable URL, explain the limit and request a direct link or a genuinely available, authorized host upload. These MCP tools do not upload arbitrary media: do not invent hosting, publish private media without permission, embed account credentials in URLs or repurpose training uploads.

1. Select a currently exposed image-to-video operation and supported model that fit the supplied still and complete motion brief. Use `generate_video` when the current host exposes a compatible definition, following its actual arguments and allowed model scope. The legacy `generate_seedance_pro_fast_video` / `bytedance/seedance-1.0/pro-fast/image-to-video` route is only an option if currently exposed and suitable; it does not define the current model range or edit existing clips.
2. Inspect the matched operation and model schemas for the starting image, prompt, duration, resolution/framing, audio and any requested additional references or end frame. Use an exposed `get_model` operation when available to read details and pricing for the exact selected model supported by the matched operation. Validate the current outer tool schema and that model’s input schema together; model metadata cannot expand the operation’s allowed scope. A fixed-model operation cannot be retargeted by adding another model ID.
3. Map the product checklist and motion brief to the operation without dropping essential inputs. If a required model, format, duration or reference capability is missing, explain the unavailable capability and stop unless the user accepts a supported changed scope. Other operations must be genuinely exposed and schema-compatible.

Audio controls must come from the actual schema. Do not automatically add `generate_audio` or `audio_url`, invent narration, claim a supplied soundtrack is preserved, or promise silence without a supported control. Ask about sound only when the missing choice materially affects the requested clip or cost.

## Paid scope and request ledger

Explain the requested output/job count and available `base_price_usd`/`price_unit` estimate, including duration/resolution/audio-dependent uncertainty. `get_balance()` is available when relevant to a funds question/error and returns `balance.balance_usd` and `balance.balance_microdollars`.

Use only the connected account’s existing balance or entitlement. Authenticate through this plugin’s OAuth connection flow, never by collecting credentials in chat. If balance or entitlement is insufficient, explain why the task cannot run and stop; do not initiate or link to purchases, top-ups, subscriptions or upgrades.

Continue under existing authorization for the exact clip/batch and budget. If the user asked to wait for approval or the paid scope is unresolved, obtain the missing authorization first. Do not reconfirm every clip in an approved batch, introduce extra motion alternatives or change to a costlier scope without authorization.

Invoke the matched, actually exposed video operation once per approved job using declared typed arguments. Use asynchronous submission only if supported and save the actual returned request ID (`submission.request_id` when provided) with the product and motion brief. An acknowledgment does not establish video completion.

Use `get_model_request_status(request_id=...)` then `get_model_request_result(request_id=...)` for each ID. Do not use Serverless deployment status/result tools. Poll with pauses, at most 12 checks and about 2 minutes total per active turn; stop on terminal states and retain pending IDs for later recovery. Describe partial results separately.

Timeouts and imperfect frames do not authorize an automatic new charged job. Poll a known ID. Without an ID after a lost acknowledgment, stop and reconcile generation history with the user before any replacement; these tools cannot discover a lost request ID. Do not cancel unrelated jobs, fabricate outputs or hide failure/credit/authentication issues.

## Product-motion check and delivery

Show only actual video assets from `output_urls` or the model-defined result, preserving signed URLs. Where video/frame inspection is available, compare the source product with the beginning, motion interval and ending: intended SKU/variant, color, label/logo/text, silhouette/proportions, cap/handle/other parts, stationary-product goal and requested camera movement. Report visible drift, label blur or inconclusive checks. Sampled frames do not prove exact stability throughout the entire video; do not call an uninspected clip verified or publication-ready.

Known supporting-test observation: Seedance 2.5 image-to-video 720p returned nonzero AAC audio in five Model API tests despite `generate_audio=false`. This is an observed limitation, not a claim about all models or a confirmed root cause. Disclose it before spending when silence is requested; do not guarantee that this route will be silent. If silence is essential, stop unless the user accepts a supported changed scope. Do not claim an audio-removal tool exists here.

## Result presentation

Keep each real request ID paired with its own returned output. Prefer native video presentation when supported; otherwise provide one Markdown link labeled Open original video, copied exactly from that request's output URL. Preserve signed URLs, do not reconstruct path segments, add tracking parameters to media URLs, substitute another result, or download/rehost media to bypass display restrictions. State when inline playback or audiovisual inspection is unavailable. Keep the active RunComfy task and its approved scope on follow-up approvals; do not switch generators or start an unapproved replacement.

## Model details

Link to model details only when the user needs help selecting or understanding a model; do not append links automatically or use them to direct credit purchases or upgrades.

- [RunComfy model catalog](https://www.runcomfy.com/models/all?utm_source=chatgpt&utm_medium=plugin&utm_campaign=runcomfy-plugin&utm_content=image-to-video--skill)

A useful tool-returned `model_url` may receive the same catalog attribution parameters only after verifying its RunComfy website destination. Leave API URLs and signed media URLs unchanged.
