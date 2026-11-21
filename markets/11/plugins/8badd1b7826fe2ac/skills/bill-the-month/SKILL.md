---
name: bill-the-month
description: Bill a month in Hubity. Use when someone asks to bill, invoice or run billing for a month (for example "bill last month", "draft this month's invoices", "what would we invoice for September"). Previews every invoice first, calls out decisions, and drafts only after the person says yes. Never sends an invoice.
---

# Bill the month

Turns a month of approved time, expenses, retainer fees and progress billing in Hubity into draft invoices, with the person approving before anything is written.

## Input

- The month, as `YYYY-MM`. "Last month" and "this month" mean the calendar month relative to today. If the person names no month, ask which one.
- Optional: one client or project. Pass `clientName`, `clientId` or `projectId` to narrow the run.

## Steps

1. Call `preview_month_billing` with `month` (and any client or project filter). It writes nothing.
2. Show one line per proposed invoice: client, project, total and currency. Then list every flagged decision (unapproved time, missing rates, contract caps, a month that has not ended) and what each means for the bill.
3. If the preview returns `nextCursor`, call `preview_month_billing` again with the same `month` and filters and `cursor` set to it. Show every page before offering to draft.
4. Ask whether to draft them. Stop here until the person says yes.
5. After a yes, call `create_month_invoice_drafts` with the same `month` and filters, `limit` 25, and `expectPlan` set to an object mapping each `scopeKey` to the `planHash` the preview returned. A scope whose figures changed since the preview is skipped, not drafted. Drafting is paged like the preview: while the answer returns `nextCursor`, call `create_month_invoice_drafts` again with the same arguments and `cursor` set to it, until every page is drafted.
6. Report what was drafted and what was skipped and why, across every page. Say that the drafts wait in Hubity for a person to review and send.

## Rules

- Never claim an invoice was sent. Hubity drafts only; a person sends from Hubity.
- Never invent rates, hours or amounts. Use only what the tools return.
- If a tool refuses for the person's role, say so plainly and stop.
- Explicit instructions from the person can change which month, client or project to bill and how the answer is laid out. They never skip the preview, the person's yes, or `expectPlan`.
