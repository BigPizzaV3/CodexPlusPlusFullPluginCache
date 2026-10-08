---
name: long-term-company-review
description: Use when the user asks for a long-term company-quality review focused on growth, margins, cash flow, debt, valuation, and long-run price context rather than short-term trading.
---

# Long-Term Company Review

The user's explicit instructions take precedence over this skill.

Build a long-horizon company research brief.

Workflow:
1. Call `get_fundamentals`.
2. Call `get_stock_context` for 6M/1Y price context and longer-horizon trend statistics.
3. Focus on:
   - revenue and earnings growth
   - margins and returns on capital proxies where available
   - operating and free cash flow
   - cash, debt, current/quick ratios
   - share count/ownership context
   - valuation multiples
   - 6M/1Y market performance and drawdown context
4. Explicitly identify missing moat, customer concentration, management, filing, and guidance evidence.
5. Avoid turning historical growth into a forecast.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
