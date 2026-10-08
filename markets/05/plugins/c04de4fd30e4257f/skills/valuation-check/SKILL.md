---
name: valuation-check
description: Use when the user asks whether a stock looks expensive or cheap based on P/E, forward P/E, PEG, price-to-sales, price-to-book, EV/revenue, or EV/EBITDA.
---

# Valuation Check

The user's explicit instructions take precedence over this skill.

Evaluate valuation without presenting a single metric as definitive.

Workflow:
1. Call `get_fundamentals`.
2. Extract trailing P/E, forward P/E, PEG, P/S, P/B, EV/revenue, and EV/EBITDA where available.
3. Pair valuation with growth, margins, cash flow, debt, and profitability so multiples are not interpreted in isolation.
4. Explain missing or unusual ratios rather than guessing.
5. If comparing peers, call `compare_stocks` with fundamentals enabled and use the same metric set across all tickers.
6. Avoid declaring intrinsic value or a fair-price target unless the user provides a valuation model and assumptions.
7. Preserve the provider-data caveat.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
