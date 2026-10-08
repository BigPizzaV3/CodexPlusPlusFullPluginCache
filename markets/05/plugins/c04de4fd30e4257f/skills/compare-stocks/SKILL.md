---
name: compare-stocks
description: Use when the user wants a side-by-side comparison of two or more tickers on returns, momentum, volume, valuation, growth, profitability, or balance-sheet metrics.
---

# Compare Stocks

The user's explicit instructions take precedence over this skill.

Compare multiple securities using a consistent evidence framework.

Workflow:
1. Resolve company names to tickers with `search_symbols` when necessary.
2. Call `compare_stocks` with the requested symbols. Set `include_fundamentals=true` whenever valuation, growth, profitability, balance-sheet, or cash-flow comparison matters.
3. Build a compact comparison table using only fields returned by the tool.
4. Cover:
   - price and as-of date
   - 1D, 1M, 3M, 6M, and 1Y performance where available
   - RSI, MACD, EMA20/50, SMA200, ATR%, and relative volume
   - trailing/forward P/E, PEG, P/S, EV/EBITDA where available
   - growth, margins, liquidity, debt, and cash-flow fields where available
5. Explain where the companies differ materially; do not manufacture a ranking or winner unless the user only wants a non-political investment-style comparison, and even then frame results as factual trade-offs rather than certainty.
6. Flag missing/provider-dependent fields explicitly.
7. Preserve all delayed-data and Yahoo/yfinance limitations.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
