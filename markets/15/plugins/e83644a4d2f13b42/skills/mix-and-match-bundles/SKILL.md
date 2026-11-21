---
name: mix-and-match-bundles
description: "Use when a Shopify store owner wants product bundles: mix and match ('any 3 for...'), build-a-box / build your own bundle, frequently bought together, buy-together bundles or gift sets. Drafts the bundle in EA Bundles & Quantity Breaks. For quantity discounts on a single product, use quantity-breaks-and-bogo."
---

Goal: the right bundle type for the merchant's products, drafted with a preview.

Pick the type:
- Mix and match: any 2 / 3 / 4 items from chosen products or a collection count together for the discount.
- Build a box: shoppers fill a box from a collection on its own page; the merchant adds the "Build a box" block to a page in their theme editor.
- Buy together / frequently bought together: the viewed product plus related products, as a bundle or a popup after add to cart.
- Gift set: a ready-made bundle of products at a discount.

Steps:
1. `list_apps`; if EA Bundles & Quantity Breaks is missing, `find_ea_app` ("mix and match bundles") and share the link.
2. Ask for the products or collection and the discount. Use the exact product and collection names from the store.
3. `lookup` (app bundles, name templates) to confirm the template, `get_write_guide` for bundles, then `create_draft`.
4. Show the preview card. For build a box, remind them to add the block to a page after publishing.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
