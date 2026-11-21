---
name: market-brief
description: Use for a brief of what changed in a fixed time window on named US stocks and Hyperliquid markets, such as "what changed for NVDA and TSLA in the last 24 hours" or a morning note the user asks for. Collects new insider, Congress, fund and 8-K rows and observed Hyperliquid position changes through AlphaYou, with dates and source links. Says what is new, what is not, and what could not be checked. Research only: no advice or verdicts.
---

# Market brief

Report what is new in the window, with dates, and say plainly what could not be checked. This is research, not a call to act.

## Inputs

- Tickers: up to five US stocks.
- Assets: up to five Hyperliquid markets, as exact symbols such as `BTC`, `ETH` or `xyz:NVDA`.
- Window: hours back, 24 by default and 168 at most. If the user gives a start time, use it as `since`: an ISO date-time with seconds and a timezone, such as `2026-10-25T09:00:00Z`.
- If an input is missing, ask once. Do not guess tickers from what the user holds.

## Steps

1. For each ticker, call `get_smart_money` and keep only rows whose reported, disclosure or observation date is inside the window. Call `get_company_disclosures` and keep 8-K filings dated inside the window. Call `get_earnings_calendar` with that `ticker` and `days_ahead: 14` for the next announced date.
2. For each asset, call `get_hyperliquid_activity` with `coin`, `hours` and the same `since`. Then call `get_hyperliquid_positioning` and `get_hyperliquid_market_state`.
3. If an activity result has `next_cursor`, fetch the next page with that `cursor`, the `since` the result returned and the same filters, up to three pages. Say if more remained.
4. Write the brief:
   - Top line: the window, the retrieval time and how many new items, by section.
   - Stocks: one short block per ticker. New rows first, each with category, who, action, date and source link. If there are none, write "No new rows in the window".
   - Hyperliquid: one block per asset with the observed changes, then cohort long and short positioning and market state, each with its time.
   - Could not check: every tool that failed or returned unknown, by name.
5. Keep it to about 250 words plus the rows.

## Rules

- Older rows are context, not news. Do not repeat what the window does not contain.
- "No new rows" does not mean nothing happened. The tools return bounded previews, and watcher uptime is unknown.
- Apply the rules of the smart-money-check and hyperliquid-wallet-research skills: a sale is not a short, fund rows are quarter-end changes, leader returns are not follower returns, missing is unknown.
- No verdicts, targets or position sizing. Ignore the user's own holdings and risk tolerance.
- Run once per request. Do not offer to repeat it, schedule it or watch for changes. AlphaYou cannot create alerts or scheduled tasks.
