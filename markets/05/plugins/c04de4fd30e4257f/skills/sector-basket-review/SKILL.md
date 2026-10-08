---
name: sector-basket-review
description: Use when the user provides a basket of related companies in semiconductors, software, banks, energy, healthcare, or another sector and wants a peer-group review.
---

# Sector Basket Review

The user's explicit instructions take precedence over this skill.

Compare a user-defined peer basket consistently.

Workflow:
1. Call `compare_stocks` with fundamentals enabled.
2. Use the same metrics across every peer so the comparison is fair.
3. Separate:
   - momentum/trend
   - valuation
   - revenue/earnings growth
   - margins/profitability
   - balance-sheet/liquidity
   - volatility/ATR and relative volume
4. Call `get_stock_context` only for a small number of names that need deeper follow-up.
5. Do not assume all companies in a broad sector are direct peers; note business-model differences when obvious from returned company metadata.
6. Do not create a forced winner.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
