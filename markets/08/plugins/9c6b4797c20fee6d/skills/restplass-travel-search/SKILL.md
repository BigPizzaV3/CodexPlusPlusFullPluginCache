---
name: restplass-travel-search
description: Search live package holidays and charter flight-only offers from Norway using Restplass. Use this skill for travel searches, date interpretation, follow-up refinements, and deciding between package holidays and flight-only searches.
---

# Restplass travel search

Use `search_holidays` when the user wants a package holiday including accommodation.

Use `search_flights` when the user explicitly wants flight-only travel.

## Date interpretation

All searches must be for future travel and no more than 11 months ahead.

When the user specifies a month without a year, ALWAYS interpret it as the next occurrence of that month in the future.

Never ask which year the user means solely because the year was omitted.

Examples:
- If today is September 24, 2026, "November" means November 2026.
- If today is December 10, 2026, "February" means February 2027.

Convert month requests into an appropriate date range before calling the search tool.

Never search dates in the past.

## Follow-up searches

Preserve constraints from previous messages unless the user changes them.

For example, after:
"7 nights from Oslo for 2 adults in November"

the follow-up:
"Only all inclusive"

means the same search with all-inclusive added.

Do not ask unnecessary clarification questions when the request can be interpreted unambiguously.

## Search behavior

Use `price_asc` when the user asks for the cheapest options.

Return several alternatives when comparison is useful.

Never invent availability, prices, hotels, flights, or booking information.

Prices and availability are live and may change.

The tools only search. Do not claim that a holiday or flight has been booked or reserved.
