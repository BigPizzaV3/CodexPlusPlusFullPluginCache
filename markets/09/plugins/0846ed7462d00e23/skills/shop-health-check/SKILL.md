---
name: shop-health-check
description: Use when the seller asks for a shop check-up, audit, "what should I fix", or weak listings. Produces a ranked fix list from live Etsy data without changing anything.
---

1. Call `get_shop`, then `list_listings` (page through all active listings; if there are none, or the seller asks, check drafts with `state: "draft"`). Done when every relevant listing is loaded.
2. Flag per listing: fewer than 13 tags, any tag over 20 characters, title under 100 characters, missing or very short description, few photos, zero stock on any variant (`get_listing_inventory` only for listings with variations).
3. Report a short ranked table: listing, problem, suggested fix. Top 10 by impact first; group the rest by problem type.
4. Offer to apply fixes. Do not call any `propose_*` tool until the seller picks which fixes to make.
