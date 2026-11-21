---
name: stage-product-scenes
description: Create requested product lifestyle or studio scenes from real product references with RunComfy. Use for reference-led product placement and scene concepts; does not guarantee unchanged SKU details, labels or physical geometry.
---

# Stage product scenes

Generate the requested scene around a supplied product, using this plugin's MCP tools. Respond in the user's language. No CLI, third-party skill or automatic media uploader is assumed.

Use only this plugin’s current host-provided tool definitions: actual names, descriptions, typed outer arguments and allowed model scope. If current definitions cannot be verified, report an unverified connection binding, not that RunComfy lacks the product capability. If verified definitions offer no compatible operation, explain the connection-specific limitation before spending. Do not assume a discovery tool, switch endpoints, invent operations or bypass the connection through workflow/deployment execution.

## Product and scene inputs

Keep a product checklist separate from the scene brief: product features to retain, surface/setting, placement, lighting and framing. Use a requested sales channel or placement only to inform supported composition and dimensions; do not claim marketplace approval. Return the requested scene with observed product/detail drift and unresolved checks.

Identify the actual product reference, intended SKU/variant/color, visible material, label/logo, shape and important parts. Ask the user to resolve conflicting references instead of blending different SKUs. If a second image is a scene/style reference, state that role and preserve reference order; do not treat every image as the same object.

Use the requested setting, surface, lighting, framing and count. A named product with no photo is insufficient to promise an accurate depiction: request an appropriate reference or offer a clearly described generic concept if the user accepts it. Never silently substitute stock-looking packaging for their real item.

Describe product preservation as an aim. Generative placement can change silhouette, dimensions, label text and color, and can invent unseen surfaces. Do not promise a measured scale rendering, exact logo reproduction, guaranteed catalog accuracy, or a true 3D/360-degree reconstruction from one image. Resolve exact-preservation requirements before spending.

## References and model choice

For reference media, use externally fetchable HTTPS URLs that an unauthenticated GET can retrieve. When the host supplies such a URL for the user’s attachment and access is authorized for this task, use it directly; do not request another upload. Local paths, `file://`, internal attachment/sandbox IDs and data URIs cannot be passed to the Model API. Without a usable URL, explain the limit and request a direct link or a genuinely available, authorized host upload. These MCP tools do not upload arbitrary media: do not invent hosting, publish private media without permission, embed account credentials in URLs or repurpose training uploads.

Before a paid call, confirm each reference is a supported still image from reliable supplied metadata or an available inspection feature. A known HTML/login/model page, video or audio URL is not an image input merely because it is HTTPS or returns 200. If the media type is inaccessible or ambiguous, resolve it or request a direct supported image URL before a paid generation; do not claim a check you could not perform or invent an upload/conversion.

1. Select a currently exposed image operation that supports the actual source/reference images and requested edit or composition. Use `generate_image` when the current host exposes a compatible definition, following its actual declared arguments and allowed model scope. A text-only operation cannot substitute for a required reference input.
2. Inspect the matched operation and supported model schemas for image fields, reference count/order, dimensions, output controls and any requested mask or style controls. Use an exposed `get_model` operation when available to read details and pricing for the exact selected model supported by the matched operation. Validate the current outer tool schema and that model’s input schema together; model metadata cannot expand the operation’s allowed scope. A fixed-model operation cannot be retargeted by adding another model ID.
3. Build only that exposed operation’s declared arguments from the actual product reference, scene brief and any required background/style reference. Do not drop an essential reference, invent an input property or substitute text-only generation. Explain a missing control before considering a different user-authorized scope.

## Scope, cost and execution

Explain the output/request count and the available `base_price_usd`/`price_unit` estimate; do not present a base price as a guaranteed complete cost for all settings. `get_balance()` is available for a relevant funds question/error and returns `balance.balance_usd` and `balance.balance_microdollars`.

Use only the connected account’s existing balance or entitlement. Authenticate through this plugin’s OAuth connection flow, never by collecting credentials in chat. If balance or entitlement is insufficient, explain why the task cannot run and stop; do not initiate or link to purchases, top-ups, subscriptions or upgrades.

Use the user's existing authorization for this exact scene/batch and budget. If they asked to see a plan or paid scope is unresolved, obtain the missing authorization first. Do not reconfirm each scene in a batch already approved, introduce extra paid scenes or change the model beyond the agreed scope.

Only when a matching reference-capable image operation is exposed, invoke it once per approved job using declared typed arguments, recording the actual returned request ID (`submission.request_id` when provided) with its product and scene. Use asynchronous or multi-output controls only when exposed and matching the approved plan. An acknowledgment is not a completed picture.

Track each ID with `get_model_request_status` and fetch completion with `get_model_request_result`, both using `request_id`. Never mix these with deployment-scoped status/result tools. Poll with pauses, at most 12 checks and about 2 minutes total per active turn. Keep pending IDs for later checks and distinguish partial completion.

Timeouts do not authorize replacement generations. Poll a known ID; if the acknowledgment/ID was lost, stop and reconcile generation history with the user because these tools cannot discover missing IDs. Do not automatically retry, cancel other work or fabricate assets after failures. Explain actual authentication, credit, model or input errors without asking for secrets in chat.

## Deliver and check

Return only actual assets from `output_urls` or the model-defined result; preserve signed URLs. If images can be inspected, compare the intended SKU/variant, color, label/logo/text, proportions and components with the reference, then check the requested scene, contact shadow and plausible placement. Report observed drift or an inconclusive check; do not certify unseen details or claim a visual check from a URL alone. Keep a generated product-scene concept distinct from an accurately verified catalog photograph.

## Result presentation

Keep each request ID paired with its own actual returned output asset. Use a native displayable attachment if the tool returns one; otherwise provide one Markdown link labeled Open original image, copied directly from that request's output URL. Do not rebuild path segments, repeat a second transcription, add tracking parameters to media URLs, or substitute results from another request. Do not use image search, HTML widgets, downloading or rehosting to bypass host display restrictions. When inline display is unavailable, say so and return the original link. Keep the active RunComfy task and its approved scope on follow-up confirmations; do not switch to another image generator or silently start a new job.

## Model details

Link to model details only when the user needs help selecting or understanding a model; do not append links automatically or use them to direct credit purchases or upgrades.

- [RunComfy model catalog](https://www.runcomfy.com/models/all?utm_source=chatgpt&utm_medium=plugin&utm_campaign=runcomfy-plugin&utm_content=product-photography--skill)

A useful tool-returned `model_url` may receive the same catalog attribution parameters only after verifying its RunComfy website destination. Leave API URLs and signed media URLs unchanged.
