---
name: analyzera-build-portfolio
description: Build, create or set up an investment portfolio or strategy with Analyzera, such as "build a portfolio with AI stocks", "make me a dividend portfolio", "I want a Swedish tech portfolio" or "a 60/40 with funds". Use before calling any Analyzera screening, weighting or build tool when the client has not said how they want to build it.
---

# Building a portfolio with Analyzera

"Build a portfolio" can mean several things, and each ends differently. Find out
which one the client means before calling a screening, weighting or build tool.

## 1. Check the catalogue

For a theme, sector or style (AI, defence, energy, dividends), call
`find_portfolios` with it as `query`, for example `query='AI'`. It is a read and
saves nothing. Its result tells you whether a ready-made strategy exists.

## 2. Ask which route

Ask one question, offering the routes that apply:

1. **Use a ready-made strategy**: only when step 1 found one. Name it.
2. **Build their own strategy now**: saved, rebalances automatically, can be
   backtested. `build_equity_strategy` for single stocks,
   `build_allocation_strategy` for funds, ETFs or other strategies.
3. **Explore by hand first**: screen stocks and try weightings, nothing saved.
   `screen_equities`, then `solve_equity_weights`.

Present the routes neutrally and recommend none. The client chooses.

### Example

> **Client:** I want to build a portfolio with AI stocks
>
> `find_portfolios(query='AI')` finds "Artificial Intelligence Theme".
>
> **Ask:** "Analyzera has a ready-made Artificial Intelligence Theme strategy.
> Would you like to look at it, build your own AI strategy straight away, or
> explore AI stocks by hand with the screener and weightings first?"

## 3. Follow the answer

- **Ready-made**: show it with `open_dashboard` on its id, or answer from the
  `describe_portfolio_*` reads.
- **Build now**: ask for the construction choices the client has not stated
  (markets, weighting, roughly how many holdings), say that building saves a
  strategy, then build.
- **Explore**: screen with `screen_equities`, weight with `solve_equity_weights`,
  and measure with `describe_holdings`. Stay unsaved until the client asks to
  save. Then save the screen: pass the result's `request` unchanged, plus a name,
  to `build_equity_strategy`. Never copy the ids from a screen or weighting into
  `asset_ids`.

## A screen is saved as a screen, not as its result

Investing with a stock screener over time means running the screen again at
every rebalance, with only what was known on that date. That is what
`build_equity_strategy` does with screen arguments, and it is what makes a
backtest of the approach honest.

The companies a screen or weighting lists are today's answer. Saved as
`asset_ids` they are held through the whole history, including the years before
anyone could have picked them. That backtest shows hindsight bias, not how the
approach would have done. The same holds for a list assembled from today's
screen results, today's holdings, or both together.

Use `asset_ids` only when the client brings their own list from outside the
screener (names they chose, a list they follow) and says they want it held as
it is. If a backtest should match exactly the mix you just showed, explain that
the saved screen will hold different names in earlier years, and that this is
the point.

## When not to ask

A request that names its route goes ahead on it:

- "Screen Swedish dividend stocks": screen.
- "Build me a 60/40 with these funds": an allocation.
- "Record what I hold in my ISK": `sync_external_account`.

## Funds and ETFs

The client chooses the funds. Resolve the names they give with `find_assets`
(kinds `fund` or `etf`). There is no fund screener, so never pick funds on the
client's behalf.

## Factors and styles

The catalogue holds factor strategies (value, quality, momentum and others) side
by side. Analyzera does not recommend either direction of any factor tilt, and
having a strategy on the shelf is no endorsement. You may make a case for one from
your own sources and test it with the builders and backtests, but present it as
yours, not Analyzera's. The client chooses.
