# Explore StockViz Mutual Funds

> [@StockViz Mutual Funds](plugin://stockviz-mutual-funds@created-by-me-remote) what can you do?

<details><summary>1 previous message</summary>

> I’ll inspect the StockViz Mutual Funds plugin’s available capabilities and summarize what it can do.
</details>

The StockViz Mutual Funds plugin can:

- List published mutual-fund strategies.
- Show exact strategy rules, provenance, and current model portfolios.
- Retrieve portfolio holdings, scheme codes, factors, weights, and as-of dates.
- Find linked backtests and view their summaries.
- Calculate backtest metrics for custom date ranges.
- Compare multiple backtest runs.
- Explain factor-momentum signals for a strategy and date.
- Compare approved factor indices with NIFTY 500 TR.
- Report data freshness and validation status.

It works with published model data and backtests; it doesn’t place trades or provide personalized financial advice.

> Available strategies

<details><summary>3 previous messages</summary>

> I’ll retrieve the currently published strategies from the plugin.
>
> <details><summary>Called a tool</summary>
>
> MCP tool call
>
> stockviz-mutual-funds.list_strategies
>
> ```json
> {}
> ```
>
> ```text
> [{"strategy_id":"factor-momentum","name":"Indian MF Factor Momentum","backtest_run_id":"factor-momentum-20260925-f3de4481b982","definition":{"strategy_id":"factor-momentum","strategy_name":"Indian MF Factor Momentum","backtest_label":"factor-rotation-ew","signal_frequency":"monthly","signal_rule":"Select the factor with the highest completed prior-calendar-month return.","execution_rule":"Hold the selected factor during the following calendar month.","signal_lag":"The prior completed month determines the current month.","factor_indices":["NIFTY500 LOW VOLATILITY 50 TR","NIFTY500 MOMENTUM 50 TR","NIFTY500 QUALITY 50 TR","NIFTY500 VALUE 50 TR"],"benchmark":"NIFTY 500 TR","switch_cost":0.002,"switch_cost_convention":"Applied once when the selected factor changes.","return_frequency":"monthly","annualization_factor":12,"source_tables":{"factor_prices":"StockViz.dbo.BHAV_INDEX","benchmark_prices":"StockViz.dbo.BHAV_INDEX"},"source_script":"factor-rotation-ew.R","selection_policy":"No parameter selection; this is a fixed-rule descriptive backtest.","windows":{"pre":{"start":null,"end":"2019-12-31"},"post":{"start":"2020-05-01","end":null},"full":{"start":null,"end":null}},"run_id":"factor-momentum-20260925-f3de4481b982","generated_at_utc":"2026-09-27 04:34:44 UTC","coverage_start":"2005-05-31","coverage_end":"2026-09-25","observation_count":771,"metric_count":9,"drawdown_episode_count":75,"current_portfolio":{"strategy_id":"factor-momentum","as_of":"2026-09-25","signal_month":"2026-09","prior_month":"2026-08","factor_winner":"NIFTY500 MOMENTUM 50 TR","prior_month_return":"0.050480823507105721167214490","positions":[{"scheme_code":"152881","scheme_name":"Nippon India Nifty 500 Momentum 50 Index Fund - Direct Plan - Growth Option","factor":"NIFTY500 MOMENTUM 50 TR","weight":1}],"provenance":{"source":"PortfolioManager.plan","signal_rule":"Select the factor with the highest completed prior-calendar-month return.","execution_rule":"Hold the selected factor during the following calendar month.","dataset_version":"factor-momentum-20260925-f3de4481b982"}},"publication_counts":{"strategy_definitions":1,"backtest_runs":1,"backtest_metrics":9,"backtest_observations":771,"drawdown_episodes":75,"reference_indices":1,"index_observations":257}},"dataset_version":"factor-momentum-20260925-f3de4481b982"}]
> ```
>
> </details>
>
> MCP server elicitation
>
> Status: completed
> Action: accept
</details>

Currently, one strategy is published:

**Indian MF Factor Momentum** (`factor-momentum`)

- Monthly factor-rotation strategy
- Selects the factor with the highest completed prior-month return
- Holds the selected factor during the following month
- Covers Low Volatility, Momentum, Quality, and Value indices
- Current selected fund: Nippon India Nifty 500 Momentum 50 Index Fund — Direct Growth
- Latest portfolio as of **25 September 2026**

> One strategy’s rules and current portfolio.

<details><summary>5 previous messages</summary>

> I’ll fetch the strategy’s exact rules and its latest model portfolio.
>
> <details><summary>Called a tool</summary>
>
> MCP tool call
>
> stockviz-mutual-funds.get_strategy_definition
>
> ```json
> {
>   "strategy_id": "factor-momentum"
> }
> ```
>
> ```text
> {"strategy_id":"factor-momentum","name":"Indian MF Factor Momentum","backtest_run_id":"factor-momentum-20260925-f3de4481b982","definition":{"strategy_id":"factor-momentum","strategy_name":"Indian MF Factor Momentum","backtest_label":"factor-rotation-ew","signal_frequency":"monthly","signal_rule":"Select the factor with the highest completed prior-calendar-month return.","execution_rule":"Hold the selected factor during the following calendar month.","signal_lag":"The prior completed month determines the current month.","factor_indices":["NIFTY500 LOW VOLATILITY 50 TR","NIFTY500 MOMENTUM 50 TR","NIFTY500 QUALITY 50 TR","NIFTY500 VALUE 50 TR"],"benchmark":"NIFTY 500 TR","switch_cost":0.002,"switch_cost_convention":"Applied once when the selected factor changes.","return_frequency":"monthly","annualization_factor":12,"source_tables":{"factor_prices":"StockViz.dbo.BHAV_INDEX","benchmark_prices":"StockViz.dbo.BHAV_INDEX"},"source_script":"factor-rotation-ew.R","selection_policy":"No parameter selection; this is a fixed-rule descriptive backtest.","windows":{"pre":{"start":null,"end":"2019-12-31"},"post":{"start":"2020-05-01","end":null},"full":{"start":null,"end":null}},"run_id":"factor-momentum-20260925-f3de4481b982","generated_at_utc":"2026-09-27 04:34:44 UTC","coverage_start":"2005-05-31","coverage_end":"2026-09-25","observation_count":771,"metric_count":9,"drawdown_episode_count":75,"current_portfolio":{"strategy_id":"factor-momentum","as_of":"2026-09-25","signal_month":"2026-09","prior_month":"2026-08","factor_winner":"NIFTY500 MOMENTUM 50 TR","prior_month_return":"0.050480823507105721167214490","positions":[{"scheme_code":"152881","scheme_name":"Nippon India Nifty 500 Momentum 50 Index Fund - Direct Plan - Growth Option","factor":"NIFTY500 MOMENTUM 50 TR","weight":1}],"provenance":{"source":"PortfolioManager.plan","signal_rule":"Select the factor with the highest completed prior-calendar-month return.","execution_rule":"Hold the selected factor during the following calendar month.","dataset_version":"factor-momentum-20260925-f3de4481b982"}},"publication_counts":{"strategy_definitions":1,"backtest_runs":1,"backtest_metrics":9,"backtest_observations":771,"drawdown_episodes":75,"reference_indices":1,"index_observations":257}},"dataset_version":"factor-momentum-20260925-f3de4481b982"}
> ```
>
> </details>
>
> MCP server elicitation
>
> Status: completed
> Action: accept
>
> <details><summary>Called a tool</summary>
>
> MCP tool call
>
> stockviz-mutual-funds.get_strategy_portfolio
>
> ```json
> {
>   "strategy_id": "factor-momentum"
> }
> ```
>
> ```text
> {"strategy_id":"factor-momentum","as_of":"2026-09-25","signal_month":"2026-09","prior_month":"2026-08","factor_winner":"NIFTY500 MOMENTUM 50 TR","prior_month_return":"0.050480823507105721167214490","positions":[{"scheme_code":"152881","scheme_name":"Nippon India Nifty 500 Momentum 50 Index Fund - Direct Plan - Growth Option","factor":"NIFTY500 MOMENTUM 50 TR","weight":1}],"provenance":{"source":"PortfolioManager.plan","signal_rule":"Select the factor with the highest completed prior-calendar-month return.","execution_rule":"Hold the selected factor during the following calendar month.","dataset_version":"factor-momentum-20260925-f3de4481b982"}}
> ```
>
> </details>
>
> MCP server elicitation
>
> Status: completed
> Action: accept
</details>

### Indian MF Factor Momentum

Rules:

- Rebalance monthly.
- Select the factor with the highest return in the completed prior calendar month.
- Hold that factor during the following month.
- Covered factors: Low Volatility, Momentum, Quality, and Value.
- A 0.2% switching cost applies when the selected factor changes.
- Benchmark: NIFTY 500 TR.

Current portfolio, as of **25 September 2026**:

| Fund | Factor | Weight |
|---|---|---:|
| Nippon India Nifty 500 Momentum 50 Index Fund — Direct Growth | NIFTY500 Momentum 50 TR | 100% |

The Momentum factor won the August 2026 comparison with a **5.05%** return.

> Its backtest results.

<details><summary>3 previous messages</summary>

> I’ll retrieve the published backtest summary for the Indian MF Factor Momentum strategy.
>
> <details><summary>Called a tool</summary>
>
> MCP tool call
>
> stockviz-mutual-funds.get_backtest_summary
>
> ```json
> {
>   "run_id": "factor-momentum-20260925-f3de4481b982"
> }
> ```
>
> ```text
> {"run_id":"factor-momentum-20260925-f3de4481b982","strategy_id":"factor-momentum","definition_json":"{\"strategy_id\":\"factor-momentum\",\"strategy_name\":\"Indian MF Factor Momentum\",\"backtest_label\":\"factor-rotation-ew\",\"signal_frequency\":\"monthly\",\"signal_rule\":\"Select the factor with the highest completed prior-calendar-month return.\",\"execution_rule\":\"Hold the selected factor during the following calendar month.\",\"signal_lag\":\"The prior completed month determines the current month.\",\"factor_indices\":[\"NIFTY500 LOW VOLATILITY 50 TR\",\"NIFTY500 MOMENTUM 50 TR\",\"NIFTY500 QUALITY 50 TR\",\"NIFTY500 VALUE 50 TR\"],\"benchmark\":\"NIFTY 500 TR\",\"switch_cost\":0.002,\"switch_cost_convention\":\"Applied once when the selected factor changes.\",\"return_frequency\":\"monthly\",\"annualization_factor\":12,\"source_tables\":{\"factor_prices\":\"StockViz.dbo.BHAV_INDEX\",\"benchmark_prices\":\"StockViz.dbo.BHAV_INDEX\"},\"source_script\":\"factor-rotation-ew.R\",\"selection_policy\":\"No parameter selection; this is a fixed-rule descriptive backtest.\",\"windows\":{\"pre\":{\"start\":null,\"end\":\"2019-12-31\"},\"post\":{\"start\":\"2020-05-01\",\"end\":null},\"full\":{\"start\":null,\"end\":null}},\"run_id\":\"factor-momentum-20260925-f3de4481b982\",\"generated_at_utc\":\"2026-09-27 04:34:44 UTC\",\"coverage_start\":\"2005-05-31\",\"coverage_end\":\"2026-09-25\",\"observation_count\":771,\"metric_count\":9,\"drawdown_episode_count\":75,\"current_portfolio\":{\"strategy_id\":\"factor-momentum\",\"as_of\":\"2026-09-25\",\"signal_month\":\"2026-09\",\"prior_month\":\"2026-08\",\"factor_winner\":\"NIFTY500 MOMENTUM 50 TR\",\"prior_month_return\":\"0.050480823507105721167214490\",\"positions\":[{\"scheme_code\":\"152881\",\"scheme_name\":\"Nippon India Nifty 500 Momentum 50 Index Fund - Direct Plan - Growth Option\",\"factor\":\"NIFTY500 MOMENTUM 50 TR\",\"weight\":1}],\"provenance\":{\"source\":\"PortfolioManager.plan\",\"signal_rule\":\"Select the factor with the highest completed prior-calendar-month return.\",\"execution_rule\":\"Hold the selected factor during the following calendar month.\",\"dataset_version\":\"factor-momentum-20260925-f3de4481b982\"}},\"publication_counts\":{\"strategy_definitions\":1,\"backtest_runs\":1,\"backtest_metrics\":9,\"backtest_observations\":771,\"drawdown_episodes\":75,\"reference_indices\":1,\"index_observations\":257}}","coverage_start":"2005-05-31","coverage_end":"2026-09-25","dataset_version":"factor-momentum-20260925-f3de4481b982","definition":{"strategy_id":"factor-momentum","strategy_name":"Indian MF Factor Momentum","backtest_label":"factor-rotation-ew","signal_frequency":"monthly","signal_rule":"Select the factor with the highest completed prior-calendar-month return.","execution_rule":"Hold the selected factor during the following calendar month.","signal_lag":"The prior completed month determines the current month.","factor_indices":["NIFTY500 LOW VOLATILITY 50 TR","NIFTY500 MOMENTUM 50 TR","NIFTY500 QUALITY 50 TR","NIFTY500 VALUE 50 TR"],"benchmark":"NIFTY 500 TR","switch_cost":0.002,"switch_cost_convention":"Applied once when the selected factor changes.","return_frequency":"monthly","annualization_factor":12,"source_tables":{"factor_prices":"StockViz.dbo.BHAV_INDEX","benchmark_prices":"StockViz.dbo.BHAV_INDEX"},"source_script":"factor-rotation-ew.R","selection_policy":"No parameter selection; this is a fixed-rule descriptive backtest.","windows":{"pre":{"start":null,"end":"2019-12-31"},"post":{"start":"2020-05-01","end":null},"full":{"start":null,"end":null}},"run_id":"factor-momentum-20260925-f3de4481b982","generated_at_utc":"2026-09-27 04:34:44 UTC","coverage_start":"2005-05-31","coverage_end":"2026-09-25","observation_count":771,"metric_count":9,"drawdown_episode_count":75,"current_portfolio":{"strategy_id":"factor-momentum","as_of":"2026-09-25","signal_month":"2026-09","prior_month":"2026-08","factor_winner":"NIFTY500 MOMENTUM 50 TR","prior_month_return":"0.050480823507105721167214490","positions":[{"scheme_code":"152881","scheme_name":"Nippon India Nifty 500 Momentum 50 Index Fund - Direct Plan - Growth Option","factor":"NIFTY500 MOMENTUM 50 TR","weight":1}],"provenance":{"source":"PortfolioManager.plan","signal_rule":"Select the factor with the highest completed prior-calendar-month return.","execution_rule":"Hold the selected factor during the following calendar month.","dataset_version":"factor-momentum-20260925-f3de4481b982"}},"publication_counts":{"strategy_definitions":1,"backtest_runs":1,"backtest_metrics":9,"backtest_observations":771,"drawdown_episodes":75,"reference_indices":1,"index_observations":257}},"metrics":[{"series":"Factor Equal Weight","window_start":"2005-05-31","window_end":"2026-09-25","TotalReturn":38.680100524091955,"CAGR":0.18752163283944978,"Volatility":0.21391302746762259,"Sharpe":0.9168779858947689,"Sortino":1.4833165532084605,"MaxDD":-0.5654575676532292,"Calmar":0.34685563869125824,"N":257,"annualization_factor":12,"PositiveMonths":0.6264591439688716},{"series":"Factor Rotation","window_start":"2005-05-31","window_end":"2026-09-25","TotalReturn":63.93016578345234,"CAGR":0.21514429620813913,"Volatility":0.2717701891680962,"Sharpe":0.8508726110432562,"Sortino":1.60769447727502,"MaxDD":-0.6361689735889503,"Calmar":0.3634911793271305,"N":257,"annualization_factor":12,"PositiveMonths":0.622568093385214},{"series":"NIFTY 500 TR","window_start":"2005-05-31","window_end":"2026-09-25","TotalReturn":16.271054406581705,"CAGR":0.14228281441945012,"Volatility":0.21813058805924088,"Sharpe":0.7232921946920704,"Sortino":1.1317951115924285,"MaxDD":-0.6043618749158531,"Calmar":0.26105576528765534,"N":257,"annualization_factor":12,"PositiveMonths":0.6303501945525292}],"metric_status":"ok","metric_provenance":{"dataset_version":"factor-momentum-20260925-f3de4481b982","calculation":"@railpath/finance-toolkit@0.5.4","annualization_factor":12,"risk_free_rate":0,"sortino_mar":0,"calmar_numerator":"annualized arithmetic mean"}}
> ```
>
> </details>
>
> MCP server elicitation
>
> Status: completed
> Action: accept
</details>

Backtest period: **31 May 2005 – 25 September 2026**
Monthly data, with a **0.2% switching cost** applied when the selected factor changes.

| Series | Total return | CAGR | Volatility | Sharpe | Max drawdown |
|---|---:|---:|---:|---:|---:|
| Factor Rotation | 6,393.0% | 21.51% | 27.18% | 0.85 | -63.62% |
| Factor Equal Weight | 3,868.0% | 18.75% | 21.39% | 0.92 | -56.55% |
| NIFTY 500 TR | 1,627.1% | 14.23% | 21.81% | 0.72 | -60.44% |

The rotation strategy produced the highest CAGR and total return, but also experienced higher volatility and a deeper maximum drawdown than the equal-weight factor portfolio.

> A comparison of supported indices.

<details><summary>5 previous messages</summary>

> I’ll compare all supported factor indices against the NIFTY 500 TR benchmark over their aligned available history.
>
> <details><summary>Called a tool</summary>
>
> MCP tool call
>
> stockviz-mutual-funds.get_index_metrics
>
> ```json
> {
>   "indices": [
>     "NIFTY500 LOW VOLATILITY 50 TR",
>     "NIFTY500 MOMENTUM 50 TR",
>     "NIFTY500 QUALITY 50 TR",
>     "NIFTY500 VALUE 50 TR",
>     "NIFTY 500 TR"
>   ]
> }
> ```
>
> ```text
> {"requested_start":null,"requested_end":null,"winner":null,"metrics":[],"missing":[],"provenance":{"source_table":"bhav_index_observations","calculation":"@railpath/finance-toolkit@0.5.4","annualization_factor":252,"risk_free_rate":0,"dataset_version":"mf-eod-20260930-e6874ee15805"},"status":"data_gap","reason":"Requested indices do not have the same trading dates; no winner was inferred."}
> ```
>
> </details>
>
> MCP server elicitation
>
> Status: completed
> Action: accept
>
> The full set has mismatched trading-date coverage, so the plugin correctly declined to infer a single winner. I’ll run aligned pairwise comparisons against NIFTY 500 TR to provide a useful comparison.
>
> <details><summary>Called 4 tools</summary>
>
> MCP tool call
>
> stockviz-mutual-funds.get_index_metrics
>
> ```json
> {
>   "indices": [
>     "NIFTY500 LOW VOLATILITY 50 TR",
>     "NIFTY 500 TR"
>   ]
> }
> ```
>
> ```text
> {"requested_start":null,"requested_end":null,"winner":null,"metrics":[],"missing":[],"provenance":{"source_table":"bhav_index_observations","calculation":"@railpath/finance-toolkit@0.5.4","annualization_factor":252,"risk_free_rate":0,"dataset_version":"mf-eod-20260930-e6874ee15805"},"status":"data_gap","reason":"Requested indices do not have the same trading dates; no winner was inferred."}
> ```
>
> MCP tool call
>
> stockviz-mutual-funds.get_index_metrics
>
> ```json
> {
>   "indices": [
>     "NIFTY500 QUALITY 50 TR",
>     "NIFTY 500 TR"
>   ]
> }
> ```
>
> ```text
> {"requested_start":null,"requested_end":null,"winner":null,"metrics":[],"missing":[],"provenance":{"source_table":"bhav_index_observations","calculation":"@railpath/finance-toolkit@0.5.4","annualization_factor":252,"risk_free_rate":0,"dataset_version":"mf-eod-20260930-e6874ee15805"},"status":"data_gap","reason":"Requested indices do not have the same trading dates; no winner was inferred."}
> ```
>
> MCP tool call
>
> stockviz-mutual-funds.get_index_metrics
>
> ```json
> {
>   "indices": [
>     "NIFTY500 MOMENTUM 50 TR",
>     "NIFTY 500 TR"
>   ]
> }
> ```
>
> ```text
> {"requested_start":null,"requested_end":null,"winner":null,"metrics":[],"missing":[],"provenance":{"source_table":"bhav_index_observations","calculation":"@railpath/finance-toolkit@0.5.4","annualization_factor":252,"risk_free_rate":0,"dataset_version":"mf-eod-20260930-e6874ee15805"},"status":"data_gap","reason":"Requested indices do not have the same trading dates; no winner was inferred."}
> ```
>
> MCP tool call
>
> stockviz-mutual-funds.get_index_metrics
>
> ```json
> {
>   "indices": [
>     "NIFTY500 VALUE 50 TR",
>     "NIFTY 500 TR"
>   ]
> }
> ```
>
> ```text
> {"requested_start":null,"requested_end":null,"winner":null,"metrics":[],"missing":[],"provenance":{"source_table":"bhav_index_observations","calculation":"@railpath/finance-toolkit@0.5.4","annualization_factor":252,"risk_free_rate":0,"dataset_version":"mf-eod-20260930-e6874ee15805"},"status":"data_gap","reason":"Requested indices do not have the same trading dates; no winner was inferred."}
> ```
>
> </details>
</details>

The plugin supports these indices:

- NIFTY500 Low Volatility 50 TR
- NIFTY500 Momentum 50 TR
- NIFTY500 Quality 50 TR
- NIFTY500 Value 50 TR
- NIFTY 500 TR benchmark

A direct daily comparison is currently unavailable because the indices do not share identical trading-date coverage. The plugin therefore returned a data-gap status and did not infer a winner.

The published backtest does support comparison of the combined **Factor Rotation**, **Factor Equal Weight**, and **NIFTY 500 TR** series.

> compare it over the backtest period

<details><summary>3 previous messages</summary>

> I’ll compare the published backtest series over the full available period: Factor Rotation, Factor Equal Weight, and NIFTY 500 TR.
>
> <details><summary>Called a tool</summary>
>
> MCP tool call
>
> stockviz-mutual-funds.get_backtest_metrics
>
> ```json
> {
>   "run_id": "factor-momentum-20260925-f3de4481b982",
>   "start": "2005-05-31",
>   "end": "2026-09-25",
>   "series": [
>     "Factor Rotation",
>     "Factor Equal Weight",
>     "NIFTY 500 TR"
>   ]
> }
> ```
>
> ```text
> {"run_id":"factor-momentum-20260925-f3de4481b982","requested_series":["Factor Rotation","Factor Equal Weight","NIFTY 500 TR"],"requested_start":"2005-05-31","requested_end":"2026-09-25","metrics":[{"series":"Factor Equal Weight","window_start":"2005-05-31","window_end":"2026-09-25","TotalReturn":38.680100524091955,"CAGR":0.18752163283944978,"Volatility":0.21391302746762259,"Sharpe":0.9168779858947689,"Sortino":1.4833165532084605,"MaxDD":-0.5654575676532292,"Calmar":0.34685563869125824,"N":257,"annualization_factor":12,"PositiveMonths":0.6264591439688716},{"series":"Factor Rotation","window_start":"2005-05-31","window_end":"2026-09-25","TotalReturn":63.93016578345234,"CAGR":0.21514429620813913,"Volatility":0.2717701891680962,"Sharpe":0.8508726110432562,"Sortino":1.60769447727502,"MaxDD":-0.6361689735889503,"Calmar":0.3634911793271305,"N":257,"annualization_factor":12,"PositiveMonths":0.622568093385214},{"series":"NIFTY 500 TR","window_start":"2005-05-31","window_end":"2026-09-25","TotalReturn":16.271054406581705,"CAGR":0.14228281441945012,"Volatility":0.21813058805924088,"Sharpe":0.7232921946920704,"Sortino":1.1317951115924285,"MaxDD":-0.6043618749158531,"Calmar":0.26105576528765534,"N":257,"annualization_factor":12,"PositiveMonths":0.6303501945525292}],"provenance":{"dataset_version":"factor-momentum-20260925-f3de4481b982","calculation":"@railpath/finance-toolkit@0.5.4","annualization_factor":12,"risk_free_rate":0,"sortino_mar":0,"calmar_numerator":"annualized arithmetic mean"}}
> ```
>
> </details>
>
> MCP server elicitation
>
> Status: completed
> Action: accept
</details>

Over the full backtest period (**31 May 2005 – 25 September 2026**):

| Series | Total return | CAGR | Volatility | Sharpe | Max drawdown |
|---|---:|---:|---:|---:|---:|
| Factor Rotation | 6,393.0% | 21.51% | 27.18% | 0.85 | -63.62% |
| Factor Equal Weight | 3,868.0% | 18.75% | 21.39% | 0.92 | -56.55% |
| NIFTY 500 TR | 1,627.1% | 14.23% | 21.81% | 0.72 | -60.44% |

Factor Rotation delivered the highest return and CAGR, while Factor Equal Weight had the best Sharpe ratio and lowest drawdown. These are the published backtest series; individual factor-index metrics are not separately published in this run.

> Dataset freshness.

<details><summary>3 previous messages</summary>

> I’ll check the plugin’s latest dataset freshness and validation status.
>
> <details><summary>Called a tool</summary>
>
> MCP tool call
>
> stockviz-mutual-funds.get_data_quality
>
> ```json
> {}
> ```
>
> ```text
> {"status":"published","counts":{"strategy_definitions":1,"backtest_runs":1,"backtest_metrics":9,"backtest_observations":771,"drawdown_episodes":75,"reference_indices":1,"index_observations":257,"fund_nav_observations":1652,"model_valuations":3,"bhav_index_observations":28261},"warnings":[],"publication_catalog":[{"catalog_name":"index","active_dataset_version":"mf-eod-20260930-e6874ee15805","status":"published","expected_counts_json":"{\"bhav_index_observations\":20}"},{"catalog_name":"nav","active_dataset_version":"mf-nav-20260930-cdd773f5e338","status":"published","expected_counts_json":"{\"fund_nav_observations\":1652,\"scheme_row_counts\":{\"152881\":489,\"152949\":475,\"153470\":344,\"153474\":344}}"},{"catalog_name":"research","active_dataset_version":"factor-momentum-20260925-f3de4481b982","status":"published","expected_counts_json":"{\"strategy_definitions\":1,\"backtest_runs\":1,\"backtest_metrics\":9,\"backtest_observations\":771,\"drawdown_episodes\":75,\"reference_indices\":1,\"index_observations\":257}"},{"catalog_name":"valuation","active_dataset_version":"mf-eod-20260930-e6874ee15805","status":"published","expected_counts_json":"{\"model_valuations\":3}"}]}
> ```
>
> </details>
>
> MCP server elicitation
>
> Status: completed
> Action: accept
</details>

Dataset status: **Published and validated**
Warnings: **None**

Latest datasets:

- **Index and valuation data:** 30 September 2026
- **Fund NAV data:** 30 September 2026
- **Strategy research/backtest:** through 25 September 2026

Published counts include:

- 1 strategy definition
- 1 backtest run
- 771 backtest observations
- 1,652 fund NAV observations
- 28,261 index observations
- 3 model valuations

> which fund should i buy?

<details><summary>2 previous messages</summary>

> The plugin can identify its current model fund, but that is not the same as a personal recommendation. I’ll verify the fund’s official product information before answering.
>
> <details><summary>Searched the web</summary>
>
> Searched the web for `site:nipponindiamf.com Nippon India Nifty 500 Momentum 50 Index Fund Direct Growth official`
>
> Searched the web for `Nippon India Nifty 500 Momentum 50 Index Fund Direct Growth official`
>
> </details>
</details>

If you mean “which fund does the StockViz strategy currently select,” it is:

**Nippon India Nifty 500 Momentum 50 Index Fund — Direct Plan — Growth**
Scheme code: **152881**
Model weight: **100%**
Selection date: **25 September 2026**

This is a momentum-focused equity index fund, so it can be volatile and is not automatically suitable for every investor. The official fund page lists its inception as **30 September 2024**. [Nippon India official fund page](https://mf.nipponindiaim.com/FundsAndPerformance/Pages/Nippon-India-Nifty-500-Momentum-50-Index-Fund.aspx?rmfsource=corporate)

I can identify the model’s selection, but I can’t determine what you personally should buy without knowing your investment horizon, risk tolerance, liquidity needs, and existing portfolio.

> but it

Could you complete your question? For example: “but it has…”, “but it underperformed…”, or “but it’s too risky…”

> buy it

I can’t buy mutual funds or place orders. I can help you verify the scheme, compare it with alternatives, and outline the steps to purchase it through your broker or AMC platform.

> Show my actual broker holdings and account balance using StockViz

StockViz Mutual Funds cannot access your actual broker account, holdings, cash balance, or transactions. It only provides published model portfolios, backtests, index data, and fund NAV information.

You’ll need to check your broker or mutual-fund platform directly for live account data.

> Use StockViz to calculate S&P 500 index metrics.

StockViz currently supports only:

- NIFTY500 Low Volatility 50 TR
- NIFTY500 Momentum 50 TR
- NIFTY500 Quality 50 TR
- NIFTY500 Value 50 TR
- NIFTY 500 TR

It does not currently support S&P 500 metrics.

