---
name: backtest-a-strategy
description: Turn an investing or trading strategy the user describes in plain English into explicit Shadowfolio rules, ask for any missing specifics (what to trade, when to buy, when to sell, how often to rebalance, how to size positions), backtest it over the last 12 months against a benchmark, and offer to save it for daily forward tracking. Use when the user wants to test, backtest, paper-trade or track a strategy of their own. Not for picking investments.
---

Use this skill when the user describes a strategy of their own and wants to know how it would have done, or wants to track it from today. The user's explicit instructions always come first.

## Inputs

The strategy in the user's words. The `strategy` fields of the Shadowfolio tools hold what the user said:

- **What to trade:** their tickers (`universe.symbols`, up to 50), `universe.preset` `sp500` (optionally one `sector`) or `popular_etfs`.
- **When to buy:** `entry` rules, all of which must hold: price against an N-day average, a fast and a slow average, RSI, return over N days, distance from an N-day high. A rule can look at another ticker with `symbol`, for example "only while SPY is above its 200-day average". `rank` chooses among many ("the 5 with the best 6-month return": `rank` by `return`, 126 days, `highest`, `max_positions` 5).
- **When to sell:** `exit` rules (any one sells), `stop_loss_pct`, `take_profit_pct`, `max_hold_days`. An empty `exit` list means "sell what no longer qualifies at the next rebalance".
- **How often:** `rebalance` daily, weekly, monthly or quarterly.
- **How to size:** `sizing` equal, inverse_volatility or fixed_weights (with `weights` in percent), and `max_positions`.
- Optional: `cash_symbol` (where idle money sits), `benchmark` (SPY unless named), `cost_bps`.

Months are 21 trading days (3 months = 63, 6 months = 126, 1 year = 252).

## Flow

1. When any of the five specifics is missing, `draft_strategy` takes what the user said and returns the open questions, each with its default, short enough to ask in one message. Tickers, numbers and rules come from the user, or from those defaults.
2. Once the user answers, or accepts the defaults, `run_backtest` takes the rules (the `rules` from `draft_strategy`, updated with the answers).
3. The result ends with a summary suitable to show the user: return, benchmark return, max drawdown, Sharpe ratio, trades and win rate, and that the results are hypothetical.
4. When the user wants to keep it, `save_strategy` takes the same rules. Shadowfolio tracks it daily from the latest close.
5. Later, `list_my_strategies` shows how each saved strategy is doing, and `show_strategy` shows one in detail. `create_share_link` makes a public link when the user asks for one.

## Scope

- Shadowfolio doesn't recommend, pick or rank securities, funds or strategies, and its results don't say whether a strategy is good, will work or should be followed.
- Backtest and tracking figures come from the tools' results, computed on stored daily closes.
- Shadowfolio can't trade, connect to a broker or move money.
- A tool result with a `problem` (an unknown ticker, prices still loading) has a sentence for the user that says what happened.
- A question about what to buy is investment advice, which Shadowfolio doesn't give; it can test a rule the user describes.
