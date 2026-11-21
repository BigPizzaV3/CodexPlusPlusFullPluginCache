---
name: manage-etsy-shop
description: Plan or manage Etsy categories, attributes, variants, personalization, shipping/processing profiles, package measurements, returns, sections and seller settings using confirmed facts; prepare manual worksheets without MCP.
---

# Manage Etsy shop settings

Read [delivery/packaging](../../references/shipping-packaging.md) for shipping and [options/personalization](../../references/variations-personalization.md) for item choices. Read [operation recipes](../../references/etsy-operation-recipes.md) for connected actions. Offline, produce complete named settings and manual field steps without invented IDs.

## Select the resource

- Category/attributes: seller taxonomy and category properties; choose the most specific accurate supported option. Do not infer materials or assign unrelated occasions. `etsy_get_listing_properties` reads the list; single-property read may return501.
- Delivery: origin/destinations, processing versus transit, confirmed packed weight/size/units, actual service/rates. A profile name does not prove paid/free rates.
- Processing: actual ready-to-ship/made-to-order times and working calendar; readiness-state and shipping-profile unit enums differ.
- Returns: seller-approved returns/exchanges/deadline; custom goods do not automatically mean no returns.
- Variants/inventory: full sellable matrix and semantic readback; preserve unchanged combinations.
- Personalization: up to five questions and 1024 text characters in MakeBox/direct Etsy, practical instructions, complete existing set and prices preserved. Optional text supports a fixed fee; variation offerings use full item prices.
- Sections/partners: real organization/maker relationships, no SEO slogans substituted for factual attributes.

## Execute accurately

Identify shop, read resource and inspect live schema. Assign an existing shipping/return profile with `etsy_update_listing` using the exact profile ID; the connector can do this on existing listings. Changing destination prices requires the destination tool, not profile metadata update.

Before editing shared profiles, show the affected scope and reuse only authorization covering it. If the request is for one item, do not change every other listing. New profile creation and subsequent assignment are different steps. Deletion/consolidation may remove a resource or move many listings; surface that consequence. Read authoritative state after each approved action.

Use the [105-operation index](../../references/etsy-operation-index.md) when a capability is unclear; inspect schema before saying it is unavailable. Tools cover the published API, not every Etsy website feature. Keep acceptance separate from verification and do not retry uncertain writes. Return settings, affected IDs, readback, unresolved facts and next step.
