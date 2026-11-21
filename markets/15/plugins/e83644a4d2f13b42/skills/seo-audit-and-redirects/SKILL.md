---
name: seo-audit-and-redirects
description: "Use when a Shopify store owner wants an SEO check of their store, to fix broken links or 404 pages, add URL redirects, improve meta titles and descriptions, structured data / rich results, a sitemap page, robots.txt rules or an llms.txt file for AI search. Uses EA SEO & Page Speed Optimizer. For load speed, use speed-up-store."
---

Goal: the store's SEO issues found, explained in plain words, and the fixes drafted.

What the app does:
- SEO check of the store or one page, with fixes the merchant can apply.
- Broken links: redirect them to a working page; add or remove URL redirects.
- Meta tags and structured data for rich results; an HTML sitemap page; an llms.txt file; hide pages from search.
- robots.txt rules: the app prepares them; the merchant adds them to the theme's robots.txt template, so they are live only after that step.
Be honest: rankings depend on many things; never promise a position or traffic.

Steps:
1. `list_apps`; if EA SEO & Page Speed Optimizer isn't installed, `find_ea_app` ("SEO broken links redirects").
2. `get_setup` for page_speed; `lookup` (page_speed) for the latest SEO check, fixes, redirects.
3. To run a new check: `create_draft` with the SEO check action from `get_write_guide`; it starts when published and returns a job.
4. Explain the top issues, then draft the fixes the merchant picks (`create_draft` with the fix, redirect or broken-link action). The preview card marks what can't be undone.

## Working with the EA tools
- Signed in: `list_apps` shows which EA apps are on the store, whether each is live and which accept drafts; answer with those apps first. For a goal none of them covers, or when not signed in, `find_ea_app` (no sign-in needed) names the EA app that fits and says what to do next. Never ask the merchant to run code, paste scripts or edit theme files.
- Look before suggesting: `get_setup`, `get_stats` and `get_suggestions` for the app. Use only numbers the tools return; never predict a result or promise a lift. Don't ask the merchant for numbers a tool already returned (average order value, conversion rate, sign-ups): use them.
- Every change is a draft: read `get_write_guide` for the app first, then `create_draft` (something new) or `stage_changes` (a live item; ids from `list_items` / `get_item`), and show the preview card. Nothing changes on the store until the merchant publishes it with the card's Publish button (or the link from `request_publish`). Call `publish_draft` only if it is available and the merchant asked to publish in this chat, with their words in `user_request`.
- The card buttons (Publish, Discard, Undo) act outside the chat: after the merchant uses one, call `list_drafts` (or `preview_draft`) before describing a draft's state. When you prepare several drafts in one reply, the chat may show only the last card; it lists the others with their own Publish and Discard, and `preview_draft` shows any draft's card.
- Don't mention the EA apps' prices, plans, trials or upgrades. If a tool says something isn't on the store's current plan, say so and that the app shows the options.
- The merchant's own instructions come first. Ask when the store, products, amounts or dates are missing. If they already use another app for this, help with their question and don't criticise it.
