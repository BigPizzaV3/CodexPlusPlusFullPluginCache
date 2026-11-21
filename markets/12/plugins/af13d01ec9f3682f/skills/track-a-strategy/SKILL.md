---
name: track-a-strategy
description: Save a backtested strategy and follow it as a hypothetical shadow portfolio updated after every US market close, list saved strategies, show one, share its record or delete it. Use when the user wants to paper-trade, forward-test or check on a strategy they saved with Shadowfolio.
---

Use this skill when the user wants to keep a strategy going from today, or comes back to ask how a saved strategy is doing. The user's explicit instructions always come first.

## Flow

1. `save_strategy` takes the same rules that were backtested and starts a hypothetical 10,000 shadow portfolio from the latest close. It is kept under the user's anonymous ChatGPT ID; there is no account.
2. After every US market close the portfolio is updated from that day's closing prices.
3. `list_my_strategies` lists each saved strategy with its number, name and return since it was saved, next to its benchmark over the same days.
4. `show_strategy` shows one strategy by number or name: its forward-tracking record since saving (return, max drawdown, benchmark), its current simulated holdings and recent simulated trades, and the backtest from when it was saved.
5. `create_share_link` creates, or returns the existing, public link to a page with that strategy's rules and hypothetical record, when the user asks to share it.
6. `delete_strategy` stops tracking one strategy and deletes its record and share link; `delete_my_data` deletes everything of this user. Both are permanent.

## Scope

- Every figure is hypothetical: no real money, no broker connection and no trades are involved.
- Shadowfolio doesn't say whether a strategy is good or should be followed, and doesn't suggest changes on its own.
- Each result ends with a summary suitable to show the user; the card shows the chart and holdings.
