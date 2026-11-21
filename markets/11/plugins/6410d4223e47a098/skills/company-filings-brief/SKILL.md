---
name: company-filings-brief
description: Use when the user asks for a US company's reported earnings, EPS, revenue, margins, guidance, SEC financial statements, financial-quality ratios, recent 8-K filings or upcoming earnings dates, or for US macro and CFTC futures context. Reads stored SEC and government data with filing links and period dates through AlphaYou. No prices, valuation, analyst estimates or advice.
---

# Company filings brief

Give the figures the filings state, with the period and the link beside each one.

## Tools

- `get_company_earnings`: company-reported earnings, GAAP and adjusted EPS, revenue, margins, segments and guidance from release facts. `ticker`, and `limit` for the number of reports (up to 8).
- `get_stock_fundamentals`: stored SEC financial statements with period dates and a representative filing link. `ticker`.
- `get_financial_quality`: profitability and balance-sheet ratios computed only from matching SEC periods. `ticker`.
- `get_company_disclosures`: 8-K and 8-K/A filings over the last 365 days, newest first. `ticker`.
- `get_earnings_calendar`: earnings dates the company announced in 8-Ks. `ticker` (optional), `days_ahead` (1 to 90).
- `get_macro_context`: stored US government macro series with units and observation dates. No inputs.
- `get_futures_positioning`: weekly CFTC reports for `SPX`, `TY`, `WTI` or `GC` (`contract`, and `reports` up to 8).

## Steps

1. Match the question to the tools. "How did X do last quarter" is `get_company_earnings`. "Show the financials" is `get_stock_fundamentals`. "What did X file" is `get_company_disclosures`. "When does X report" is `get_earnings_calendar`. Context questions use the macro and futures tools.
2. Write the answer first, in one or two sentences. Then a short table: metric, value, unit, period end, link.

## Rules

- Each metric has its own period. A cash-flow figure can cover the year to date while earnings cover one quarter. Never apply one duration to every metric. If a duration is unverified, say it is unknown.
- A period link is a representative filing. It does not verify every value on that row.
- Earnings dates come from company announcements and can change. A missing date is unknown, not "no earnings soon".
- AlphaYou has no stock prices, valuation multiples, analyst estimates, beat or miss comparisons or news. Say so instead of filling the gap from memory.
- Futures positions are weekly and lag trading. They show categories of traders, not named wallets or live flows.
- Never turn the figures into a buy or sell call. Ignore the user's holdings, goals and risk tolerance.
