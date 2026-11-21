# MCP Editing

Finish existing media through the connected PixVerse MCP service. Use its live editing
tools and keep host OAuth credentials in the host.
Never invoke FC, storage APIs, shell commands or a separate rendering service from this workflow.
Desktop workflows keep their original CLI contracts.

## Availability

Discover `edit_video`, `edit_status` and `render_edit` on the connected service before
promising a finished film. If unavailable, explain that this connection does not yet
provide editing; preserve existing IDs and offer the desktop route. Do not switch
environments, invoke FC directly or submit generation as a substitute.

## Plan and inputs

Read `account` before paid editing. Preserve any requested spending/confirmation policy.
Use existing owned upload, image, video or audio IDs, or import authorized HTTPS media with
`import_url`/`import_asset`, then wait for `import_status`. Do not invent IDs or infer media
length from a thumbnail. Ask for missing durations or subtitle timing when unavailable.
Build one complete timeline before submitting; no per-clip processing or intermediate uploads.
Inspect the live `edit_video` input schema for timeline fields, units, supported controls,
limits and output formats. Keep source sound unless the user requests removal; preserve
reference identity and the agreed clip order. Do not guess subtitle synchronization or
claim transcription: this workflow accepts supplied timed text only. Translate only when requested.

Omit output overrides to preserve source quality. Do not insert the generation default of 1080p into editing requests.
Use live capabilities for explicit resolution, aspect, frame-rate, font and audio controls.
Do not promise unsupported transitions, animated overlays, variable speed, arbitrary filters,
lossless/HDR output, every Unicode glyph or automatic transcription.

## Submit, preview and recover

1. Submit `edit_video` once with all inputs and one stable client_request_id. An intentional
   revision gets a new key; an ambiguous/timeout retry retains the same key and exact payload.
2. Immediately call `render_edit` with the returned operation_id, even when still processing.
   Use one live card per operation. It updates in place and provides playback with one download action. The finished card
   has no information dialog or manual status button; processing updates automatically.
   Never pass the operation_id to render_media or download_media: those use generation IDs.
3. Recover with `edit_status` using the same operation_id and the live tool’s bounded wait. Reopening or
   refreshing render_edit is read-only and never renders or charges again. Do not create a new
   operation to fix a missing preview, lost response or download failure.
4. On completed, deliver the card. If the host cannot render MCP Apps, deliver the final MP4
   URL from edit_status as a clickable link. Do not claim playback was checked unless observed.
5. Failed/cancelled jobs have no finished deliverable. Explain the returned error; change only
   the invalid timeline/input with user scope preserved. A payment_pending result is rendered
   but withheld pending settlement: retain the operation and resolve payment without resubmitting.
   Cancel only when requested, using edit_cancel; cancellation during publication may be refused.

Editing is charged separately from source generation. Report actual returned charges,
never a guessed exact quote or a copied price table. Use the live editing tool's supported
budget control when the user sets a ceiling; if it cannot enforce the ceiling, stop before
submitting. Status and preview calls do not incur new editing charges.
