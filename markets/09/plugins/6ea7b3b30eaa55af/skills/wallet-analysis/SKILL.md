---
name: wallet-analysis
description: Analyze a public Solana wallet's trading performance, holdings, best and worst trades and recent activity. Use when the user shares a Solana wallet address and asks how it trades, whether it is profitable, or what it holds.
---

# Solana wallet analysis

Use this workflow when the user gives a Solana wallet address and wants to understand it.

## Steps

1. Call `get_wallet_pnl_summary` for total, realized and unrealized PnL, ROI, win rate, trade counts and hold time. Note any public label (for example a KOL name) and whether it is flagged as an arbitrage bot.
2. Call `get_wallet_positions` with `sort: "pnl"` for the biggest winners. If the user asks about losses, call it again with `filter: "losing"`.
3. Call `get_wallet_holdings` if the user asks what the wallet holds now or what it is worth.
4. Call `get_wallet_recent_trades` if the user asks what the wallet has been doing lately.

## Report format

- **Who:** public label if known, otherwise just the shortened address.
- **Performance:** total PnL, realized vs unrealized, ROI, win rate, tokens traded, average hold time.
- **Best and worst positions:** token, PnL, ROI.
- **Current holdings** (if requested): total value and largest positions.
- **Recent activity** (if requested): latest buys and sells.

Only analyze the address the user provided. Present figures neutrally, do not recommend copying trades, and link to the wallet on Solana Tracker.
