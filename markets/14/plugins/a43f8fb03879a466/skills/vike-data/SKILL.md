---
name: vike-data
description: Use the Vike Data API MCP tools for crypto research questions about on-chain wallets and tokens, Hyperliquid perps and wallet cohorts, and Polymarket.
---

# Vike Data API

## What the tools cover

- **On-chain wallets and tokens** on Ethereum, BNB Chain, Base and HyperEVM: wallet flows and balances, PnL history, counterparties, first funder, exchange usage, entity labels and risk flags, token holders, transfers and a token screener.
- **Hyperliquid perps**: wallet positions and fills, liquidations, leaderboards, builders, market stats and candles.
- **HL Cohorts**: hourly long/short positioning of each Hyperliquid perp split by wallet cohort (account size, realized-PnL percentile, PnL bands, position size).
- **Polymarket**: markets, order books, trade tape, settlements, wallet profiles, leaderboard and smart-money flows.

## Conventions

- All times are UTC; pass ISO-8601, e.g. `2026-10-01T00:00:00Z`.
- Addresses are 0x-prefixed hex. Chains: `ethereum`, `bsc`, `base`, `hyperevm`.
- Hyperliquid tickers are plain symbols (`BTC`, `ETH`, `HYPE`); HIP-3 markets are `dex:TICKER`, e.g. `xyz:TSLA`.
- Cohort `bias` is a fraction from -1 (all short) to +1 (all long), not a percent.
- For backtests, ask for point-in-time cohort labels; the default PnL grading is today's, which looks ahead.
- Polymarket "smart money" = wallets with $1k+ realized PnL over 5+ resolved markets.
- Long results are paged: pass the returned cursor back verbatim for the next page.

## Good questions

- Are whales long or short BTC on Hyperliquid right now?
- What has wallet 0x… been doing on Base this week?
- Who are the top holders of this token, and what are they labelled?
- Where did Polymarket smart money flow in the last 24 hours?
