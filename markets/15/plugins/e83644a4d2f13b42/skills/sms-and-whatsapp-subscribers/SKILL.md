---
name: sms-and-whatsapp-subscribers
description: "Use when a Shopify store owner wants to collect phone numbers for SMS or WhatsApp marketing: an SMS sign-up popup, email and phone together, or WhatsApp marketing consent. Uses EA Email Popup & Spin Wheel."
---

Goal: a popup that collects phone numbers with the right marketing consent, drafted with a preview.

Facts:
- A campaign can ask for email, phone (SMS) or both, including a separate phone step after the email.
- Shoppers who tick the consent box get SMS marketing consent on their phone number in Shopify; WhatsApp marketing consent can be asked for too.
- Sending SMS or WhatsApp messages is done by the merchant's SMS tool or Shopify, not by the popup.
- Consent rules differ by country; the merchant is responsible for the wording they use. Don't give legal advice.

Steps:
1. `list_apps`; missing app: `find_ea_app` ("SMS sign-up popup").
2. `get_setup` for popups to see whether a campaign already collects phone numbers.
3. `get_write_guide` for popups, then `create_draft` or `stage_changes` with the phone fields and consent options it lists.
4. Show the preview card; live after the merchant publishes it.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
