---
name: nella-month-end-finance-review
description: Check whether a month's books are reliable before anyone interprets the numbers, and list what is outstanding. Use when the user asks if their books are up to date or ready to close, what is outstanding for a month, whether last month's numbers can be trusted, or what needs sorting before month end. Do not use for interpreting performance; for cash, runway or affordability; for money owed by customers or to suppliers; for tax or filing deadlines; or for a broad "what needs my attention" request, which goes to the finance director briefing. "Outstanding" here means work outstanding on the books - unreconciled items, unposted documents, checks not yet run. Outstanding MONEY owed by a customer is receivables, and owed to a supplier is payables.
---

# Month-end finance review

This skill answers one question: **can these numbers be relied on yet, and if
not, what is missing?** It is a readiness check, not an analysis.

## Gather

Start with `get_close_readiness` — it covers data completeness, bank, sales,
purchases, payroll, taxes, balance sheet and analytical review. Pass `year` and
`month` when the user names a month.

| Tool | Add it when |
|---|---|
| `get_reconciliation_status` | The bank specifically is in question, or close readiness flags it |
| `get_anomalies` | Something looks wrong and you need what moved |
| `get_comparative_pl` | The user wants to see the numbers a blocker would distort |
| `list_invoices_and_bills` | Unposted or unpaid documents are the blocker |
| `search_transactions` | You need to find a specific item behind a flag |

## Structure the answer

1. **Overall readiness** — ready, nearly, or not, and why in one line
2. **Blockers** — what must be resolved before the numbers can be relied on
3. **Outstanding** — what is incomplete but not blocking
4. **Could not be assessed** — checks that did not run, named
5. **Where each item sits** — with the user, or with their accountant

Section 4 is not optional. A checklist that silently omits what it could not
check reads as a clean bill of health.

## Rules you must follow

**`awaiting_data` and `not_supported` are NOT problems and NOT clean.** A check
that cannot run on the user's platform is reported as one of those and never as
passed. Say which checks could not be assessed rather than counting them either
way.

**Never report a partial or not_assessable check as clean or up to date.**
Report it as unconfirmed, and say the user should check in their accounting
software.

**`counts` is where the unassessed live.** Checks are counted by status:
passed, warning, failed, critical, awaiting_data, not_supported,
awaiting_user_action, resolved. Report awaiting_data and not_supported
separately — folding either into passed or failed misstates what is known.
(`checks_not_available` belongs to `get_reconciliation_status`, not to this
tool.)

**`blocker` means nothing could be assessed at all.** It is set when there is no
ledger connection or the equivalent. Where it is present, say the books could
not be assessed and stop — do not report the empty check list as a clean close.

**`close_run.available: false` is not an all-clear.** It means exception
handling and sign-off are not part of this answer, NOT that there is nothing
outstanding. Say which it is; reading it as "nothing to do" is the exact
false-all-clear this review exists to prevent.

**A null amount is not zero.** On a close check, `amount_gbp` is null when the
platform did not report it — the payload says so. Do not read a null as
nothing found. (`coverage: partial` is a `get_reconciliation_status` field,
not a close-readiness one.)

**Reconciliation is not the whole close.** A reconciled bank does not mean the
books are ready — reconciliation is one input among sales, purchases, payroll,
taxes and the balance sheet. Do not answer "are my books ready" from
`get_reconciliation_status` alone.

**Reconciliation status is a POSITION at a date, not activity over a period.**

**VAT reconciliation is not available.** Nella cannot reconcile a VAT return,
and no combination of these tools produces one. Where a close check touches VAT,
report exactly what that check says and nothing more. If the user asks for a VAT
reconciliation, say plainly that it is not something Nella can do and route them
to their accountant — do not assemble a substitute from the ledger, the P&L or
tax indicators.

**State the period.** "Ready to close" for which month is the whole question.

## Boundary

Nella provides a read-only assessment from connected records. It has not
posted, filed, approved, paid or sent anything. Estimates and projections are
identified separately from recorded figures.

The journals, reconciliations and adjustments are the user's to make in their
own software, or their accountant's.

Where `recommendation_withheld` is true, the next step is a judgement for a
qualified accountant rather than something to action from here. Relay the
pointer; do not substitute your own advice.

Nella does not close periods, lock ledgers or file anything.

## When to stop or ask

- If the user does not name a month, answer for the last complete month and say
  which month that is.
- If `blocker` is set, or close readiness cannot be produced at all, say so and
  do not assemble a substitute from other tools — a checklist stitched together
  from unrelated signals is not a readiness assessment.
- If the books are not ready, give the readiness verdict first and mark any
  figures drawn from them provisional, naming the blocker that affects them.
  This skill's whole subject is reliability, so state it plainly — but a
  blocker in one area does not make every figure suspect, and saying which is
  affected is more useful than a blanket warning.
