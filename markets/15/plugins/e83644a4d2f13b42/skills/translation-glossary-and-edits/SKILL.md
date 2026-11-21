---
name: translation-glossary-and-edits
description: "Use when a Shopify store owner wants to control or fix translations on their store: a glossary or 'don't translate' words (brand names), a wrong translation, find and replace across translations, theme or cart texts that stay untranslated, or images per language. Uses EA AI Language Translate."
---

Goal: the specific translation fixed, and future translations kept consistent.

Tools in the app (as drafts through this plugin):
- Glossary: words to keep as they are or to always translate one way; it can also be applied to existing translations (a one-time action).
- Edit or revert one translation.
- Find and replace across a language's translations, with a preview of the matches first.
- Images per language, and backups of translations before big changes.
- Theme texts (cart drawer, pop-ups and other theme strings) have their own section in the app's editor.

Steps:
1. `list_apps`; missing app: `find_ea_app` ("translation glossary").
2. `get_setup` for translate. Use `lookup` (translate) for the current translation of a text or the status of a job.
3. `get_write_guide` for translate, then `create_draft` with the action (glossary entry, edit, find and replace) or `stage_changes` for glossary settings.
4. Show the preview card; it marks one-time actions that can't be undone.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
