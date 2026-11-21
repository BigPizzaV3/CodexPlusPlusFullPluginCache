---
name: age-verification-popup
description: "Use when a Shopify store owner needs an age check popup on their store, such as 'are you over 18 / 21?' or a date of birth check before shoppers can browse. Uses the information popup of EA Email Popup & Spin Wheel."
---

Goal: an age check popup with the merchant's minimum age, drafted with a preview.

Facts to tell the merchant:
- The popup asks the visitor to confirm their age (a yes / no question or a date of birth) and remembers the answer for a number of days.
- It is a self-declared check shown in the browser, not identity verification; whether that is enough depends on the merchant's products and local law. Don't give legal advice.

Steps:
1. `list_apps`; missing app: `find_ea_app` ("age verification popup").
2. Ask for the minimum age, yes / no or date of birth, the texts, and how long to remember a confirmed visitor.
3. `get_write_guide` for popups and use the information popup's age check fields, then `create_draft`. If the guide doesn't list them, tell the merchant it is set in the app's campaign editor under the information popup.
4. Show the preview card; live after publishing.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
