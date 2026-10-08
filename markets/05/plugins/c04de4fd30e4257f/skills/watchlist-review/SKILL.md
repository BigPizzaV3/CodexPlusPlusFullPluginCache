---
name: watchlist-review
description: Use when the user provides a list of tickers and wants a watchlist scan, daily review, triage, or quick summary across the whole list.
---

# Watchlist Review

The user's explicit instructions take precedence over this skill.

Review a supplied watchlist without assuming any hidden portfolio or browser-saved symbols.

Workflow:
1. Require the user to provide the ticker list if it is not present in the conversation.
2. Call `compare_stocks` on up to 30 tickers. Include fundamentals only when the user asks for valuation/company quality or when a slower-moving review is useful.
3. Organize results into:
   - strongest recent movers
   - weakest recent movers
   - unusual relative volume
   - high or low RSI extremes
   - names above/below key moving averages
   - high ATR% / volatility names
4. Do not call a stock 'good', 'bad', 'safe', or a guaranteed opportunity based on one indicator.
5. Note the data timestamp and that scanner prices are latest daily-bar closes unless a dedicated quote is requested.
6. If a specific ticker deserves closer inspection, call `get_stock_context` for that ticker before discussing it in detail.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
