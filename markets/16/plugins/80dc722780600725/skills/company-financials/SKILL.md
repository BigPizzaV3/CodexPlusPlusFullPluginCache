---
name: company-financials
description: Use when the user asks for a company's reported financial figures (revenue, profit, assets, equity, cash flow or detailed line items), how they changed over time, or what had been filed by a past date, for companies and other registered entities in the 13 markets Trading Agent Data covers. Explains how to pick the right company, read the figures and present them with their periods, filing dates and sources.
---

# Company financials from filings

Trading Agent Data serves company financial statements as they were filed with company registers and regulators, each figure keyed to its filing date. Use its tools as follows.

## 1. Find the right company

- Call `search_companies` with the company name. Add `market` (for example `DK`, `JP`, `TW`) when the user names a country.
- One name can match companies in several markets, such as LEGO A/S in Denmark and a US company whose ticker is LEGO. Pick the entity in the market the user means and say which one you used (name, ticker, market).
- If the user's intent is unclear, list the matches with their markets and ask which one they mean.

## 2. Read the figures

- Current figures: `get_latest_fundamentals` with the ticker.
- Trends and multi-year tables: `get_fundamentals_history`, with `from` set to the earliest period end the user asks about.
- "As of" questions (what had been filed by a given day): pass `as_of` as YYYY-MM-DD.
- Metric names follow the vocabulary listed by `get_coverage` (for example `revenue`, `net_income`, `assets`, `equity`, `cash_flow_operating`). If a requested metric comes back in `metrics_not_found`, check that vocabulary and try the matching name, or omit `metric` to get all metrics.
- Use `get_data_dictionary` before comparing a detailed line item across markets.

## 3. Present the answer

- Give each figure with its currency, period (fiscal year or quarter and period end), filing date and source register, as the reply states them.
- Keep the reply's attribution notice with the figures.
- Say whether the figures are group (consolidated) accounts or the company's own (solo) accounts when the reply states the basis.
- If a reply covers the most recent reported fiscal year for that company, say which year it covers. Do not estimate or fill in other years.

## 4. Read the data correctly

- Taiwan (`.TW`) quarterly values are already single-quarter amounts. Do not subtract adjacent quarters. A full-year row stands in for the fourth quarter.
- For quarterly rows in the US and Taiwan, `fy` and `fp` are the calendar quarter that contains the period end.
- A missing figure is not a zero. `stale: true` means the company has filed since without that metric, so the figure is not current.
- Detailed line items keep the sign as filed (capex is negative in Taiwan and Japan).

## 5. Stay within scope

- The data is filed financial statements. It contains no share prices, forecasts or ratings, and no personal information about individuals.
- Do not turn the figures into buy or sell recommendations, price targets or forecasts. The tools cannot place trades or change any data.
