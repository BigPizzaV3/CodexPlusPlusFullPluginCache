---
name: get-started
description: "Use right after the merchant installs or connects EA Ecommerce Apps, or when they ask what it can do for their Shopify store ('what can you do?', 'set up EA apps', 'where do I start?'). Gives a short tour based on the EA apps on their store and one first step."
---

Goal: in one short answer, show the merchant what this plugin can do on their own store and get them to one useful first step.

1. Call `list_apps`. If it asks the merchant to sign in, tell them they can sign in with their Shopify store, then click Allow in their Shopify admin. Until then, `find_ea_app` and `list_ea_apps` work without signing in.
2. If no EA app is installed, ask what they want to improve (sales per order, email sign-ups, conversion, a sale, translation, accessibility or speed) and call `find_ea_app` with their answer.
3. If apps are installed, call `get_suggestions` (no `app`, so it covers every installed EA app).
4. Answer with:
   - The EA apps on the store, one line each on what they do there (live or not).
   - Two or three suggestions from `get_suggestions`, in plain words.
   - An offer to prepare the first one as a draft with a preview card.
5. Mention once that changes are drafts the merchant publishes, and that published changes can be undone.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
