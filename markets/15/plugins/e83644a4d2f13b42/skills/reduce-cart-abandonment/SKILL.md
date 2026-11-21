---
name: reduce-cart-abandonment
description: "Use when a Shopify store owner says shoppers add to cart but don't buy, asks how to reduce cart abandonment or 'abandoned carts', or wants to improve their conversion rate from cart to checkout. Plans on-site fixes with EA Sticky Add to Cart Drawer and EA Email Popup & Spin Wheel. Does not send abandoned-cart emails."
---

Goal: on-site changes that address the common reasons shoppers leave, drafted one at a time.

Common causes and fixes:
- Surprise shipping cost: show a free shipping goal in the cart (EA Sticky Add to Cart Drawer) or a free shipping bar (EA Free Shipping Bar & Upsell).
- Doubt at the last step: trust badges, express checkout buttons and a clear checkout button in the cart drawer (EA Sticky Add to Cart Drawer).
- Leaving to "think about it": an exit-intent popup that captures the email with an offer (EA Email Popup & Spin Wheel), so the store can follow up through its email tool.
- Cart opens on a separate page: a slide-out cart drawer keeps shoppers on the page (EA Sticky Add to Cart Drawer).

Abandoned-checkout emails are sent by Shopify or the merchant's email app, not by the EA apps; say so if they ask.

Steps:
1. `list_apps`; `get_setup` and `get_stats` for sticky_cart and popups.
2. Pick the one or two fixes the store doesn't have yet and explain why.
3. Draft them (sticky_cart: `get_write_guide` then `stage_changes`; popups: `get_write_guide` then `create_draft`).
4. Missing app: `find_ea_app` ("reduce cart abandonment").

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
