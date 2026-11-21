---
name: cubrik-agent-builder
description: Turn a trading idea into a cubrik agent. Use when the user wants an agent, a bot, an automation or "something that trades / watches / alerts for me" — e.g. "make an agent that buys BTC when RSI is under 30", "set up a London breakout bot", "alert me when gold breaks 2,400", "every morning summarise my positions". Settles the essentials in one round of questions, offers a backtest of the rules, creates the agent paused with create_agent, tests it, and starts it only when the user says so.
---

An agent is an instruction cubrik's AI follows on a schedule, on the platforms the user connected.
It is created **paused** and does nothing until it is started. Your job is to write an instruction
that is complete enough to run unattended, and to let the user decide when it goes live.

## 1. Settle the essentials — one round of questions

Read what the user already said, then ask in ONE message only for what is missing:

- **Markets** — which instruments (BTC, EUR/USD, gold, a list).
- **When to act** — the entry condition, as precisely as they can say it.
- **How to get out** — stop, target, a trailing rule, a time limit.
- **Size and leverage** — risk per trade or a fixed amount; leverage and margin mode if they trade
  futures. Margin mode (isolated or cross) is theirs to choose: never pick one for them.
- **How often it runs** — every 5–30 minutes, hourly, daily at a time, weekly, monthly.
- **Trade or only watch** — an agent that only reports or alerts has `may_trade: false`.

Do not ask about anything they already gave. Call `get_account` if you need the fastest schedule
their plan allows, and `list_platforms` if more than one platform is connected (the agent must be
told which one through `platforms`).

## 2. Offer a backtest when the idea has rules

If the plan is mechanical (indicators, levels, a regular buy), offer to backtest it first with the
skill `cubrik-backtesting`. Report the result honestly, then continue. Skip this for agents that
only watch, report or alert, and for discretionary instructions with no testable rule.

## 3. Write the instruction

The instruction is everything the agent will know on every run. Write it in full sentences:

1. What it trades and on which timeframe.
2. The entry condition, exactly.
3. The exit: stop, target, management (e.g. "at +50% on margin move the stop to entry"), time limit.
4. Size, leverage, margin mode (or "use the account's current mode" if they did not choose).
5. What to do with a position already open, and when not to trade (news, weekends, a session).

Then call `create_agent` with `name`, `trigger`, `instructions`, `may_trade`, the limits the user
gave (`max_daily_loss_pct`, `max_positions_per_instrument`) and `platforms` when needed. The answer
says what is still missing — for example a connected broker.

## 4. Test, then start only on the user's word

- Offer `test_agent`: a dry run that reads the market and says what it would have done, placing
  nothing. It uses credits; say so.
- Start the agent only when the user says to. On cubrik's full server that is `start_agent`
  (`run_now: true` makes the first run immediately, which uses credits); an agent that may trade
  places orders from then on — say so in one line before starting it. Where the app offers
  `start_watch_agent` instead (the version in ChatGPT's directory), only an agent with
  `may_trade: false` can be started here: an agent that trades is started in cubrik, from the link
  `get_agent` returns.
- To stop it later: `pause_agent`; all of them at once: `pause_all_agents`.

## Rules

- Never start an agent the user did not ask to start, and never set `may_trade: true` for an
  agent they described as watching or alerting.
- Never promise results. A backtest describes the past; an agent trades live prices.
- When `create_agent` or `start_agent` refuses (plan limit, schedule too fast, no broker), say what
  the limit is and offer what fits within it.
- If they ask to change an agent, use `update_agent` with only what changes; the instruction field
  replaces the whole instruction, so send the full new text.
