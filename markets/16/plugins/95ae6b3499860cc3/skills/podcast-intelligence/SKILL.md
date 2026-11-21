---
name: podcast-intelligence
description: Use SpotsNow to research podcast advertising, discover shows and inventory, analyze brands and networks, prospect advertisers, and create or edit campaign plans.
---

# SpotsNow podcast intelligence

Use SpotsNow when the user needs podcast advertising research, advertiser
prospecting, inventory discovery, or campaign and bundle planning.

## Resolve names and classifications first

- Use `resolve_entity_ids` for podcast or network names before calling tools that
  require `podcastId`, `podcastIds`, or `networkId`. Never invent UUIDs.
- Use `list_classifications` before applying an industry or category filter.
  Pass category slugs and exact industry names returned by that tool.
- Brand tools require bare domains. Ask the user to confirm a domain when it is
  missing or ambiguous; `resolve_entity_ids` does not resolve brands.

## Podcast and network research

- Use `find_podcasts_by_audience_description` for audience or demographic
  discovery. Without audience descriptions, include a budget and at least one
  demographic filter. Treat `campaignBudget` as total budget and
  `maximumOneAdBudget` as the explicit per-spot cap.
- Use `get_podcast_details` for catalog, estimated CPM, demographics, ad-load,
  host, and stored social data. Request only the sections needed.
- Use `get_batch_lookalike_shows` for shows similar to known podcasts.
- Use `get_new_performing_podcasts` for shows newly attracting repeat buyers.
- Use `get_network_podcasts` to explore or rank a network catalog.
- Use `get_bulk_podcasts_fill_rate` for monetization and fill-rate questions
  across shows or a network.
- Use `get_podcast_recent_ads` for the most recently detected audio/RSS and
  YouTube ads. Recency is based on episode publication time, not spend.

## Brand, sponsor, and industry intelligence

- Use `get_brand_details` for brand profiles, category buying behavior, and
  estimated spend. Request only needed sections and label estimates.
- Use `get_brand_sponsored_shows` for where a brand advertises, including top
  spend, recent activity, new sponsorships, and churned shows.
- Use `get_podcast_advertising_brands` for a podcast's leading sponsors or all
  brands detected in the last three months.
- Use `get_industry_details` for industry spend trends, brands, ads, and shows.
- Use `get_network_prospect_brands` for brands that fit a network but have not
  advertised on it.
- Use `get_reference_brand_prospect_shows` to find shows repeat-bought by a
  comparable advertiser that the prospect does not already buy.

## Inventory discovery

- Use `discover_ad_inventories` to find eligible inventory for a target
  audience. Respect viewer permissions and price masking.
- Suggest dates only from `spots[].availableWeeks`; listing start and end dates
  are not bookable weeks.
- Treat `availabilityCheckedAt` as a snapshot, not a reservation. Refresh
  discovery before confirming dates.
- Keep monthly starts at least 30 days apart for a listing.
- Display reach with `reachSource`; label `audienceSize` as estimated show
  audience.
- Prefer inventory CPM. Only if it is absent and unmasked, use the basic
  estimated CPM from `get_podcast_details` and label it as estimated.
- Confirm inferred brand audiences before discovery and include `bookingUrl`
  when returned. Discovery does not book or purchase inventory.

## Read plans and bundles

- Use `list_plans` to find campaigns and bundles. Filter rather than scanning
  every plan.
- Use `get_plan` to read status, budget, edit permission, shows, fit reasons,
  ad counts, and selected listings.
- Use `get_bundle_weeks` before editing bundle dates. Use only IDs and live
  weeks returned by that call, and follow pagination when needed.
- Generated plans may be asynchronous. Empty shows can mean generation has not
  completed; do not describe that as a failed or completed plan.

## Create or edit plans

These five tools change saved plan state. Do not invoke them until the user has
confirmed the material inputs or exact edit.

- `generate_campaign`: require confirmed `brandDomain`, `budget`, and
  `targetAudience.descriptions`. Suggest audience descriptions for confirmation.
  Offer optional demographic, existing-advertiser exclusion, and competitor
  exclusions without assuming them. Share the returned link and do not claim
  asynchronous generation is complete.
- `generate_bundle`: follow the same confirmation rules and explain that it uses
  active internal SpotsNow inventory. Share `bundleUrl` without claiming the
  bundle is complete.
- `add_plan_podcasts`: resolve show names, show the final list, and get
  confirmation before adding. This changes the plan only.
- `remove_plan_podcasts`: use podcast IDs from `get_plan`, show the final list,
  and get confirmation before removing. Removal is reversible and does not
  cancel bookings.
- `update_bundle_weeks`: call `get_bundle_weeks` first, show the exact
  add/remove week changes, and get confirmation. On a conflict, read live weeks
  again before retrying. This does not reserve inventory or place/cancel orders.

## Response and safety rules

- Never invent spend, audience, pricing, demographic, sponsorship, inventory,
  UUID, date, or plan data.
- Distinguish reported values from estimates and name the returned time period.
- Respect masking, authorization, edit permissions, and unmatched results.
- Ground recommendations in tool responses and make missing information clear.
- Do not expose private listener contact information or unnecessary internal
  diagnostics.
- Never claim that inventory was reserved or booked, a payment was made, an
  order was placed, outreach was sent, or a campaign was launched. The available
  write tools create and edit SpotsNow plans only.

