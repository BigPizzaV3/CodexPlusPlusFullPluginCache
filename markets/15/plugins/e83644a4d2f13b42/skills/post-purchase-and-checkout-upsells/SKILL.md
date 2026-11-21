---
name: post-purchase-and-checkout-upsells
description: "Use when a Shopify store owner wants offers after the order or at checkout: post-purchase one-click upsells, thank-you page or order status page offers, checkout upsells, or a popup before checkout. Drafts it in EA Bundles & Quantity Breaks."
---

Goal: an offer at the right step after or around checkout, drafted with a preview.

Where offers can show:
- Before checkout: a popup when the shopper clicks checkout.
- After payment: a one-click post-purchase offer, before the thank-you page.
- Thank-you page: product offers on the thank-you / order status page.
- In checkout: product offers inside checkout, only on Shopify Plus stores. Don't suggest it for other stores.

Steps:
1. `list_apps`; if EA Bundles & Quantity Breaks isn't installed, `find_ea_app` ("post purchase upsell").
2. `get_setup` for bundles to see existing post-purchase or thank-you offers.
3. Ask which products to offer (accessories, refills and consumables usually fit) and the discount, if any.
4. `lookup` (bundles, templates), `get_write_guide`, then `create_draft` with the template for that step.
5. Show the preview card; it goes live when the merchant publishes it.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
