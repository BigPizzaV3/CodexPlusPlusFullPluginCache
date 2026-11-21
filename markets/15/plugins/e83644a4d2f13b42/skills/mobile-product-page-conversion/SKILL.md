---
name: mobile-product-page-conversion
description: "Use when a Shopify store owner wants more shoppers to add to cart from product pages, especially on mobile: a sticky add to cart bar, a buy button that stays visible, quick buy / quick add from collection pages. Uses EA Sticky Add to Cart Drawer."
---

Goal: the add to cart button always within reach, set up as a draft.

What helps:
- A sticky add to cart bar that stays on screen while shoppers scroll the product page (desktop and mobile settings are separate).
- Quick buy buttons on collection pages so shoppers add without opening the product.
- A cart drawer that opens after add to cart, so shoppers stay on the page.

Steps:
1. `list_apps`; if EA Sticky Add to Cart Drawer is missing, `find_ea_app` ("sticky add to cart bar") and share the link.
2. `get_setup` and `get_stats` for sticky_cart to see what's on and how often the bar is used.
3. `lookup` (sticky_cart, cart_settings) for the sticky bar or quick buy section, `get_write_guide`, then `stage_changes` with the keys to change (mobile and desktop as the merchant wants).
4. Show the card; it goes live when published.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
