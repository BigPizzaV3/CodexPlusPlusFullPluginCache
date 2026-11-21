---
name: cubrik-library
description: Find, compare and copy ready-made agents from cubrik's Library. Use when the user asks for a ready-made strategy or agent, "something that trades gold / BTC / forex", "what agents are popular", "show me the Library", wants to compare two agents' backtests, or wants to copy one into their account. Searches the Library, reads an agent's details and weekly backtest history, compares them on return and drawdown together, and copies one — paused — only when the user asks.
---

The Library holds cubrik's ready-made agents (and agents members chose to share), each backtested
over twelve months and re-tested every week. Nothing in it is ranked or recommended: present the
figures, help the user compare, and let them choose.

## Calls

1. `search_library` (`query` narrows by name, market or style; `limit` up to 50). Each entry has its
   markets, style, timeframe, schedule, leverage, the 12-month backtest (return, max drawdown, win
   rate, trades, profit factor, a curve), copies running, and the Jev score where it has one. In apps
   that show cubrik's screens this draws the Library cards with Copy buttons.
2. `get_library_agent` (`library_id` from the search) — the rules in words, the instruction a copy
   carries, its limits, and the backtest by market.
3. `copy_library_agent` (`library_id`; `platforms` from `list_platforms` when more than one is
   connected; `time_zone`) — makes a paused agent in the user's account and returns its link.

## Comparing

Put candidates side by side on the same columns: 12-month return, maximum drawdown, win rate,
number of trades, and the markets. Read return and drawdown together — 40% with a 35% drawdown is a
different thing from 15% with 5%. Say when a figure rests on few trades. The Jev score summarises
the backtest (return for the risk, deepest fall, consistency, both halves of the year, profit
factor, and how clearly the plan is written); it describes the past and predicts nothing.

## Copying

Copy only on the user's request. The copy is created **paused**: say so, give its link, and offer
to test it (`test_agent`) or to start it later (skill `cubrik-agent-builder`). If the account has
more than one platform, ask which one the copy should trade on before copying.

## Rules

- Never call a Library agent "the best", "recommended" or "profitable going forward".
- Always say a backtest describes past prices and an agent trades live ones.
- A copy obeys the user's plan: if they are at their agent limit the copy still works but cannot
  be started until another agent is paused.
