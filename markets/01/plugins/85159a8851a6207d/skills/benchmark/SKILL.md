---
name: benchmark
description: >-
  Use this skill for MSCI benchmark and market-reference analysis: index performance and levels, trailing/forward valuation multiples, sector/country/industry composition, factor scores, benchmark-relative weights, or return series for beta/CAPM. Trigger when the user asks how a market/region is doing, what it trades at, or where a portfolio is over/underweight, even if they do not explicitly say MSCI.
---

# Benchmark and market reference

Use the MSCI Index app to answer market and benchmark-relative questions with reproducible index identity, date, variant, and currency.

## Output

Lead with the requested number or comparison. Then give only the supporting detail needed to interpret it. Always identify the resolved index and state the as-of date, variant, and currency for performance/level analytics.

## Workflow

1. Resolve every requested index with `search_index_indexes`. Never guess an MSCI index code. For several independent indexes, resolve them in parallel when possible.
2. Discover the required datapoint or IMX metric with `search_index_datapoints`.
3. Prefer an `imx` result with `calculate_metrics` for comparable **equity index-level** returns, ratios, risk, volatility, factor exposure, and other supported analytics. For fixed income, hedged, or other non-equity indexes, use catalog datapoints instead.
4. For catalog datapoints, route from the returned flags: point-in-time with `supports_single_day=true` → `fetch_index_data`; history with `supports_range=true` → `fetch_index_timeseries`.
5. Read and obey `strict_gate`, `range_window`, and `constraints.notes` before fetching.
6. Use `daily` frequency for true maxima/minima or exact peak/trough dates. Use `monthly` for month-by-month trends or end-of-month datasets.

## Performance rules

- `GRTR` is gross total return, `NETR` net total return, `STRD` price/standard. Do not treat them as interchangeable.
- When the user does not specify a variant and asks generic performance, use gross total return only when compatible and clearly say so.
- For IMX calculations, honor the tool's anchor-date semantics. A start date is the base date, not necessarily the first observation.
- Relative IMX metrics require a benchmark. Without `benchmark_portfolio`, tracking error, information ratio, active return and active drawdown return null rather than erroring - the absolute metrics populate and the relative ones come back blank. Pass a benchmark whenever the question is relative, and never read a blank as zero active risk.
- Calendar-year return: prior year-end business-day anchor through the requested year-end; report the period total, not an annualized number.
- YTD: prior year-end business-day anchor through the requested as-of date.
- N-year return when the user says "annualized": use the N-year anchor and report the annualized result.
- If the user wants performance through the latest available date, prefer `fixed_start` over inventing an end date.

## Valuation and composition

Discover exact ids rather than composing them from memory. Typical search concepts include:

- trailing/forward P/E, P/B, ROE, payout ratio, dividend yield
- ratio/fundamental data date
- sector, country, and industry-group weights
- value, growth, quality, momentum, size, volatility, liquidity, and dividend-yield factor scores

When a ratio has a separate source/fundamental date, report it alongside the calculation date. Do not imply a stale fundamental observation is current merely because the index calculation date is recent.

For over/underweight analysis, show portfolio weight, benchmark weight, and the difference. If portfolio weights were supplied by the user, do not replace them with index constituent weights.

## Guardrails

- Never assume index composition from its name.
- Never substitute a non-MSCI benchmark silently.
- Index-level ratios are aggregates, not necessarily constituent medians. Use the formula/definition returned by discovery when interpretation matters.
- If history is unavailable from `fetch_index_timeseries`, say so; do not reconstruct it with repeated point-in-time calls.
- Preserve units exactly as returned.
