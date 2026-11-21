---
name: free-gift-with-purchase
description: "Use when a Shopify store owner wants to give a free gift with purchase: a gift when the cart reaches an amount, a gift with a product or bundle, or a gift link for a campaign. Sets it up with EA Rewards Bar & Free Gifts, EA Sticky Add to Cart Drawer or EA Bundles & Quantity Breaks."
---

Goal: a free gift that is added the way the merchant wants and is actually free at checkout.

Pick the mechanism:
- Gift when the cart reaches an amount, with a progress bar: EA Rewards Bar & Free Gifts (also a cart goal in EA Sticky Add to Cart Drawer).
- Gift when buying a quantity or a bundle (e.g. buy 3, get a gift): EA Bundles & Quantity Breaks.
- Several gifts to choose from: the Rewards gift picker.

Steps:
1. `list_apps`; missing app: `find_ea_app` ("free gift with purchase").
2. Ask for the gift product (exact title or handle), the amount or quantity that unlocks it, and the dates.
3. `get_setup` for the app, then `get_write_guide` and `create_draft` / `stage_changes`.
4. Show the preview card. Remind the merchant that the gift product must be in stock and available on the online store.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
