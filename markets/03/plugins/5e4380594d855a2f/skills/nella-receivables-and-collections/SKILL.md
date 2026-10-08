---
name: nella-receivables-and-collections
description: Show who owes the business money, how overdue it is, which balances are largest and oldest, and when each customer is likely to pay based on how they have paid before. Use when the user asks who owes them, what is overdue, how bad their debtors are, who to chase, when someone is likely to pay, or about a specific customer's outstanding balance. Do not use for cash forecasting, runway or affordability; for what the business owes suppliers; for performance; for whether the books are reliable or ready to close, which is month end; for tax returns or filing deadlines, which is compliance even when the user says "overdue"; or for a broad "what needs my attention" request, which goes to the finance director briefing. "Overdue" and "outstanding" here always mean money a CUSTOMER owes, never a filing and never an unreconciled item.
---

# Receivables and collections review

The user wants to know who owes them money, how overdue it is, and when it is
likely to arrive.

## Gather

Start with `get_ar_ap_ledger` — the open sales ledger, as at today. It is the
primary source and does not depend on any other tool.

| Tool | Add it when |
|---|---|
| `get_ar_chase_drafts` | Candidates ranked by overdue amount, with a tone from payment history and, on some plans, prepared draft wording |
| `list_invoices_and_bills` | The specific unpaid invoices are wanted |
| `get_invoice_or_bill_link` | The user wants to open or download a document |
| `get_top_customers_and_suppliers` | Concentration matters — one customer owing most of it |
| `get_cash_forecast` | The user asks what the collections mean for cash |
| `search_transactions` | Checking whether something was actually paid |

**If `get_ar_chase_drafts` returns `has_data: false` or is otherwise
unavailable, do not stop.** Continue from `get_ar_ap_ledger` and
`list_invoices_and_bills`: rank the outstanding balances by overdue amount and
by age of the oldest open item, and say that chase candidates were not available
so the ranking is by amount and age alone, without payment-history context.

## What is due, versus when it will arrive

`receivables.forward` gives what is DUE in the next 7 and 30 days, by due
date, over every open invoice — plus `overdue`, `undated` and the largest
items. That is timing on paper. When it will actually ARRIVE is behaviour, and
that is the section below. Keep the two apart: a customer with £10k due next
week and a 60-day payment history is not £10k next week.

## Answering "when are they likely to pay"

`get_ar_ap_ledger` returns `avg_days_to_pay` per counterparty where there is
enough settled history, plus a `trend`.

**`avg_days_to_pay` is measured from the INVOICE DATE, not the due date.** It is
the mean of (date paid − date issued) over settled invoices. Adding it to a due
date double-counts the payment terms and pushes every expectation out by roughly
the length of those terms. Apply it to the invoice date.

Where `avg_days_to_pay` is null there is too little settled history to judge —
say the customer's payment behaviour is unknown rather than assuming they pay on
time. The due date is then the only basis, and it is a weaker one.

Say plainly that this is behaviour, not a commitment. A customer who has paid in
45 days four times may still pay in 90.

## Structure the answer

1. **The conclusion** — total outstanding, how much is overdue, and how serious
   that is, in a line or two
2. **Ageing** — how old the overdue portion is
3. **Who to look at first** — ranked by overdue amount and age, with how each
   customer usually pays and when payment is likely, where that is known
4. **Concentration** — where one customer dominates the balance
5. **What could not be assessed** — undated invoices, customers with no payment
   history, anything skipped
6. **Safe checks**, and what belongs with the user's accountant

## Rules you must follow

**These are amounts OUTSTANDING NOW, not sales for a period.** Do not present
receivables as revenue or compare them to a P&L figure. For who the biggest
customers were by invoiced value, that is `get_top_customers_and_suppliers` —
the two answer different questions and will not match.

**`assessable: false` means the platform could not read that side.** It is never
a statement that nothing is outstanding.

**`has_data: false` means NOT ASSESSED.** Unread receivables are not "nobody
owes you money". Say which it is.

**The chase list is a subset, and nothing in it says by how much.**
`get_ar_chase_drafts` returns `counts` by draft status — draft, approved, sent,
cancelled — not a tally of who was left out. Customers below the chase threshold
or too recently due simply do not appear, and no field reports them.

So check it yourself: compare the number of debtors in `drafts` against
`open_count` and the overdue total on the ledger's receivables side. Where the
chase list is shorter, say it covers part of what is outstanding and give the
ledger total alongside it. Never present the chase list as everyone who owes.

**Overdue is derived, not read.** No accounting platform has an "overdue" status
of its own. A document with no due date CANNOT be judged either way — it is
neither overdue nor current, and the count of those is given. Report it.

**`coverage_note` is on `list_invoices_and_bills`, not on the ledger.** Read it
whenever you quote a count from a document listing: some platforms cannot filter
at source, so a short result means "none on this page", NOT "none in the
ledger". The ledger itself reports `open_count` for the whole side — use that
for totals, and never present a page of documents as the full picture.

**Tone is a suggestion derived from payment history** — how that customer
usually pays. It is not a judgement about them, and the rationale is given.
Relay the rationale rather than asserting someone is a bad payer.

## Boundary

Nella provides a read-only assessment from connected records. It has not
posted, filed, approved, paid or sent anything. Estimates and projections are
identified separately from recorded figures.

**Drafts may be returned, but NOTHING IS SENT.** `get_ar_chase_drafts` returns
who is overdue, by how much, for how long, and a suggested tone. Depending on
the plan it may also return prepared reminder drafts. Where wording is returned,
present it as a draft for the user to review. Where it is not, give the
candidates and their tone without inventing wording.

Either way no reminder is dispatched and Nella cannot send one. Approval and
sending happen in the Nella portal. A status of "sent" describes what was done
there, never something this connector did. Never imply a chase has gone out
because a draft exists.

`get_invoice_or_bill_link` returns a time-limited link to **open or download** a
document. It does not email, share or send it to anyone.

Whether to chase, when, and how firmly is the user's decision. Do not write a
reminder for them unless they ask, and if they do, be clear it is theirs to
review and send.

Anything about writing off a debt, provisioning for it, or the VAT treatment of
bad debt goes to a qualified accountant.

**Say "your accountant", and name no firm.** Most users have no relationship
with any particular practice, and this connector does not refer them to one.
Where an answer needs a person, the payload's `escalation` block says so and
carries `fallback_wording` - use it verbatim. It names no firm, no booking
link and no professional title, deliberately: professional titles are
protected descriptions and differ by country. The envelope's `advice_note`
says the same thing. Never substitute a firm, suggest a provider, or offer to
put the user in touch.

## When to stop or ask

- If the sales ledger cannot be read, say so and stop. Do not infer debtors from
  invoices listed elsewhere.
- If the user asks about one customer, use their name to filter rather than
  reporting the whole ledger.
- If nothing is overdue, say so plainly — but only when the ledger was readable.
