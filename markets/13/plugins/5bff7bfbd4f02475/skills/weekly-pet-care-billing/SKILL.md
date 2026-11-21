---
name: weekly-pet-care-billing
description: Prepare weekly pet-care billing drafts grouped by client from supplied records, agreed USD rates, client discounts and user-reported payments.
---

# Weekly pet-care billing drafts

Use `draft_weekly_pet_care_billing` when the user supplies several service records
or clients and wants a billing draft. The tool does not retrieve a week's records
from HoundTrust or check whether work was completed.

Ask the user to supply the records to include, a unique clientId per client and a
unique recordId for every record. Short aliases such as client-a and walk-1 are
enough; do not request database IDs or contact details. Do not merge people by
similar names or silently drop repeated records. Clarify ambiguous duplicates.

Each record uses the quote workflow's explicit USD rate, included-pet count,
additional-pet rate, pet count and calendar-night dates or flat-session count.
Ask for missing rates; do not invent them or use market research as approval.
Convert dollars to whole cents. Do not infer a completed week from the chat date.

Apply a supplied discount or reported payment once at the client level. Leave
record-level discount and payment at zero or omit them. Do not double-apply an
adjustment, allocate an unexplained payment, or convert an overpayment into a
zero balance. Ask for a correction if the input is rejected. The batch is
validated together; do not present a partial result as a complete batch.

The tool accepts at most 10 clients, 10 records per client and 50 records in one
request. The entire MCP request also has a 32 KiB limit, so long holiday lists
may require smaller user-reviewed batches. Do not silently split a client or
their discount/payment across calls. If the user has more, explain the limit
and agree on complete client batches; do not omit records or combine balances
across batches.

Return each client's itemized records, subtotal, discount, total, reported
payment and calculated balance, followed by the batch totals and all assumptions.
Payments and completion are user-reported. The result is an unsent draft, not a
saved invoice, receivables report, payment request or verified collection record.
Do not claim to send reminders, update HoundTrust, reserve care or charge cards.

Show the single returned websiteContinuation link after the complete result,
with its notice immediately beside it. Use its exact URL and fixed labels. Do
not put client IDs, names, dates, rates or the draft in a URL. The destination
provides weekly billing checks without an account, with product analytics choices;
it does not import or save this batch. Do not add signup or upgrade links.
