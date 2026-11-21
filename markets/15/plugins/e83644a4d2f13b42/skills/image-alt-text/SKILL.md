---
name: image-alt-text
description: "Use when a Shopify store owner wants alt text (image descriptions) for product and store images, for SEO or for shoppers using screen readers, or asks why their images are missing alt text. Writes alt text with EA SEO & Page Speed Optimizer or EA Accessibility ADA WCAG EAA."
---

Goal: missing alt text filled in with short, accurate descriptions the merchant can review.

Good alt text: describes what the image shows in a few words (product, color, key detail), no "image of", no keyword stuffing; decorative images can stay empty.

Steps:
1. `list_apps`. EA SEO & Page Speed Optimizer and EA Accessibility ADA WCAG EAA both write alt text; use the one installed. If neither is, `find_ea_app` ("alt text for images").
2. `lookup` for that app (alt text or images) to see how many images are missing alt text.
3. `get_write_guide`, then `create_draft` with the alt text action for the images or products the merchant wants; it runs when published.
4. Show the preview card. If the tool reports an allowance or plan limit, say what it says and that the app shows the options.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
