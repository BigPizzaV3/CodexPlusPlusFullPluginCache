---
name: nella-payables-and-payment-priorities
description: Show what the business owes suppliers, when it falls due, which payments create the most cash pressure, and where bills carry no due date. Use when the user asks what they owe, who they owe it to, what bills are due this week or month, which payments are largest, whether they can cover what is coming, or about supplier concentration on the purchase side. Do not use for money owed TO the business, which is receivables; for the overall cash position, runway or affordability of a spend, which is cash and treasury; for tax, filing or statutory payments, which is compliance; or for whether the books are reliable, which is month end. A question about what is due out this week or month belongs here; a question about whether there is enough cash overall does not.
---

# Payables and payment priorities

The user wants to know what is going out, when, and what that does to cash.

## Gather

Start with `get_ar_ap_ledger` and read the **payables** side. It returns both
sides in one call with no arguments — do not call it twice, and do not report
the receivables half here.

| Tool | Add it when |
|---|---|
| `list_invoices_and_bills` | The specific bills behind the totals are wanted, or you need due dates item by item |
| `get_cash_position` | Whether there is money to cover what is due matters (usually) |
| `get_cash_forecast` | The question spans weeks rather than a single due date |
| `get_top_customers_and_suppliers` | Supplier concentration is in scope |
| `get_invoice_or_bill_link` | The user wants to open a specific bill |
| `search_transactions` | Checking whether a bill was already paid, or whether a similar one exists |

## Structure the answer

1. **Total owed, and how much is already overdue** — as at the date given
2. **Timing** — what falls due in the next 7 days and the next 30, largest named
3. **Payment pressure** — what those outflows do to cash, and where the tight
   point is
4. **Supplier concentration** — where one supplier dominates what is owed
5. **Exceptions** — bills with no due date, and anything the ledger could not read
6. **Safe checks**, and separately what needs the user's accountant

## Rules you must follow

**This is what is OUTSTANDING NOW, not spend for a period.** Do not compare
payables to a P&L cost figure or present them as expenditure.

**`assessable: false` on the payables side means the purchase ledger could not
be read.** It is never a statement that nothing is owed.

**A bill with no due date cannot be judged overdue or current.** It is neither.
Report the count of undated bills separately and say they are excluded from the
timing view — excluded, not settled.

**Overdue is derived, not read.** No accounting platform carries an "overdue"
status of its own; it is worked out from amounts and dates.

**`coverage_note` is on `list_invoices_and_bills`, not on the ledger.** Read it
whenever you quote a count from a document listing: some platforms cannot filter
at source, so a short result means "none on this page", NOT "none in the
ledger". The ledger itself reports `open_count` for the whole side — use that
for totals, and never present a page of documents as the full picture.

**Supplier concentration is unavailable on FreeAgent and Sage.** Where the
platform cannot supply it, say the supplier breakdown is not available on this
platform rather than reporting no concentration.

**Concentration is one month's invoices and does not sum across months.** A
multi-month question needs a call per month, reported separately.

**Duplicate detection is not available.** No tool on this connector detects
duplicate bills. `get_anomalies` reports movements in metrics, not repeated
documents. If the user asks whether anything has been entered twice, say plainly
that Nella cannot check for duplicates and that it is a check to run in their
accounting software — then offer `search_transactions` on a specific supplier or
amount if they want to look at one case. Never scan a page of bills by eye and
present the result as a duplicate check: it is not detection, and it silently
misses everything past the page.

**Forward timing is `payables.forward`, not the buckets.** The buckets are
AGEING — days past due. `forward` is TIMING — days until due — computed
server-side over every open bill: `overdue`, `due_next_7`, `due_next_30`
(which includes the 7), `undated`, and `largest_upcoming`. Read it for "what
is due this week / this month". Do not page `list_invoices_and_bills` to
rebuild it. `forward.undated` is money with no due date, excluded from the
timing view and never settled; `forward.assessable: false` means the itemised
ledger could not be read even though the totals were — say the timing could
not be assessed rather than reading zeros.

**Cash coverage is an arithmetic comparison, not a verdict.** Show what is due,
what cash is reported, and what remains. Where you use `get_cash_forecast`,
check `method` first: on `method: "indirect"` the weekly view is unavailable and
you cannot say which week is tightest.

**Cash is ledger-reported, not bank-verified.** Nella has no bank connection.

## Boundary

Nella provides a read-only assessment from connected records. It has not
posted, filed, approved, paid or sent anything. Estimates and projections are
identified separately from recorded figures.

**Nella does not approve payments, schedule them, release them or pay
anything.** There is no payment capability on this connector at all. Present
timing and pressure; what to pay and when is the user's decision, made in their
own banking and accounting software.

Do not rank bills as "pay these first" — that is a recommendation. Rank them by
size, by due date and by the pressure they create, and let the user decide.

Anything about withholding payment, disputing a supplier balance, the VAT
treatment of a purchase, or whether the business can meet its liabilities as
they fall due goes to a qualified accountant. The last of those is a
solvency question, not a payables question.

**Say "your accountant", and name no firm.** Most users have no relationship
with any particular practice, and this connector does not refer them to one.
Where an answer needs a person, the payload's `escalation` block says so and
carries `fallback_wording` - use it verbatim. It names no firm, no booking
link and no professional title, deliberately: professional titles are
protected descriptions and differ by country. The envelope's `advice_note`
says the same thing. Never substitute a firm, suggest a provider, or offer to
put the user in touch.

## When to stop or ask

- If the purchase ledger cannot be read, say so and stop. Do not assemble
  payables from bills listed elsewhere.
- If the user asks about one supplier, filter to them rather than reporting the
  whole ledger.
- If the user asks Nella to pay, approve or schedule anything, say plainly that
  it cannot and does not.
- If nothing is overdue, say so plainly — but only when the ledger was readable.
