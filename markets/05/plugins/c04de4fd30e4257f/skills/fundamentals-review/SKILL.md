---
name: fundamentals-review
description: Use when the user asks about valuation, revenue growth, earnings growth, margins, cash, debt, liquidity, free cash flow, ownership, short interest, analyst metadata, or earnings dates.
---

# Fundamentals Review

The user's explicit instructions take precedence over this skill.

Perform a fundamentals-focused review using Yahoo-derived company metadata.

Workflow:
1. Resolve the ticker with `search_symbols` if necessary.
2. Call `get_fundamentals`.
3. Organize results into:
   - company/profile
   - valuation
   - growth
   - profitability
   - balance sheet and liquidity
   - operating/free cash flow
   - ownership and short interest
   - analyst metadata and events
4. Distinguish raw provider metadata from interpretation.
5. Explicitly state when values are missing, stale, provider-dependent, or potentially affected by corporate actions/currency differences.
6. For consequential claims, recommend verification against current filings and official investor-relations material.
7. Do not treat analyst recommendations or price targets as authoritative forecasts.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
