---
name: ab-test-offers-and-cart
description: "Use when a Shopify store owner wants to A/B test something on their store with the EA apps: two versions of a popup, of the cart drawer, or of a bar, and which one wins. Sets up and reads the test in EA Email Popup & Spin Wheel, EA Sticky Add to Cart Drawer or the EA bar apps."
---

Goal: a clean test of one change, and a fair read of the result.

Guidance:
- Change one thing per test (the offer, the headline, the layout), so the result means something.
- Let it run long enough for both versions to get a meaningful number of visitors and orders; small stores need weeks, not days. Don't declare a winner from a handful of conversions.

Where tests run:
- Popups: a B version of a campaign (EA Email Popup & Spin Wheel).
- Cart drawer: one cart A/B test at a time, version B = the settings that differ (EA Sticky Add to Cart Drawer); end it by keeping A or using B.
- Bars: a B version of a free shipping, announcement or countdown bar.
- Bundles offers: tested in the EA Bundles & Quantity Breaks app itself.

Steps:
1. `list_apps`; `get_setup` for the app to see a running test.
2. `get_write_guide` for the app, then `create_draft` / `stage_changes` with the test fields it lists.
3. To read a test, `get_stats` for the app; report the numbers for each version as they are, with how many visitors each had. Ending a test is a draft the merchant publishes.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
