---
name: black-friday-cyber-monday
description: "Use when a Shopify store owner is preparing a Black Friday, Cyber Monday, BFCM or holiday-season sale and wants the store ready: sale offers, a popup to build the list before the sale, a countdown, announcement messages and bigger-order offers. Plans and drafts the set with the EA apps."
---

Goal: a short BFCM plan for this store and drafts the merchant can review and publish on the right dates.

A typical setup (adapt to what the store has):
1. Before the sale: an early-access or sign-up popup to grow the list (EA Email Popup & Spin Wheel).
2. During the sale: the offer itself, e.g. tiered quantity breaks or a store-wide sale offer with a countdown (EA Bundles & Quantity Breaks), a countdown bar to the end of the sale (EA Countdown Timer Bar) and an announcement bar with the code or the deal (EA Announcement Bar Banner).
3. Bigger orders: a free shipping or free gift goal (EA Free Shipping Bar & Upsell, EA Rewards Bar & Free Gifts) and cart upsells (EA Sticky Add to Cart Drawer).
4. After the sale: switch the popup back to the regular offer.

Steps:
1. `list_apps`, then `get_setup` for the installed apps above to see what's already scheduled.
2. Ask for the dates and time zone, the discount and which products. Use start and end dates on every offer so it switches itself on and off.
3. Draft each piece (`get_write_guide` then `create_draft` / `stage_changes`), one preview card each, and list what will go live when.
4. For a missing app, `find_ea_app` ("Black Friday sale") and share what it returns.
Don't promise sales results; suggest checking `get_stats` after the first day.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
