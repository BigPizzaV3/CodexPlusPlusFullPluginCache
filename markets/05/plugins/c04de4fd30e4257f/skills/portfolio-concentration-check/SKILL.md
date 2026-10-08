---
name: portfolio-concentration-check
description: Use when the user provides portfolio holdings or weights and wants concentration, overlap, sector exposure, or position-risk context. The plugin does not read brokerage accounts.
---

# Portfolio Concentration Check

The user's explicit instructions take precedence over this skill.

Review concentration only from holdings/weights the user supplies.

Workflow:
1. Do not assume access to brokerage accounts or hidden portfolio data.
2. Ask for ticker weights if they are missing.
3. Use `compare_stocks` to enrich the supplied holdings with market/volatility/fundamental context.
4. Compute simple concentration observations from the user-provided weights:
   - largest positions
   - top-3/top-5 share
   - sector/theme clustering when evident
5. If ETF look-through holdings are not provided, state that look-through concentration cannot be calculated from this plugin alone.
6. Do not infer the user's risk tolerance or prescribe a target allocation.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
