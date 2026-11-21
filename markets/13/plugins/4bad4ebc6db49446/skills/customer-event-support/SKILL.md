---
name: customer-event-support
description: Find Eye.Photo customers and photos, inspect processing and edit summaries, check event readiness, retrieve artwork and prepare event exports.
---

Follow the shared [account connection and permissions](../../scripts/AUTHENTICATION.md) instructions. Determine the permissions needed for the current task before initial account setup, preserve the task through host-managed authorization, and use the get-started workflow to select an authorized studio.

If the account is disconnected or a startup connection call returns **Unknown tool**, **Tool not found**, or is unavailable, follow connection recovery immediately: show a real **Connect Eye.Photo** link from `../../scripts/CONNECTION.json` when present and validated by the shared instructions, otherwise [Connect Eye.Photo](https://chatgpt.com/settings/plugins-settings). Tell the user to open **Settings → Plugins → the installed Eye.Photo plugin → Connect**, sign in, approve their studio, then return and say **Connected** so this same request can continue. A connection-tool lookup failure alone does not establish a backend defect. Do not finish with only the error or repeatedly call missing tools.

Establish the selected studio. Search customers using name, exact email or phone with `customer_search`, then `customer_get` when needed. Resolve ambiguous matches before preparing changes. Use `photo_search` by customer, event, reference, processing status or inclusive local dates; use `photo_get` and `photo_edit_history` for detail. Follow `next_offset` pagination; do not claim a complete search after reading one page.

When visual browsing will help, use `photo_finder_show` with the resolved studio and optional customer/event/search filters. Its compact card shows at most eight thumbnails per page, supports filters and scoped photo details, and refreshes expiring previews. Keep data tools available when the host cannot display UI. Do not duplicate the card's entire contents in chat.

Use `event_search`, `event_get` and `event_customer_status` to inspect events and readiness. Obtain artwork with `event_art_files`. Preserve identifiers and statuses returned by tools; queued or processing work is not finished. Use returned dashboard links for customer updates, photo reassignment/retry and event creation.

Use `event_progress_show` for a resolved event when progress or export downloads benefit from a card. It shows actual finished/processing/failed photo counts and art readiness; uploads alone do not mean processing is finished. Merely showing it creates nothing. Its explicit Create export action emails the requester on completion, so explain that consequence before requesting an export. The card uses the separately exposed export tools and stops polling when work finishes or the card closes.

When asked to export artwork, first quietly check `plugin_connection_status` with required_scopes ["studio:read", "exports:create"]. If permissions_ready is false, use the shared native authorization flow for those scopes; continue the same export request afterward. Once permissions are ready, call `event_art_export_create` with one unique idempotency key for the logical request. Reuse that key and the identical arguments for ambiguous retries. Poll `event_art_export_get` sparingly until completion or failure, then use `event_art_export_files` with pagination to get download links. Refresh expiring links through the corresponding get/files tool instead of re-enqueueing jobs. If the key conflicts, inspect the original operation before starting a genuinely new request.

Present the selected studio, customer or event, actual progress and expiring downloads. Render tool-provided images inline when useful. Only share the personal data necessary for the user's task. Do not send general artwork emails; that is a dashboard task in v1.
