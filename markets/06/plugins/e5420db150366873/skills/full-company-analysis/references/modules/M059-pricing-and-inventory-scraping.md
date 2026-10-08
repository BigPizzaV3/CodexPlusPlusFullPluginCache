<!-- Generated loss-aware reference mirror from God_Level_Public_Company_Financial_Analyst_Job_Guide_V6_99_ALL_SUB70_FIXED.docx. Canonical source remains the bundled DOCX. -->

<!-- Module: 059 | Title: Pricing and Inventory Scraping -->

## PART XII - ALTERNATIVE DATA AND CHANNEL WORK | MODULE 059

# Pricing and Inventory Scraping

> Mission. Track availability, discounting, lead times, SKU breadth, and channel inventory without overfitting.

## Decision output

Objective: Track availability, discounting, lead times, SKU breadth, and channel inventory without overfitting. The completed work product must be reproducible from evidence, show the downstream financial or decision effect when material, state the strongest contrary case, and define a dated update rule.

## Explicit operating procedure

1. Define permitted data sources, terms/robots/compliance constraints, SKU/location universe, frequency, timestamp, and raw-page retention before scraping.

1. Create stable product identifiers and handle variants, bundles, coupons, loyalty pricing, shipping, taxes, geography, and out-of-stock states consistently.

1. Distinguish list price, transacted/advertised price, discount depth, promotion frequency, availability, lead time, and inventory proxy; do not collapse them into one price series.

1. Monitor site layout/API changes and build validation checks for missing pages, duplicated SKUs, unit changes, bot blocking, and false stockouts.

1. Aggregate by economically meaningful category and weight, then compare with company-reported pricing, volume, mix, inventory, and channel evidence.

1. Backtest the scraped signal before using it to forecast revenue or margin and preserve the raw observations for audit.

## Required evidence and model bridge

- Primary-source set: documented datasets, sampling frame, legal/compliance approval, backtests, source provenance. Preserve exact document/version, date, period, and source location for every material factual input used in pricing and inventory scraping.

- For each key concept - permission, SKU identifiers, timestamps, seller/channel, matched baskets, stock status - state whether it is a reported fact, analyst calculation, management claim, external estimate, or judgment. Quantitative concepts must retain raw components and units; qualitative concepts must retain the specific evidence and counterevidence.

- Map only economically relevant findings into the model or decision record. Process-control modules such as pricing and inventory scraping may have no direct valuation line; in that case document the downstream error or governance risk the control prevents.

## Metrics and calculation controls

| Metric / concept | Construction | Required validation |
| --- | --- | --- |
| in-stock rate | Observed SKU-location checks showing available inventory divided by valid SKU-location observations. | in-stock rate: Recalculate from same-scope numerator and denominator; confirm period, units, cohort/geography, and issuer definition; reconcile material differences to filings or operating data. |
| matched-SKU price index | Current price of the same SKU/location basket divided by base-period price of that identical basket, weighted by a fixed basket or documented economic weights. | matched-SKU price index: Recalculate price/cost from underlying dollars and physical units; test mix, rebates, FX, timing, and unit-definition effects; reconcile to reported revenue or expense. |
| promotion intensity | Discounted/promoted observations or promotion dollars divided by total observations or gross sales, with depth and duration separately tracked. | promotion intensity: Recalculate from same-scope numerator and denominator; confirm period, units, cohort/geography, and issuer definition; reconcile material differences to filings or operating data. |



## Worked application

> Case: average price rises because low-priced SKUs go out of stock.

- Reconstruct the relevant reported fact from primary evidence before interpreting the case. For pricing and inventory scraping, show the raw components rather than only the resulting ratio or narrative.

- Build the causal chain through permission, SKU identifiers, timestamps, seller/channel, then identify which link is directly observed and which link remains an assumption.

- Calculate in-stock rate, matched-SKU price index, promotion intensity from sourced components under the reported/base interpretation and at least one skeptical alternative interpretation.

- Translate the difference between cases into the variable that matters for pricing and inventory scraping: evidence quality, revenue, operating profit/NOPAT, free cash flow, invested capital, financing/dilution, risk, or valuation. Mark non-applicable links instead of inventing them.

- Expert consistency test: separate price from mix and monitor scraping failure as a data-quality event.

- Precommit the specific future filing, KPI, customer/supplier observation, regulator action, or market input that would materially invalidate the pricing and inventory scraping conclusion.

## Failure tests

- FAIL if permission cannot be defined and reproduced from the source pack.

- FAIL if scraped price or availability is interpreted without SKU matching, channel coverage, promotions, product mix, data-quality controls, and a baseline.

- FAIL if the pricing and inventory scraping conclusion depends on an unstated assumption, unreconciled definition, or evidence that cannot be traced to its source/version.

- FAIL if evidence materially inconsistent with the pricing and inventory scraping conclusion is omitted, reclassified, or dismissed without a documented definition, materiality, causal, timing, and source-quality analysis.

## Completion test

A senior reviewer must be able to reproduce the pricing and inventory scraping conclusion, vary the most sensitive assumption independently, trace the change through the model, understand the strongest opposing case, and identify the next evidence that would force an update. If any link is missing, the module remains open.
