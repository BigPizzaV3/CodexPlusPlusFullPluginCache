---
name: accessibility-statement-eaa
description: "Use when a Shopify store owner selling to customers in the EU asks about the European Accessibility Act (EAA), needs an accessibility statement page, or wants ongoing accessibility monitoring and reports. Uses EA Accessibility ADA WCAG EAA."
---

Goal: a published accessibility statement page and regular checks, with accurate wording.

Be accurate: the EAA applies to many online stores selling to EU consumers, with exceptions (for example some micro-enterprises). Whether and how it applies is a legal question for the merchant; don't give legal advice and never call the store compliant.

What the app does:
- Creates an accessibility statement page for the store, which the merchant reviews and edits.
- Monitors the store on a schedule and emails reports.
- Scans pages and suggests fixes, plus the shopper widget.

Steps:
1. `list_apps`; missing app: `find_ea_app` ("European Accessibility Act").
2. `get_setup` for accessibility; `lookup` (accessibility) for the current statement and monitoring.
3. `get_write_guide` for accessibility, then `create_draft` with the statement page action, or `stage_changes` for monitoring and report emails.
4. Show the preview card; live after publishing. Suggest the merchant reads the statement before it goes live and adds a link to it in the footer menu.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
