---
name: setup
description: Set up Sperax Trading Desk for a new user by collecting their account size, default risk per trade, usual leverage and coins they trade, then running a first positioning check. Use right after installation or when the user asks how to get started.
---

# Get started with Sperax Trading Desk

Help the user set defaults once so later trade plans need fewer questions. Keep it short: ask everything in one message, then confirm.

## 1. Collect trading defaults

Ask for:

- **Account size** in USD that they size positions against.
- **Risk per trade** as a percentage of the account. Suggest 0.5–1% if they are unsure, and explain that this is the loss taken if the stop is hit.
- **Usual leverage** for perpetual futures, or 1 for spot only.
- **Coins they trade most**, up to five, such as BTC, ETH or SOL.

Don't ask for exchange logins, API keys, wallet addresses or seed phrases. Sperax Trading Desk never needs them and cannot place orders.

## 2. Confirm and remember for this conversation

Repeat the defaults back in one line, for example: "Account $10,000, risk 1% per trade, 3x leverage, watching BTC, ETH and SOL." Use these values whenever the user later asks to size a trade without restating them.

## 3. Run a first check

Call `get_derivatives_positioning` for the first coin they listed. Summarize funding, open interest change and the crowding and squeeze-risk labels in three or four sentences.

## 4. Show what to ask next

Offer two examples that use their own defaults:

- "Size a long on {coin} at {price}, stop {stop}, target {target}." This uses `build_trade_plan`, which also checks whether their leverage would liquidate the position before the stop.
- "Backtest buying {coin} when RSI drops below 30 and selling above 70 over 180 days." This uses `backtest_signal_strategy`.

End with: "These are analysis tools, not financial advice."
