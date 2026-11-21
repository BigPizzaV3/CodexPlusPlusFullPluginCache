---
name: month-end-wip
description: Month-end work in progress (WIP) from Hubity. Use when someone asks for WIP, unbilled time, what is ready to bill, or a month-end close review. Reads only; never drafts or changes anything.
---

# Month-end WIP

Shows what a month has earned but not yet invoiced, and what stands between it and an invoice.

## Input

- The month, as `YYYY-MM`. If the person names no month, use last month and say so.

## Steps

1. Call `preview_month_billing` with `month`. While it returns `nextCursor`, call it again with the same `month` and `cursor` set to it, until every page is read.
2. Call `list_invoices` with `status` `draft` and `limit` 50 to find drafts already waiting for review. Its `total` is the full count; when it is more than the rows returned, say the list shows the first 50.
3. Answer in four parts:
   - Ready to bill: approved, not yet invoiced, per client and project, with the total.
   - Time not yet approved: which client and project, how many hours, and roughly how much it would bill.
   - Other decisions: missing rates, contract caps, a month that has not ended.
   - Drafts awaiting review: number, client and amount.
4. End with the next three actions, the most money first.

## Rules

- Read only. Do not call `create_month_invoice_drafts` unless the person asks to bill; then follow the bill-the-month workflow.
- If `list_invoices` is refused for the person's role, say drafts cannot be shown and continue with the rest.
- Never invent figures.
