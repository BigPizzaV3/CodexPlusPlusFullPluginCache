---
name: material-reconciliation
description: Reconcile delivered material quantities against placed/measured quantities
  to expose waste, loss, and record errors — delivered vs placed, concrete recon,
  waste tracing.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Material Reconciliation — Delivered vs Placed

Reconcile delivery-note quantities for a material against the quantities recorded as placed or
measured on the activities that material feeds, to expose waste, loss, and record errors. This
differs from the delivered-vs-**usage** reconciliation inside `$delivery-notes` (which
compares against `dashboardResourceMaterial` consumption): this skill compares against **placed/
measured progress on mapped activities** — "did the concrete we poured account for the concrete
delivered?" Follow the shared patterns: `../../shared/patterns/01-project-resolution.md`
(project resolution), `../../shared/patterns/02-date-range-parsing.md`
(date parsing), `../../shared/patterns/03-empty-data-handling.md` (empty
data handling), `../../shared/patterns/04-pagination-rate-limits.md`
(pagination), `../../shared/patterns/08-report-numbering.md` (report
numbering), and `../../shared/patterns/14-commercial-profile.md` (the
commercial profile).

---

## Step 1: Resolve Project, Material, and Period

1. **Project** — Pattern 1.
2. **Material(s)** — take from `the user’s request` if stated (e.g. "concrete", "rebar", "C40/50"); if
   none given, ask which material(s) to reconcile.
3. **Period** — Pattern 2. Recommend **at least a month**: delivery precedes placement, so a
   short window compares deliveries that haven't been placed yet against placement drawing on
   prior stock, and reads as a false waste or false surplus. If the resolved period is shorter
   than a month, warn explicitly: "This period is under a month — delivery-to-placement lag may
   distort the figures below; consider widening the window." Proceed if the user confirms.

---

## Step 2: Retrieve Delivered Quantities

Follow the same retrieval order as `$delivery-notes` Step 2: check `getReportSchemas` for
a delivery-capable report (supplier, delivery reference, quantity delivered fields) and call
`getCachedReport` if found; otherwise fall back per **Pattern 20 (Evidence Retrieval Fallback)**
from `../../shared/patterns/20-evidence-retrieval.md`. Filter to the
material(s) from Step 1 by fuzzy match (e.g. "concrete" matches "Ready Mix Concrete", "C32/40").

Do **not** use `dashboardResourceMaterial` here — that report is usage, not delivery, and is
outside this skill's data source per the design brief.

If nothing is found, apply Pattern 3 (wrong project, wrong dates, filter too narrow, not
recorded) and stop.

---

## Step 3: Map Material to Activity — Confirm When Ambiguous

Call `getCachedReport` (`dashboardProgress`) for the project and period to list activities.

For each material, determine which activity(ies) its placement is measured against:

- If exactly one activity plausibly consumes the material (e.g. "Rebar" → "Deck Steel Fixing"),
  propose it and proceed.
- If more than one candidate exists, or the mapping isn't obvious from naming alone, **list the
  candidate activities and ask the user to confirm the mapping** before reconciling — never guess
  a mapping silently, since a wrong mapping invalidates every figure downstream. Record the
  confirmed mapping for the output header.

---

## Step 4: Retrieve Placed/Measured Quantities

Using the mapped activity(ies) and the same period, take the actual/recorded output quantity and
unit from the Step 3 `dashboardProgress` data (as in `$progress` Step 5's "Actual Qty").
Sum across mapped activities only if their units match (Pattern 9, unit consistency) — never sum
mixed units.

**Pattern 12 schema gate:** if `dashboardProgress` lacks a per-activity quantity/unit breakdown
for this workspace, degrade explicitly — state that placed quantity is not available at this
granularity for that material, rather than substituting a guessed figure.

---

## Step 5: Unit Conversion — Stated Factors Only

If delivered and placed units already match, proceed directly.

If they differ, convert **only** using a factor the user states this session or one recorded in
the commercial profile — **never an assumed density, yield, or volume conversion**. Cite the
factor's source inline (e.g. "1.35 t/m³ per commercial profile" / "user-supplied this session").

If no factor is available, do not convert or block the output: present the delivered and placed
figures **side by side, unconverted**, with a note: "[Material] delivered in [unit A], placed in
[unit B] — no stated conversion factor, figures shown unconverted."

---

## Step 6: Build the Reconciliation Table

For each material (per mapped activity where units allow):

| Material | Delivered | Placed | Implied surplus/waste | Waste % | Norm % (profile) | Variance |
|---|---|---|---|---|---|---|

- **Implied surplus/waste** = Delivered − Placed.
- **Waste %** = (Implied surplus/waste / Delivered) × 100. Delivered = 0 → "n/a", Pattern 12
  divide-by-zero convention, flagged as a data-quality issue rather than a number.
- **Norm % (profile)**: read `material_norms` from the commercial profile (Pattern 14) matched by
  material name. If the profile is absent, or the material has no norm entry, show "not in
  profile" — never invent a typical waste allowance.
- **Variance** = Waste % − Norm % where both exist; "—" otherwise.

Every row cites its evidence: delivery note reference(s)/dates and the mapped activity/progress
record date range.

---

## Step 7: Flags

**Waste above norm** (Variance clearly positive): flag the material and, if a matching item and
rate exist in the commercial profile's `activity_rates` (or the user supplies one this session),
price the excess as (Implied surplus/waste above the norm-allowed quantity) × rate, citing the
source. If no rate exists, present the excess quantity only with "rate not in commercial profile"
(Pattern 14 rule 2) and point once to `$commercial-profile` — never block on this.

**Negative waste** (Placed > Delivered) — this skill's signature guardrail. State **both**
possible explanations side by side and assert **neither**:

> [Material] shows placed quantity exceeding delivered quantity by [X] [unit] for the period.
> This may reflect **missing delivery records** (deliveries not logged in Gather, or delivered in
> an earlier period outside this window) **or** a **measurement error** (placed quantity
> over-recorded, or measured against the wrong activity). Records do not distinguish between
> these — investigate delivery logging and the measurement basis before treating this as either.

List any other material for which the Step 2 or Step 4 data lacked the fields needed to complete
its row (Pattern 12 degradation), naming the missing field.

---

## Step 8: Recommended Record Fixes

One line per flag, e.g.: "Log delivery notes for [material] covering [gap dates] to close the
missing-record possibility on the negative-waste flag"; "Confirm [activity] progress records are
measured against the correct material code — a mismatch would explain the [material] variance";
"Capture a stated conversion factor for [material] in the commercial profile to remove the
unconverted side-by-side presentation."

---

## Step 9: Present Results

```
MATERIAL RECONCILIATION — [Project Name]
Ref: MR-[NNN]
Period: [Start Date] to [End Date]
Material(s): [material list] — mapped to: [activity(ies)]
Generated: [Today's Date]
```

Followed by: the Step 1 period-length warning (if triggered), the Step 6 reconciliation table,
a **FLAGS** section (Step 7), and a **Recommended Record Fixes** section (Step 8). Close with:

> Ref: MR-[NNN] is a session-local sequence number for cross-referencing (Pattern 8).
> Figures trace to delivery note references and progress records cited above; no rate or
> conversion factor is assumed — only stated ones are applied.

---

## Related Skills

- `$delivery-notes` — delivery summaries and the delivered-vs-usage reconciliation
  (`dashboardResourceMaterial`) — a different comparison to this skill's delivered-vs-placed
- `$progress` — the underlying placed/measured quantities by activity
- `$commercial-profile` — capture `material_norms` and `activity_rates` used here
- `$resource-analysis` — broader resource picture across materials, labour, and plant
