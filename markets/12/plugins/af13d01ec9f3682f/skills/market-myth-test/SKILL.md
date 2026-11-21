---
name: market-myth-test
description: Check a common market rule of thumb, such as a golden cross, buying a dip from the high, an RSI oversold signal or a 200-day moving average filter, against buy-and-hold over the last 12 months with Shadowfolio. Use when the user asks whether a well-known trading rule or market saying would have worked.
---

Use this skill when the user asks whether a familiar rule beat simply holding: "did a golden cross on QQQ beat buy-and-hold this year?", "does buying SPY after a 5% dip from its high work?", "is RSI under 30 a good buy signal for AAPL?". The user's explicit instructions always come first.

## Turning the saying into rules

The rule types Shadowfolio can test, each optionally on another ticker with `symbol`:

- **Moving-average filter:** price above or below its N-day average (`price_vs_sma`), for example 200 days.
- **Golden or death cross:** a fast average above or below a slow one (`sma_cross`), for example 50 and 200 days.
- **RSI level:** RSI over N days above or below a value (`rsi`), for example 14 days below 30.
- **Momentum:** the return over N days above or below a percent (`return`).
- **Dip from the high:** the distance from the N-day high above or below a percent (`pct_from_high`), for example more than 5% under the 252-day high.

Months are 21 trading days (3 months = 63, 1 year = 252). Calendar sayings such as "sell in May" have no matching rule type.

## Flow

1. `draft_strategy` takes the saying in the user's words, maps it onto these rules and returns any open questions (what to trade, when to sell, how often to check) with their defaults.
2. `run_backtest` tests the settled rules over the last 12 months of daily closes against a benchmark, SPY unless the user names one; naming the traded ticker itself (QQQ for a QQQ rule) makes it a buy-and-hold comparison. The result gives the strategy's return next to the benchmark's, max drawdown, Sharpe ratio, trades and win rate.
3. One year is a short window, and the summary says the results are hypothetical. A user who wants to keep watching the rule can save it (see the strategy tracking skill).

## Scope

- Shadowfolio tests the rule the user describes; it doesn't say whether a rule is good or should be followed, and it doesn't pick securities.
- Daily closes of US stocks and ETFs only; no intraday data, no other markets.
