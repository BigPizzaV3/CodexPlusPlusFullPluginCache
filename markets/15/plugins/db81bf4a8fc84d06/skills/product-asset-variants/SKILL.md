---
name: product-asset-variants
description: Generate a bounded set of product-image composition or aspect-ratio variants from supplied product references with RunComfy. Use for requested campaign assets; generated variants may redraw details and are not lossless resizing or guaranteed identical SKUs.
---

# Product asset variants

Create only the campaign variants the user requested using this plugin's RunComfy MCP tools. Respond in the user's language. This skill does not depend on a CLI, another skill, an uploader or an exact image-resizing service.

Use only this plugin’s current host-provided tool definitions: actual names, descriptions, typed outer arguments and allowed model scope. If current definitions cannot be verified, report an unverified connection binding, not that RunComfy lacks the product capability. If verified definitions offer no compatible operation, explain the connection-specific limitation before spending. Do not assume a discovery tool, switch endpoints, invent operations or bypass the connection through workflow/deployment execution.

## Define the variant matrix

For each requested asset, include its intended channel or placement when supplied, supported format/ratio, product details to retain and allowed scene changes. This is a bounded campaign deliverable, not an automatic store integration: label each result against its row and distinguish verified format/product checks from unresolved ones.

List each requested output as a row with its intended product/SKU, real source reference, color/variant, scene or allowed change, aspect ratio/size and count. Do not automatically take the Cartesian product of every SKU, scene and ratio. Resolve mismatched SKU references rather than copying one product's label onto another.

Keep product color, label/logo/text, silhouette, proportions, materials and distinctive parts as explicit preservation targets. Product/SKU labels are task bookkeeping, not invented schema properties. If the user explicitly requests a color variant, describe it as a generated concept unless they provide a real reference confirming that product variant. Do not present a synthetic recoloring as evidence that the SKU exists.

Changing aspect ratio with a generative model can redraw the product and scene. It is not a lossless resize, crop or pixel-identical catalog conversion. Explain this distinction when exact pixels, labels, calibrated colors, measured geometry or print specifications matter. Do not promise alpha transparency or an unchanged product across sizes. If exact processing is essential, say the exposed tools do not provide that guarantee rather than silently substituting a generative edit.

## Source files and schema

For reference media, use externally fetchable HTTPS URLs that an unauthenticated GET can retrieve. When the host supplies such a URL for the user’s attachment and access is authorized for this task, use it directly; do not request another upload. Local paths, `file://`, internal attachment/sandbox IDs and data URIs cannot be passed to the Model API. Without a usable URL, explain the limit and request a direct link or a genuinely available, authorized host upload. These MCP tools do not upload arbitrary media: do not invent hosting, publish private media without permission, embed account credentials in URLs or repurpose training uploads.

Before a paid call, confirm each reference is a supported still image from reliable supplied metadata or an available inspection feature. A known HTML/login/model page, video or audio URL is not an image input merely because it is HTTPS or returns 200. If the media type is inaccessible or ambiguous, resolve it or request a direct supported image URL before a paid generation; do not claim a check you could not perform or invent an upload/conversion.

1. Select a currently exposed image operation that supports the actual source/reference images and requested edit or composition. Use `generate_image` when the current host exposes a compatible definition, following its actual declared arguments and allowed model scope. A text-only operation cannot substitute for a required reference input.
2. Inspect the matched operation and supported model schemas for image fields, reference count/order, dimensions, output controls and any requested mask or style controls. Use an exposed `get_model` operation when available to read details and pricing for the exact selected model supported by the matched operation. Validate the current outer tool schema and that model’s input schema together; model metadata cannot expand the operation’s allowed scope. A fixed-model operation cannot be retargeted by adding another model ID.
3. Build only that exposed operation’s declared arguments from each approved product/scene/format row and its matching real reference. Do not drop an essential reference, invent an input property or substitute text-only generation. Explain a missing control before considering a different user-authorized scope.

## Paid batch and request tracking

Explain the planned outputs and number of paid jobs using the returned `base_price_usd`/`price_unit` where available. Give an honest batch estimate with parameter-dependent uncertainty. Use `get_balance()` only for a relevant funds question or account error; it returns `balance.balance_usd` and `balance.balance_microdollars` and does not buy credit.

Use only the connected account’s existing balance or entitlement. Authenticate through this plugin’s OAuth connection flow, never by collecting credentials in chat. If balance or entitlement is insufficient, explain why the task cannot run and stop; do not initiate or link to purchases, top-ups, subscriptions or upgrades.

Preserve the user's existing exact batch/budget authorization. If they asked to wait for approval or the paid scope is unclear, resolve that before starting. Do not ask separately for each already approved row. A new SKU, extra output, higher-cost model or retry after an imperfect result needs an authorized scope.

Only when a matching reference-capable image operation is exposed, invoke it once per approved job with declared typed arguments, recording each actual returned request ID (`submission.request_id` when provided) against its row. Use asynchronous or batch-output controls only when exposed and matching the plan. Repeated submissions can be separately billable and are not an idempotent retry.

Poll each ID with `get_model_request_status(request_id=...)` and fetch completed assets with `get_model_request_result(request_id=...)`. Do not use Serverless deployment tools. Use pauses, at most 12 status checks and about 2 minutes total per active turn. Stop on terminal states and report complete, pending, cancelled and failed rows separately; retain pending IDs for later recovery.

If a wait expires, continue with the existing IDs later instead of submitting again. A lost acknowledgment without an ID leaves that row's acceptance uncertain: reconcile generation history with the user before replacing it; these tools cannot list missing IDs. Do not automatically retry failures, cancel other rows or declare the whole batch complete because one tool returned `ok: true`.

## Deliver the actual variant set

Label each returned asset by the requested SKU/scene/size row, using only actual `output_urls` or model-defined outputs. Preserve signed URLs. If actual dimensions are not returned or inspected, do not claim they were verified. When visual inspection is available, compare SKU identity, color, label spelling/logo, silhouette, proportions and components against the matching source in every variant; flag mismatches or unreadable details. Otherwise report output retrieval without claiming visual quality assurance. Do not say the batch is production-ready solely because it generated successfully.

## Result presentation

Keep each request ID paired with its own actual returned output asset. Use a native displayable attachment if the tool returns one; otherwise provide one Markdown link labeled Open original image, copied directly from that request's output URL. Do not rebuild path segments, repeat a second transcription, add tracking parameters to media URLs, or substitute results from another request. Do not use image search, HTML widgets, downloading or rehosting to bypass host display restrictions. When inline display is unavailable, say so and return the original link. Keep the active RunComfy task and its approved scope on follow-up confirmations; do not switch to another image generator or silently start a new job.

## Model details

Link to model details only when the user needs help selecting or understanding a model; do not append links automatically or use them to direct credit purchases or upgrades.

- [RunComfy model catalog](https://www.runcomfy.com/models/all?utm_source=chatgpt&utm_medium=plugin&utm_campaign=runcomfy-plugin&utm_content=product-photography--skill)

A useful tool-returned `model_url` may receive the same catalog attribution parameters only after verifying its RunComfy website destination. Leave API URLs and signed media URLs unchanged.
