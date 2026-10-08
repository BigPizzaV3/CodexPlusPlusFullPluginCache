---
name: despegar-travel
description: >-
  Search and book Despegar travel (flights, hotels, activities, insurance) via
  Vivi MCP tools. Use when the user wants flights, hotels, activities, insurance,
  deals, or price trends on Despegar. Do NOT use for non-travel tasks. Never
  date-scan flights by calling flight-search across many dates.
---

# Despegar travel (Vivi MCP)

Help the user find and start checkout for Despegar travel products using this
plugin’s MCP tools. Prefer tool results and widgets over inventing inventory or
prices.

## When to activate

- Flights, hotels, activities, travel insurance, flight deals, or fare trends
- Checkout / “buy” / “comprar” for an offer already returned by a search tool

## When NOT to activate

- Non-travel questions (coding, general knowledge, other brands)
- Requests to scrape Despegar.com or bypass MCP tools

## Required inputs before search

Ask for missing fields; do not guess cities, dates, or passenger counts.

| Product | Must have before calling |
|---------|--------------------------|
| Flights (`flight-search`) | Origin, destination, **exact** departure date (and return date if round-trip), passengers |
| Hotels | Destination, check-in, check-out |
| Activities | Destination (and dates when the tool requires them) |
| Insurance | Context from a prior eligible search / explicit trip details the tool needs |

If the user only has a **flexible** window (“sometime in March”, “cheapest week”),
do **not** invent dates and do **not** date-scan — use the allowed alternatives below.

## Workflow

1. Confirm product type and required inputs (see table).
2. Call **one** appropriate MCP tool with complete arguments.
3. Present the tool/widget output. Summarize briefly; do not invent offers.
4. On buy/checkout: call `execute-product-action` with `actionId`, `userMessage`,
   and any `session.chatId` / `contextId` / `taskId` from the prior search result.
5. Open or share the returned `redirectUrl` when present. Do not fabricate checkout URLs.

### Tool map

| Goal | Tool |
|------|------|
| Specific-date flights | `flight-search` |
| Flexible date suggestions | `flight_flexible_search` |
| Fare / price trends | `flight-price-trend` |
| Deal map / inspiration | `flight-deals` |
| Hotels | `search_hotels_on_destination` |
| Activities | `search_activities_on_destination` |
| Insurance | `search_insurances` |
| Start checkout | `execute-product-action` |

## Hard limits (must follow)

Load [references/hard-limits.md](references/hard-limits.md) when unsure. Summary:

1. **No date scanning for flights.** Never call `flight-search` repeatedly while
   varying only dates to discover the cheapest day/week/month.
2. **At most one `flight-search` per user turn**, unless the user explicitly asks
   to search a **different specific date** they named.
3. **No parallel fan-out** of `flight-search` across a date grid.
4. If dates are unknown or flexible → ask clarifying questions **or** call
   `flight_flexible_search` / `flight-price-trend` / `flight-deals` (**one** call),
   then let the user pick concrete dates before `flight-search`.
5. Never invent prices, availability, airlines, or hotel inventory.
6. Never scrape websites or call tools outside this plugin’s MCP for Despegar inventory.
7. Never retry the same failing tool call in a tight loop; explain the error and ask how to proceed.

## Output style

- Be concise. Prefer the product widgets when the host shows them.
- Use currency and cities as returned by tools.
- If a tool returns no results, say so and suggest one concrete next step
  (different dates, nearby airport, flexible-search tool) — still without date scanning.
