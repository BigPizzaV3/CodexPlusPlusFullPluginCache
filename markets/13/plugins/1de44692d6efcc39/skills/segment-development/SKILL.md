---
name: segment-development
description: Shows how a company's business segments developed with the dibsresearch connector - revenue per segment over recent quarters, segment operating income or margin where the company reports it, and the shift in the revenue mix - as tables with a source link for every value. Use when the user asks about a company's segments, divisions, business units or product lines, which part of the business grows, the revenue mix or mix shift, or segment margins, or wants one segment compared across companies.
license: Proprietary, for use with dibsresearch only (see LICENSE.txt)
metadata:
  author: dibsresearch
  version: "1.0.0"
---

# Segment development

Answers "how did the segments of X develop" from the dibsresearch connector: segment revenue, segment profit and the
revenue mix over time, each value with its source.

## Steps

1. `search_companies(query)` when the user gives a name; it returns the ticker and whether KPI series exist. Without
   KPI series, say that dibsresearch has no segment figures for the company yet and offer the statement lines
   (`get_financial_statements`) instead.
2. `list_company_kpis(symbol)`: collect the segment KPIs. Segment revenue usually reads "Revenue · <segment>"; segment
   profit "Operating income · <segment>" or a segment margin. Use the company's own segment names and the definitions
   listed. Follow `next_offset` when the list comes in pages.
3. For each segment revenue KPI: `get_kpi_series(symbol, kpi=<key>, quarters=8, include_derived=true,
   derived_kinds=["yoy", "share"])`. `share` is the segment's part of the company's total as the template sums it; it is
   absent when the segments do not add up to a reported total.
4. For each segment profit KPI: `get_kpi_series(symbol, kpi=<key>, quarters=8, include_derived=true,
   derived_kinds=["margin"])`. A margin the company prints itself is its own KPI; take that one when both exist.
5. Optional, when the user asks why a segment moved: `search_documents(query="<segment> revenue increased",
   symbol=<ticker>)` and `get_document_passage(document_id, query)`; quote the company's explanation word for word
   with its link. Give no reasons of your own.

Read all segments with the same number of quarters, so the tables line up.

## Answer

1. **Segment revenue**: one row per quarter (newest first, by period end), one column per segment, a
   source link per row (or per value when the row mixes documents).
2. **Revenue mix**: the `share` values per quarter and segment, as percentages. One sentence per notable shift, naming
   only values from the table ("<segment> rose from <share> in <quarter> to <share> in <quarter>").
3. **Segment profit**: operating income and margin per segment where reported; segments without a reported profit
   figure say "not reported".
4. **Notes**: definition changes and recast segments listed by `list_company_kpis` (a series that starts or ends
   inside the window, a renamed segment), quarters marked provisional, and segments the company stopped reporting.
   Never splice an old and a new segment definition into one series.

For one segment across several companies, use `compare_companies(metric="<segment KPI name>", metric_type="kpi",
symbols=[…], periods=4)` (up to 25 companies) and show each company's own `kpi_name`, because segments are defined
differently.

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
