---
name: grow-email-list
description: "Use when a Shopify store owner wants more email subscribers: grow the email list or newsletter, collect emails, a sign-up popup with a discount, a spin-to-win wheel, scratch card or mystery discount popup, or connecting sign-ups to their email marketing tool. Uses EA Email Popup & Spin Wheel. For SMS or WhatsApp sign-ups, use sms-and-whatsapp-subscribers."
---

Goal: a sign-up popup that fits the store, drafted as a campaign with a preview.

Choosing the format:
- Spin to win, scratch card or mystery discount: playful, good for broad audiences and sales periods.
- A classic email popup with a welcome discount: simple and calm, good for premium brands.
- A small teaser or side tab so the popup doesn't block the first visit.
Timing and targeting matter as much as the design: a short delay or exit intent, and not on every page.

Steps:
1. `list_apps`; if EA Email Popup & Spin Wheel isn't installed, `find_ea_app` ("grow my email list") and share the link.
2. `get_setup` and `get_stats` (30d) for popups: live campaigns, views, sign-ups.
3. Ask for the offer (e.g. 10% off the first order, or no discount), the look (wheel, scratch, classic), and where it should show.
4. `get_write_guide` for popups, then `create_draft` for a new campaign (or `stage_changes` to change a live one).
5. Show the preview card; it goes live when the merchant publishes it.
6. Sign-ups go to Shopify customers with email marketing consent and to the email tools the merchant connected in the app. Subscriber contact details never come through this plugin: `lookup` (popups, subscriber_export) gives a link to the Subscribers page in their admin.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
