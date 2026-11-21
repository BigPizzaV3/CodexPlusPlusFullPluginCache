---
name: reference-guided-image
description: Create a new still image guided by user-provided reference images with RunComfy, such as a reference-led composition or visual concept. Requires remotely accessible image inputs; does not provide automatic attachment hosting or guarantee exact identity preservation.
---

# Reference-guided image

Create the requested still using reference-capable RunComfy models exposed by this plugin. Respond in the user's language. All steps here use MCP tools; do not assume a CLI, uploader or another plugin skill exists.

Use only this plugin’s current host-provided tool definitions: actual names, descriptions, typed outer arguments and allowed model scope. Old published caches and conditional names in previous packages do not establish current availability or its limits. If current definitions cannot be verified, report an unverified connection binding, not that RunComfy lacks the product capability. If verified definitions offer no compatible operation, explain the connection-specific limitation before spending. Do not assume a discovery tool, switch endpoints, invent operations or bypass the connection through workflow/deployment execution.

## Resolve the reference input first

Identify which reference supplies the subject, which supplies a style or composition, what should change, and what the user wants preserved. Keep reference order explicit. Obtain the desired output count and framing without adding a batch the user did not request.

For reference media, use externally fetchable HTTPS URLs that an unauthenticated GET can retrieve. When the host supplies such a URL for the user’s attachment and access is authorized for this task, use it directly; do not request another upload. Local paths, `file://`, internal attachment/sandbox IDs and data URIs cannot be passed to the Model API. Without a usable URL, explain the limit and request a direct link or a genuinely available, authorized host upload. These MCP tools do not upload arbitrary media: do not invent hosting, publish private media without permission, embed account credentials in URLs or repurpose training uploads.

When a reference is used, confirm it is a still image: a known HTML page, video or audio URL is not a valid substitute. Resolve an ambiguous media type before a paid request; do not invent conversion or claim an uninspected URL was verified.

Treat signed asset URLs as access-bearing data: pass them only to the selected model for this task and avoid repeating them in prose unnecessarily.

## Match an exposed image operation

1. Select a currently exposed image operation that supports the actual source/reference images and requested edit or composition. Use `generate_image` when the current host exposes a compatible definition, following its actual declared arguments and allowed model scope. A text-only operation cannot substitute for a required reference input.
2. Inspect the matched operation and supported model schemas for image fields, reference count/order, dimensions, output controls and any requested mask or style controls. Use an exposed `get_model` operation when available to read details and pricing for the exact selected model supported by the matched operation. Validate the current outer tool schema and that model’s input schema together; model metadata cannot expand the operation’s allowed scope. A fixed-model operation cannot be retargeted by adding another model ID.
3. Build only that exposed operation’s declared arguments from the actual subject/style/composition references and their roles. Do not drop an essential reference, invent an input property or substitute text-only generation. Explain a missing control before considering a different user-authorized scope.

## Authorize and generate

Use returned `base_price_usd`/`price_unit` when present to explain the expected cost basis and the number of paid requests. Reference count, dimensions or other options may affect price; label an estimate honestly. `get_balance()` is available when a funds question or error makes it relevant; it returns `balance.balance_usd` and `balance.balance_microdollars` and does not buy credit.

Use only the connected account’s existing balance or entitlement. Authenticate through this plugin’s OAuth connection flow, never by collecting credentials in chat. If balance or entitlement is insufficient, explain why the task cannot run and stop; do not initiate or link to purchases, top-ups, subscriptions or upgrades.

Respect the user's existing authorization for this exact run/batch and budget. If they asked for a plan first or have not authorized the paid scope, obtain it before submitting. Do not repeat a confirmation already provided for the same scope.

After verifying a matching reference-capable image operation in the current host definitions, invoke it once per approved job with declared typed arguments. Use asynchronous submission only if supported. Preserve the actual returned request ID (`submission.request_id` when provided). An acknowledgment is not a finished image, and repeated submissions may be separately charged.

## Track, recover and return the real output

Use `get_model_request_status(request_id=...)` and then `get_model_request_result(request_id=...)` for the same ID. These are Model API calls; do not use Serverless deployment status/result tools.

Use pauses and a bounded wait of at most 12 status checks and about 2 minutes per active turn. Stop on terminal states/errors. If the job remains pending, retain the ID and report that state so a later check can resume. Do not resubmit because a wait expired. If a submission acknowledgment is lost and no ID is known, explain that acceptance is uncertain and reconcile generation history with the user before any replacement is authorized; the available tools cannot list missing request IDs.

On failure, cancellation, unavailable tools, authentication errors or insufficient funds, report what actually happened and the useful next step. Do not return a fabricated image or automatically retry a charged operation.

During planning and progress, show only text and the user's actual supplied reference images. Do not use image search or insert mood images, stock images, unrelated thumbnails or preview cards unless the user explicitly asks for reference exploration. After completion, use only output assets returned for the recorded request ID. A remote output URL alone does not prove that this host can render the image. If the result contains a URL but no native displayable image attachment, provide one Markdown link labeled Open original image, and explain that inline display is unavailable. Copy that link from the selected current request output_urls entry without rebuilding any path segments. Do not repeat a second transcription of the same URL in a code block or paragraph: duplicating long media addresses can mix paths from earlier requests. If the user specifically asks for the raw URL, return that exact field once in a fenced text block instead of also making a clickable link. Keep each request ID paired only with its own returned media field. Do not create HTML, iframe, canvas or visualization widgets to display remote result URLs, do not use image-search results as previews, and do not download or rehost assets to bypass host presentation restrictions. If the tool directly returns a native displayable image attachment, display that attachment. Preserve every original output media URL exactly, including its query string; do not add tracking parameters. The host may decorate rendered hyperlinks; do not claim that the final clickable destination is byte-for-byte unchanged without checking it. Never substitute another image or claim an uninspected preview is correct. Read assets from `output_urls` or the model-defined result output.

If you can inspect the result, check it against the requested subject, composition and change; otherwise do not claim visual verification. Reference guidance can drift in identity, geometry, text or fine product details. Describe those limitations and any visible mismatch; promise no exact consistency or pixel preservation. Further paid iterations require the user's authorized scope.

## Model details

Link to model details only when the user needs help selecting or understanding a model; do not append links automatically or use them to direct credit purchases or upgrades.

- [RunComfy model catalog](https://www.runcomfy.com/models/all?utm_source=chatgpt&utm_medium=plugin&utm_campaign=runcomfy-plugin&utm_content=ai-image-generator--skill)

A useful tool-returned `model_url` may receive the same catalog attribution parameters only after verifying its RunComfy website destination. Leave API URLs and signed media URLs unchanged.
