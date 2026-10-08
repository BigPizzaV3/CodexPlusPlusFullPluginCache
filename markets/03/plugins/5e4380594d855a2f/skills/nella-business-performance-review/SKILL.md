---
name: nella-business-performance-review
description: Explain how the business performed over a period, what moved and why, using Nella's finance tools. Use when the user asks about profit, margin, revenue or costs, how a month or quarter went, why profit changed, whether performance is improving, or for a management-accounts style commentary. Do not use for a broad "how is my business doing" or "what needs my attention" request, which goes to the finance director briefing, and do not use for cash and runway, month-end readiness, debtors, supplier payments or filing deadlines.
---

# Management performance reporting

The user has asked about performance. Answer with a structured explanation of
what moved and why — not one figure, and not a general business briefing.

## Gather

Always start with `get_comparative_pl`. Then call the tools the question
actually needs — do not call all of them by reflex:

| Tool | Add it when |
|---|---|
| `get_kpi_dashboard` | Margin, ratios or headline trend are in scope |
| `get_budget_variance` | A budget exists and the user asks against plan |
| `get_anomalies` | Asked what changed, what looks wrong, or for a full review |
| `get_top_customers_and_suppliers` | Concentration or "my biggest customers" is relevant |
| `get_cashflow_history` | The question is how profit converted to cash |
| `get_management_summary` | A prepared management-accounts narrative exists — note it is a PACK, fixed at its generation date, not a live read |
| `get_report_link` | The user wants the management pack itself — a time-limited download link, not an email |
| `get_vertical_benchmarks` | The user asks how they compare to their sector |
| `search_transactions` | You need the items behind a movement |

## Structure the answer

1. **The conclusion** — how the period performed, in one or two lines
2. **What moved** — revenue, cost, margin, profit, against the comparative
3. **Why it moved** — the drivers, as far as the data supports them
4. **Unusual movements** — anomalies worth attention
5. **What could not be assessed** — named
6. **What merits attention**, ordered by size of impact

Lead with what is material. Do not restate every figure a tool returned; a
review that repeats the dashboard is not a review.

## Explaining a movement

Attribute a change only as far as the data reaches. Where the P&L shows cost of
sales rose and gross margin fell, say that. Where you cannot see whether it was
price, volume or mix, say the data does not separate them rather than choosing
one. An invented driver is worse than an unexplained movement.

## Rules you must follow

**State the period and the currency.** Every payload carries `period_start`,
`period_end`, `currency` and `data_freshness`. A few tools also carry a `period`
label — comparative P&L, budget variance, management summary and top customers —
but most do not, so read the start and end dates rather than looking for one.
A figure without its period is not an answer.
Relay `interpretation` where a tool provides it — "last year" means the
business's own financial year, which is rarely January to December, and the user
can only correct a wrong reading if they see which months were used.

**`has_data: false` means NOT ASSESSED, never clean.** An empty `anomalies`
list with `has_data: false` means detection has not run — say the books have not
been assessed. Reporting "no anomalies found" there is the most reassuring wrong
answer this connector can give. The same applies to `get_kpi_dashboard`.

**Null is not zero.** A null figure is one the ledger did not report. Never
substitute zero, and never treat an absent figure as a nil balance.

**Performance rests on the books being reliable.** Where the user's question
depends on the numbers being right, say what you know about that and point them
to a readiness check — do not certify the close from here.

**Never sum concentration across months.** `get_top_customers_and_suppliers`
returns shares of ONE month's invoices, ex-VAT, of invoices raised — not P&L
revenue. Shares do not add up, and a supplier ranked sixth every month can
outrank one that spiked once. A multi-month question needs a call per month.

**Benchmarks are comparative context, not a target.** Relay the basis and the
sample where given.

**Read `limitations` and relay them.** They are written to be passed on, not
summarised away.

**Distinguish fact from projection.** The P&L and KPIs are what the ledger
reported. Forecasts, runway and indicators are projections from it.

## A prepared pack and the live ledger are not the same thing

`get_management_summary` returns a **pack**: a narrative prepared on a date,
covering a period that ended before that date. `get_comparative_pl` reads the
**live ledger** for the latest complete month. They routinely differ, and
neither is wrong.

**They usually cover different months.** The latest pack may be July while the
latest complete month is August. That is not a labelling error — it is a pack
that has not been prepared yet for the newer month. Say which month each
covers and why they differ. Never describe it as an offset or imply one is
mislabelled.

**They can differ on the SAME month.** A pack fixed on 12 August and a ledger
read on 13 September will disagree about July if anything was posted, amended
or reclassified in between. A few hundred pounds on a month's revenue is the
normal shape of this. The pack is what was reported at the time; the ledger is
what the books say now.

So before calling anything a disagreement, check three things:

1. **Which period** does each cover? Different months is not a conflict.
2. **When was the pack generated**, against the ledger's freshness? A gap
   explains a gap.
3. **Is the difference material** to the question asked? A £756 difference on
   a £47k month changes no conclusion and does not need to lead the answer.

Report it as what it is: "the July pack was prepared on 12 August and shows
£47,533; the ledger now shows £46,777 for July, so something was posted or
amended after the pack was produced." That is useful. "One of these is
mislabelled" is not, and it is wrong.

**Where the difference IS material** — a changed conclusion, a moved margin,
a sign flip — say so plainly, give both figures with their dates, and note
that a re-run pack would settle it. Do not pick one.

## Boundary

Nella provides a read-only assessment from connected records. It has not
posted, filed, approved, paid or sent anything. Estimates and projections are
identified separately from recorded figures.

Nella shows, answers, tracks and flags. It does not advise, recommend or
optimise. Describe what the numbers show and what merits attention; do not tell
the user what to decide.

Anything needing accounting or tax judgement — a treatment, a tax position,
whether to make a distribution — goes to a qualified accountant.

**Say "your accountant", and name no firm.** Most users have no relationship
with any particular practice, and this connector does not refer them to one.
Where an answer needs a person, the payload's `escalation` block says so and
carries `fallback_wording` - use it verbatim. It names no firm, no booking
link and no professional title, deliberately: professional titles are
protected descriptions and differ by country. The envelope's `advice_note`
says the same thing. Never substitute a firm, suggest a provider, or offer to
put the user in touch.

## When to stop or ask

- If no accounting platform is connected, say so and stop. Do not estimate.
- If the user asks about a specific month, pass `year` and `month` where the
  tool accepts them rather than answering for a different period.
- If two tools disagree, report both and say they disagree. Do not reconcile
  them yourself — but first check whether they are answering different
  questions, because most apparent disagreements here are not disagreements
  (see the section below).
