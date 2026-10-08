---
name: momentum-scan
description: Use when the user asks which supplied stocks have strong or weak momentum, breakouts, pullbacks, RSI extremes, relative-volume changes, or moving-average trend shifts.
---

# Momentum Scan

The user's explicit instructions take precedence over this skill.

Perform a momentum-focused scan across user-supplied tickers.

Workflow:
1. Call `compare_stocks` with fundamentals off unless specifically requested.
2. Use returned 1D/5D/1M/3M/6M/1Y performance, RSI, MACD, EMA20/50, SMA200, ATR%, and relative volume.
3. Surface:
   - acceleration or deceleration across multiple horizons
   - RSI extremes
   - MACD direction where available
   - price relationship to EMA20/50 and SMA200
   - relative-volume confirmation or lack of confirmation
   - ATR% as a volatility context signal
4. Avoid simplistic rules such as 'RSI below 30 means buy' or 'above 70 means sell'.
5. If the user asks about one candidate in depth, call `get_multitimeframe_technicals` or `get_stock_context`.
6. Label conclusions as technical observations, not forecasts.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
