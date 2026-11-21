---
name: text-to-image
description: Generate a new still image from a text brief with RunComfy hosted models, including illustrations, posters and visual concepts. Use for requested image creation without a source image; writing a prompt alone does not authorize generation.
---

# Text to image

Turn the user's brief into an actual image using this plugin's RunComfy MCP tools. Respond in the user's language. This skill is self-contained and requires no CLI, local software or other plugin skill.

Use only this plugin’s current host-provided tool definitions: actual names, descriptions, typed outer arguments and allowed model scope. Old published caches and conditional names in previous packages do not establish current availability or its limits. If current definitions cannot be verified, report an unverified connection binding, not that RunComfy lacks the product capability. If verified definitions offer no compatible operation, explain the connection-specific limitation before spending. Do not assume a discovery tool, switch endpoints, invent operations or bypass the connection through workflow/deployment execution.

## Inputs and routing

Use the requested subject, style, framing, aspect ratio, exact visible text and output count. Ask only for information that materially affects the request or is required by the selected model. Preserve an explicitly chosen model when available. For a source-image request, a reference-capable model and reachable image URL are required; do not silently replace reference guidance with text-only generation.

If the user supplies reference media for a supported reference workflow, use its actual authorized host HTTPS URL when available; do not require another upload or publish a private attachment. Otherwise explain the need for a usable direct link or an actually available authorized upload feature. Text-only generation needs no media URL.

1. Select a currently exposed image operation and supported model that fit the text brief and requested controls. Use `generate_image` when the current host exposes a compatible definition, following its actual declared arguments and allowed model scope. A text-only operation cannot accept a required source image.
2. Read the current typed outer arguments and selected model schema for prompt, image size, seed and optional controls. Use a model selector or nested input object only where the current operation declares it. Use an exposed `get_model` operation when available to read details and pricing for the exact selected model supported by the matched operation. Validate the current outer tool schema and that model’s input schema together; model metadata cannot expand the operation’s allowed scope. A fixed-model operation cannot be retargeted by adding another model ID.
3. Construct only the supported arguments from the brief, preserving an explicitly selected model and requested output count. Resolve unsupported requirements without silently changing the model or task. A prompt or estimate request alone never starts generation.

## Cost and submission

Details for the model bound to a matched exposed operation may provide `base_price_usd` and `price_unit` when available. Explain relevant estimated cost and output count before a paid run; a base price may not include every size or model-dependent option, so do not present it as a guaranteed final charge. Use `get_balance()` when the user asks about available funds or an account/balance issue needs investigation. It returns `balance.balance_usd` and `balance.balance_microdollars`.

Use only the connected account’s existing balance or entitlement. Authenticate through this plugin’s OAuth connection flow, never by collecting credentials in chat. If balance or entitlement is insufficient, explain why the task cannot run and stop; do not initiate or link to purchases, top-ups, subscriptions or upgrades.

Execute only the run or batch the user has authorized. If this exact paid scope and budget were already approved, continue without another confirmation. If the user asked to wait, or paid scope is unclear, obtain the missing authorization first. Never expand a one-image request into a paid batch or switch to a more expensive model outside the agreed scope.

Invoke the matched, actually exposed image operation once per approved job using its declared typed arguments. Use asynchronous submission only if the tool exposes that option. Preserve the actual returned request ID (`submission.request_id` when provided) before polling. `ok: true` acknowledges the request; it does not establish image completion.

## Completion and recovery

- Use `get_model_request_status(request_id=...)` for that ID, then `get_model_request_result(request_id=...)` when completed. Model requests use these tools, not deployment-scoped `get_request_status` or `get_request_result`.
- Poll with pauses and a bounded wait: at most 12 status checks and about 2 minutes in one active turn, stopping sooner on a terminal state or error. If waiting must stop, keep the original ID, describe the current state, and resume by checking that ID later. Do not start a replacement job because polling stopped.
- A pending result is not a success. If the API reports failure or cancellation, report the actual state and useful returned reason. Do not fabricate an image or automatically retry a paid submission.
- If submission times out or loses its acknowledgment, its acceptance is uncertain. With a known ID, check that ID. Without one, stop and ask the user to check their RunComfy generation history before authorizing a replacement; these tools cannot list missing requests. An empty/missing ID is not proof the job was rejected.
- On authentication errors, explain the plugin’s OAuth reconnect step without requesting credentials in chat. On insufficient balance or entitlement, explain why execution is unavailable without directing a purchase. If required tools are absent, explain that connection capability limit instead of inventing a local execution path.

## Result and useful navigation

During planning and progress, show only text and the user's actual supplied reference images. Do not use image search or insert mood images, stock images, unrelated thumbnails or preview cards unless the user explicitly asks for reference exploration. After completion, use only output assets returned for the recorded request ID. A remote output URL alone does not prove that this host can render the image. If the result contains a URL but no native displayable image attachment, provide one Markdown link labeled Open original image, and explain that inline display is unavailable. Copy that link from the selected current request output_urls entry without rebuilding any path segments. Do not repeat a second transcription of the same URL in a code block or paragraph: duplicating long media addresses can mix paths from earlier requests. If the user specifically asks for the raw URL, return that exact field once in a fenced text block instead of also making a clickable link. Keep each request ID paired only with its own returned media field. Do not create HTML, iframe, canvas or visualization widgets to display remote result URLs, do not use image-search results as previews, and do not download or rehost assets to bypass host presentation restrictions. If the tool directly returns a native displayable image attachment, display that attachment. Preserve every original output media URL exactly, including its query string; do not add tracking parameters. The host may decorate rendered hyperlinks; do not claim that the final clickable destination is byte-for-byte unchanged without checking it. Never substitute another image or claim an uninspected preview is correct. Read assets from `output_urls` or the model-defined result output.

Distinguish an output the tool returned from an image you have visually inspected. Report relevant mismatches without promising perfect text, likeness or composition. Offer another paid iteration only when it serves the user's request; it needs its own authorized scope.

## Model details

Link to model details only when the user needs help selecting or understanding a model; do not append links automatically or use them to direct credit purchases or upgrades.

- [RunComfy model catalog](https://www.runcomfy.com/models/all?utm_source=chatgpt&utm_medium=plugin&utm_campaign=runcomfy-plugin&utm_content=ai-image-generator--skill)

A useful tool-returned `model_url` may receive the same catalog attribution parameters only after verifying its RunComfy website destination. Leave API URLs and signed media URLs unchanged.
