---
name: exit-intent-discount-popup
description: "Use when a Shopify store owner wants an exit-intent popup, a welcome or first-order discount popup, or a discount code that shows to visitors who are about to leave. Uses EA Email Popup & Spin Wheel."
---

Goal: a popup with the right trigger and offer, drafted with a preview.

Guidance:
- Exit intent catches visitors who move to leave (on desktop) and works well with a one-time discount for an email.
- A welcome discount on the first visit works better after a short delay or some scrolling than instantly.
- Limit how often it shows, and hide it from customers who already signed up.
- Discount codes can be unique per shopper and expire; the app creates them in Shopify.

Steps:
1. `list_apps`; missing app: `find_ea_app` ("exit intent popup").
2. `get_setup` for popups: existing campaigns and their triggers, so two popups don't compete.
3. Ask for the offer, the trigger (exit intent, delay, scroll) and the pages.
4. `get_write_guide` for popups, then `create_draft` (new campaign) or `stage_changes` (change a trigger).
5. Show the preview card; live after publishing. To check a code later, `lookup` (popups, code) shows its status and use.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
