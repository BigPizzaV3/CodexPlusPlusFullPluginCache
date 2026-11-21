---
name: earnings-day-brief
description: Writes a short earnings-day brief from the dibsresearch connector - a company's newest reported quarter against the quarter before and the same quarter a year earlier (statement lines, the company's reported KPIs, the outlook in its own words), every figure with its source link and nothing from outside the filings. Use when the user asks what a company reported this quarter, for a results recap, an earnings summary or brief, or how the latest quarter compares with the previous one.
license: Proprietary, for use with dibsresearch only (see LICENSE.txt)
metadata:
  author: dibsresearch
  version: "1.0.0"
---

# Earnings-day brief

A one-screen brief of a company's newest reported quarter, from the dibsresearch connector only: what the company
reported, compared with the quarter before and the same quarter a year earlier.

## Steps

1. `search_companies(query)` when the user gives a name.
2. `get_financial_statements(symbol, statement="income", period="quarterly", periods=5)`: the newest quarter, the one
   before and the same quarter a year earlier. Note `anchor` (newest period and its filing) and `newer_results`.
3. If `newer_results` names a filing or release for a later quarter than the rows: the company has reported, but
   dibsresearch has not read the figures yet. Say so first, with the document's form, date and link, and do not take
   figures from it. Then brief the newest quarter dibsresearch has, named as such.
4. `get_financial_statements(symbol, statement="ratios", period="quarterly", periods=5)` for gross, operating and net
   margin (twelve months ending at each quarter: say so). Where the server does not serve ratios yet (the call is
   refused), leave the margins out and say so.
5. `list_company_kpis(symbol)`, then for up to six headline KPIs (segment revenue first, then the operating KPIs the
   company leads with): `get_kpi_series(symbol, kpi=<key>, quarters=5, include_derived=true, derived_kinds=["yoy",
   "qoq"])`.
6. Outlook: `search_documents(query="outlook guidance", symbol=<ticker>, date_from=<newest period end>)`, then
   `get_document_passage(document_id, query="outlook")` on the newest earnings release or filing. Quote up to three
   sentences word for word, with the link. If the company gives no outlook, say "No outlook in the documents read."

## Brief

- **Header**: company, quarter (`fiscal_label`, period end), the filing or release with its date and link.
- **Reported figures**: Line | This quarter | Prior quarter | Same quarter last year | Source, for revenue, gross
  profit, operating income, net income and diluted EPS as reported. Lines the company did not report stay "not
  reported".
- **Margins**: the ratios from step 4, labelled as trailing twelve months.
- **KPIs**: KPI | This quarter | QoQ | YoY | Source, the changes from the tool's computed values only.
- **Outlook**: the quoted sentences, marked as the company's words.
- **Not available**: what was asked or expected but not found.

Write it as facts: "revenue rose", "the margin fell". No "beat" or "miss" (there are no estimates here), no view on
the shares.

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
