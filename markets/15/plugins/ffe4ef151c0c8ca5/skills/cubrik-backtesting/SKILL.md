---
name: cubrik-backtesting
description: Backtest a trading idea on historical candles with cubrik and read the result honestly. Use when the user asks to backtest, test, simulate or "check if this would have worked" — an indicator rule (RSI, EMA crossover, MACD, Bollinger, SuperTrend), a smart-money setup (sweep, order block, fair value gap, break of structure), a breakout, or a regular buy (DCA). Writes the rules in cubrik's rule format, runs run_backtest, follows it with get_backtest until it finishes, and reports return, drawdown, win rate and trades with the assumptions — never as a promise.
---

A backtest runs the idea's rules over stored candles and simulates every trade. It changes nothing
on any account and costs no credits. The result is only as good as the rules match the idea, so
the work is in writing the rules right, then in reading the numbers without overselling them.

## 1. Pin the plan down

Ask in ONE message only for what is missing: the market(s), the timeframe (1m, 5m, 15m, 1h, 4h,
1D), the entry, the exit (stop %, target % or none, signal exits, a maximum time in trade), the
risk per trade and the leverage. A regular buy (DCA) needs only the pair, how often and the amount.

Defaults you may use without asking: 12 months of history, a 10,000 starting balance (leave
`starting_balance` out unless the user named one).

## 2. Write the rules

`run_backtest` takes the rules as structured data — its schema describes every operand. The
mistakes that make a backtest silently wrong are in `references/rules.md`; read it the first time
you write rules in a conversation. The four that matter most:

1. **A sequence needs `within`.** "A sweep, then a reclaim" is two conditions; the earlier one
   carries `within: 10`–`30` bars, or both must be true on the same bar and it never trades.
2. **Compare like with like.** An oscillator against a number or another oscillator; a price
   against a price. "RSI above the price" is refused.
3. **No fixed target is `takeProfitPct: null`**, never a far target standing in for it.
4. **A regular buy is `accumulate: { amount }`**, long, leverage 1, on the spot pair (BTC/USDT, not
   BTC/USDT:USDT). Without it the "daily buy" is one trade held for the whole window.

Use the perpetual spelling (SOL/USDT:USDT) whenever the plan uses leverage. If unsure a market
exists, call `list_instruments` rather than assuming it does not.

## 3. Run it and follow it

Call `run_backtest`. It returns a `backtest_id` (and a `batch` of ids, one per symbol, when there
are several) and runs in the background. Call `get_backtest` with the id a few seconds later; while
`status` is `queued` or `running`, wait and ask again. In apps that show cubrik's screens, the
backtest card follows the run by itself and draws the equity curve when it is done.

If the answer is `too_many_backtests`, the account already has runs going: say so and read those
instead of starting more.

## 4. Report it honestly

Lead with the four figures, then what they mean:

- **Return** and **maximum drawdown** together — a return means nothing without the fall it took.
- **Win rate** and **number of trades** — under ~30 trades is little evidence; say so.
- **Profit factor** when present (gross profit ÷ gross loss; above 1.3 is worth a look).
- **Month by month**: was it one lucky month? Compare with the market's own move (`pricePct`).
- The **assumptions** listed in `methodology` (fees, fills, what is not simulated).

Then, if they want it live, hand over to the skill `cubrik-agent-builder` with the same rules in words.

## Rules

- Always say the figures are simulated on historical candles and are not a forecast.
- Never state a return, win rate or drawdown that did not come back from `get_backtest`.
- Do not tune parameters until the past looks good and present that as an edge: if the user
  optimises, say plainly that a rule fitted to the past tends to do worse on new data.
- A failed backtest has a reason (`failure`): `timeframe_unavailable` means that market keeps no
  history on that timeframe (try 1h or longer); `no_candles` and `not_enough_history` mean the
  stored history is missing or too short. Say which; do not estimate a result.
