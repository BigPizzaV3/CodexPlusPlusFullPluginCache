---
name: character-scene-variations
description: Generate requested character or scene variations as still images with RunComfy, using a written concept or an accessible reference. Use for a requested series or alternate scenes; do not promise identical characters or start unrequested paid variants.
---

# Character and scene variations

Generate the user's requested alternatives while making continuity limits clear. Respond in the user's language. This workflow uses only the RunComfy MCP tools described here and requires no CLI or cross-plugin skill.

Use only this plugin’s current host-provided tool definitions: actual names, descriptions, typed outer arguments and allowed model scope. Old published caches and conditional names in previous packages do not establish current availability or its limits. If current definitions cannot be verified, report an unverified connection binding, not that RunComfy lacks the product capability. If verified definitions offer no compatible operation, explain the connection-specific limitation before spending. Do not assume a discovery tool, switch endpoints, invent operations or bypass the connection through workflow/deployment execution.

## Define the approved series

Separate the shared subject/appearance/style from the changes in each scene. Use an existing user brief when sufficient; clarify only missing constraints that change the intended series. Establish the requested count, scenes and budget. Do not manufacture extra variations to promote more runs.

For text-only concepts, a series can reuse a concise appearance/style description. This does not create a persistent character model. For a reference, keep the original reference(s) and their role explicit across the series. Character training and custom LoRA creation are outside this image-generation workflow.

For reference media, use externally fetchable HTTPS URLs that an unauthenticated GET can retrieve. When the host supplies such a URL for the user’s attachment and access is authorized for this task, use it directly; do not request another upload. Local paths, `file://`, internal attachment/sandbox IDs and data URIs cannot be passed to the Model API. Without a usable URL, explain the limit and request a direct link or a genuinely available, authorized host upload. These MCP tools do not upload arbitrary media: do not invent hosting, publish private media without permission, embed account credentials in URLs or repurpose training uploads.

When a reference is used, confirm it is a still image: a known HTML page, video or audio URL is not a valid substitute. Resolve an ambiguous media type before a paid request; do not invent conversion or claim an uninspected URL was verified.

## Exposed operation and series routing

1. For a text-led series, select a currently exposed image operation and model that fit the shared brief and each scene. Use `generate_image` when the current host exposes a compatible definition, following its actual declared arguments and allowed model scope. Reusing text does not create a persistent identity model.
2. For reference-led variants, select a current operation and model whose schemas accept every essential reference and its role. Do not replace image references with a text guess or route them through a text-only legacy tool. Read actual seed, ratio and output-count controls; none guarantees identical identity.
3. Use an exposed `get_model` operation when available to read details and pricing for the exact selected model supported by the matched operation. Validate the current outer tool schema and that model’s input schema together; model metadata cannot expand the operation’s allowed scope. A fixed-model operation cannot be retargeted by adding another model ID. Map each authorized variation and real reference to its own declared arguments and output/request count.

## Cost and single submission per request

Use model-returned `base_price_usd` and `price_unit` to explain an estimate for the whole approved series, noting parameter-dependent uncertainty. If there will be separate model jobs, state the count. Use `get_balance()` only when a balance check is relevant; read `balance.balance_usd`/`balance.balance_microdollars` without claiming it guarantees a final price.

Use only the connected account’s existing balance or entitlement. Authenticate through this plugin’s OAuth connection flow, never by collecting credentials in chat. If balance or entitlement is insufficient, explain why the task cannot run and stop; do not initiate or link to purchases, top-ups, subscriptions or upgrades.

Use existing explicit authorization for the exact paid series and budget. If the user asked to wait or the paid scope is unresolved, obtain the missing authorization before execution. Do not re-confirm each scene inside a batch the user already approved.

Invoke the matched, actually exposed image operation once per approved job with declared typed arguments, recording the actual returned request ID (`submission.request_id` when provided) against its scene/variant. Use asynchronous or multi-output controls only when exposed and consistent with the plan. Do not duplicate jobs after slow polling or an imperfect result.

## Progress, failures and result handling

Track every recorded ID with `get_model_request_status(request_id=...)`; fetch completed assets using `get_model_request_result(request_id=...)`. Never mix a Model API ID with deployment-scoped status/result tools. `ok: true` is an acknowledgment, not evidence every variant finished.

Use pauses and a bounded wait of at most 12 status checks and about 2 minutes total in an active turn. Stop polling a terminal request. Report completed, pending, failed and cancelled variants separately, retaining the IDs for future checks. Do not call a partially finished series complete.

If a submission times out, use its known ID to reconcile status. If no ID was returned, mark that scene's acceptance uncertain and stop before replacing it or expanding the batch; reconcile RunComfy generation history with the user. The exposed tools cannot discover a lost request ID. Do not automatically retry, cancel or replace other work because one variant failed.

During planning and progress, show only text and the user's actual supplied reference images. Do not use image search or insert mood images, stock images, unrelated thumbnails or preview cards unless the user explicitly asks for reference exploration. After completion, use only output assets returned for the recorded request ID. A remote output URL alone does not prove that this host can render the image. If the result contains a URL but no native displayable image attachment, provide one Markdown link labeled Open original image, and explain that inline display is unavailable. Copy that link from the selected current request output_urls entry without rebuilding any path segments. Do not repeat a second transcription of the same URL in a code block or paragraph: duplicating long media addresses can mix paths from earlier requests. If the user specifically asks for the raw URL, return that exact field once in a fenced text block instead of also making a clickable link. Keep each request ID paired only with its own returned media field. Do not create HTML, iframe, canvas or visualization widgets to display remote result URLs, do not use image-search results as previews, and do not download or rehost assets to bypass host presentation restrictions. If the tool directly returns a native displayable image attachment, display that attachment. Preserve every original output media URL exactly, including its query string; do not add tracking parameters. The host may decorate rendered hyperlinks; do not claim that the final clickable destination is byte-for-byte unchanged without checking it. Never substitute another image or claim an uninspected preview is correct. Read assets from `output_urls` or the model-defined result output. Label each output by its requested scene.

When visual inspection is available, compare recognizable features, clothing, style and requested scene changes and report observed drift. Otherwise state that only returned assets were verified. Do not certify identity consistency, automatic best-variant scoring or exact preservation. A revision is a new paid request unless the service explicitly says otherwise and needs an authorized scope.

## Model details

Link to model details only when the user needs help selecting or understanding a model; do not append links automatically or use them to direct credit purchases or upgrades.

- [RunComfy model catalog](https://www.runcomfy.com/models/all?utm_source=chatgpt&utm_medium=plugin&utm_campaign=runcomfy-plugin&utm_content=ai-image-generator--skill)

A useful tool-returned `model_url` may receive the same catalog attribution parameters only after verifying its RunComfy website destination. Leave API URLs and signed media URLs unchanged.
