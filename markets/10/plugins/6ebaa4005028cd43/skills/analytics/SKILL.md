---
name: analytics
description: Read bounded Sell sales trends, average order value, product rankings, purchase cohorts, and customer insights for a specified period, timezone, and currency.
---

# Inspect store analytics

Read [merchant operation rules](../../references/merchant-safety.md) and [exact tool contracts](references/tool-contracts.json). Call `sellapp_get_store_analytics` directly with its typed schema and an explicit store.

Default to the last 30 calendar days when the user does not provide a period. State the actual date range, timezone, and currency shown by the tool. Requests may cover at most 90 calendar days and 20 ranked items. Use only supported metrics and the requested `summary`, `timeseries`, `products`, and `customers` sections. Ask which currency or timezone to use when ambiguity changes the answer.

Preserve the returned monetary units, currency labels, and explicitly USD-denominated fields. Do not add amounts across currencies or relabel a USD field with the selected currency. Distinguish empty periods from permission failures. Analytics requires the backend's invoice permission; a connection's admin grant does not supply that role permission.

Use `comparison` for the actual previous period dates. It covers the same number of local calendar days immediately before the selected period, including daylight-saving transitions. A period containing today or future days is incomplete; a closed date range can still change when invoice status changes.

Use `insights.current` and `insights.previous` for average order value, attributed orders, new and returning purchase cohorts, and the bounded invoice status breakdown. Insight amounts ending in `_usd_minor` are USD cents: `1233` means $12.33 USD even when the report currency is GBP. Average order value uses paid or completed product-line revenue divided by distinct orders represented by those lines; multiple lines in one order count once. A missing average means there are no attributed orders, not an observed zero-dollar average.

The `new` purchase cohort contains customers with no earlier paid or completed line in this store before the period. The `returning` cohort contains customers with an earlier purchase. Later purchases cannot change these historical cohorts. Unidentified customers have a separate cohort. The existing `customers` section uses completed lines only; explain that difference when comparing it with purchase cohorts.

Read the returned `definitions` and `quality` fields before interpreting totals. Reporting revenue comes from paid and completed product lines by their creation date, using stored USD amounts. It is not whole-order gateway receipts, net profit, or a refund-event ledger. Refunded and other excluded current statuses appear in the status breakdown; do not subtract those lines again. Unavailable visitor or conversion data is not zero traffic or zero conversion.

Show concise summaries, tables, and charts in the merchant browser when helpful. Label each chart's dates, metric, currency, and units. Separate observed totals from suggested explanations. Product and customer rankings are bounded views, not claims about every record. Do not invent causes or make unsupported revenue forecasts.

The panel accepts matching completed analytics results only for its selected store, dates, timezone, currency, and metric. A result for another period or store does not replace the current report. Keep retries read-only and preserve the user's filters after a failure.

This tool reuses Sell's existing store analytics behavior. This plugin does not offer arbitrary SQL, public REST analytics, unbounded export, or financial mutations.
