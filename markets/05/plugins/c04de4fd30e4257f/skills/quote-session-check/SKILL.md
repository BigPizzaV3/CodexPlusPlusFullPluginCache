---
name: quote-session-check
description: Use when the user asks for the latest available price, market state, regular close, day high/low, exchange, currency, timestamp, or whether a quote is real time.
---

# Quote & Session Check

The user's explicit instructions take precedence over this skill.

Return precise quote/session metadata.

Workflow:
1. Call `get_market_quote`.
2. Report:
   - latest available price
   - price type
   - latest bar timestamp
   - market state
   - regular-market close and previous regular close
   - day high/low
   - currency and exchange
3. Always preserve `realtime_guarantee=false` when returned.
4. Never call the result exchange-grade real time.
5. If the user asks for return context or technicals, follow with `get_stock_context`.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
