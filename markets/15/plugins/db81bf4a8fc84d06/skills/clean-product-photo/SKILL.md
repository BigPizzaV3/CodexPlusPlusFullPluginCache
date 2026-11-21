---
name: clean-product-photo
description: Improve a user-supplied product photo with RunComfy, such as a cleaner studio background, lighting or minor visual cleanup. Requires an accessible source photo; does not provide exact product preservation or transparent cutouts.
---

# Clean a product photo

Use this plugin's RunComfy MCP tools to make the requested edit to the actual supplied product image. Respond in the user's language. This skill requires no CLI, external skill or assumed uploader.

Use only this plugin’s current host-provided tool definitions: actual names, descriptions, typed outer arguments and allowed model scope. If current definitions cannot be verified, report an unverified connection binding, not that RunComfy lacks the product capability. If verified definitions offer no compatible operation, explain the connection-specific limitation before spending. Do not assume a discovery tool, switch endpoints, invent operations or bypass the connection through workflow/deployment execution.

## Establish the product and permitted change

Record a short product checklist from the supplied image, then use the requested destination—such as a listing hero, catalog card or ad—to choose supported framing and dimensions. Do not infer marketplace requirements or certify compliance. The deliverable is the requested cleanup plus a source-to-result check of product details and any verifiable output format.

Use the supplied product/SKU reference to record the intended item, variant/color, material, visible label/logo/text, silhouette and important components. A filename or SKU string alone does not establish what an unseen product looks like. Ask about an ambiguity only when it affects which product or feature must be retained.

Separate the requested cleanup from product attributes: for example, change the background or reduce a distracting reflection while aiming to retain the bottle, cap, label and amber color. Do not silently remove a logo or physical component as a blemish, recolor the item, substitute a similar SKU, or recreate an unavailable source from a text guess. Product identifiers guide the task; do not invent a `sku` model input property.

Treat preservation as a goal to check, not a guarantee. This generative workflow can redraw labels, geometry and color. If the user needs exact packaging text, calibrated color or pixel-identical product pixels, explain the limitation before a paid edit. A white background is not transparency: do not promise an alpha cutout, invent a mask parameter or call a white JPEG a transparent PNG.

## Source photo and exposed operation

For reference media, use externally fetchable HTTPS URLs that an unauthenticated GET can retrieve. When the host supplies such a URL for the user’s attachment and access is authorized for this task, use it directly; do not request another upload. Local paths, `file://`, internal attachment/sandbox IDs and data URIs cannot be passed to the Model API. Without a usable URL, explain the limit and request a direct link or a genuinely available, authorized host upload. These MCP tools do not upload arbitrary media: do not invent hosting, publish private media without permission, embed account credentials in URLs or repurpose training uploads.

Before a paid call, confirm each reference is a supported still image from reliable supplied metadata or an available inspection feature. A known HTML/login/model page, video or audio URL is not an image input merely because it is HTTPS or returns 200. If the media type is inaccessible or ambiguous, resolve it or request a direct supported image URL before a paid generation; do not claim a check you could not perform or invent an upload/conversion.

1. Select a currently exposed image operation that supports the actual source/reference images and requested edit or composition. Use `generate_image` when the current host exposes a compatible definition, following its actual declared arguments and allowed model scope. A text-only operation cannot substitute for a required reference input.
2. Inspect the matched operation and supported model schemas for image fields, reference count/order, dimensions, output controls and any requested mask or style controls. Use an exposed `get_model` operation when available to read details and pricing for the exact selected model supported by the matched operation. Validate the current outer tool schema and that model’s input schema together; model metadata cannot expand the operation’s allowed scope. A fixed-model operation cannot be retargeted by adding another model ID.
3. Build only that exposed operation’s declared arguments from the actual product reference, requested cleanup and product checklist. Do not drop an essential reference, invent an input property or substitute text-only generation. Explain a missing control before considering a different user-authorized scope.

## Paid request and recovery

Use returned `base_price_usd` and `price_unit` when present to explain an estimate and output count; dimensions, references or other settings can change the final price. Use `get_balance()` only when a funds question or account error makes it relevant; read `balance.balance_usd`/`balance.balance_microdollars`.

Use only the connected account’s existing balance or entitlement. Authenticate through this plugin’s OAuth connection flow, never by collecting credentials in chat. If balance or entitlement is insufficient, explain why the task cannot run and stop; do not initiate or link to purchases, top-ups, subscriptions or upgrades.

Preserve existing authorization for this exact paid edit and budget. If the user requested a plan first, asked to wait, or has not authorized the paid scope, obtain what is missing before running. Do not repeatedly ask for approval of an already authorized edit or turn one photo into an unrequested paid batch.

Only after a suitable product-image edit operation is actually exposed, invoke it once per approved request with declared typed arguments. Use asynchronous submission only if supported and save the actual returned request ID (`submission.request_id` when provided) before polling. An acknowledgment does not establish that an image exists.

Use `get_model_request_status(request_id=...)` and, when complete, `get_model_request_result(request_id=...)` for that same ID. Do not use deployment-scoped status/result tools. Poll with pauses, at most 12 status checks and about 2 minutes per active turn; retain pending IDs for later checks. Stop on terminal states or errors.

Do not resubmit because a wait expired. A lost submission acknowledgment means acceptance is uncertain: check a known ID; without one, reconcile generation history with the user before an authorized replacement. These tools cannot list lost request IDs. Report actual failure, cancellation, authentication or credit errors and useful next steps instead of fabricating outputs or automatically retrying paid jobs.

## Product check and delivery

Show actual returned assets from `output_urls` or the model-defined result and preserve signed URLs exactly. If visual inspection is available, compare against the source: intended SKU/variant, color, label spelling/logo, silhouette, proportions, cap/handle/other parts and the requested cleanup. Mark visible drift or unreadable text; do not say checks passed if you could only retrieve a URL. The result is a generated edit, not proof of exact product fidelity. A requested correction is a new paid scope unless the service explicitly says otherwise.

## Result presentation

Keep each request ID paired with its own actual returned output asset. Use a native displayable attachment if the tool returns one; otherwise provide one Markdown link labeled Open original image, copied directly from that request's output URL. Do not rebuild path segments, repeat a second transcription, add tracking parameters to media URLs, or substitute results from another request. Do not use image search, HTML widgets, downloading or rehosting to bypass host display restrictions. When inline display is unavailable, say so and return the original link. Keep the active RunComfy task and its approved scope on follow-up confirmations; do not switch to another image generator or silently start a new job.

## Model details

Link to model details only when the user needs help selecting or understanding a model; do not append links automatically or use them to direct credit purchases or upgrades.

- [RunComfy model catalog](https://www.runcomfy.com/models/all?utm_source=chatgpt&utm_medium=plugin&utm_campaign=runcomfy-plugin&utm_content=product-photography--skill)

A useful tool-returned `model_url` may receive the same catalog attribution parameters only after verifying its RunComfy website destination. Leave API URLs and signed media URLs unchanged.
