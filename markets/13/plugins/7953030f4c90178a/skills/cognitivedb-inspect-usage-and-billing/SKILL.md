---
name: cognitivedb-inspect-usage-and-billing
description: >-
  Read CognitiveDB Space credit usage, Compute metering, Organization costs,
  balances, and historical payment records. Use for authorized usage or accounting
  questions, date ranges, pagination, and evidence-backed summaries.
metadata:
  version: "dev-1.5.3-chatgpt.1"
---

# Inspect Usage and Billing

Keep this Skill read-only. Never infer missing amounts, dates, permissions,
pages, units, or unavailable billing data.

## Boundaries

- Read current-Space daily credits and Compute metering, plus Organization
  balances, limits, costs, existing order summaries, payment history, and refunds
  for accounting purposes.
- For purchases, credit top-ups, subscriptions, upgrades, or payment-method setup,
  explain that this plugin does not support the transaction. Do not initiate or
  resume checkout, or retrieve or present payment links or payment QR codes.
- Never substitute SQL, browser, direct APIs, or access mutations. Treat
  permission denial as denial, not zero usage.

## Core Instructions

- Bind the selected Space for usage and Organization billing. The server resolves
  its Organization; do not request a separate tenant identity or switch Spaces
  to repair denied Organization access.
- Use `cognitivedb_organization_billing_overview_get` for balances, trial grants,
  the current UTC month summary, and daily limits. Select the dedicated cost,
  payment-history, order-list, or refund read for other accounting questions,
  requesting only the needed information. Payment configuration and checkout
  details are outside this Skill's scope.
- Resolve a period for Space usage. For Organization reads, apply a requested
  period only where supported and use the live date or month defaults otherwise.
  Ask once about material period ambiguity; current balances and limits do not
  require dates. State when requested historical data is unavailable rather than
  substituting current data for that period.
- Use bounded pages and continue only as needed for the requested coverage.
  A permission denial or tool failure is not zero usage.
- For Space usage, report the period, Space, returned units, totals, grouping,
  pagination coverage, and freshness fields when available.
- For Organization billing, distinguish balances, limits, usage, and funding.
  Keep monetary amounts, currencies, raw usage quantities, and credits distinct;
  preserve returned monetary precision. Report only returned fields. A failed
  aggregate read is unavailable, not a partial successful balance.

## Allowed MCP Tools

- `cognitivedb_organization_billing_overview_get`
- `cognitivedb_organization_daily_usage_get`
- `cognitivedb_organization_monthly_spend_get`
- `cognitivedb_organization_payment_history_list`
- `cognitivedb_organization_payment_orders_list`
- `cognitivedb_organization_payment_refunds_list`
- `cognitivedb_organization_workspace_spend_get`
- `cognitivedb_space_current_get`
- `cognitivedb_space_usage_get`
