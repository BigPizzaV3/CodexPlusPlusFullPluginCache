---
name: check-card-prices
description: Check FC Ultimate Team card price observations and 24-hour or seven-day price history with FCData, including console/PC differences, missing prices and observation freshness. Use for card market questions, not purchases, forecasts, or unrelated financial questions.
---

Use the `fcdata` MCP server's `get_card_prices` and `get_price_history` tools.
Use `search_cards` or `get_card` when a confirmed card variant is still needed.

1. Resolve edition and variant first. Default to FC27 (`gameYear: 2027`);
   label FC26 (`2026`) as historical. Use only confirmed `definitionId` values.
   Clarify multiple matching variants instead of guessing one by player name.
2. Confirm console versus PC when unknown; retain that choice for follow-ups.
   “And on PC?” changes the platform and requires a new price query.
3. Retrieve up to five variants per price call. Report coins, platform and
   original `observedAt`. These are stored market observations, not executable
   offers. Calling the tool again does not make an old observation current.
4. Translate `availability` and `freshness` into clear language. Unavailable
   prices are unknown, not zero; never substitute a console price for PC.
   A future or missing timestamp has unknown freshness. A recent timestamp
   is within the server's 15-minute display threshold, not a delivery guarantee.
5. For history choose only `24h` or `7d`, matching the user's question. Use
   `get_price_history` to display its centered interactive chart with card
   artwork and console/PC and period controls. Do not replace that chart with
   `render_cards`. Controls retain the confirmed edition and variant.
   Use returned time bounds and the selected platform's summary. Preserve null
   points as observation gaps. `pointsSampled` means the server reduced the
   points; its summary still uses the complete source series. When
   `hasObservationGaps` is true, do not connect sampled points into a continuous
   chart: sampling may omit individual null markers. If `hasSufficientData` is false, explain that a
   reliable trend is unavailable. Historical movement is not a forecast.
6. Link the card name to its returned `url`, and provide the FCData card link
   for interactive inspection. Answer the user's price question in ChatGPT.
7. Handle explicit errors separately from absent quotes. For a retryable
   failure offer a retry or the confirmed card link; never fabricate prices.

Use the user's language. Do not invoke tools for unrelated finance questions,
request EA account credentials, create alerts, initiate purchases or claim
an exact future price. Account actions and MCP Events are later phases.

Examples:

- “What do these three cards cost on PC?”: query those canonical IDs on PC;
  show each observed price and time, retaining unavailable entries.
- “How did this console card change over seven days?”: query `7d` on console;
  show the returned change and data sufficiency, with the FCData card link.
- “Buy this player for me”: explain that purchases are not supported.
