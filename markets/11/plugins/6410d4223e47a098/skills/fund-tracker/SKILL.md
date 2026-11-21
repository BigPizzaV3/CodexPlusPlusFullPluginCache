---
name: fund-tracker
description: Use when the user asks what a hedge fund or famous investor bought, sold or holds, or which funds hold a stock. Examples are "what did Berkshire buy last quarter", "Michael Burry's latest 13F", "Ackman portfolio changes", "which hedge funds own NVDA" and "did any big fund sell TSLA". Reads 13F holdings changes through AlphaYou, with the quarter end, filing date and SEC link. Research only: no advice and no claim that following a fund would earn anything.
---

# Fund tracker

Show what a fund disclosed, for which quarter, and when it was filed.

## Tools

- `get_smart_money` with `category: funds`: 13F holdings changes. Pass `actor` for a fund or manager name such as Berkshire, Scion or Pershing, `ticker` for one stock, and `activity` `buy` or `sell` for direction.

## Steps

1. Find the fund, the stock and the direction in the question. "What did X buy" is `actor` with `activity: buy`. "Who holds Y" is `ticker` with no actor.
2. Use the manager's fund name as the `actor` if the user names a person, for example Berkshire for Buffett. If no row comes back, say so and do not guess another name.
3. Write the answer first, in one or two sentences. Then one row per change: fund, stock, added or reduced, the quarter end, the filing date and the link.

## Rules

- 13F rows are quarter-end holdings filed up to 45 days later. They are not current trades and they show no purchase price. A change in reported value mixes share changes with price moves.
- 13F filings cover long US equity positions only. Shorts, cash and most other assets are not in them.
- If the latest quarter is not filed yet, say which quarter the newest filing covers.
- AlphaYou has no fund performance ranking in this app. If the user asks which fund did best, say so and do not rank from memory.
- No verdict on which fund to follow. Ignore the user's holdings and risk tolerance.
