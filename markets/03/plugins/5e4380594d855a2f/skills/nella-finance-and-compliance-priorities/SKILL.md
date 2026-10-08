---
name: nella-finance-and-compliance-priorities
description: Show what the business has to file and pay — filing and payment dates, the Corporation Tax estimate where one is available, VAT-threshold and tax indicators, and what is overdue — ranked by urgency. Use ONLY when the request concerns tax, filing, regulatory or statutory obligations: what tax or filing deadlines are coming up, whether a return or filing is due or overdue, the VAT or registration threshold, or the Corporation Tax position. Do not use for a general "what do I need to sort out" or "anything due?" request unless it names tax, filing or a statutory obligation — an unscoped request goes to the finance director briefing. Do not use for supplier bills or payment timing, which are payables; for overdue customer invoices, which are receivables; for cash, runway or affordability; for profit or margin; or for reconciliation and close readiness.
---

# Finance and compliance priorities

The user is asking what needs dealing with. Answer with what is due, what is
flagged, and in what order — not a general review.

## Gather

| Tool | Purpose |
|---|---|
| `get_obligations` | Filing and payment dates, and the Corporation Tax estimate where held |
| `get_tax_and_compliance_indicators` | VAT-threshold and Corporation Tax indicators from run-rate figures |
| `get_close_readiness` | Whether the books behind any of it are reliable |
| `get_cash_position` | Whether there is cash to meet what is due |
| `get_anomalies` | Anything in the numbers needing attention |

Start with `get_obligations` and `get_close_readiness`.

## Read `coverage` — never infer it

`get_obligations` states which source answered. **Read the field. Do not work
it out from the items.**

| `coverage` | What is on file | What is NOT |
|---|---|---|
| `filing_record` | The maintained set for the jurisdiction: Corporation Tax return and payment, VAT, PAYE, Self Assessment, MTD, annual accounts, confirmation statement — with a recorded `amount` where one is held | Anything not yet generated. An empty category is not a statement that nothing is due in it |
| `companies_house` | Statutory filings from the public register only: annual accounts, the confirmation statement, and Corporation Tax dates derived from the accounting reference date | **No VAT, PAYE or Self Assessment dates at all, and no amounts.** Not held, not assessed — never "none due" |
| `none` | Neither source answered | Everything. Say nothing was assessed |

Each item also carries `category` (filing, payment, return, registration),
`authority`, `frequency` and `jurisdiction`, so you can describe an obligation
without knowing the country's vocabulary in advance. An item with a null
`category` is unclassified, not un-owed.

`assessed` on the payload agrees with `coverage`: a `companies_house` answer is
`assessed: partial` and `assessed_note` gives the scope in words you can relay.

## Four things to keep apart in the answer

Do not let these blur into one list, and never present the second or third as
the first:

1. **Assessed obligations** — items actually returned, with their dates. These
   are on file.
2. **Potentially applicable but not covered** — where `coverage` is
   `companies_house`, VAT, PAYE and Self Assessment are not held for this
   business. Name them as not covered. A business with employees almost
   certainly has PAYE obligations; the absence of PAYE items says only that
   this source does not hold them.
3. **Unsupported areas** — anything outside a validated jurisdiction, or a
   `category` the payload does not classify. Say it is not supported rather
   than not due.
4. **Unknown coverage** — `coverage: none`, or `assessed: none`. Nothing was
   assessed; report that and stop.

**Never claim comprehensive coverage.** Do not say "you are up to date", "there
is nothing outstanding", "everything is filed", or "that is all your
obligations" unless `coverage` is `filing_record` — and even then, say it
covers what the filing record holds, not everything the business owes. On
`companies_house` or `none`, a completeness claim is false and the user may
miss a filing because of it.

## Structure the answer

1. **Overdue** — anything already past its date
2. **Due soon** — with dates and days remaining
3. **Amounts** — where an obligation carries one, clearly labelled as an
   estimate from the records held, not an assessed or filed figure
4. **Indicators worth watching** — VAT threshold, CT position
5. **Data quality caveats** — where the books behind this are not reliable
6. **What needs attention**, ordered by urgency then consequence

Section 5 comes before section 6 deliberately, and it CALIBRATES section 6
rather than cancelling it. Dates and filing deadlines are largely independent
of whether the ledger is reconciled; amounts and threshold indicators are not.

- Reconciliation weak or unassessed, question is about DATES — answer normally.
  A filing deadline does not move because the bank is unreconciled.
- Reconciliation weak or unassessed, question is about AMOUNTS or thresholds —
  label the answer provisional, say which figures rest on the unreconciled
  data, and give the reconciliation state in a line. Do not withhold the
  figure; a user who cannot see it cannot act on it.
- Reconciliation assessed and clean — answer normally and say the numbers
  behind it were checked.

State the limitation in terms of what it changes. "Your VAT-threshold indicator
uses turnover from books whose bank reconciliation has not been assessed, so
treat it as provisional" is useful. "The books may be unreliable" is not.

## Rules you must follow

**The Corporation Tax estimate comes from `get_obligations` and nowhere else.**
It is an estimate derived from the records held. It is not a computation, not a
filed position and not confirmed by HMRC. Where no amount is held, say the date
is known and the amount is not — never supply a figure from elsewhere.

**Never answer a company Corporation Tax question from a personal tax tool.**
`get_estimated_tax_position` is a personal tax projection for an individual.
A company's Corporation Tax and a director's personal tax are different
taxpayers and different liabilities. If a personal projection is what the user
wants, treat it as a separate question and say which taxpayer it concerns.

**VAT reconciliation is not available.** Nella cannot reconcile a VAT return,
and no combination of these tools produces one. If the user asks to reconcile
VAT, check a VAT return, or agree VAT to the ledger, say plainly that it is not
something Nella can do and route them to their accountant. Do not assemble a
substitute from tax indicators, the P&L or the balance sheet — a figure built
that way looks like a reconciliation and is not one.

VAT *obligations* and VAT-threshold *indicators* are different things and may be
reported where the tools supply them.

**An empty obligations result is not "nothing to file."** `coverage` tells you
which case you are in; these are the reasons behind it:

- No company registration number on the accounting software's organisation
  record means the lookup could not run. Tell the user to add it — that is a
  thing they can fix.
- A failed lookup is a lookup that did not answer, not a company with nothing
  due.
- Sole traders and unincorporated businesses have no Companies House filings, so
  an empty result is expected for them.

**A Corporation Tax date that has passed is not a delinquency.** Nella has no
HMRC connection and cannot see whether something was paid or filed. Report that
the date has passed and that payment status is not visible.

**Tax indicators are INDICATIVE, derived from run-rate figures.** Not a
computation, not a filing position, not advice. A VAT-threshold indicator says
the run rate is approaching a threshold; it does not say the business must
register.

**Nothing here has been filed, submitted, registered or paid.**

**Non-UK businesses get no UK filing dates.** Where the ledger shows a business
outside the UK, the tool says so — relay that rather than substituting generic
deadlines.

**Read `limitations` and relay them.**

## Boundary

Nella provides a read-only assessment from connected records. It has not
posted, filed, approved, paid or sent anything. Estimates and projections are
identified separately from recorded figures.

Everything in this area is close to regulated advice, so route more readily than
elsewhere: whether to register for VAT, how to treat a liability, whether a
filing approach is right, what to do about an overdue return — all go to a
qualified accountant. State the dates and the indicators; leave the
judgement.

Nella never files, never submits and never pays.

**Say "your accountant", and name no firm.** Most users have no relationship
with any particular practice, and this connector does not refer them to one.
Where an answer needs a person, the payload's `escalation` block says so and
carries `fallback_wording` - use it verbatim. It names no firm, no booking
link and no professional title, deliberately: professional titles are
protected descriptions and differ by country. The envelope's `advice_note`
says the same thing. Never substitute a firm, suggest a provider, or offer to
put the user in touch.

## When to stop or ask

- If no accounting platform is connected, say so and stop.
- If the books are not close-ready, say so alongside the answer and mark any
  amount or indicator provisional. Deadlines still stand; the figures are the
  part that carries the caveat.
- If the user asks about VAT or PAYE deadlines and `coverage` is
  `companies_house`, say plainly that those dates are not held for this business
  rather than estimating them.
- If `coverage` is `none` or `assessed` is `none`, say nothing could be assessed
  and stop. Do not assemble a compliance picture from the indicators or the
  close check.
