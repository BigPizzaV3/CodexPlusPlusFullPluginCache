# Variations, inventory and personalization

Read this before complete listing creation or any options change. Distinguish a product option that affects a sellable combination from buyer-entered personalization information.

## Design the buying choices

Prepare `choice | values | price/stock impact | SKU | image mapping | processing impact`. Keep labels short and understandable. Use actual offered colors/sizes, not all colors visible in a chart. Do not imply a decorative prop is an option. Confirm which combinations are unavailable; an enabled combination with zero quantity is different from deleting it.

A custom text field is suitable for a name; a size/color variation is suitable for selecting a priced/stocked item. Do not hide paid options in free-text instructions or combine unrelated items into a misleading price range. Digital listings do not support ordinary physical-product variations; provide separate accurate listings/file bundles when needed.

## Full inventory replacement

1. Read `etsy_get_listing_inventory` and current variation-image links. Get category/property capabilities from `etsy_get_properties_by_taxonomy_id`.
2. Build a complete matrix of property values/products and offerings: SKU, price in the shop currency, quantity, enabled state, readiness/processing IDs and price/quantity/SKU/readiness property mappings.
3. Patch only approved cells. Preserve every other product/option and dependency. Do not blindly resend a GET response containing read-only IDs or money objects: transform to the current writable schema, including numeric price values using the returned divisor/currency correctly.
4. Preview before/after values and removals. Obtain authorization for that scope, then call `etsy_update_listing_inventory` once.
5. Read back full inventory and compare **semantics**: property/value combination, currency/price, quantity, enabled state, SKU, processing and mapping. Etsy may reorder products or replace generated IDs. Array order/IDs alone cannot establish a mismatch.

A mismatch/timeout means the state is unconfirmed until read. Never retry the write automatically; changes may already exist. Record which fields agree and which remain unresolved.

MakeBox's current implementation supports up to three axes, 70 options per axis, 400 products when price or quantity varies on every axis, and 2500 products otherwise. Shop/API rollout and live schemas may be narrower; verify eligibility. A third axis must not be forced through a two-axis client. Price/stock configuration and Cartesian-product size must be checked before constructing an enormous payload.

## Personalization: current direct API versus MakeBox staging

The direct migration supports 1–5 questions and at most one upload-type question. Text responses can allow 1–1024 characters; MakeBox's updated web editor and MCP support the same 1024-character ceiling. Use the route's actual constraint. A short name field should usually have a practical small limit rather than the maximum.

Each question has `question_text`, `question_type`, `required`. A question title is 1–45 characters; instructions, when allowed, are at most 120. `text_input` needs `max_allowed_characters`; upload questions need `max_allowed_files` (1–10); `labeled_upload` requires at least two files and matching labels. `dropdown` needs 1–30 unique option labels up to 20 characters and no instructions. Direct options use `label`, not the local staging helper's `value` shape. Check the official migration/live schema for additional text constraints and shop availability.

Read `etsy_get_listing_personalization` first. `etsy_update_listing_personalization` replaces the **entire set**. Set top-level `supports_multiple_personalization_questions: true` for multi-question/new-type writes and preserve existing question/option IDs where supported. Removal uses `etsy_delete_listing_personalization`; do not assume an empty POST array can clear it.

Original single-text example: title `Name for your sign`, instructions `Enter the name exactly as it should appear. Example: Olivia. Maximum 24 characters.`, required true, limit 24. Mention any actual proof/correction process in the description, not a fabricated promise. Do not collect unnecessary buyer personal information.

## Supported pricing

A variation offering contains the full item price in the shop currency. If the base item is $25 and a larger option costs $5 more, that offering price is $30, not $5. Preserve every other combination's price/stock/SKU; do not apply a second fee for an option already included in its price.

Optional `text_input` questions (`required: false`) support a fixed `add_on_price`. The fee is applied when that field is used, regardless of text length. Etsy's range is $0.20–$500 USD equivalent; writes use a number in shop currency. Required text, dropdowns and uploads cannot have this surcharge. Never promise a per-letter formula.

Read prices as Money: `amount / divisor`, preserving `currency_code`. On update include the existing question ID and explicit numeric `add_on_price` to preserve/change it, or `0`/`null` to remove it. Do not omit an existing fee after Etsy's migration window. One fixed optional engraving field might use `add_on_price: 5`, `max_allowed_characters: 1024`; obtain seller approval for that buyer charge.

MakeBox `set_listing_personalization` uses `fields[].title/type/max_characters/add_on_price`. Direct `etsy_update_listing_personalization` uses `body.personalization_questions[].question_text/question_type/max_allowed_characters/add_on_price` and `supports_multiple_personalization_questions:true`. Both validate the configuration; connected writes require semantic readback of all fields and fees. `get_listing_personalization` returns current Etsy data unless a local pending draft is being edited. A failed read must not be presented as an empty configuration.

Reference: [Etsy add-on pricing](https://developers.etsy.com/documentation/tutorials/personalization-addon-pricing/).

## Offline output

Return a settings table and exact question text/instructions/type/required/limit. Return the full variant table for manual entry, with unavailable combinations noted. Explain which changes are proposals rather than configured Etsy fields. Never fabricate a taxonomy/property/profile ID. Use [handoff template](../templates/listing-handoff.md).

Source checked 2026-10-04: [Etsy personalization migration](https://developers.etsy.com/documentation/tutorials/personalization-migration/). Implementation snapshot: MakeBox personalization and Etsy-limit modules. Current API documentation corrects older schema prose describing only one text field; verify the live response when rolling out newer types.

An unrelated SEO/content push preserves even a single existing Etsy question when MakeBox only has a legacy snapshot. Editing the question requires a read of its current full configuration and approval of the replacement.
