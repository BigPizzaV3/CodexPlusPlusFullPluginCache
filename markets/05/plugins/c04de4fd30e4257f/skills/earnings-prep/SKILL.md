---
name: earnings-prep
description: Use when the user asks for an earnings-date check, pre-earnings stock review, event-risk preparation, or what market/fundamental context to inspect before results.
---

# Earnings Prep

The user's explicit instructions take precedence over this skill.

Prepare a pre-earnings factual brief from the data available in Noweir Market Data.

Workflow:
1. Call `get_fundamentals` for event metadata and company fundamentals.
2. Call `get_stock_context` for current performance, volatility, technicals, and volume.
3. Summarize:
   - reported upcoming earnings/event timestamp if available
   - recent price performance
   - ATR% and relative volume
   - valuation and growth metadata
   - balance-sheet/cash-flow context
4. Clearly list evidence the plugin does not provide, including the latest filing text, management guidance nuance, consensus revisions, current news, and transcript content.
5. Do not predict whether earnings will beat/miss or how the stock will react.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
