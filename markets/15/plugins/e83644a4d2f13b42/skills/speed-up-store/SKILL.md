---
name: speed-up-store
description: "Use when a Shopify store owner says their store or site is slow, loads slowly, takes long to load or is slow on mobile, asks how to speed it up or make it faster, or wants a better PageSpeed or Core Web Vitals score (LCP, CLS, INP). Reads the store's own latest speed test with EA SEO & Page Speed Optimizer, finds the real causes (oversized images, missing lazy loading, app scripts, heavy sections) and drafts fixes that can be undone, such as image compression and lazy loading. For SEO fixes, use seo-audit-and-redirects."
---

Goal: measured speed, the biggest causes explained, and safe fixes drafted.

Facts:
- Speed scores vary between runs; compare runs on the same page and device, not single numbers.
- Shopify serves stores from a fast CDN, but oversized images, missing lazy loading, app scripts and heavy theme sections still slow pages down; the store's own speed test shows which of these apply here, so start from it rather than a generic checklist.
- Big wins are usually large images, too many apps or scripts, and heavy theme sections. The app compresses images (originals can be restored), adds lazy loading and preloading, and runs speed tests; theme code and other apps are the merchant's choice.
- Never promise a score or a sales lift.

Steps:
1. `list_apps`; if EA SEO & Page Speed Optimizer isn't installed, `find_ea_app` ("speed up my store").
2. `lookup` (page_speed) for the latest speed test (lookup speed_test) and image findings (lookup images), or `create_draft` with the speed test action from `get_write_guide` (runs when published, returns a job).
3. Explain the main issues on this store in plain words, with the numbers the test returned (score, LCP, the heaviest images).
4. Draft the fixes the merchant picks: apply speed fixes, compress images. The preview card says which can be undone.
5. After publishing, suggest a new speed test on the same page to compare.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
