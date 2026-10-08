---
name: technical-setup-review
description: Use when the user asks for chart-style technical analysis, trend structure, moving averages, RSI, MACD, ATR, support/resistance, breakout, pullback, or multi-timeframe setup analysis.
---

# Technical Setup Review

The user's explicit instructions take precedence over this skill.

Build a disciplined technical-analysis brief.

Workflow:
1. Call `get_multitimeframe_technicals` for the ticker.
2. Call `get_stock_context` when support/resistance candidates, volume trend, or longer-horizon statistics are also needed.
3. Analyze hourly, daily, and weekly structures separately before synthesizing them.
4. Discuss EMA10/20/50, SMA200, RSI14, MACD, ATR14/ATR%, and relative volume.
5. Treat support/resistance values as algorithmic pivot candidates, not guaranteed reversal levels.
6. Treat hourly returns as intentionally omitted when the tool says so; never relabel intraday bar counts as calendar returns.
7. State whether timeframes agree or conflict.
8. Avoid predicting a specific future price or claiming a breakout is certain.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
