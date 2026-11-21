---
name: tiered-cart-rewards
description: "Use when a Shopify store owner wants tiered rewards or discounts by cart value: 'spend $50 get 10% off, spend $100 get 15%', spend more save more, reward tiers that unlock a discount, free shipping or a gift. Sets it up with EA Rewards Bar & Free Gifts or the reward tiers of EA Sticky Add to Cart Drawer."
---

Goal: clear reward tiers with a progress bar, drafted with the merchant's amounts.

Design tips: two or three tiers are easier to understand than many; the first tier should be reachable for a typical order and the last a stretch. Use the merchant's numbers.

Steps:
1. `list_apps`. EA Rewards Bar & Free Gifts is the dedicated bar; EA Sticky Add to Cart Drawer has reward tiers inside the cart. If neither is installed, `find_ea_app` ("tiered discounts").
2. `get_setup` for the app, then ask for each tier: amount and reward (percent or amount off, free shipping, free gift).
3. `get_write_guide` for the app, then `stage_changes` (existing program or settings) or `create_draft`.
4. Show the preview card; it goes live when published. For quantity-based tiers (buy 2, buy 3), use quantity-breaks-and-bogo instead.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
