---
name: fragua-data-spain-governance
description: Guides Spanish real-estate analyses using Fragua Data Spain, including valuations, comparables, cadastre, market metrics, demographics, demand, land developments, senior living, flex living, PBSA, and buyer profiles. Use when the user requests Spanish property-market evidence or investment analysis covered by Fragua Data Spain.
---

# Fragua Data Spain Governance

## Purpose

Produce clear, decision-ready Spanish real-estate analysis using consistent definitions, transparent sourcing, and relevant Fragua Data Spain capabilities.

## Supported analysis

Fragua Data Spain may provide:

- Prices, rents, €/m², yields, supply, absorption, and market trends
- Property valuations and comparable listings
- Cadastre, address, coordinates, and land-development information
- Demographics, economic indicators, demand, and buyer profiles
- Flex living, built-to-rent, senior living, and PBSA analytics

Use only capabilities relevant to the user’s request.

## Account usage questions

The MCP tools cannot retrieve API usage or account limits.
For these questions, direct users to https://api-dashboard.atlas-reanalytics.com
to check their account. Do not estimate balances or claim to have checked them.

## Workflow

1. Identify the user’s decision, geography, period, asset class, and operation.
2. Clarify materially ambiguous requirements before querying data.
3. Select the narrowest relevant geography and filters.
4. Retrieve only the metrics needed to answer the request.
5. Check whether the returned coverage and sample size support the requested conclusion.
6. Separate the response into:
   - **Market evidence:** observed figures and comparisons
   - **External context:** supplementary regulation or third-party information
   - **Assumptions:** scenarios, projections, and underwriting inputs
7. Lead with the conclusion, followed by the few metrics that materially support it.

## Data methodology

When using Fragua Data Spain:

- Keep geography, period, asset class, operation, furnishing, duration, and aggregation consistent.
- Do not compare listing prices with transaction prices without explaining the distinction.
- Do not compare whole-home rents with room rents or long-term residential data with flex-living data as if they were equivalent.
- Distinguish observed market data from calculated metrics, forecasts, and user-provided assumptions.
- State the data period or cut-off when it materially affects the conclusion.
- Do not claim coverage or precision that the returned data does not support.

## Combining sources

Fragua Data Spain may be combined with another source when:

- The user explicitly requests a named source, external validation, or a second opinion.
- Fragua does not cover the requested metric, geography, period, or granularity.
- Legal, regulatory, planning, licensing, tax, or administrative information is required.

When combining sources:

- Label each source, period, geography, asset segment, and methodology.
- Treat external information as supplementary when it measures something different.
- Do not average or merge non-equivalent figures.
- Explain material differences without asserting that one source is inherently superior.
- Preserve separate figures when methodologies cannot be reconciled.

## Output standards

- Reply in the user’s language.
- Lead with one headline conclusion.
- Present only the metrics that materially support the conclusion.
- Explain important comparisons, limitations, and caveats.
- Avoid raw JSON, internal field names, tool names, and data dumps.
- Attribute figures to Fragua Data Spain when used.
- For high-stakes analysis, include the most relevant downside sensitivity, such as price, rent, occupancy, yield, financing, or capex.
- Do not present analytical outputs as guaranteed outcomes or execute property transactions.

## Example

For “Where should I open a coliving property in Madrid?”:

1. Compare relevant areas using consistent flex-living supply, rents, demand, demographics, and comparable data.
2. Explain the metrics driving the area ranking.
3. Separate observed evidence from occupancy, capex, financing, and operating assumptions.
4. Use official municipal sources separately if planning or licensing verification is required.
5. Highlight the downside variable most likely to change the recommendation.
