---
name: swing-setup-precheck
description: Use when the user wants an informational precheck of a possible swing setup using trend, momentum, volatility, volume, and algorithmic levels. This skill does not execute trades or promise outcomes.
---

# Swing Setup Precheck

The user's explicit instructions take precedence over this skill.

Evaluate a proposed swing setup as an informational checklist.

Workflow:
1. Call `get_stock_context`.
2. Call `get_multitimeframe_technicals` when cross-timeframe confirmation matters.
3. Review:
   - trend vs EMA20/50 and SMA200
   - RSI/MACD state
   - relative-volume confirmation
   - ATR% / volatility
   - recent performance
   - algorithmic support/resistance candidates
4. If the user supplies an entry, stop, and target, compute the arithmetic relationship in the answer; do not invent levels.
5. State what would invalidate the thesis in observable terms where possible.
6. Do not place a trade, claim a setup will work, or convert algorithmic levels into guaranteed support/resistance.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
