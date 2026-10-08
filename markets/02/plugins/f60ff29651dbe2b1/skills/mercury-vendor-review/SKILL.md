---
name: mercury-vendor-review
description: Review business vendors or personal merchants and payees for payment concentration, possible duplicates, unusual changes, and recipient identity exceptions. Use for who-was-paid questions. Do not infer unpaid bills or personal relationships.
---

# Mercury Vendor Review

## Personal payees and merchants

This workflow also supports personal merchant and payee reviews. Use "merchant" or "payee" for personal activity, including rent and household payments. Do not treat personal recipients as business vendors or interpret concentration as business supply risk.

For personal use, read `../mercury-personal-finance/SKILL.md` and use its thresholds instead of business currency floors. Keep observed payments separate from future bills; past rent payments do not prove an upcoming amount or due date. Never infer relationships between people from names or transfers. Recipient identity checks remain limited to explicit evidence.


Build a read-only vendor-payment review. Do not present transactions as a complete accounts-payable ledger.

Read `../mercury-mcp-shared/SKILL.md` before retrieval. In `references/review-rules.md`, read only the rules for the requested checks and materiality.

## Set the period

Use the user-provided period. If the user does not provide one, use the last six complete calendar months. Use all active accounts unless the user selects accounts.

Retrieve the immediately preceding equal-length period only when the user asks for change, increase, or new vendors. Do not retrieve a comparison period for a review limited to counterparties, concentration, possible duplicates, payment outliers, or recipient identity.

If the live transaction call limit prevents a complete result, do not calculate from partial data. Ask for a narrower period.

## Retrieve complete data

Inspect the live schemas. Use account tools to resolve scope. Use the transaction-list tool for the review period and any required comparison period.

Use recipient-list data only when the user requests recipient review or a material transaction needs an identity check. Recipient results can contain full bank and routing numbers. Remove these fields immediately. Do not place them in an artifact or answer. Use a single-recipient detail tool only when required for one high-priority item.

The live MCP can expose customer invoices. Customer invoices are accounts-receivable records. Do not use them as vendor bills or accounts-payable aging.

## Prepare and verify the data

Create minimized transaction and recipient tables. Exclude failed, cancelled, reversed, and blocked activity. Exclude only confirmed internal transfers.

Report the page count, transaction count, recipient count when used, account count, exact filters, returned dates, status counts, missing rates, exclusions, and unmatched recipient links.

Do not join a recipient to a transaction from name similarity alone. Use an explicit identifier when available. Keep low-confidence name matches in a review queue.

## Calculate with code

Use exact programmatic arithmetic. Calculate only the fields required for the requested analyses. Use the equal-length comparison period only for change, increase, or new-vendor results.

Keep original counterparty names and abbreviated transaction IDs.

## Build and order the review queue

Apply only the parts of `references/review-rules.md` needed for the request. For a general vendor review, include material concentration, possible duplicates, and payment outliers. Identify material vendor increases and new material counterparties only when a comparison period is in scope. Use recipient data only when recipient identity is in scope.

Order the queue by possible duplicate exposure, outlier or increase, new counterparty, identity exception, and concentration review. For each item, state the rule, confidence, evidence IDs, amount, and next human check.

Use `possible duplicate`, not fraud. Treat concentration as a review signal, not a risk conclusion.

## Deliver the report

Lead with the highest-value review items. Include only the scope, data quality, concentration, period changes, review queue, recipient exceptions, human checks, and limits needed to support the answer.

Never expose recipient banking details.

## Requests to make changes

This review workflow remains read-only. When the user explicitly requests a supported payment, transfer, category, or transaction metadata change, route that part to `../mercury-actions/SKILL.md`. Keep any requested analysis separate from the authorized change.
