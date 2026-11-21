---
name: cubrik-performance-review
description: Review how the user's trading and agents are doing with cubrik's Analytics, and act on its advice. Use when the user asks "how am I doing", "which agent is losing money", "weekly review", "why am I down this month", "what should I change", or asks about win rate, profit factor, drawdown or results by session, day or holding time. Reads results, the Analytics report and the per-agent advice, explains them with numbers, and applies a piece of advice only when the user says so.
---

A review answers: what was made or lost, where it came from, and what the record suggests changing.
cubrik's Analytics reads the user's own closed trades on each connected platform; its advice is
drawn from each agent's trades (for example "stop trading the New York session" with the trades
behind it and what it would have added).

## Calls

1. `get_trading_results` — the period's profit and loss, trades and win rate, split by agent and
   by account. Start here for "how am I doing".
2. `get_analysis` (`period`: today, week, month, all; `account` from `list_platforms` when there is
   more than one) — KPIs (net result, win rate, profit factor, average R, maximum drawdown, best and
   worst trade), the equity curve and breakdowns by session, holding time and weekday.
3. `get_advice` (same `account` and `period`) — per-agent advice, each with the evidence (trades,
   wins, net) and `gain`, what applying it would have added in the period. Applied advice is listed
   with what it has saved since.
4. Optional: `get_agent_runs` / `get_conversation` to explain a specific trade or run.

## The review

1. **The headline**: net result for the period, number of trades, win rate, profit factor.
2. **Where it came from**: the best and worst agents (from `get_trading_results`), and the
   breakdown row that stands out (a session, a weekday, long holds).
3. **The advice**, in the order cubrik gives it (largest effect first): what to change, for which
   agent, the evidence in one line ("10 of 47 trades in New York, 2 won: −2,140 USDT"), and what it
   would have added this period.
4. Ask whether to apply any of it.

Apply only what the user chooses, with `apply_advice` (`advice_id` from `get_advice`, same
`account` and `period`). It writes a rule on that agent from its next run; say which agent changed.
In apps that show cubrik's screens the Analytics card has an Apply button per piece of advice.

## Rules

- The advice describes the past. Say "would have added", never "will make".
- Small samples: under ~20 trades in a row of the breakdown is weak evidence; say so.
- Never apply advice the user did not pick, and never change an agent's instruction to "fix" a
  result without being asked — offer it instead.
- Amounts are in the account's currency; keep the sign and the currency on every figure.
