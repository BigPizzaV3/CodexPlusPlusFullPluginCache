---
name: quantity-breaks-and-bogo
description: "Use when a Shopify store owner wants quantity breaks, volume or bulk discounts, 'buy more save more', multi-packs, buy 2 get 1, BOGO or buy X get Y offers on product pages. Drafts the offer in EA Bundles & Quantity Breaks with a preview of the prices shoppers will see."
---

Goal: a quantity-break, multi-pack or BOGO offer drafted on the right products, with the discounted prices shown on the preview card.

1. `list_apps`. If EA Bundles & Quantity Breaks isn't installed, call `find_ea_app` ("quantity breaks") and share its Shopify App Store page.
2. Collect: which products or collection, the tiers (e.g. 2 = 10% off, 3 = 15% off) or the BOGO rule, and an end date if it's a promotion. Suggest sensible tiers if they ask, and say they are a starting point.
3. `get_setup` for bundles to avoid a second offer on the same products; `lookup` (app bundles, name templates) lists the offer templates (for example quantity breaks, buy more save more, multi-packs, BOGO bars, bulk buy, quantity breaks with a free gift).
4. `get_write_guide` for bundles, then `create_draft` with the template, products and tiers.
5. Show the preview card (prices after the discount per tier) and ask them to publish it, or change tiers with `edit_draft`.
6. After it runs a while, `get_stats` for bundles shows views, add to carts and revenue for the offer.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
