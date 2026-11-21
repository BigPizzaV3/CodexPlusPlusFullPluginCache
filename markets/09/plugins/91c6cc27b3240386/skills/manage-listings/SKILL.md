---
name: manage-listings
description: Review, find, edit, publish or hold Hustle Got Real listings. Use when the user asks about their active, pending or ended listings, wants to change a price, quantity, title or note, or wants to publish or pause a pending listing.
---

Use this skill for listing questions and changes. Explicit user instructions always take priority over these steps.

## Find listings

1. Call `hgr_list_stores` and resolve the store. Ask which one if several match.
2. Use the list tool for the state the user means: `hgr_list_active_listings`, `hgr_list_pending_listings` or `hgr_list_ended_listings`. Request only the `fields` you need, and use `sortBy`, `sortDirection` and `limit` for rankings such as "most expensive" or "lowest stock".
3. For one listing's full detail, variations and images, call `hgr_get_listing_details` with its `productId`. For trends, use `hgr_get_listing_price_history` or `hgr_get_listing_stock_history`.
4. Answer from the returned rows, and mention when results were limited.

## Change a listing

1. Identify the exact listing by `productId` (and `variationProductId` for one variation). If more than one listing could match, list the candidates and ask.
2. State the exact change: field, current value if known, and new value. If the user's request already states the exact change, that is their confirmation; otherwise ask before changing anything.
3. Call `hgr_update_listing` with only the fields that change and `confirmed=true`.
4. Report what changed. Changes reach the marketplace on HGR's normal sync schedule, so do not claim the marketplace already shows them.

## Pending listings

- To publish one now, confirm first, then call `hgr_publish_pending_listing` with its `pendingListingId` and `confirmed=true`.
- To hold one for manual review instead of automatic publishing, confirm first, then call `hgr_move_pending_listing_to_review` with its `pendingListingId` and `confirmed=true`.
- If a call returns `success: false`, say the change was not applied and suggest checking the listing in Hustle Got Real.

Never delete, end or bulk-change listings with this plugin; it has no tools for that. Do not change prices across many listings unless the user explicitly asks for each one.
