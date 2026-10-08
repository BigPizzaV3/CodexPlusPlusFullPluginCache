---
name: symbol-finder
description: Use when the user knows a company name or partial ticker but needs the listed symbol before analysis.
---

# Symbol Finder

The user's explicit instructions take precedence over this skill.

Find likely listed symbols without silently choosing an ambiguous company.

Workflow:
1. Call `search_symbols` using the company name or ticker fragment.
2. Prefer exact ticker-prefix and exact/near-exact company-name matches.
3. Return a short set of candidates with the symbol and company name.
4. If there is a single clear match, proceed to the user's requested downstream analysis.
5. If several plausible matches remain, ask the user which one they mean.
6. Note that the built-in search directory is focused on U.S.-listed symbols; Yahoo-formatted symbols such as `.TO` may still work when supplied directly even if not discoverable through search.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
