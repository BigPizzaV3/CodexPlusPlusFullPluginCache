# Static tool contract

The connected tool descriptors are authoritative. Every operation has a fixed input schema, output schema and explicit annotations. No generic executor or runtime schema-discovery operation exists.

Seven generation tools use a nested `request` containing an exact `model`, model-specific `prompt`, strict `inputs` and strict `options` plus required `client_request_id` and optional `approved_credit`. They return `task_id`, `idempotent_replay` and `poll_after_ms`, with optional `frozen_credit` from the upstream creation receipt. Optional `estimated_credit` is present only for explicit amount protection or legacy idempotent replays. Neither amount is a final settlement record; an absent amount is unknown, not zero. Normal generation omits `approved_credit` and makes no pre-submission estimation request. Unknown inputs and unsupported models/settings are rejected. A repeated request must preserve its identifier and business inputs; a different task uses a new identifier. Submitting normally consumes existing credits.

Credit fields in creation receipts are optional. Refresh cached tool definitions after upgrading from a server that required `estimated_credit`; do not treat its absence as a failed creation or resubmit. Older servers and legacy replays may still return only `estimated_credit`; keep its estimate meaning and never relabel it as frozen credits.

`estimate_credits` accepts `{ "request": { "operation": ..., "generation": { ...business_request } } }`. Its seven action branches reuse all 127 static model branches from the generation tools without submission-control fields. It returns `generation_operation`, `estimated_credit` and optional `balance`. It never submits a task.

| Read tool | Behavior |
| --- | --- |
| `get_account` | Existing membership/credits, no account identifiers or transaction links |
| `get_account_card` | Model-visible balance, entitlements and available nickname/email in the text result and `structuredContent.account`; renders a card only on user request, with no buttons or navigation links |
| `get_generation` | `task_ids` (1–50), optional `wait_ms` (0–60000); defaults to 25000; returns tasks, `all_terminal`, `poll_after_ms` |
| `get_generation_card` | Render finished tasks once using `task_ids` |
| `list_generations` | Background history data: optional task IDs (max 50), statuses (max 20), positive page and page size (max 100); returns `generations` and `total`; no time-window input |
| `list_generations_card` | Same input and output as `list_generations`, with a history card showing task identity, status, timestamps and available media immediately; use for user-requested history and pagination |
| `list_assets` | Name keyword, asset ID, media types and pagination; returns generation-ready `file_id` |

Uploads are two separate write operations around a host-performed PUT. `create_upload` accepts metadata and SHA-1 digests, returns a presigned transfer or completed rapid upload. `complete_upload` accepts only the ticket ID after the transfer and returns `file_id`. They cannot receive file bytes or fetch arbitrary URLs. Upload availability depends on the host's actual byte/hash/PUT capabilities.

The account card's available nickname and email are declared in its output schema and returned in both text `content` and `structuredContent.account`, so they are visible to the model. The widget renders identity from these structured fields. A missing nickname uses the email prefix when available, otherwise a generic name; a missing email omits the email row. The card displays account information without buttons or navigation links. Do not repeat its identity or rendered data in the assistant's prose.

Errors have `ok: false`, `error.code`, `message`, `retryable` and optional diagnostic fields. The text and structured result agree. Billing errors do not contain transaction actions. Internal diagnostics are not user-facing content.

## Model-specific inputs

A generation example is `{ "request": { "model": "image2image_gpt_image_2", "prompt": "A watercolor interpretation", "inputs": { "image_file_ids": ["authorized-file-id"] }, "options": { "quality": "low", "size": "1024x1024" } }, "client_request_id": "stable-user-task-id" }`.

Model-specific `options.dimensions` uses an exact `WIDTHxHEIGHT` string enum, for example `"1024x1024"`. Select a complete value declared for that model; never send `[width, height]` arrays or mix widths and heights. Refresh tool definitions after upgrading from the array format. Resolution and duration may have coupled alternatives. Follow the whole branch, including required source alternatives; an options object is never an arbitrary parameter dictionary. File metadata restrictions are described but validated by the upstream service. Automatic dimensions, arbitrary storyboard/character JSON and Web UI concurrency are not exposed.

Explicit aspect-ratio, resolution and pixel-size requirements must be represented in the selected model's `request.options`; writing them only in `prompt` leaves the sizing defaults in effect. See [Output size](prompt-engineering.md#output-size) for field selection, supported presets and unsupported-size handling.

`motion_control` requires a reference image and a motion video. `image_audio_to_video` requires an image and audio, with no prompt in its current branch. Reference video models can have different image, video, audio and document fields; source names and limits are not shared across all models. Unsupported fields fail before submission. Existing source media is preserved and generated content remains private to the authenticated account.
