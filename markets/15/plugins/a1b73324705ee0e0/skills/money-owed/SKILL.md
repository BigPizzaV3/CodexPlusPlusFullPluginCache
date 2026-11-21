---
name: money-owed
description: A digest of what's still owed on events in Excellent — deposits and installments coming due or overdue, partly paid and unpaid invoices, by venue and event date, one invoice in full — and draft, correct or schedule a draft invoice for a person to send. Use for "which deposits are outstanding", "unpaid invoices", "who owes us money", "payments due this week", "draft the invoice for the Adler wedding", "invoice the Patel dinner", "bill the Friday buyout", "fix the tax on that draft invoice", "split it into a deposit and a balance".
---

# Money owed digest

This skill reads, and can draft, revise and schedule an invoice that is still a draft. It never charges,
records a payment, sends an invoice or contacts a guest.

## 1. Collect

1. `agenda` with `days: 14` (or the window the person names) — `payments_due` lists every installment still
   owed that falls due before the window ends, overdue ones included, with `left_minor`. If
   `payments_due_truncated` is true, say there are more than shown.
2. `list_invoices` with `status: "partial"`, then `status: "sent"` — paging with `next_offset` until null.
   Each row carries the total, deposit due, amount paid and linked event.
3. For an invoice the person asks about, `get_invoice` with its id from `list_invoices` reads it in full:
   every line, the totals, the deposit due and amount paid, its event (id and title) and its payment schedule.
   `get_event` on that event shows every payment; for an installment in `payments_due`, take the `event_id`
   from there.

## 2. Write the digest

One line of totals first: "$X owed across N invoices; $Y overdue."

Then:

- **Overdue** — event, event date, installment, what's left, days late. Most overdue first.
- **Due in the window** — the same, soonest first.
- **Sent, nothing paid yet** — invoice, event, total, deposit due.
- **Partly paid** — invoice, paid, balance.

Flag events that happen before their balance is due-dated or paid. Amounts arrive in minor units (cents):
divide by 100. Mark sample data (`is_sample: true`) and keep it out of the totals unless the person wants it.

Offer, don't do: reminder wording can be drafted in this chat for a person to send; collecting payment
happens in Excellent.

## 3. Draft a missing invoice (if asked)

For a booked event with no invoice, `get_event` shows what was agreed (the contract's or proposal's menu and
client total). If the event already has an invoice, don't draft a second one: read it with `get_invoice` and
correct it (step 4). If the agreed document says some prices are still to be confirmed, or no tax and service
rates are set yet, its total is partial: say so and ask for the missing figures. Draft the invoice with
`draft_invoice`: the `event_id`, its `lines` (each a `label`, a whole
`qty` and a `unit_price_minor` in cents, taken from what was agreed — never an invented price), and any
`tax_minor` / `fee_minor` the agreement states. Excellent computes the totals and the deposit from the
group's deposit schedule. Give back the figures and the review link: the person checks it and sends it from
the invoice page in Excellent. Nothing is sent from here. To find the link again, `get_review_link` with `kind`
`invoice` and the invoice's `id`.

## 4. Correct or schedule a draft invoice (if asked)

Find the invoice (`list_invoices` with `status: "draft"`, or the id `draft_invoice` returned), then read it
with `get_invoice`. Only an invoice whose `revisable` is true can change here; when it is false, tell the
person why in the words of `not_revisable_because`, and don't try. Say what will change first.

- **Correct it:** `revise_invoice_draft` with the `invoice_id` and what changes — `title`, `tax_minor`,
  `fee_minor`, or `lines`. `lines` replaces every line, so start from the `lines` `get_invoice` returned
  (`label`, `qty`, `unit_price_minor`, in order), change only the lines the person asked about, and pass the
  whole list back with every other line exactly as it was. Excellent re-derives the totals and re-prices the
  deposit for the party size.
- **Schedule payments:** `add_invoice_installment` with the `invoice_id`, the `amount_minor`, an optional
  `label` ("Deposit", "Balance") and `due_on` (`YYYY-MM-DD`), one installment per call. Check the
  installments `get_invoice` lists first, so none is added twice. The answer says how much of the total the
  schedule now covers: say if it falls short of the total or runs past it. No reminder is sent and no pay
  link is made.

An invoice that was sent, paid, frozen or voided is left as it is: a sent invoice is corrected in Excellent.
If the answer says the draft changed while this was being prepared, read it again with `get_invoice` and
rebuild the change from what it returns before retrying. Give back the figures and the review link; nothing
is sent until the person sends it from the invoice page.

Safety: invoices stay drafts behind their review link. Nothing is sent to a guest, charged or recorded as paid
from ChatGPT, and nothing is deleted.
