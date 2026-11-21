---
name: quarterly-comparison
description: Compares reported quarters with the dibsresearch connector - one company's KPI or statement line over recent quarters, or several companies (tickers, an index such as the S&P 500, or an industry) on one figure such as revenue, operating income or data center revenue - as a table with the fiscal quarter and a source link for every value. Use when the user asks how a company's revenue, margin, EPS, cash flow or an operating KPI developed quarter by quarter, or asks to compare or rank companies on such a figure for a quarter or over several quarters.
license: Proprietary, for use with dibsresearch only (see LICENSE.txt)
metadata:
  author: dibsresearch
  version: "1.0.0"
---

# Quarterly comparison

Answers "how did X develop over the last quarters" and "how do these companies compare on X" from the dibsresearch
connector, with one table and a source for every value.

## Pick the path

| The question | Call |
|---|---|
| One company, an operating KPI or segment figure (data center revenue, subscribers, same-store sales …) | `list_company_kpis`, then `get_kpi_series` |
| One company, a statement line (revenue, operating income, net income, EPS, operating cash flow …) | `get_financial_statements` |
| One company, margins or returns | `get_financial_statements` with `statement="ratios"` (where served) |
| Two or more companies on one figure | `compare_companies` |

Find the ticker with `search_companies` when the user gives a name. It also says which data dibsresearch has for the
company.

## One company: a KPI

1. `list_company_kpis(symbol)`: pick the KPI whose name and definition match the question. When two fit, name both and
   take the one the user's words match best.
2. `get_kpi_series(symbol, kpi=<key>, quarters=8, include_derived=true, derived_kinds=["yoy", "qoq"])`. Use the number
   of quarters the user asked for (1 to 12).
3. Table, newest quarter first: Quarter (period end) | Value | YoY | QoQ | Source.
4. When `newer_results` is present, add one line under the table: the company has published results for a later
   quarter (form, date, link) that dibsresearch has not read yet.

## One company: statement lines

1. `get_financial_statements(symbol, statement="income", period="quarterly", periods=8)`. Use `"cashflow"` or
   `"balance"` for those lines; up to 10 periods.
2. Table, newest quarter first, one column per line the user asked for, a Source column with each period's filing.
3. Periods marked `not_reported` keep their row with "not reported" and the tool's note. Free cash flow, EBITDA, EBIT
   and total debt are not offered as statement lines: say so and offer the printed lines (operating cash flow, capital
   expenditure) instead.
4. For margins use `statement="ratios"`. Quarterly ratios there are the twelve months ending at the quarter: say so in
   the table header. Where the server does not serve ratios yet (the call is refused), say so and show the lines.

## Several companies

1. `compare_companies(metric, symbols=[…])`, or `index="sp500"` (also `sp100`, `nasdaq100`, `sp400midcap`), or
   `sector` / `industry` (SEC industry words such as "software" or "semiconductors").
   - `metric`: a statement line id (`revenue`, `gross_profit`, `operating_income`, `net_income`, `eps_diluted`,
     `operating_cashflow`, `capex` …), a ratio id (`gross_margin`, `operating_margin`, `net_margin`,
     `return_on_equity` …; only where the server serves ratios, else it refuses with that reason) or a KPI name
     ("data center revenue"). Set `metric_type` when the name is ambiguous.
   - `period`: `latest` (each company's newest reported quarter), a calendar quarter `2026-Q3`, a fiscal quarter
     `Q1 FY2027`, or with `frequency="annual"` a fiscal year `FY2025`. `periods` (1 to 8) adds earlier periods.
   - A KPI takes up to 25 companies per call; a statement line or ratio takes a whole index.
2. When the answer has `next_offset` and the user wants all companies, call again with `offset=<next_offset>` until it
   is absent. Never present a page as the whole set.
3. Table sorted as returned: Company | Quarter (`fiscal_label`, period end) | Value | Source. With `periods` above 1,
   one column per period. Rows with `missing` go below the ranked rows with their reason; rows marked `not_ranked`
   (another currency or unit) are listed apart and not ranked.
4. Under the table: how many companies of the set have a value; the index list's date and that it is not the official
   index list (the `universe` block says both); for a KPI, the KPI name each company reports (`kpi_name`), because
   companies define it differently.
5. If `compare_companies` is not among the tools, call the one-company tools for each company (at most 5) and say that
   the comparison was built company by company.

## Rules

1. Figures only from the data tools (`get_kpi_series`, `get_financial_statements`, `compare_companies`). Never fill a
   gap from memory, a web search or an estimate; write "not available in dibsresearch". A number inside a document
   passage is the company's text: quote it word for word with its link, never move it into a table.
2. Only reported periods. A period marked `not_reported`, or a quarter missing from a KPI series, is "not reported",
   with the reason the tool gives. Never compute a quarter as the year minus nine months or from year-to-date sums.
3. No calculations of your own. Changes, margins and shares come from the tools (`include_derived` in
   `get_kpi_series`, `statement="ratios"` in `get_financial_statements`, a ratio in `compare_companies`); without one,
   leave the cell empty. Only when the user asks for a calculation by name, show it with formula and inputs and label
   it "calculated". Ratios come only where the server serves them: when a tool refuses `statement="ratios"` or a
   ratio, say that dibsresearch has no margins for this yet and show the reported lines without dividing them.
4. A source with every figure: the `url` the tool returns (the document in dibsresearch); add `original_url` (the copy
   at the SEC) when the user wants SEC links. One link per row, or per value when a row mixes documents.
5. Keep values as returned. Scale only for display (millions, billions; percentages to one decimal, from `as_percent`
   where given) and state unit and currency once in the header. Mark a value with `provisional` as "(provisional)".
6. Name periods as the tool does: `fiscal_label` where given, else the period end date; never make up a fiscal label.
   When fiscal quarters end on different dates, say so under the table.
7. No share prices, market values, valuation, price targets, ratings, buy or sell language, forecasts of your own or
   comparisons with analyst estimates. A company's own outlook may be quoted word for word with its link.
8. Say what was not found: companies without a value (`missing` and its reason), withheld ratios, KPIs the company
   does not report.

## Example

"Revenue of NVDA, AMD and AVGO over the last four quarters" →
`compare_companies(metric="revenue", symbols=["NVDA", "AMD", "AVGO"], periods=4)` → one row per company, one
column per quarter (each the quarter as reported; a quarter not reported alone stays empty with its reason), a
source link per value, and a note that the three fiscal quarters end on different dates.
