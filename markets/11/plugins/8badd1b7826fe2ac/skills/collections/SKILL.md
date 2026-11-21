---
name: collections
description: Plan collections on overdue invoices in Hubity. Use when someone asks who owes money, which invoices are overdue or longest unpaid, accounts receivable aging, or who to chase this week. Reads only; never contacts a client.
---

# Collections

Turns the overdue invoices in Hubity into a follow-up plan for the week.

## Steps

1. Call `list_invoices` with `status` `overdue` and `limit` 50. Its `total` is the full count; when it is more than the rows returned, say the plan covers the 50 invoices shown and that the sum is a subtotal for those 50, not the full amount overdue.
2. Sort the invoices oldest first, then by the largest balance. Group them by age: over 90 days, 61 to 90, 31 to 60, and 1 to 30.
3. Answer with:
   - The follow-up order, one client at a time, so a client with several late invoices gets one conversation.
   - A suggested action for each: a friendly reminder under 30 days, a call from the project lead at 31 to 60, and a firm notice or a hold on new work beyond that.
   - The total overdue, per currency, labeled a subtotal of the invoices shown when `total` is more than the rows returned.
4. For "the longest-open unpaid invoice", give the one with the most days overdue, with its client and amount due.

## Rules

- Never say a reminder was sent. Hubity does not contact clients from here. Offer to draft the wording of a reminder for the person to send.
- If no invoice is overdue, say so.
- Never invent amounts or dates.
