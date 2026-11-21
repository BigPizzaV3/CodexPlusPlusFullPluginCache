---
name: imotesa-property-record
description: Inspect Bulgarian property records, current offers, and observed asking-price history when a user needs evidence about a property or a filtered set of properties.
---

Use this skill for requests to find Bulgarian properties, inspect a property's record, or understand its observed asking-price history. Do not use it for legal advice, mortgage guidance, investment recommendations, forecasts, or properties outside Bulgaria.

## Workflow

1. For a property request without a slug, call `search_properties`. Use `list_locations` only when the user needs help choosing or confirming a city or neighbourhood.
2. For a specific property, call `get_property`. If the user asks about price reductions, relisting, or time observed on the market, also call `get_property_history` with the property's slug.
3. Call `get_market_stats` only when the user asks for local price context. Do not use it to make a prediction or recommendation.
4. Link the relevant `canonical_url` in the result. Call `resolve_search_url` only when the user explicitly asks for a reusable URL; it creates or updates an internal search-page record.

## Reporting rules

- Describe all prices as observed asking prices in EUR, not transaction prices. Rent figures are monthly.
- Treat each listing history as a separate observation series. Different agencies or sellers can advertise the same property at different prices.
- Say that an inactive listing was no longer observed; do not infer a completed transaction.
- Distinguish the property record from the local market context. Prefer median figures and include sample size when citing market statistics.
- If a requested segment is unavailable or a location was matched approximately, state that clearly and offer the wider segment or resolved location returned by the tool.
- Give factual context and leave the decision to the user. Do not present a property as a recommendation or a guaranteed opportunity.
