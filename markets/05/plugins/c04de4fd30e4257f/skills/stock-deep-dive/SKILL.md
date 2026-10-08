---
name: stock-deep-dive
description: Use when the user wants a comprehensive review of one stock, including quote context, performance, technicals, volume, valuation, fundamentals, and explicit evidence gaps. Do not trigger for trade execution or guaranteed real-time pricing.
---

# Stock Deep Dive

The user's explicit instructions take precedence over this skill.

Use Noweir Market Data to build a structured single-stock research brief.

Workflow:
1. Identify the ticker. If the user gave a company name but not a ticker, call `search_symbols` first and choose only a clearly matching result.
2. Call `get_stock_context` for the ticker.
3. If the user asks for extra valuation or company detail, call `get_fundamentals`.
4. If the user asks for more technical detail, call `get_multitimeframe_technicals`.
5. Present the result in this order:
   - latest available quote/session context and timestamp
   - 1D, 5D, 1M, 3M, 6M, 1Y, and YTD performance where available
   - daily and weekly trend structure
   - RSI, MACD, EMA10/20/50, SMA200, ATR, and relative volume
   - support/resistance candidates, clearly labeled as algorithmic candidates rather than validated trade zones
   - valuation, growth, profitability, balance-sheet, and cash-flow highlights
   - explicit evidence gaps and what still requires current primary-source verification
6. Distinguish provider data from interpretation. Do not invent missing fields.
7. Preserve the service disclosure that Yahoo/yfinance data is not guaranteed exchange-grade streaming real time.
8. Do not claim that the output is a recommendation to buy, sell, or hold. If the user asks for a decision, summarize the factual trade-offs and evidence instead of making the decision for them.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
