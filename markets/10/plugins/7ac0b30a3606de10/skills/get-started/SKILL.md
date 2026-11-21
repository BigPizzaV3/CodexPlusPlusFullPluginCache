---
name: hyperliquid-pnl-nav-auditor
description: Analyze read-only Hyperliquid public account data, portfolio history, positions, recent fills, funding, and source coverage. Use when a user asks to audit Hyperliquid PnL, NAV components, account equity, drawdown context, or history gaps.
---

# Hyperliquid PnL Auditor

Use the read-only Hyperliquid tools to inspect the public address the user provides. Ask for a public address if none was provided. Never request a private key, seed phrase, signing permission, API secret, or exchange password.

## Pick the smallest useful tool

- Use `get_account_snapshot` for current perpetual account value and positions, spot token balances, and vault equity.
- Use `get_portfolio_history` for Hyperliquid's own account-value and PnL chart series. State the selected period and source.
- Use `audit_recent_activity` for the capped recent fills and up to 90 days of funding returned by the source.

## Explain the numbers carefully

- Keep perpetual account value, spot token quantities, and vault equity separate. Do not sum them into a total NAV unless there is a valid price and ownership basis for every component.
- Distinguish realized PnL, fees, funding, and unrealized PnL. Do not count deposits or withdrawals as trading profit.
- Include returned timestamps, row counts, source, and API limits. The recent fills endpoint is capped; do not claim lifetime completeness.
- Hyperliquid portfolio history is a source series, not a reconstructed all-wallet equity curve.
- Do not provide tax advice, guarantee a tax basis, or recommend/execute trades. Encourage checking consequential figures against the source.

## Privacy

Only the public address is sent to Hyperliquid's public Info API for the requested read. The service does not store it. Refer users to the listing's privacy page for details.
