---
name: cashflow-forecast
description: Produce a cashflow forecast for an Exact Online administration by delegating to DataFlowr's hosted forecasting agent, then poll it and report the timeline with its assumptions. Use when the user asks about future cash, a liquidity outlook, a 13-week forecast, runway, or what the coming months look like.
---

# Cashflow forecast

## Overview

Never extrapolate cash yourself. DataFlowr hosts a forecasting agent over a
deterministic two-layer engine: open AR/AP converted to weekly buckets by due
date, and fitted monthly P&L series reconciled — with cash as the balancing
item — into a closed monthly cash statement. No arithmetic on the money path is
done by a model, and none should be done by you.

Two tools: `forecasting_agent` runs a forecast, `forecasting_agent_status`
polls it.

## Steps

**1 — Resolve the division and the anchor.**
Call `exact_online_divisions` first. The anchor is a financial period
(`FinYear`, `FinPeriod`), the same convention the closing agent uses. Left out,
it defaults to the last completed financial period. If the tool answers
`FCST_ANCHOR_UNRESOLVED`, the administration's period table cannot prove which
calendar month a period covers — ask the user for an explicit year and period
rather than assuming one from today's date.

**2 — Run it.**
Call `forecasting_agent` with the division, the anchor and the horizon the user
asked for. It returns a correlation key (`fcst-XXXXXX`).

Where the administration maintains a budget in Exact Online, budgeted P&L cells
override the fitted values by default. Pass `use_budget: false` only if the user
explicitly wants a purely statistical forecast; if several budget scenarios
exist for a year, name one with `budget_scenario` or the budget is skipped.

**3 — Poll.**
A run past the synchronous budget comes back `running`. Poll
`forecasting_agent_status` with the key. Do not start a second run.

**4 — Report.**
Lead with the shape of the timeline — where cash troughs, and how deep. Then:

- the **crossover**: where the forecast stops being driven by real open items
  (`direct`) and starts being driven by fitted series (`fitted`), with the
  blended stretch in between;
- the **assumptions** the engine lists — DSO/DPO lags, VAT cadence, payroll wage
  tax, exclusions, any one-offs the user supplied;
- per-series **model and error** (which fit won, and its backtest MAE), and
  which months came from budget rather than a fit.

Say plainly which parts are observed and which are modelled. A forecast reported
without its assumptions is worse than no forecast.

## Hard stops

- `FCST_UNSUPPORTED_PERIOD_STRUCTURE` or `FCST_CALENDAR_UNVERIFIED` → the
  administration is not on monthly periods the engine can map. Report that; do
  not approximate.
- `FCST_BUDGET_UNAVAILABLE` → the budget could not be read. Offer to re-run with
  `use_budget: false` rather than silently dropping it.
- The forecast is read-only. Nothing here books anything.
