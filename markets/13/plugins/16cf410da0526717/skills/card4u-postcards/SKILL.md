---
name: card4u-postcards
description: Create, preview, edit and explicitly order physical postcards with Card4U. Use for Card4U postcard requests and recovery from its tool errors.
---

Use the connected Card4U MCP tools for physical postcards. Check connection
status when ownership or paid ordering matters. Guests can create free drafts;
paid orders require the user's connected account and sufficient balance.

Use artwork_file for actual ChatGPT attachments, with the host-provided
download_url and file_id. Never invent either value. If a native host explicitly
accepts a local path for upload, its adapter uploads it; a raw remote MCP server
cannot read local paths. Otherwise request an attachment or reachable artwork_url.
artwork_base64 is inline data. Artwork is optional for a blank front.

The service renders message and recipient address on the back. Do not duplicate
them in front artwork. Format addresses in separate recipient, street, postcode/
city and country lines while preserving the supplied details. Ask for missing
details rather than inventing them. Fonts must come from list_fonts.

After creating or editing, use get_postcard until rendering has finished and
has_print_pdf is true. Share the returned view_url or claim_url. Inspect message,
address, estimated_cost_euro, currency, requires_warning, address_issues and
layout_warnings. Explain warnings and let the user correct the draft. Address
checks are formatting hints; they do not verify delivery. A layout warning can
exist even when address_state is valid.

Show the actual preview, recipient and current estimated price before ordering.
Call send_postcard only after the user explicitly confirms this specific paid
physical-postcard order. Order the reviewed UUID. A rendering response is not
an order confirmation; wait and retry as directed. Report only the order result
actually returned. Never claim a guaranteed delivery date.

Delete only an unpaid draft after the user explicitly requests deletion of that
draft. Paid/approved cards and bulk workflows are outside this deletion tool.
For execution errors explain the returned cause and recovery guidance; do not
claim success. On auth_required, request account linking. These tools cannot
purchase parcel labels, transfer credit to bank accounts or manage bulk orders.

For a new account-owned postcard, connect the intended account before creating the draft and verify owned=true. Use postcard_id exactly as returned by the successful create_postcard response for subsequent preview, edit and send calls in the same account. Never use sample UUIDs, a view URL, claim token, title or an ID from another account. If access fails, explain the returned error and check the connected account; do not try arbitrary IDs or claim an order succeeded.
