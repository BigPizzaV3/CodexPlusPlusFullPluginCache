---
name: climate
description: >-
  Use this skill for MSCI climate and regulatory sustainability metrics at index/security level, including Weighted Average Carbon Intensity (WACI), Implied Temperature Rise (ITR), carbon footprinting, Climate VaR physical/transition risk, SFDR principal adverse impact indicators, and EU Taxonomy alignment. Also use it to show how a climate or sustainability screen — PAB, CTB, SRI, or a low-carbon or screened variant — reshapes an index against its parent. Always pair metrics with available coverage fields.
---

# Climate and regulatory sustainability metrics

Report climate/sustainability metrics with coverage, units, date, and definition. Coverage is part of the result, not optional metadata.

## Output

For each metric show: metric name, value, unit, coverage, as-of/fetched date, and index/security identity. Spell out WACI on first use. Describe Climate VaR as modelled scenario impact, not realized loss.

## Workflow

1. Resolve the index with `search_index_indexes`, or the security with `search_index_securities` for security-level questions.
2. Discover the exact metric with `search_index_datapoints`; do not construct ids from naming patterns.
3. When discovery returns an equivalent `imx` metric for an **equity index-level** analytic, prefer `calculate_metrics`. Otherwise use the catalog datapoint route.
4. Discover and fetch the metric's `cov_*` or other documented coverage counterpart whenever available. Do not report a coverage-sensitive climate/SFDR metric without its coverage field if the catalog provides one.
5. For catalog data: `fetch_index_data` for point-in-time; `fetch_index_timeseries` for supported history.
6. Read `constraints.notes`, variant/currency requirements, and date availability. Sustainability data can be end-of-month; if a request snaps, report the effective fetched date.

## Interpretation

- State the exact currency/denominator basis for WACI or carbon metrics when returned by the catalog.
- Use the returned metric definition/formula to distinguish similarly named carbon metrics.
- EU Taxonomy nuclear and gas components should remain separate unless the returned methodology explicitly defines an aggregate the user requested.
- Climate VaR is model-based and scenario-dependent.
- Implied Temperature Rise is a forward-looking modelled alignment estimate in degrees Celsius, not a realised or measured temperature. Report the model basis and date returned by discovery, and never present ITR as a carbon intensity or convert between the two.

## Screened index versus parent

For "how does the PAB/CTB/SRI version differ from the parent", or "what does this screen change":

1. Resolve both the screened index and its parent with `search_index_indexes`. Do not infer the parent from the name — confirm it, or ask.
2. Report the same metric id, currency, and date for both, following the `compare` alignment contract.
3. Give the metric difference first, then the compositional reason where the data supports it — for example excluded constituents or changed sector weights from `composition`.
4. For the governing exclusion rule or threshold itself, hand off to `methodology`. Do not infer a screen's rule from the metric gap.

## Guardrails

- Never omit available coverage.
- Do not imply regulatory disclosure sign-off; the data supports disclosure but does not replace the user's reporting methodology and controls.
- Missing coverage/data is a limitation, not zero exposure.
