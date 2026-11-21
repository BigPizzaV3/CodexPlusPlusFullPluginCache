---
name: dativue-search-trends
description: Use Dativue when a user asks whether topics or keywords are growing, declining, seasonal, or gaining interest on Google Search or YouTube over time.
---

# Dativue search trends

Use `search_keyword_trends` for one to five comparable terms. Use the previous six months unless the user requests another supported period. Choose `youtube` only when the question is specifically about YouTube search interest; otherwise use `web`.

Run routine research without a quote. Estimate with `research_credit_quote` when asked, and get user approval for any call whose maximum hold exceeds 50 credits.

Google Trends values are measured relative interest from 0 to 100 within the requested comparison, not absolute search volume. Keep three layers distinct:

- Measured: returned points and averages.
- Calculated: first-window average, last-window average, relative change, and direction.
- Interpretation: seasonality, momentum, or recommendations inferred from those values.

Mention missing or insufficient data and preserve the Google Trends verification URL.
