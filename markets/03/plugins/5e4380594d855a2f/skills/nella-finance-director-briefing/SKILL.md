---
name: nella-finance-director-briefing
description: Coordinate Nella's finance tools into one prioritised briefing across performance, cash, working capital, obligations and data reliability. Use when the user asks how the business is doing overall, what needs their attention, for a weekly or monthly finance briefing, whether the business is financially safe, or what their biggest financial risks are. Also use for an unscoped "what do I need to sort out", "what should I look at first" or "anything I should know about?" - a request that names no area belongs here, not to compliance. Do not use when the question names one area: profit and performance, cash and runway, month-end readiness, debtors, supplier payments and tax or filing deadlines each have their own skill.
---

# Finance director briefing

The user has asked a question no single specialist answers. Produce one
coordinated briefing that ranks what matters, rather than a tour of every tool.

## How to work

**Do not call everything.** Start high, then investigate only what the first
results make material. A briefing that calls twelve tools and reports all of
them is a dashboard, not a director's answer.

**Opening pass** — always:

| Tool | Why |
|---|---|
| `get_kpi_dashboard` | The headline position |
| `get_cash_position` | Whether there is money |
| `get_close_readiness` | Whether the numbers underneath can be relied on |

If `get_close_readiness` is unavailable on this connection, use
`get_reconciliation_status` for the reliability leg instead — and say it is the
weaker signal. A reconciled bank is one input to whether the books can be
relied on, not the whole close. Do not let the opening pass silently run on
two legs.

**Then investigate, based on what the opening pass showed:**

| Add | When the opening pass shows |
|---|---|
| `get_comparative_pl` | Profit or margin moved, or the user asked what changed |
| `get_cash_forecast` | Cash is tight, falling, or the question was about safety |
| `get_ar_ap_ledger` | Working capital is material on either side |
| `get_obligations` | Anything is due, or the question was about risk |
| `get_anomalies` | Close readiness flagged something, or the user asked what looks wrong |
| `get_top_customers_and_suppliers` | One counterparty appears to dominate |

Stop when you can rank. An exception you have not investigated is reported as
an exception, not omitted.

## Structure the answer

1. **Position and confidence** — where the business stands in two or three
   lines, and how far the underlying data can be relied on
2. **The top three matters**, ranked by financial impact, then urgency, then
   how confident the figure is
3. **By area, briefly** — performance, liquidity, working capital, obligations,
   data reliability. One or two lines each; omit an area with nothing to say
   rather than padding it
4. **What could not be assessed** — named, not summarised away
5. **Safe checks** the user can make, and separately **what needs a qualified
   accountant**

Lead with the conclusion. Do not open with a tool inventory or a data-quality
essay — put confidence in one sentence at the top and the detail in section 4.

## Ranking

Rank by money at stake, then by how soon it bites, then by how sure the figure
is. A large uncertain exposure outranks a small certain one, but say which it
is. Where two are close, the one with a deadline goes first.

## Rules you must follow

**Check `method` on `get_cash_forecast` before saying anything about
liquidity.** `method: "direct"` means `weeks[]` holds a real week-by-week
schedule and you may name the tightest week. `method: "indirect"` means only a
monthly run-rate was available: `weeks[]` is empty, and you must not describe it
as a 13-week position or answer which week is tightest. Say the weekly view was
unavailable and give the monthly projection for what it is.

This matters most here, because "is my business financially safe" is the
question this skill fronts, and a run-rate cannot answer it at week resolution.

**Check `assessed` first, on every tool.** Every payload carries
`assessed: full | partial | none` and `assessed_note`. `none` means nothing
was assessed and every empty list, null and zero is unassessed, never nil;
`partial` means a leg is missing and the note names it. Read the note before
any figure.

The per-tool flags still exist and agree with `assessed`. Where you need the
detail behind a `partial`, these are where it lives:

| Tool | What says "not assessed" |
|---|---|
| `get_kpi_dashboard`, `get_cash_position`, `get_anomalies` | `has_data: false` |
| `get_cash_forecast` | `method: null` (no forecast at all), or `coverage.*` for a component |
| `get_ar_ap_ledger` | `assessable: false`, inside `receivables` and `payables` separately |
| `get_obligations` | `has_obligations` — and read the coverage, which differs by business |
| `get_close_readiness` | `blocker`, `counts` and `stages`; checks report their own state |
| `get_comparative_pl` | `coverage` |
| `get_top_customers_and_suppliers` | `basis` and `headline`; there is no emptiness flag |

An empty anomalies list with `has_data: false` means detection did not run.
Reporting "nothing found" there is the most reassuring wrong answer this
connector can give — and the same trap exists on every tool above under a
different field name. Where a tool has no emptiness flag at all, say what it
returned and do not infer an all-clear from a short list.

**Null is not zero, unavailable is not none, unassessed is not clean.** Say
which of the three you are reporting.

**Keep facts, estimates, indicators and projections visibly apart.** The P&L
and the ledger are what was recorded. Forecasts, runway, tax indicators and
predicted receipt dates are derived. Never present the two at the same
confidence.

**Where tools disagree, say so.** Outstanding receivables and invoiced value
answer different questions and will not match — that is not a disagreement. A
genuine contradiction is reported as one, not reconciled by you.

**State the period, the currency and the as-at date** on every figure.

**Do not answer a specialist question from the opening pass alone.** If the user
follows up on debtors, supplier payments or filing dates, that belongs to the
specialist skill, not to a deeper paragraph here.

## Boundary

Nella provides a read-only assessment from connected records. It has not
posted, filed, approved, paid or sent anything. Estimates and projections are
identified separately from recorded figures.

Nella shows, answers, tracks and flags. It does not advise, recommend or
optimise. Rank what merits attention and say why; do not tell the user what to
decide.

Anything needing accounting or tax judgement — a treatment, a tax position,
whether to distribute, whether the business is solvent — goes to a qualified
accountant. Solvency in particular is a legal test, not a cash
balance, and must be routed rather than inferred from a forecast.

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
- If close readiness is weak or unassessed, still rank — but say so in the
  confidence line at the top and mark the items that depend on the unreconciled
  data as provisional. Items with a date or an external deadline are unaffected
  and should not be hedged. Refusing to prioritise is worse than prioritising
  with a stated confidence: the user asked what to attend to, and the
  reconciliation state is itself one of the things they should attend to.
- If the opening pass mostly returns unavailable, report what could not be read
  rather than briefing from the fragment that did.
