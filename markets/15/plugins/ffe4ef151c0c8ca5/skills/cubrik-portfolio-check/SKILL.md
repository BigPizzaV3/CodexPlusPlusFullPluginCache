---
name: cubrik-portfolio-check
description: A morning or on-demand check of the user's cubrik account — balances and open positions on every connected platform, what the agents did, what is coming up. Use when the user asks "how's my portfolio", "what's open", "what did my agents do overnight", "give me my daily brief", "am I exposed to the Fed today", or opens the conversation with a check-in. Reads balances and positions live from the platforms, the agents and their latest runs, notifications and the economic calendar, and reports risk plainly without telling the user what to buy or sell.
---

The check answers four questions in order: what does the account hold, what did the agents do,
what is at risk, and what is coming. Report with numbers; leave decisions to the user.

## Calls (keep it to these)

1. `get_portfolio` — balances and open positions on every connected platform, read from the
   platforms themselves (positions are cached for 20 seconds; `refresh: true` re-reads balances).
   In apps that show cubrik's screens this draws the portfolio card.
2. `list_agents` — which agents are active, their schedule and next run.
3. `list_notifications` — what the agents reported, risk alerts, finished backtests. Mark them read
   with `mark_notifications_read` only if the user asks.
4. `get_economic_calendar` — the high-impact events in the next day or two for the markets held.
5. Optional, when an agent did something worth explaining: `get_agent_runs` for that agent, and
   `get_conversation` for one run's full reasoning.

## The report

**Accounts** — one line per platform: balance (and equity when different), currency.

**Open positions** — per position: market, side, size and leverage, entry, unrealised P&L, stop and
target. Flag, factually:
- a position with **no stop** ("no stop-loss on the platform");
- a position whose loss is a large share of the account;
- two positions that are really one bet (BTC and ETH long at high leverage together).

**Agents** — active count; for each that ran since the last check, one line of what it did (from
its run summary). An agent that failed or skipped (no credits, no broker) gets a line saying why.

**Coming up** — high-impact events that touch what is held, with the time in the user's zone.

## Rules

- Only report figures the tools returned. If a platform could not be read, say which one; do not
  fill in a balance.
- No advice: "no stop on this position" is a fact; "set a stop at 2,350" is advice — do not.
- If the user wants to act (close, set a stop, pause an agent), use the matching tools only on
  their explicit instruction: `pause_agent` / `pause_all_agents` for agents, and the platform's own
  tools (skill `cubrik-trading`) for positions.
