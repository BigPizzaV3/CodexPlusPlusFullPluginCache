---
name: slide-cart-drawer
description: "Use when a Shopify store owner wants a slide-out cart drawer / side cart instead of their theme's cart, or wants to change how their cart drawer looks or behaves (layout, colors, texts, buttons, trust badges, express checkout buttons). Uses EA Sticky Add to Cart Drawer."
---

Goal: the cart drawer set up or changed the way the merchant wants, as a draft they preview.

1. `list_apps`. If EA Sticky Add to Cart Drawer isn't installed, `find_ea_app` ("cart drawer") and share the link. After installing, the app embed must be on in the theme (the app's setup shows how).
2. `get_setup` for sticky_cart: is the drawer on, which template, which extras (upsells, goals, trust badges, express checkout).
3. For a specific setting, `lookup` (app sticky_cart, name cart_settings, with a section or keys) shows the setting keys and current values.
4. `get_write_guide` for sticky_cart, then `stage_changes` on the settings item with only the keys to change.
5. Show the before and after card. Changes reach the storefront when the merchant publishes them; they can be undone.

Don't promise that the drawer replaces every theme's cart in the same way; if the theme's own cart still opens, the app's setup has a switch to turn the theme's cart drawer off.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
