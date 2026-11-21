---
name: urgency-countdown-and-low-stock
description: "Use when a Shopify store owner wants urgency on their store: a countdown timer to the end of a sale, a timer per visitor, a 'only X left in stock' low-stock message, or a limited-time offer. Uses EA Countdown Timer Bar and EA Announcement Bar Banner (and limited-time offers in EA Bundles & Quantity Breaks)."
---

Goal: honest urgency that matches a real deadline or real stock, drafted with a preview.

Rules: only show a deadline that is real (the sale really ends) and stock counts from the store's inventory. Fake urgency hurts trust and can break consumer rules in some countries.

Options:
- Countdown bar to a fixed date and time, or a timer that runs per visitor (EA Countdown Timer Bar).
- Low-stock text using the product's real inventory, e.g. "Only {{stock_left}} left" (EA Countdown Timer Bar, EA Announcement Bar Banner); the write guide shows the exact text variable.
- A limited-time offer popup with a countdown (EA Bundles & Quantity Breaks).
- A Shopify discount code shown in the bar, created by the bar app.

Steps:
1. `list_apps`; missing app: `find_ea_app` ("countdown timer" or "low stock").
2. `get_setup` for the bar app; `list_items` to find the bar to change.
3. `get_write_guide` for countdown_bar / announcement_bar, then `stage_changes` on the bar or `create_draft` for a new one, with the end date and time zone.
4. Show the preview card; live after publishing.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
