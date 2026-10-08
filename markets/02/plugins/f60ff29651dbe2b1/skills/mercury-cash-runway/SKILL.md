---
name: mercury-cash-runway
description: Review business or personal Mercury cash balances and cash flow. Analyze business burn and runway, or personal cash buffers and expense coverage using the personal-finance definitions. Use for cash questions, not detailed spend or duplicate reviews.
---

# Mercury Cash and Runway

## Personal and household use

For personal cash flow, emergency funds, savings goals, or "how long will my money last," read `../mercury-personal-finance/SKILL.md` and use its personal definitions. Keep business operating runway distinct from expense coverage without income and cash depletion with income. Do not label household spending operating burn. A current balance question still needs no transaction history.

Use only accounts in the selected personal, household, or business scope. Treasury is included only when requested or part of requested total liquidity and actually accessible. Missing products are a coverage limit, not zero balances.


Build a read-only cash and runway report. Separate observed data from classifications and scenarios.

Read `../mercury-mcp-shared/SKILL.md` before retrieval. In `references/metric-definitions.md`, read liquidity for balance questions and only the other definitions required for the requested calculations.

## Set the period

Use the current date supplied by the host as the as-of date. Match the period to the request:

- For current deposit balance or liquidity, retrieve current balances. Do not retrieve transactions.
- For burn or runway, use the user-provided period. If the user does not provide one, use the trailing three complete calendar months.
- For cash history or a monthly cash report, use the user-provided period. If the user does not provide one, use the last six complete calendar months.
- Retrieve an additional comparison period only when the user requests a comparison.

If the live transaction call limit prevents a complete result, do not calculate from partial data. Ask for a narrower period.

## Retrieve complete data

Inspect the live schemas. Use account tools for current deposit balances. Use Treasury tools only when Treasury is in scope. Treasury is in scope when the user asks for Treasury, total Mercury liquidity, or cash across Mercury. Use the transaction-list tool only when the requested result needs transaction history.

Use Treasury transaction data when it is needed to confirm a deposit-to-Treasury transfer or explain a Treasury balance change. Use credit tools only for a separate credit-capacity section that the user requests. Credit is not liquidity.

Use statements only when the user requests a month-end tie-out or transaction data cannot support it.

## Reconcile the source

Create minimized account and transaction tables. Remove account and routing numbers before calculation.

Exclude failed, cancelled, reversed, and blocked activity. Exclude confirmed internal transfers from both inflow and outflow. Keep possible internal transfers in the primary cash-flow result and show a sensitivity result when material.

Do not add a Treasury balance to deposit balances until the live result shows that it is separate and available. Do not infer restricted cash status. State when the MCP does not return this status.

Report the account count and balance scope. When transactions are used, also report the page count, transaction count, exact filters, returned dates, statuses, missing rates, and exclusion reconciliation.

## Calculate actuals with code

Use exact programmatic arithmetic. Apply `references/metric-definitions.md`.

Calculate only the measures required for the request. For each required complete month, calculate external inflow, external outflow, net cash flow, and unadjusted burn. Calculate adjusted operating burn only when the request needs it and evidence supports each classification. Do not remove a flow only because it is large or unusual.

For the as-of date, show available deposit balance, current deposit balance when different, separately verified Treasury balance, identified unavailable cash, and total available liquidity. Keep currencies separate.

## Calculate runway

Use the runway method that the user requests. If the user does not select a method, use the trailing three-month average. Add a most-recent-month or six-month method only when the user asks for a comparison or sensitivity result.

If burn is zero, state `cash-flow positive in the selected period`. Do not report infinite runway. If fewer than three complete months exist, label runway low confidence.

## Explain drivers and scenarios

Explain drivers only when the user requests them or when a material flow affects the selected burn result. Use the smallest supporting set of counterparties, shares, changes, and evidenced one-time flows. Cite abbreviated transaction IDs.

Add a scenario only when the user requests one. Use only user-supplied changes. State the amount, direction, start month, revised burn, revised runway, and difference from the base case. A scenario is not a forecast.

## Deliver the report

Lead with the requested balance, liquidity, burn, or runway result. Include only the scope, data quality, components, monthly cash flow, method, driver evidence, scenarios, actions, and limits needed to support the answer.

## Requests to make changes

This review workflow remains read-only. When the user explicitly requests a supported payment, transfer, category, or transaction metadata change, route that part to `../mercury-actions/SKILL.md`. Keep any requested analysis separate from the authorized change.
