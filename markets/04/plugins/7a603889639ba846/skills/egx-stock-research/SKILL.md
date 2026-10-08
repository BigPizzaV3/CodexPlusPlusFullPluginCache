---
name: egx-stock-research
description: Research an Egyptian Exchange listed company using current quotes, fundamentals, price history, disclosures, bulletins, and market order-book data. Use when a user asks to find, analyze, or compare EGX stocks; do not use for non-EGX assets or general financial planning.
---

# EGX stock research

Use Halan Borsa market-data tools to answer the user's specific research question.

1. Resolve a company name, Arabic or English name, ticker, or Reuters code with `search_symbols`. If the user already supplied a 12-character ISIN, use it directly.
2. Choose only the data needed:
   - `get_stock_quote` for a current price snapshot.
   - `search_symbols` for fundamentals and the 52-week range.
   - `get_symbol_history` for daily prices; convert requested dates to Unix milliseconds and state the analyzed period.
   - `list_news` and `list_bulletins` for disclosures and corporate events. Page when the first result set may be incomplete.
   - `get_best_bid_ask` for top of book, `get_active_orders` for single-symbol depth, or `get_order_book_history` for past order events.
   - `is_market_open` when current session status affects the interpretation.
3. Distinguish facts returned by tools from calculations or interpretation. Report currency and timestamps clearly.
4. If comparing stocks, use the same fields and time period for each stock and disclose missing data.

Do not invent an ISIN, quote, news item, or unavailable metric. The order-book tools describe the public market and do not identify the user's own orders. Provide data and neutral analysis, not personalized financial advice or a promise of future performance.
