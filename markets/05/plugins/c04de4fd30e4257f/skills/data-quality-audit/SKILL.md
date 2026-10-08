---
name: data-quality-audit
description: Use when the user asks whether the market data can be trusted, why fields disagree, whether a number is current, or what still needs verification.
---

# Data Quality Audit

The user's explicit instructions take precedence over this skill.

Audit the evidence quality behind a Noweir Market Data result.

Workflow:
1. Call the relevant tool that produced the disputed result.
2. Identify:
   - source class: Yahoo/yfinance market data or company metadata, Nasdaq Trader symbol directory
   - quote timestamp and price type
   - whether `realtime_guarantee` is false
   - missing/provider-dependent fields
   - differences between trading-session approximations and calendar-period statistics
3. Explicitly separate facts returned by the provider from model interpretation.
4. List evidence gaps that require filings, investor-relations releases, Reuters/current news, macro data, or another authoritative source.
5. Never 'repair' a suspicious value by inventing a replacement.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
