---
name: mercury-spend-review
description: Review business expenses or personal and household spending, budgets, recurring charges, possible duplicates, unusual changes, and savings candidates. Use for spending and subscription reviews. Use personal-finance definitions for household budgets.
---

# Mercury Spend Review

## Business and personal spending

Use this workflow for company expenses or personal and household spending. For personal budgets, subscriptions, or savings questions, also read `../mercury-personal-finance/SKILL.md`. Use the selected account scope and the user's categories or budget. Do not infer a budget, household size, or whether a purchase was necessary.

Separate observed bank cash outflow from purchase spending. When both card purchases and card repayment are visible, reconcile the repayment and count each purchase once. When only repayment is visible, show it as a card payment with unavailable purchase detail. Reimbursements and refunds need source evidence; show them separately before any netting. A transfer to savings is not consumption when ownership is confirmed.

For personal use, apply the personal review thresholds in `../mercury-personal-finance/SKILL.md` instead of business currency floors in the reference. Recurring-charge and duplicate-only requests must not omit small charges. Describe subscriptions as candidates unless source evidence or the user confirms them; do not claim that a recurring charge is unwanted or cancel it.


Build a read-only spend report that a finance owner can verify and act on.

Read `../mercury-mcp-shared/SKILL.md` before retrieval. In `references/review-rules.md`, read only the rules for the requested checks and materiality.

## Set the period

Use the user-provided period. If the user does not provide one, use the last three complete calendar months. Use the current date supplied by the host.

Retrieve the immediately preceding equal-length period only when the user asks for a comparison, trend, increase, or new vendor. Do not retrieve a comparison period for a review limited to recurring charges, duplicate candidates, concentration, categories, or transactions in the review period.

Use all active accounts unless the user selects accounts. Keep currencies separate. If the MCP does not return an account currency code, use the label required by the shared skill.

## Retrieve complete data

Inspect the live schemas. Use the live account-list tool to resolve the account population. Use the live transaction-list tool for the review period and any required comparison period.

Use posted-date filters and the settled or sent status when the live schema supports them. Follow the live transaction pagination, truncation, and call-limit rules. Do not request field selection when the schema does not support it.

Use category tools only when category data is required and absent, or when the user asks for category definitions. Use a transaction-detail tool only for a material item that lacks required evidence.

## Prepare and verify the data

Create a minimized transaction table. Remove sensitive account fields before calculation. Exclude failed, cancelled, reversed, and blocked activity. Exclude only confirmed internal transfers. Keep possible internal transfers in the primary totals and show a sensitivity result when they are material.

Report the page count, transaction count, account count, exact filters, returned date range, status counts, missing rates, and exclusion reconciliation.

## Calculate with code

Use exact programmatic arithmetic. Calculate only the measures required for the request. Available measures include:

- external outflow as a positive value;
- monthly outflow and month-over-month change;
- category and normalized-counterparty totals;
- transaction count, median, and largest transaction;
- top 5 and top 10 counterparty shares.

Keep the returned transaction sign in the evidence table. Show the denominator for each share and change.

## Build the review queue

Apply only the parts of `references/review-rules.md` needed for the request. For a general spend review, include material recurring patterns, possible duplicates, and outliers. Detect vendor increases and new material counterparties only when a comparison period is in scope.

Cite abbreviated transaction IDs. State the rule and confidence for each item. A recurring charge is not proof of an unwanted subscription.

## Estimate the opportunity

Estimate opportunity only when the user asks for savings or when a material review candidate has bounded exposure. Show identified exposure before estimated savings. Do not count one transaction in more than one exposure amount.

Annualized recurring cost is exposure, not recoverable savings. Use a savings estimate only when the user gives a reduction assumption or the evidence supports a bounded possible-duplicate amount. State each assumption.

## Deliver the report

Lead with up to five material findings. Include only the scope, data quality, spend summary, review queue, opportunity, human checks, and limits needed to support the answer.

Do not modify transactions or categories.

## Requests to make changes

This review workflow remains read-only. When the user explicitly requests a supported payment, transfer, category, or transaction metadata change, route that part to `../mercury-actions/SKILL.md`. Keep any requested analysis separate from the authorized change.
