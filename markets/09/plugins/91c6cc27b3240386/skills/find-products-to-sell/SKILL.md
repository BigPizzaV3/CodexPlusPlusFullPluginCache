---
name: find-products-to-sell
description: Find supplier products a Hustle Got Real seller could list, from HGR's recommendations or similar to an existing listing, and add the chosen ones to a store. Use when the user asks for product ideas, products to sell, or products like one of theirs.
---

Use this skill to help the user find products and add the ones they choose. Explicit user instructions always take priority over these steps.

## 1. Pick the store

Call `hgr_list_stores`. If the user did not name a store and has more than one, ask which store to use. Use that store's `channelOAuthId` in every later call.

## 2. Find products

Choose the source that matches the request:

- **Recommended products:** call `hgr_list_recommended_products` with a `limit` close to what the user asked for (default 10). Present title, supplier price, suggested selling price and estimated profit, and link each title to its supplier page. Search filters are not available; sort or shortlist the returned items yourself if the user asks.
- **Products like one of theirs:** get the reference listing with `hgr_list_active_listings` or `hgr_get_listing_details`. Call `hgr_list_suppliers` for the store's country, then search the web only on those supplier sites for similar products. For each, give name, supplier, price and the exact product link. Never invent links or prices; if you cannot verify one, leave it out.

## 3. Add the chosen products

- Before adding anything, confirm the exact products, the store, and whether to hold them for review. Default to review before publishing unless the user says otherwise.
- For recommended products, call `hgr_publish_recommended_products` with each product's `id` and `title`, plus `needsReview`, `confirmed=true` and `impactConfirmed=true`.
- For supplier links, call `hgr_add_products_from_links` with the `urls`, `reviewBeforePublishing`, `confirmed=true` and `impactConfirmed=true`. To let the user review links visually first, call `hgr_open_store_manager` with `view` set to `add` and the `urls` instead.
- Leave `optimizeTitle` and `optimizeDescription` off unless the user asks for AI rewriting; it uses their AI tokens.

## 4. Report the result

- For links, report each status (for example Processed, DuplicatedUrl, InvalidUrl or NoQuota) and what it means.
- For recommended products, call `hgr_get_recommended_products_status` after a short wait and report any errors, such as a forbidden word.
- Tell the user where the products will appear: pending listings when held for review, or live after publishing.

Stop and explain if the store needs reconnecting, the quota is full, or a tool returns an error. Do not retry in bulk.
