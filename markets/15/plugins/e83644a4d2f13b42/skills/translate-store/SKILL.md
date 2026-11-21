---
name: translate-store
description: "Use when a Shopify store owner wants their store in other languages: translate the store, add a language, a multilingual store, a language selector, or selling to customers in other countries in their language. Uses EA AI Language Translate. For fixing specific translations or a glossary, use translation-glossary-and-edits; for currencies, use currency-switcher."
---

Goal: the right languages live on the store, with a selector shoppers can find.

What the merchant should know:
- Store translations are saved in Shopify, so translated pages can be indexed by search engines; a live Google Translate option can cover extra languages instantly.
- A language must be added and published in Shopify (with the merchant's Markets) for shoppers to see it; the app can publish and unpublish languages.
- Report each language's two facts separately: whether shoppers get it (get_setup: `publishedInShopify`, `offeredInSelector`) and how much of it is translated (% of fields). Never call a language enabled, active or live unless it is published; translations saved for a language that isn't published, or isn't a Store translation language any more, are not visible to shoppers.
- Running a full store translation is a one-time action that can't be undone as a whole; individual translations can be edited or reverted later, and the app keeps backups.

Steps:
1. `list_apps`; if EA AI Language Translate isn't installed, `find_ea_app` ("translate my store") and share the link.
2. `get_setup` for translate: per language, published to shoppers or not, offered in the selector or Off, and % translated; plus the selector settings.
3. Ask which languages and for which countries or Markets.
4. `get_write_guide` for translate, then `create_draft` with the translation action it lists (e.g. run store translation for a language) and `stage_changes` for selector settings.
5. Show the preview card, which marks one-time actions; a long run returns a job the merchant can follow in the app. Don't promise sales from new languages.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
