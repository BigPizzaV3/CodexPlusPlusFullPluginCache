# Direct Etsy API through MakeBox

MakeBox is the authenticated intermediary. The chat reasons about the seller's request; the server sends the approved values to Etsy and returns the current Etsy response. The live MCP catalogue and each tool's input schema are authoritative. The October 1, 2026 server snapshot provides 105 official Etsy operations as distinct `etsy_*` tools.

For exact operation names/inputs use the [105-operation index](etsy-operation-index.md), [schema snapshot](etsy-tool-schemas.json) and [validated recipes](etsy-operation-recipes.md), checked against the local server implementation on 2026-10-04. They are references, not authority to execute illustrative IDs. Without MCP the plugin still provides drafting, audits, evidence analysis and manual field/settings worksheets.

## Choose the right path

Use a direct `etsy_*` operation when the seller asks for an Etsy action or supplies finished content. Direct calls use Etsy IDs, require no prior MakeBox import, do not run a MakeBox model, and do not debit MakeBox AI allowances. Existing plan gates and Etsy fees still apply.

Use MakeBox workflow tools only when the seller wants their additional behavior: local staging, keyword-database research, internal AI optimization, or a quoted bulk job. Do not run `optimize_listing` just to transmit copy already written in the chat.

Discover the relevant live tool before deciding a capability is unavailable. A limitation of one convenience tool does not establish an Etsy API limitation. Do not invent tool names, parameters or an arbitrary HTTP request; select the named MCP operation and use its current schema.

## Identity and authorization

1. Identify the connected workspace and task with `list_shops` and `get_account_status`.
   MakeBox workspace UUIDs are not Etsy shop IDs. Use `etsy_get_me` for the authorized Etsy user/shop IDs; private direct operations supply their shop identity server-side.
2. Read the current resource through the relevant direct tool.
3. Collect missing business facts. Never guess materials, price, maker, origin, processing times, rates, returns, buyer data or tracking.
4. Show the exact target and proposed values before an external write. Use the seller's explicit approval already given for that scope; do not ask again merely because it spans multiple tools. New targets, changed values or publication beyond the approved scope need authorization.
5. Set `confirm: true` only for an authorized write. Deleting a listing also needs `expected_title` matching the current Etsy title.
6. Read back the result and report the actual state.

Private shop and user identity is supplied by the server. Public research tools may accept another shop's ID; that does not authorize writes to it. Optional personal email and saved-address methods concern the connected Etsy user's account. If Etsy refuses a required scope, show the returned reconnect link and let the seller decide whether to grant it. Never ask for a password, token or API key.

## Request and response contract

- Fields at the tool's top level are path/query inputs such as `listing_id`, `limit` or `offset`. Write fields go inside `body` when the schema specifies it.
- Use the exact Etsy enum values. For example, direct listing creation uses the current Etsy `type` enum; do not substitute a convenience tool's `digital` label for an Etsy value such as `download`.
- Preserve the seller's values, omitted fields, explicit clears, zero, false and null as the schema allows. Do not inject defaults or extra SEO text.
- The direct layer applies Etsy's documented constraints. It does not impose the MakeBox generation rule of exactly 13 multi-word tags on a seller-approved direct update.
- `ok: true` and `accepted_by_etsy: true` with `verified: false` mean Etsy accepted the request. Follow the returned `readback` tool/arguments when present, or the corresponding direct read, before declaring a verified change.
- An error, timeout or `sync_status: unconfirmed` may leave the write outcome uncertain. Read first; never automatically repeat the write.
- Return the useful Etsy error and permission details. Do not invent a cause or describe an accepted request as a completed publication.
- Direct writes may leave MakeBox's imported web snapshot behind. A direct Etsy read is authoritative; a web refresh/sync updates the snapshot.

## Common routes

| Seller intent | Direct operations |
| --- | --- |
| Find/read listings | `etsy_get_listings_by_shop`, `etsy_get_listing` |
| Create an Etsy draft | `etsy_create_draft_listing`, then `etsy_get_listing` |
| Change text, category, shipping/return assignment or state | `etsy_update_listing`, then `etsy_get_listing` |
| Read/replace prices, quantities and variations | `etsy_get_listing_inventory`, `etsy_update_listing_inventory` |
| Read/replace personalization | `etsy_get_listing_personalization`, `etsy_update_listing_personalization` |
| Read shipping profiles and rates | `etsy_get_shop_shipping_profiles`, `etsy_get_shop_shipping_profile` |
| Read/manage processing profiles | `etsy_get_shop_readiness_state_definitions` and the matching create/update/delete operation |
| Read orders and line transactions | `etsy_get_shop_receipts`, `etsy_get_shop_receipt`, `etsy_get_shop_receipt_transactions_by_receipt` |
| Add tracking or mark shipped | `etsy_create_receipt_shipment` or `etsy_update_shop_receipt`; read the receipt afterward |
| Read financial records | `etsy_get_shop_payment_account_ledger_entries`, `etsy_get_shop_payment_by_receipt_id`, `etsy_get_payments` |
| Research public listings, shops and reviews | `etsy_find_all_listings_active`, `etsy_find_shops`, `etsy_get_reviews_by_listing`, `etsy_get_reviews_by_shop` |
| Check granted Etsy permissions | `etsy_token_scopes` |

These are routing examples, not a frozen exhaustive tool list. The current schema decides which parameters an operation accepts. Price and quantity updates use inventory in the current Etsy API; do not send fields that `etsy_update_listing` does not expose. Inventory and personalization updates can replace complete sets, so preserve existing options unless the seller approved removal.

## Media

For a seller-owned local file, use `get_upload_link` with authorized file access or let the seller upload through its browser page. The response gives an Asset Library `asset_id`. A direct binary field accepts an object such as `{"asset_id": 12, "filename": "product.jpg"}`, not a local path or image text.

For example, after approval, `etsy_upload_listing_image` takes `listing_id`, `confirm: true`, and a `body` containing `image: {asset_id: 12, filename: "product.jpg"}` plus supported fields such as `rank` or `alt_text`. Use the returned Etsy media ID and `etsy_get_listing_images` to verify. File and video operations follow their own live schemas. Existing Etsy media IDs can be reassociated without reupload when Etsy permits it.

Removing the last digital file can change the listing's product type according to Etsy's API. Deleting or editing a shared profile may affect multiple listings. Explain these concrete consequences before obtaining approval.

## Limits of the API

The official API surface is not every Etsy website feature. Do not promise general Etsy messaging, coupon or advertising controls absent from the live catalogue. Payment and ledger endpoints read records; they do not authorize refunds or transfers. Etsy may deny a method or field because of seller scopes, app-level permissions or business validation. Report that boundary honestly.

Reference: [Etsy Open API](https://developers.etsy.com/documentation/reference/).
