---
name: store-performance-review
description: "Use when a Shopify store owner asks how their EA apps are doing, wants a weekly or monthly review of their offers, popups, cart and bars, or asks 'what should I improve next?'. Reads stats and suggestions across the EA apps on their store."
---

Goal: a short, honest review based on the store's own numbers, with two or three next steps.

Steps:
1. `list_apps` to see the installed EA apps and which are live.
2. For each live app, `get_stats` for the period asked (default 30d; this_month / last_month for calendar months), and `get_setup` when a number needs context.
3. `get_suggestions` (no `app`) for ideas based on the store's setup and numbers.
4. Answer with:
   - One line per app: the key numbers exactly as returned (e.g. bundle revenue, popup sign-ups, cart upsell sales), with the period.
   - What stands out (a campaign that gets views but few sign-ups, an app installed but not live).
   - Two or three next steps, offering to draft the first.
Rules: use only the numbers the tools return; say when a period has too little data; don't compare with other stores or promise results. These are aggregates only, never customer details.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
