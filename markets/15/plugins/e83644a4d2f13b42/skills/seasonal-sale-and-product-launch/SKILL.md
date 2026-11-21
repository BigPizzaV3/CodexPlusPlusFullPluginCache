---
name: seasonal-sale-and-product-launch
description: "Use when a Shopify store owner is planning a sale or launch other than Black Friday: a flash sale, store-wide or seasonal sale, Valentine's Day, Mother's Day, Father's Day, Easter, back to school, Christmas gifting, a store anniversary, or a new product launch. Drafts the offer, countdown, announcement and popup with the EA apps."
---

Goal: the campaign pieces for this one event, scheduled for its dates.

Pieces to choose from:
- The offer: a sale offer, gift set or quantity breaks (EA Bundles & Quantity Breaks).
- Urgency: a countdown bar to the end of the sale or the launch moment (EA Countdown Timer Bar).
- The message: an announcement bar with the deal or the launch news, with a discount code if wanted (EA Announcement Bar Banner).
- The list: a popup for early access or launch updates (EA Email Popup & Spin Wheel).

Steps:
1. `list_apps`; `get_setup` for the installed apps to avoid clashing with running offers.
2. Ask for the event, the dates and time zone, the products and the discount (or none, for a launch).
3. Draft the two or three pieces that fit (`get_write_guide`, then `create_draft` or `stage_changes`), each with start and end dates.
4. Show each preview card and summarise the schedule. Missing app: `find_ea_app` with the event.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
