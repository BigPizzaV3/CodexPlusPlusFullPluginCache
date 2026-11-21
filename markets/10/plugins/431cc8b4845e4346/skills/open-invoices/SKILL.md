---
name: open-invoices
description: Find outstanding Apex rental balances and summarize payment status.
---

# Open invoice review

Use this skill to help an authorized rental operator review outstanding balances.

## Workflow

1. Confirm an authorized Apex Rental Pro connection.
2. If the user gives a period, ask for both inclusive start and end dates in `YYYY-MM-DD` format.
3. Call `list_open_invoices` with no dates for all returned open balances, or with both dates for a date-constrained result.
4. Report booking ID, event date, customer name only when needed, total, paid amount, balance, and payment status.
5. State that the result is a read-only snapshot and advise the operator to use Apex Rental Pro for payment actions.

## Example prompts

- “Which bookings still have an unpaid balance?”
- “Show open balances for events from 2026-06-01 to 2026-06-30.”

## Guardrails

- Never process, request, or expose payment-card data or payment credentials.
- Never mark an invoice paid, send a collection message, or change a booking.
- Do not infer why a balance is open or promise a due date unless the tool returns it.
- Minimize customer information in summaries. Use booking ID and event date when names are not needed.
- If dates are incomplete or reversed, ask the user to correct them before calling the tool.
