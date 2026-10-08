---
name: risk-volatility-check
description: Use when the user asks about volatility, drawdown, ATR, risk, downside range, relative volume, or which supplied stocks are more volatile.
---

# Risk & Volatility Check

The user's explicit instructions take precedence over this skill.

Assess observable market-risk characteristics without predicting losses.

Workflow:
1. For one ticker, call `get_stock_context`.
2. For multiple tickers, call `compare_stocks`.
3. Focus on ATR%, realized-volatility fields, horizon max drawdown, distance from period highs/lows, relative volume, and multi-horizon returns.
4. Distinguish volatility from business quality and from probability of permanent loss.
5. Never infer a user's risk tolerance.
6. If the user supplies position size or portfolio weights, discuss concentration arithmetically but do not assume brokerage data.
7. State that historical volatility and drawdown do not bound future outcomes.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
