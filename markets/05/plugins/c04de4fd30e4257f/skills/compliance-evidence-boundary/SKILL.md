---
name: compliance-evidence-boundary
description: Use when the user asks whether a stock satisfies Shariah/halal, ESG, regulatory, or another external compliance screen that Noweir Market Data does not authoritatively provide.
---

# Compliance Evidence Boundary

The user's explicit instructions take precedence over this skill.

Prevent unsupported compliance conclusions.

Workflow:
1. Use `get_stock_context` or `get_fundamentals` only for factual financial metadata relevant to the user's question.
2. Explicitly state that the plugin does not provide an authoritative current Shariah/halal, ESG, sanctions, legal, or regulatory-compliance determination unless such a source is directly returned by a tool.
3. Identify which current external evidence would be required.
4. Do not convert ratios or company metadata into an authoritative compliance label.
5. If the host has separate web/research capabilities and the user requested broader research, those sources may be used separately and clearly distinguished from Noweir Market Data.

## Shared boundaries

- Use only tool-returned values for numerical market/fundamental claims.
- Do not invent missing data.
- Treat Yahoo/yfinance data as secondary market-data/provider metadata and not guaranteed exchange-grade real time.
- Preserve timestamps and price-type/session distinctions when relevant.
- The plugin is read-only and cannot place trades, move money, modify brokerage accounts, or execute transactions.
