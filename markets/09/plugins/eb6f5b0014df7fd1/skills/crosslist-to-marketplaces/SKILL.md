---
name: crosslist-to-marketplaces
description: List the user's existing items on more marketplaces (crosslisting). Use when the user wants to post, list, copy or move items to Vinted, eBay, Depop, Etsy, Shopify, Facebook Marketplace, Poshmark, Mercari, Grailed or another marketplace, or asks which items aren't listed somewhere yet.
---

# Crosslisting

1. Call `list_channels` and use only the channel ids it returns. Never guess a marketplace name.
2. Find candidates with `list_products` and `not_on_platforms: ["<channel>"]`. Show title, price and
   the marketplaces each item is already on.
3. Name the items and the target marketplaces, then **ask the user to confirm**. Crosslisting
   publishes real listings.
4. Call `crosslist` with the `vid` values exactly as `list_products` returned them.
5. Report each marketplace's `status` honestly. `queued` means the seller's own browser extension or
   the FLUF app finishes the listing within minutes (Vinted and Facebook work this way). It has not
   failed, so don't resend it.
6. If a marketplace refused an item for a fixable reason, use the fix-failed-listings skill rather
   than calling `crosslist` again.
