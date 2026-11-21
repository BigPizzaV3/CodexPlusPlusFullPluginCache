# Listing creation: field and tool guide

Use the seller's facts and approval. Read [Direct Etsy API through MakeBox](direct-etsy-api-guide.md) for the transport and result contract. This guide does not authorize a write by itself.

For content preparation, first use the [fact brief](product-brief.md) and [quality playbook](listing-quality-playbook.md). No MCP is needed to create a copy-ready packet: use the [handoff](../templates/listing-handoff.md), settings worksheets and [worked examples](worked-examples.md). The steps below concern connected execution, not prerequisites for drafting.

## Prepare the draft

1. Identify the workspace with `list_shops` and access with `get_account_status`. Workspace UUIDs are not Etsy shop IDs; `etsy_get_me` returns the authorized Etsy identity. Private direct operations bind the shop inside the server.
2. Read the current `etsy_create_draft_listing` schema. Confirm real price/currency, quantity, title, description, category and maker/provenance. Select Etsy's actual product-type enum: a download value in a direct tool must not be replaced with a convenience tool's `digital` label.
3. Prepare requested copy in the chat, or preserve seller-supplied finished copy. Use relevant research where requested. Do not add internal AI generation just to transmit this content. Follow Etsy's native tag limits; a separate generation rule is not grounds to reject a valid direct request.
4. Use the taxonomy reads for `taxonomy_id`. For physical goods, read shipping profiles and the exact selected profile's destinations/rates. Confirm origin, packed weight/dimensions and units when needed. Read return policies and show returns/exchanges/deadline before choosing one. Confirm sections and production partners as relevant.
5. Show the complete intended draft and media/option plan. After the seller approves the exact card, send `etsy_create_draft_listing` once with the approved `body` and `confirm: true`. It creates an Etsy draft; do not treat it as live publication.

## Complete and verify

- Read the returned listing with `etsy_get_listing`. No MakeBox import is needed for direct reads/writes. If creation is uncertain, inspect live listings before trying again.
- For a local photo, file or video, obtain an authorized upload through `get_upload_link` or the Asset Library. Use `asset_id` in the direct multipart field: `image`, `file` or `video`, according to the specific live schema. Existing Etsy media IDs may support reassociation.
- Use `etsy_upload_listing_image` and `etsy_get_listing_images` for photos; `etsy_upload_listing_file` and `etsy_get_all_listing_files` for digital downloads; `etsy_upload_listing_video` and `etsy_get_listing_videos` for existing videos. These upload/manage media and do not generate new images or video.
- Read the complete existing inventory before `etsy_update_listing_inventory`. Preserve every approved product, variation value, offering, price, quantity, enabled flag and processing/readiness value. Price and quantity belong to inventory in the current API. Do not replace a full table with just the changed cell.
- Read `etsy_get_listing_personalization` before a requested `etsy_update_listing_personalization`; preserve approved questions/options and explain complete-set replacement.
- Use `supports_multiple_personalization_questions: true` for new question types/multiple questions; direct options use `label`. Direct API text limits differ from local MakeBox staging; see [options guide](variations-personalization.md).
- Assign an existing shipping or return profile through `etsy_update_listing` using only the intended profile ID. Read the listing afterward. This can update an existing Etsy draft or active listing without changing its state unless that state change is explicitly sent.
- Read current language/translation information before supplying approved translations through the matching direct translation operation.

## Publication

Show the completed draft, media, options, price, delivery and return terms. Only explicit seller approval to publish permits `etsy_update_listing` with `body.state: "active"`. Etsy may apply its normal fees. Follow the returned readback hint and confirm the actual Etsy state.

The presence of an Etsy ID or an accepted HTTP request is not proof that every requested detail is complete. Report failed media transfers, validation errors and uncertain steps accurately.

## Optional MakeBox staging

If the seller specifically wants a MakeBox-local draft, saved variation configuration or internal AI workflow, use the corresponding MakeBox tools and their documented cost/sync behavior. Local staging is not an Etsy update. It is an optional workflow, not a prerequisite for direct API use.
