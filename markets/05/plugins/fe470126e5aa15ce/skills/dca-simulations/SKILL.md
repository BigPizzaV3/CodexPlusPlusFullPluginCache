---
name: dca-simulations
description: Use when someone asks what a regular buying plan would have been worth — "what if I'd put $50 a week into Bitcoin since 2018" — or wants to compare assets, buying schedules or start dates against real price history. Covers how to call the BTC DCA Engine tools and how to report what comes back.
---

# Running a dollar-cost-averaging simulation

The BTC DCA Engine answers one question with arithmetic: given an asset, an amount, a schedule and a
start date, what would that plan be worth now? It reads published daily closes. It does not forecast,
recommend or trade.

## Start with the catalogue

Call `list_assets` before composing a plan unless you already know the exact key. It returns each
asset's key, the dates its price series covers, and how often that series has a value. Two things go
wrong without it:

- **Asset keys are exact strings.** Bitcoin is `btc_daily`; the S&P 500 is `S&P 500`. A guessed name
  is refused rather than silently matched to something close.
- **A start date before an asset's first close is refused**, and the refusal names the first date.
  Solana begins in April 2020, Ethereum in November 2017; several macro series are quarterly, so a
  weekly plan on them buys on the dates that exist.

## Composing a run

`run_dca` takes one plan, `compare_plans` takes several and ranks them by final value.

- `amount` is money per purchase, not a total.
- `frequency` is `daily`, `weekly`, `monthly` or `quarterly`.
- `start_date` and the optional `end_date` are `YYYY-MM-DD`.
- `as_of` pins the run to a data vintage. Use it whenever the figure will be written down or compared
  later: without it, the same request returns a slightly different answer tomorrow, because the
  underlying data has moved on.
- `include` asks for the per-purchase ledger (`head` for the first 20, `all` up to 200) and
  end-of-year checkpoints. Ask for the ledger only when someone wants to see individual buys.

## Reporting the result

Lead with what was put in and what it is worth, then the returns:

- `total_invested` and `final_value`, and `net_profit` between them.
- `simple_annualized_pct` is the growth of the whole pot per year. `money_weighted_pct` accounts for
  money arriving over time, and is the honest figure for a plan that bought gradually. If you quote
  only one, quote the money-weighted one, and say which it is.
- `units` is how much of the asset the plan accumulated.
- `data_as_of` is the date the prices run to. Say it — a value "today" means the last completed day.

**Always pass on the `share_url`.** It reopens the identical run in the web app, pinned to the same
data, so the person can see the chart and check the numbers rather than take them on trust.

Keep the answer readable: short labelled lines rather than a wide table, and the link on its own.

## What needs an account

Without one, seven assets are available — Bitcoin, Ethereum, Solana, XRP, the S&P 500, the Nasdaq 100
and gold — and two plans per comparison. The rest of the catalogue, larger comparisons, and the
lump-sum, inflation, Mayer Multiple, risk and buy-rule settings need a paid account. A request beyond
the free plan is refused with a message naming what it needs; relay that plainly and move on. Do not
push the paid tier, and do not retry the same request hoping it goes through.

## Saying it accurately

- These are historical outcomes, not predictions. Never present a result as advice or a forecast.
- Past returns say nothing about future ones, and the engine's own results carry that note.
- If someone asks "should I", answer what the history shows and leave the decision with them.
