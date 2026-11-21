---
name: formatry-api
description: Create advertising images and animated banners from product photos and brand copy, adapt designs for posts and stories, and edit saved Formatry creatives.
---

# Formatry API

Use the bundled hosted `formatry-api` MCP tools for Formatry previews and saved Studio creative workflows. Local stdio is a developer-only opt-in and is not the plugin default.

## Workflow

### 1. Connection and Authentication
Call `formatry_connection_status` only when account or authentication context is unknown or an operation returns 401. If authentication is missing, start native OAuth sign-in (`codex mcp login formatry-api` in Codex). Keep identity verification and terms/permission choices in the connection window; never ask for passwords or codes in chat. Only mention a scoped key at `/studio/settings/developer` when the user explicitly chose manual API-key configuration; never ask them to paste the secret.

### 2. Standalone Previews
When the user asks for a preview without an existing creative, call `formatry_create_preview` directly with a stable `idempotencyKey` and a supported `sizeId`. For example, `sizeId: "square-1080"` selects a 1080×1080 canvas; `square` is not a valid id. A custom format needs matching `sizeId` and `customSize.id` (such as `custom-1080x1080`) plus numeric width/height, not dimensions alone. Use the tool schema for other supported formats. Do not make preparatory balance, quota, or asset listing calls: the preview endpoint enforces rate limits and quota internally and returns quota metadata in its response. Inspect `formatry_get_preview_quota` only when the user explicitly asks about preview limits, when planning large batch previews, or upon receiving `429 PREVIEW_QUOTA_EXCEEDED` / `PREVIEW_RATE_LIMITED`.

Use `copy.headline` for the main text, `copy.subtitle` for supporting text, `copy.cta` for the action and `copy.descriptor` for a footer note; `title` is not a copy field. Present the actual returned image or moving preview using the host's native image/resource presentation; a prose description does not show the preview. If the host collapses tool images, the existing image remains in that tool result: open it when supported instead of rendering again. State a real host display limitation plainly rather than claiming an unseen preview was shown.

### 3. Saved Studio Creative Workflows
For campaign design or editing existing work, do not generate generic standalone previews:
- **Inspect State:** Use `formatry_get_studio_creative` to read the exact persisted revision.
- **Preview Saved Creative:** Use `formatry_create_studio_creative_preview` for Images stills. For Animation, use `formatry_create_studio_animation_preview` to inspect the moving WebP.
- **Apply Edits:** Use the explicit operation tool (e.g. `formatry_set_studio_copy` for copy, `formatry_apply_studio_preset` for presets) with matching target IDs, UUID `commandId`, exact `expectedRevision`, and stable `idempotencyKey`. Re-read the creative revision and preview the exact updated revision after changes.
- **Campaign Creation & Multi-variant details:** See [references/campaign-export-workflow.md](references/campaign-export-workflow.md).
- **Animation Details:** See [references/animation-banners.md](references/animation-banners.md).

### 4. Quoting and Delivery
1. Call `formatry_create_studio_export_quote` with `current` or `selected` output scope to display the output set, billing mode, and applicable cost/allowance.
2. For free raster quotes: confirm the authorized output set via `formatry_confirm_studio_export_quote` using the quote ID and idempotency key. Honor any request to wait for separate confirmation; a quote-only request never authorizes export.
3. For non-free Images or Animation: inspect balance, present the fresh quote's ordinary credit cost (`fundingSource: account_balance`), and require explicit approval before calling `formatry_confirm_credit_export` with exact matching `approvedUnits`.
4. Await completion with `formatry_wait_for_generation_job`, verify a ready `formatry_get_artifact_manifest`, and retrieve files using `formatry_download_artifact_file` (or the native file helper in Codex).

### 5. Local File Handling in Codex
Use the bundled helper `scripts/formatry-files.mjs` for local filesystem files. Local paths are never passed to remote MCP tools. For local uploads use `formatry_prepare_asset_upload` and `formatry_complete_asset_upload`; for downloads use `formatry_prepare_artifact_download`. See [references/native-file-helper.md](references/native-file-helper.md) for complete file and video container guidelines.

## Boundaries

When the user wants to edit visually, call `formatry_open_studio` with the saved creative's `projectId` and `creativeId`. In MCP Apps hosts this opens the interactive surface for that same creative. A successful opener alone does not prove the interface appeared. After manual edits, read the current saved revision before the next agent command; reconcile conflicts instead of overwriting newer changes. If the host lacks embedded UI support, state that limitation and continue with actual tool previews and delivered files.

- Support Images (PNG/JPG/WebP) and Animation (animated WebP, GIF, MP4). The separate Video workspace and HTML5 export are unavailable. Native file ingestion can store an existing video in the `media` slot; it cannot bind that video into an Images or Animation scene. App Store packs, review documents and editable vector outputs remain outside this plugin.
- Do not call internal Formatry admin, payment, worker, renderer, or storage routes.
- Do not print API keys, signed upload URLs, signed download URLs, cookies, or payment data.
- Do not store raw IP addresses, user agents, client markers, temporary trial secrets, or signed URLs in evidence.
- A preview is not a downloadable deliverable. Require a succeeded generation job and ready artifact manifest before returning files. Never initiate checkout or purchase credits/subscriptions. Non-free exports consume only the exact approved cost from the existing ordinary account balance through `formatry_confirm_credit_export`. Animation never uses the free-image confirmation route.
- Pass local paths only to the bundled helper under the host's ordinary filesystem and execution permissions. Never put local paths into remote MCP arguments. The local trial tool and developer-only stdio server are not part of this workflow.
