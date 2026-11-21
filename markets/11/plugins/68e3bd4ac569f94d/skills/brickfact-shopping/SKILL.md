---
name: brickfact-shopping
description: Find and compare LEGO sets with Brickfact, choose gifts, assess recorded retail prices, and prepare app handoffs for price alerts or watchlists.
---

Use Brickfact's public catalogue tools for LEGO shopping in DE, AT, CH, GB, US, FR, NL, ES and IT. Reply in the user's language where supported.

## Shopping context

Reuse the delivery market already supplied in the conversation. If it is missing, ask which country the user is shopping in; language and currency alone do not establish delivery country. Keep that market when the user changes budget, theme or result language.

Use `price_basis: delivered` for shopping detail, offer and comparison calls as well. For a shopping budget including shipping, call `search_sets` with `price_basis: delivered`. These searches filter and sort known delivered totals before pagination. Use `item` only when the user wants item prices excluding shipping. A missing shipping fee is unknown, never free. A feed timestamp is not proof of stock or delivery by a deadline.

Resolve named themes with `list_themes`; do not guess their IDs. Preserve explicit price, piece-count and retirement constraints. If there are no results, explain which constraint could be relaxed and ask before exceeding the budget or changing market. Do not silently retry an unavailable delivered-price search as item-price search.

## Gifts and discovery

Use the age, interests, budget and market the user has already provided. Ask only for missing information that materially affects the selection; offer a small range when preferences are broad. Translate interests into supported theme searches and explain matches using returned attributes. Manufacturer age labels are building recommendations, not safety certification, and an 18+ label alone does not establish difficulty. Never invent build quality, play features, recipient suitability or a guaranteed arrival date.

Use `find_alternatives` for a known set, optionally with `preference: cheaper`, a delivered `max_price`, or `fewer_pieces`. These are bounded related candidates, not an exhaustive best-of ranking. Fewer pieces does not mean a smaller finished model.

## Presentation and evidence

After choosing final IDs from search or alternatives, call `render_sets` for up to six shopping cards, or use `view: comparison` for two to four sets. Keep a text answer useful when the host has no UI. Refer to the main differences; avoid repeating every field shown in the cards.

For any price-history, price-development or Preisentwicklung question, call `get_retail_price_history` first. Use `days: 365` for the last 12 months. Show the returned merchant history even if recording began later: report the actual first/last recorded dates, observation days, currency and freshness. For example, 20 recorded days in a requested 365-day window is available history with partial coverage, not "no merchant history". Do not interpolate missing days or claim the returned period covers a full year.

Use `assess_deal` for a current-offer comparison. History excludes Amazon, so do not describe the recorded low as the lowest price ever across all shops. A failed call means temporarily unavailable data, not an empty history. If no eligible observations are returned, state the selected market, window and known-shipping restriction, then link to the set page. Never substitute market valuations for partial, missing or failed merchant history.

Use `get_price_history` only when the user explicitly asks for collector value, resale valuation or Marktwert, or asks to see that series separately as well. It is a separate EUR sealed-set valuation series, not historical retailer pricing or a forecast.

## Shortlists, watchlists and alerts

The shopping card's shortlist belongs to that card and is not synced to a Brickfact account. Do not imply it is a persistent account wishlist.

For a price alert or account watchlist, call `get_app_handoff` with the chosen set, market, action and optional target price. Give the returned app link and remaining steps. `created: false` means nothing has been created: the user must sign in and finish in the app. Do not ask for passwords, payment details, email addresses or notification tokens. Do not promise notification delivery or ongoing monitoring by this conversation.
