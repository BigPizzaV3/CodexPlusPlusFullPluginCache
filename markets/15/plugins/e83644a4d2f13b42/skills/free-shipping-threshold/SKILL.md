---
name: free-shipping-threshold
description: "Use when a Shopify store owner wants a free shipping threshold or goal ('free shipping over $75'), a free shipping progress bar, different goals per country, market or currency, or discounted shipping. Sets it up with EA Free Shipping Bar & Upsell (or the free shipping goal in the EA Sticky Add to Cart Drawer cart)."
---

Goal: a free shipping goal shoppers can see, in the right currency for each market.

Choosing the goal: a goal a little above the store's typical order value tends to nudge bigger orders; ask the merchant for their typical order value and shipping costs instead of guessing.

Important: the bar shows the goal; whether shipping is free at checkout depends on the store's Shopify shipping rates, or on the shipping discount the app can create. Check which one the merchant wants and say what each does.

Steps:
1. `list_apps`. EA Free Shipping Bar & Upsell is the dedicated bar; EA Sticky Add to Cart Drawer shows a free shipping goal inside the cart. If neither is installed, `find_ea_app` ("free shipping bar").
2. `get_setup` for the app: existing bars, goals per country or currency.
3. `get_write_guide` for free_shipping_bar (or sticky_cart), then `stage_changes` on the existing bar, or `create_draft` for a new bar: goal amount, messages before and after the goal, goals per country or currency for other markets.
4. Show the before and after card; it goes live when published.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
