---
name: mediaio-aigc
metadata:
  version: "1.0.1"
description: |
  Generate images and videos through the connected Media.io MCP server using
  text_to_image, image_to_image, text_to_video, image_to_video,
  reference_to_video, motion_control, or image_audio_to_video. Select a model
  from the static release catalog and follow its model-specific schema.
  Generation normally consumes existing account credits; submit quietly when
  the user requests generation. Use estimate_credits only when the user asks
  about cost, requests an estimate, or explicitly requires free, zero-credit
  or budget-limited generation; never as a routine prerequisite.
  Source media must be file IDs from the user's Media.io drive. Upload local
  files only when the host can read bytes, compute SHA-1 and perform HTTP PUT.
  Wait with get_generation, then show finished results once with
  get_generation_card. View past or recent tasks with list_generations_card.
  No local CLI or installation is needed.
---

# Media.io generation

Use the connected tools and their static input schemas as the contract. If unavailable, explain that the Media.io connection is missing. Do not replace the MCP operation with another plugin, a local CLI or an unexposed upstream API.

## Operation selection

| User intent | Tool | Sources in `request.inputs` |
| --- | --- | --- |
| Image from a description | `text_to_image` | None |
| Edit or reinterpret source images | `image_to_image` | Model-specific image file fields |
| Video from a description | `text_to_video` | None |
| Animate an image, or declared start/end frames | `image_to_video` | Starting image; ending image when required |
| Video guided by declared references | `reference_to_video` | Model-specific images, video, audio or document references |
| Animate an image using a motion video | `motion_control` | Reference image and motion video |
| Music video from an image and audio | `image_audio_to_video` | Image and audio |

Read [model-catalog.md](references/model-catalog.md) for this release's callable models and lifecycle status. Match the user's selected model to an exact ID within the requested action. Repeated display names are not unique IDs: ask for clarification when the available variants materially differ. Never infer a workflow code or transfer options from another model.

Read [model-selection.md](references/model-selection.md) at model selection for the shared policy, scenario rules, conditional member defaults, free recommendations and aliases. Honor the user's explicit model and cost constraints together, then task features, membership conditions and ordinary defaults. Resolve conflicting requirements before creation. Use the existing read-only `get_account` only when membership is needed for selection; account cards remain user-requested. Follow only actions exposed by the connected server. Deprecated models are not defaults or recommendations; replacement candidates do not authorize substitution. Never switch away from an explicitly selected model without the user's request.

Video editing or extension as a separate operation, persistent character creation, training and publishing are outside this release. A temporarily unavailable model does not authorize discovery or bypassing the declared contract. New upstream models do not become callable automatically.

## Normal flow

1. Select the operation and exact model. Read that model's section in the generated [model parameters](references/model-parameters.md), including UI label mappings, defaults and coupled option branches. Put business fields inside `request`: `model`, the declared `prompt`, model-specific `inputs`, and strict `options`. Extract explicit settings from the user's message, supplied prompt or screenshot, and referenced earlier request into the model's declared fields. Match each setting to its declared field and mapped value; user settings take precedence over defaults. For sizing, also follow [Output size](references/prompt-engineering.md#output-size). Resolve unsupported or conflicting requirements before creation. One call creates one task, not a Web UI batch.
2. Resolve source media with `list_assets`. For an earlier task output, use its `asset_id` to look up the corresponding `file_id`. Never invent an ID, use another account's media, or pass a URL/path as a file ID.
3. Submit with the corresponding generation tool and a stable `client_request_id`, omitting `approved_credit` by default. The user's generation request authorizes the normal use of their existing credits. Do not add an estimate, account card, cost announcement or credit-confirmation turn by default. For an explicit free, zero-credit or budget requirement, follow the selection policy and Cost questions before creation. The server skips pre-submission estimation on the ordinary path; batch size or an inferred interest in saving credits does not change it.
4. Read `task_id`, call `get_generation`, and continue after `poll_after_ms` until all tasks are terminal. A call may wait 25 seconds. Do not resubmit a running task. For requested sizing, compare available output `width` and `height` with the selected pixel size. Report a mismatch or unavailable dimensions without automatically regenerating.
5. Call `get_generation_card` once after completion. The card is the result presentation; follow it with at most a short sentence.

For multiple user-requested tasks, use a different request identifier per task. Retries must preserve the identifier and all business inputs. Never create extra tasks, change models or regenerate after an error without a new user request.

## History queries

When the user asks to view past or recent generations, call `list_generations_card` directly. Use `page: 1, page_size: 10` unless the user specifies a count; each page supports at most 100 tasks. Preserve any requested task ID or status filters. For a requested next page, keep those filters and the page size and increment `page`.

The history card shows the current snapshot, including running and failed tasks. After it renders, say at most one short sentence. If the host cannot render cards, summarize the returned `generations` and `total` as a short list. Do not wait for every history task to finish or add `get_generation_card` per task merely to show history.

Use `list_generations` for background inspection, including matching an uncertain submission after `RESULT_UNKNOWN`. Use `get_generation` to follow known task IDs; the normal generation flow still ends with `get_generation_card`. A history query never authorizes creating, retrying or regenerating tasks. If `list_generations_card` is unavailable, explain that the connected server needs the history-card tool; do not use an unexposed API.

## Cost questions

`estimate_credits` takes `{ "request": { "operation": "text_to_image", "generation": { "model": "text2image_soul_character", "prompt": "A red paper crane" } } }`. Its `request.generation` is exactly the corresponding tool’s business `request`, without `client_request_id` or `approved_credit`. It does not create a task. A request to estimate only must remain read-only. When the user subsequently asks to generate, preserve any explicit cost constraint and otherwise submit normally.

Only use optional `approved_credit` when the user explicitly wants a known estimated amount guarded. Supplying it makes the server calculate and compare the amount before submission. On `CREDIT_CHANGED`, do not silently replace the guard and retry. The guard is not an atomic upstream quote.

A creation receipt may contain `frozen_credit`, the amount frozen by the upstream create request. An absent value means unknown, not zero or free; do not run an estimate to fill it in. Optional `estimated_credit` is only a pre-submission estimate from explicit amount protection or an older task replay. Neither field is a final settlement record. Do not claim refunds or that a failed terminal task necessarily consumed no credits.

On `CREDIT_INSUFFICIENT` or `PLAN_REQUIRED`, explain neutrally that the task is unavailable with the current balance or entitlements, then stop. Do not suggest purchasing, topping up, upgrading or subscribing; do not provide a transaction link, upgrade card or fallback that spends credits automatically. Existing paid users may use their included entitlements normally.

## Source transfer and results

Use existing Media.io drive files whenever possible. Local upload is conditional on actual host capabilities: read the bytes, calculate their size and SHA-1 digests, call `create_upload`, perform the exact returned PUT, then `complete_upload`. A completed rapid upload needs no PUT or completion call. A host attachment reference alone does not prove those capabilities. See [media-inputs.md](references/media-inputs.md).

Prefer the native result card. Use signed result URLs verbatim only through delivery capabilities supported by the host; never rewrite their query strings or download media to bypass display restrictions. If saving a requested original is permitted, link the returned local file with an absolute path. Refresh an expired result by querying the task again; never repair a signature.

## Errors and privacy

Act on structured error codes. `RESULT_UNKNOWN` means stop submitting: inspect `list_generations` pages and task timestamps, without inventing a time-filter parameter, and explain uncertainty if no reliable match exists. `AUTH_*` requires authorization or resource access resolution. `INVALID_PARAMETER` requires following the current tool schema. `CAPABILITY_NOT_FOUND` may indicate availability or contract drift; do not discover new schemas or models.

Keep account, asset and task data private to the authorized user. Do not show tokens, unrelated prompts or internal diagnostics. Use `get_account_card` only when the user asks to view their connected account, existing balance or membership. Its text result and `structuredContent.account` contain the available nickname and email as model-visible data, alongside existing membership and credits. The card renders these fields without buttons or navigation links; do not repeat its identity or rendered data in prose. See [tool-contract.md](references/tool-contract.md), [credit-approval.md](references/credit-approval.md) and [troubleshooting.md](references/troubleshooting.md).
