---
name: get-started
description: How to answer business-day, settlement-date, holiday and market-hours questions with the TradingCalendars tools.
---

# Using TradingCalendars

Use these tools when the user asks about financial holidays, business days,
settlement or value dates, or whether a market is open.

## Pick the calendar

- FX trade or currency value date: `<CCY>.FX` per currency (e.g. `USD.FX`, `EUR.FX`).
- Currency clearing / settlement: `currency_non_clearing_days` with an ISO 4217 code.
- Bank holidays: `bank_holidays` with a UN/LOCODE financial centre (e.g. `GBLON`, `USNYC`, `SGSIN`).
- Payment systems: `payment_system_holidays` (e.g. `TARGET2`, `FEDWIRE`, `CHAPS`).
- Exchanges: `trading_holidays`, `settlement_holidays` and `market_status` with an ISO 10383 MIC (e.g. `XNYS`, `XLON`).
- Unsure of a code: call `list_calendars`, `list_currencies`, `list_exchanges`, `list_financial_centres` or `list_payment_systems`.

## Answer the question asked

- "Is it a business day?": `is_business_day` with every calendar involved (a EUR/USD trade needs both `USD.FX` and `EUR.FX`).
- "T+N / settlement / payment date": `add_business_days`.
- "How many business days between…": `business_days_between` (start counted, end not).
- Holiday lists default to today onward: pass `start` for past dates and `end` to bound the range.

## Report clearly

- Name the holidays the tool skipped, and mention half days and early closes (`half_day`, `early_close_time`).
- Say when a date is flagged `is_estimated` (provisional, e.g. lunar holidays not yet confirmed).
- Results include a `quota` block. When it carries a note about the data window or the daily limit, tell the user.
