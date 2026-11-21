---
name: cashflow
description: Project cash forecast — applications in (certification/payment lags per
  the contract profile), cost out (ledger run rate plus user-supplied lags), retention
  movements, net curve. Every timing parameter is profile- or user-stated, never assumed.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Project Cash Forecast (Ref CS-NNN)

A forward monthly cash curve — cash in from future applications, cash out from the cost run
rate, retention movements, and net position — built **only** from timing parameters the project
actually controls: the contract profile's assessment/certification/payment lags and retention
terms, and user-supplied cost-payment lags. Follow the shared patterns for project resolution
(Pattern 1), report numbering (Pattern 8), the contract profile (Pattern 13), the commercial
profile (Pattern 14), and the cost ledger (Pattern 16), all under
`../../shared/patterns`.

**Scope note:** this is the **dated cash mechanics** — when money actually lands, month by
month, given the contract's own timing. Not a strategic outlook (Commercial Forecast agent:
ETC/EAC and variance narrative), not the period measure (`$valuation`), not cost/value
reconciliation (`$cvr`), not a labour-hours forecast (`$cost-to-complete`).
Uncertain value/cost run rates are inherited, not smoothed away — a dated cash line is only as
good as the timing parameter it is phased against; an undated line is reported as undated.

**Local files (never writes):** Pattern 13 `contract-profile.md` (assessment interval/day,
certification lag, payment lag, retention %, release triggers — Contract Data/schedule entries,
not standard-form fallbacks; see Step 1's departure from rule 2); Pattern 14
`commercial-profile.md` (`activity_rates`, `prelims`, `currency`, fallback `retention_pct` per
rule 6); Pattern 16 `commercial/cost-ledger.md` (cost run-rate base; absent → Step 3 degrades
per rule 4).

---

## Step 1: Resolve Project, Horizon, and Payment Terms

1. Resolve the project (Pattern 1).
2. Resolve the **horizon in months** — the second `the user’s request` token if numeric, else **default
   3 months** from the data cut-off (the latest dated value/cost data available, not today).
3. Read `contract-profile.md` (or its `<project>`-slugged variant; a mismatched `project` field
   is ignored, say so — Pattern 13 rule 4) for the payment-mechanics fields: assessment
   interval/day (which date each period's value is assessed on), certification lag (assessment
   → certificate date), payment lag (certificate → cash-in date), retention % (deducted from
   certified gross before cash-in), and retention release triggers (the only events that release
   held retention).
4. Read `commercial-profile.md` (Pattern 14) for `activity_rates`, `prelims`, `currency`, and a
   fallback `retention_pct` if the contract profile is silent on it.
5. Read `commercial/cost-ledger.md` (Pattern 16) for the cost run-rate base (Step 3).

**The one departure from the usual Pattern 13 rule 2:** other contract-profile-consuming skills
fall back to the unamended standard form when a field is absent, because the standard form
states a default for it. **Assessment intervals, certification periods, and payment periods have
no standard-form default** — they are Contract Data / schedule entries fixed by the parties (an
NEC4 ECC assessment interval is whatever Contract Data Part One states; there is no "standard"
to fall back to). So for these fields specifically:

- **Present in the contract profile** → use them, cited "per the contract profile".
- **Absent, non-interactive run** → do **not** state a standard-form assumption and continue.
  Instead say plainly: **"no payment terms available for [assessment/certification/payment] —
  cash-in phasing cannot be dated"**, and the affected cash-in line runs undated (Step 2).
- **Absent, interactive run** → ask for the missing field(s) once, grouped; proceed undated if
  unanswered.

Retention % follows the ordinary Pattern 13/14 precedence (contract profile, else commercial
profile, else "not stated — retention cannot be deducted, gross figures shown"). Retention
release triggers have no fallback source at all — commercial-profile.md carries no such field —
so an absent trigger list means **no release is ever modelled in this run** (Step 2).

---

## Step 2: Cash In — Future Applications

### 2a: Forecast Value Trajectory (labelled FORECAST, distinct from recorded actuals)

1. Establish **cumulative value to the data cut-off** using the `$valuation` method
   (records priced at Pattern 14 rates) or an `AP-[NNN]` ref already in this conversation — cite
   the basis. This figure is **recorded**, not forecast.
2. Establish the **monthly value run rate**, same method as `$programme` Step 5b /
   `$cost-to-complete` (value earned in a period ÷ months in that period, from the
   trailing data available — state how many months). A **trailing average**, not a scope
   prediction.
3. For each future month: **Forecast Cumulative Value = cumulative value to cut-off + (run rate
   × months forward)**. Label every such row **FORECAST** — never blend into recorded actuals
   unlabelled.
4. **Divide-by-zero / no-data guard (Pattern 12):** no recorded value history → "insufficient
   value history to derive a run rate — cash-in cannot be forecast", never an invented rate.

### 2b: Phase Through Assessment → Certification → Payment

For each forecast month's **incremental** value (this month's forecast cumulative minus last
month's):

1. **Assessment date** = the next assessment day on/after the value is earned, per the contract
   profile's assessment interval/day. Absent → this line is **undated** (Step 1).
2. **Certification date** = assessment date + certification lag.
3. **Payment (cash-in) date** = certification date + payment lag.
4. Incremental value lands as cash **in the calendar month containing the payment date** —
   often later than the month the work was forecast in. Show the shift explicitly (e.g. "value
   forecast for March lands as cash in May, per a 1-week certification lag + 3-week payment lag").

### 2c: Retention

Deduct retention % (Step 1) from each certified gross amount before it counts as cash-in;
accumulate the running **retention held** balance across the horizon.

**Retention release is never assumed.** Release only where a release trigger is stated in the
contract profile **and** the user confirms (or the profile's key dates confirm) it falls within,
or is reached by, the horizon. No trigger stated, or stated but unconfirmed → the retention-held
balance simply accumulates, stated plainly ("no retention release modelled — no confirmed
trigger within this horizon").

---

## Step 3: Cash Out — Cost Run Rate and Payment Lags

### 3a: Cost Run Rate by Head (labelled: derived from N months of ledger data)

From `commercial/cost-ledger.md` (Pattern 16): for each CVR head, **Monthly Run Rate = cumulative
cost to date ÷ number of ledger months available**, cited "derived from [N] month(s) of ledger
data". Where only one ledger period exists (N=1), state plainly this is a **single-period base
rate, not a trend** — a stated limitation, not a hidden one. Extrapolate each head's monthly rate
across the horizon.

**No ledger imported** → per **Pattern 16 rule 4**: cash-out reads "no cost ledger imported — run
`$cost-import`" for every head, and the curve (Step 4) carries cash-in only, net/cumulative
columns marked "cost side unavailable". Never block Step 2's cash-in on this.

### 3b: Phase by User-Supplied Payment Lags per Head

Cost incurred in a month is not necessarily paid out that month. For each head, ask for (or use
if already supplied this session) a **payment lag** — all user-supplied: labour/payroll (payroll
cycle), plant (hire terms, e.g. monthly in arrears), subcontract (assessment + certification +
pay-when-paid or fixed period), materials (supplier terms, e.g. 30/60 days), prelims/staff
(usually same-month).

**No lag supplied for a head** → that head's cash-out **cannot be dated**, stated line by line
("[head]: run rate available, no payment lag supplied — cash-out timing cannot be dated") —
never defaulted to "30 days" or any "typical" term. A head with no ledger figure at all is simply
absent from the cash-out table (per 3a).

### 3c: Subcontract Liabilities / Accruals

Any subcontract liability or accrual affecting cash-out beyond the ledger run rate is
**user-supplied only**, entered as a distinctly-labelled line (never derived from the ledger or
the records) — the same discipline as Pattern 16 rule 3 for the CVR.

---

## Step 4: The Curve

### Monthly Cash Table

| Month | Cash In (FORECAST) | Cash Out (derived run rate) | Net | Cumulative Net |
|---|---|---|---|---|
| [month 1] | [£X or "undated — see assumptions"] | [£X or "no cost ledger imported"] | [£X] | [£X] |

State currency (Pattern 9) once in the header. A month whose cash-in or cash-out line is undated
or unavailable shows the reason inline rather than a blank cell, and Net/Cumulative Net for that
month reads "not computable — see assumptions" rather than treating the missing line as zero.

### Assumptions Table and Sensitivity Note

Read `references/assumptions-and-sensitivity.md` and apply
its formats. Rows: assessment interval/day, certification lag, payment lag, retention %,
retention release trigger, value run rate, cost run rate per head, payment lag per head,
subcontract accrual/liability — sourced from Steps 1–3. Sensitivity note: compare each lag by
the £ amount that would move between adjacent forecast months if it were one interval longer or
shorter, and name the largest.

---

## Step 5: Present the Forecast

Apply Pattern 8 for the `CS-[NNN]` ref (session-local; increment on a prior `CS` ref in this
conversation, else `001`). Read
`references/output-template.md` for the header block, the
seven-section order (Summary, Cash In, Cash Out, Curve, Assumptions, Sensitivity, Standing
Caveat), and the standing-caveat text (always unmodified).

If Step 1 found no contract profile, present Section 2 with every cash-in line undated, point
once to `$contract-profile`, and continue (cost-out phasing does not depend on the
contract profile). If Step 3 found no cost ledger, present Section 3 per the Pattern 16 rule 4
degrade and continue with cash-in only, curve's cost column marked accordingly.

---

## Hard Rules

1. **No invented timing parameter, and no "typical" payment term.** Every assessment interval,
   certification lag, payment lag, and cost-head payment lag is either per the contract profile
   or user-supplied this session (see Step 1's departure from the usual fallback). A missing one
   blocks that line's dating — stated plainly, never phased against an assumed period.
2. **Forecast vs recorded is always labelled.** Every forward-looking value/cost figure carries
   FORECAST or "derived run rate"; every historical figure it is built from is cited as recorded.
3. **Retention release is never assumed.** It is modelled only against a contract-profile-stated
   trigger confirmed as reached within the horizon — otherwise retention simply accumulates.
4. **The cost side never goes to the other party** (Pattern 16 rule 6) — this is an internal
   cash forecast, not an output for the other party.
5. UK English throughout.

---

## Related Skills

- `$valuation` — records-backed period measure this skill's cash-in run rate is built from
- `$cvr` — backward-looking cost/value reconciliation (this skill is forward and dated)
- `$cost-import` — imports the cost ledger this skill's cash-out run rate reads (Pattern 16)
- `$cost-to-complete` — labour-hours EAC counterpart; shares the run-rate method
- `$prelims-monitor` — tender-duration run-rate extrapolation this skill's method mirrors
- `$contract-profile` — captures the payment-mechanics fields this skill depends on
- Commercial Forecast agent — the strategic ETC/EAC outlook; this skill stops at dated cash mechanics
