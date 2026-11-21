---
name: product-page-and-cart-upsells
description: "Use when a Shopify store owner asks where to show upsells or cross-sells: on the product page, after add to cart, in the cart drawer or on the cart page, or which products to recommend ('you may also like', 'complete the look'). Sets them up with EA Sticky Add to Cart Drawer and EA Bundles & Quantity Breaks."
---

Goal: upsells in the place that fits the store, drafted with a preview.

Placement guide:
- In the cart drawer: add-on products or recommendations while the shopper reviews the cart (EA Sticky Add to Cart Drawer). Works with manual picks, rules or Shopify's recommendations, and also in an empty cart.
- On the product page: upsell products under the add to cart button (EA Sticky Add to Cart Drawer) or recommendation cards (EA Bundles & Quantity Breaks).
- Right after add to cart: a popup with related products or a one-click "buy 2, make it 3" offer (EA Bundles & Quantity Breaks).
- On the cart page: recommendations on the cart page (EA Bundles & Quantity Breaks).

Steps:
1. `list_apps`; `get_setup` and `get_stats` for sticky_cart and bundles to see what already shows and sells.
2. Recommend one place first, based on what's missing; don't stack several upsells on the same step.
3. For the cart drawer: `get_write_guide` for sticky_cart, then `stage_changes` on its settings. For a Bundles popup or recommendation cards: `get_write_guide` for bundles, then `create_draft`.
4. Show the preview card. If a needed app isn't installed, `find_ea_app` with the request.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
