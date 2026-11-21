# Direct operation recipes

Use the live schema before executing. These recipes use **illustrative IDs**, not existing resources. Replace them only with IDs obtained from the connected seller's reads. The machine-readable examples in [api-examples.json](../examples/api-examples.json) are for local validation; never replay them against a real shop.

## Identity and current data

`list_shops` and `get_account_status` identify MakeBox workspace/access; `etsy_get_me` identifies Etsy. `etsy_get_listings_by_shop` is scoped to the connected shop in this snapshot; do not supply `shop_id`. `etsy_get_shop_shipping_profiles` similarly binds shop internally and takes `{}`. Public operations may expose a shop ID: inspect each schema rather than generalizing from the tool name. Never pass a MakeBox UUID as an Etsy shop ID.

Read `etsy_get_listing` with `listing_id`. Inventory, personalization, images, files and videos have separate reads. Paginate with actual `limit`/`offset` support; report completeness. Raw public reads are current Etsy data; an imported MakeBox listing may be a stale mirror.

## New draft from chat-authored fields

Read seller taxonomy and relevant properties. Obtain real price/quantity/provenance and applicable shipping/processing/returns. `etsy_create_draft_listing` has required `body.quantity`, `title`, `description`, `price`, `who_made`, `when_made`, `taxonomy_id`; optional `type`, tags/materials/profile IDs follow the live schema. For download use native `type: "download"`. Send approved body with top-level `confirm: true`, then get the returned listing. Draft creation does not activate it.

Complete approved media, inventory, personalization and attributes. `etsy_get_properties_by_taxonomy_id` supplies property/value/scale IDs; `etsy_update_listing_property` uses `listing_id`, `property_id`, `body.value_ids`, `body.values` and optional `scale_id`. Do not guess IDs from attribute labels.

## Text and profile assignment

Example shape:

```json
{"listing_id": 1234567890, "confirm": true, "body": {"title": "Personalized Acrylic Desk Sign, Custom Name"}}
```

Use `etsy_update_listing` for approved title/description/tags, category/attributes exposed there, shipping/return/section assignments or state. Price/quantity changes belong to inventory in this snapshot, not this body's schema. For one profile assignment send only `body.shipping_profile_id` or `body.return_policy_id`; preserve state and text. Read listing and profile contents afterward.

Activation is a separate `body.state: "active"` write with publication authority and completed prerequisites. Creating a draft or approving a title does not authorize it. Deletion needs `etsy_delete_listing`, `confirm:true` and `expected_title` matching current readback; understand permanent consequences first.

## Shipping and processing

Shipping-profile metadata and destination rates are different resources. For a new fixed-rate profile, `etsy_create_shop_shipping_profile` requires title/origin and primary/secondary costs. Add or modify destination entries/upgrades with the corresponding direct tools. `etsy_update_shop_shipping_profile_destination` uses `shipping_profile_id`, `shipping_profile_destination_id` and `body` with actual rate fields. Read existing IDs/rates; do not equate profile title with paid/free service. See [shipping guide](shipping-packaging.md).

Read/create readiness-state definitions for processing. Their units differ from shipping-profile enums; use the exact schema. Shared-profile changes/consolidation require authority covering every affected item.

## Personalization

Read the full set; use `etsy_update_listing_personalization` with top-level `listing_id`, `supports_multiple_personalization_questions:true`, `confirm:true`, and `body.personalization_questions`. Native option labels use `label`. Preserve existing IDs and every retained question; inspect field constraints in [options guide](variations-personalization.md). Read back the set. Removal has a dedicated delete method; an empty-array POST is not a substitute.

## Inventory

Read full inventory and build a writable full set. `body.products[].offerings[]` requires numeric price, quantity, is_enabled and `readiness_state_id` (nullable where allowed). Do not send a read-only money object as price or omit required nullable fields. Preserve property mappings/SKUs and disabled combinations. The [options guide](variations-personalization.md) explains semantic comparison and limits. One uncertain result must be read before another write.

## Existing files/media

After seller-authorized upload to Asset Library, the direct field is an object, e.g. `body.image: {"asset_id":12,"filename":"sign.jpg"}`. Images use `etsy_upload_listing_image`; downloaded files use `etsy_upload_listing_file` with `body.file`; videos use `etsy_upload_listing_video` with `body.video`. Multi-video handling uses the live `is_multi_video` argument when needed. Preserve current media and verify IDs/order using the list read. These operations do not generate content or accept arbitrary local paths.

## Orders and errors

Use receipts and receipt transactions for order state; financial reads are separate. `etsy_create_receipt_shipment` can send a buyer notification and requires real tracking/dispatch information. No label purchase/refund/general message tool is implied.

If a tool is missing in the client, preserve work, explain refresh/reconnect where appropriate and offer manual steps. A schema error should be repaired before a write; a timeout/uncertain acceptance requires readback before retry. Keep exact Etsy errors and field-level results; never report everything succeeded after partial media failure.
