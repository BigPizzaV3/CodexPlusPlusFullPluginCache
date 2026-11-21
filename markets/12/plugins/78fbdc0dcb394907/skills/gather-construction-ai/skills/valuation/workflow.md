---
name: valuation
description: Build the monthly AfP / interim application, priced at commercial-profile
  rates, retention and cumulative arithmetic. A draft pack for review, never a certified
  valuation. Not subcontractor claims (use subcontractor-check).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Valuation — Application for Payment (Ref AP-NNN)

The monthly measure: quantities done this period per activity, priced, evidence-backed, cumulative
and retention arithmetic done — an application pack ready for commercial review and submission.
**Scope note:** this is the backward-looking period measure. It does not forecast cost-to-complete
(use `$cost-to-complete`), analyse productivity/variance (use `$progress`), or price a
compensation event (use `$ce-quotation`). Follow the shared patterns in
`../../shared/patterns/01-project-resolution.md` for project resolution (Pattern 1), date parsing
(Pattern 2), empty data handling (Pattern 3), pagination (Pattern 4), and report numbering (Pattern 8).

**Profiles this skill reads (never writes):**
- **Pattern 14 (Commercial Profile)** — `commercial-profile.md` for `activity_rates`,
  `prelims`, `retention_pct`, `currency`. No profile, or an unmatched line item → that line runs
  quantities-only; never blocked.
- **Pattern 13 (Contract Profile)** — `contract-profile.md` for `main_option` (governs Step 8's
  caveats). Where both profiles exist, `main_option` comes from `contract-profile.md`
  (Pattern 14 rule 6). If neither states it, ask once before Step 8.

---

## Step 1: Resolve Project, Period, and Previous Valuation Position

1. Resolve the project (Pattern 1).
2. Parse the valuation period from `the user’s request` (Pattern 2) — a valuation period is normally a
   calendar month; confirm only if the input needed non-trivial interpretation.
3. Resolve the **previous valuation date and cumulative position**, in this order: (a) an earlier
   `AP-[NNN]` ref in this conversation — reuse its period-end date and cumulative/retention figures
   rather than re-deriving them; (b) a user-supplied previous valuation date and/or cumulative
   figures (the third `the user’s request` token, or asked for) — cross-check any user-supplied cumulative
   total against the figure Step 4 derives (Pattern 9, ±0.5% tolerance) and flag any material
   mismatch; (c) neither available → treat as the **first application**: previous valuation date =
   start of records, previous cumulative = zero, and state this assumption prominently.
4. Read `commercial-profile.md` and `contract-profile.md` (or their `<project>`-slugged variants)
   per the file convention in `$commercial-profile`. A profile whose `project` field does
   not match is ignored (say so, Pattern 13/14 rule 4).

---

## Step 2: Verify Progress Data Granularity (the Gate)

Reuses the same check as `$asbuilt-programme` Step 2 (Pattern 12) — this measure is only
possible if `dashboardProgress` carries a **date** per row, not just an aggregate total.

1. Call `getReportSchemas` (or inspect the first `dashboardProgress` response) to confirm rows are
   per-date, per-activity records (date, activity, unit, actualQuantity).
2. **Per-date rows confirmed** → proceed to Step 3 with the full measure.
3. **Aggregate-only** (a single cumulative total per activity, no per-date breakdown) → degrade
   explicitly:
   - State plainly: "Quantity this period cannot be computed by cumulative differencing —
     `dashboardProgress` for this project returns aggregate totals only, with no per-date
     breakdown. The priced measure (Steps 4–7) cannot be produced."
   - Offer **narrative-based support only**: scan `dashboardNarrative` for entries dated within the
     period naming each activity (Pattern 10 categories help identify relevant entries) and list
     them, dated and record-ID cited, as qualitative support for a manually-agreed quantity — never
     as a quantity itself.
   - Still produce the prelims line (Step 6) and Option caveats (Step 8), which do not depend on
     per-date progress; label the priced-measure sections "not available this run" rather than
     omitting them silently.

---

## Step 3: Retrieve Data

Make in parallel:

- **3a Progress** — `getCachedReport` (`dashboardProgress`) from the earliest available date through
  the period end. Per Pattern 4, chunk wide ranges month by month and merge.
- **3b Evidence** — `dashboardNarrative` for the period; if it lacks the detail needed, fall back
  to shift records per Pattern 20 (`../../shared/patterns/20-evidence-retrieval.md`).
  Note where a shift record carries attached photos (field + asset reference, per `$photos`)
  so the evidence column can cite "+ photo" where available.
- **3c Working time** — `dashboardShiftTable` for the period and (if prelims run from site start) the
  full history, to establish weeks elapsed.

Apply **Pattern 3** if any of these return no data for the period.

---

## Step 4: Compute Quantities This Period (Visible Cumulative Columns Guardrail)

Same guardrail as `asbuilt-programme` Step 4: never sample or estimate — sum every row.

For each activity:

| Field | Calculation |
|---|---|
| Cum. Actual to Period End | Sum `actualQuantity` across **every** row dated on or before the period-end date |
| Cum. Actual to Previous Valuation Date | Sum `actualQuantity` across every row dated on or before the previous valuation date (zero if first application) |
| **Qty This Period** | Cum. to Period End − Cum. to Previous Valuation Date |

Show both cumulative totals as columns in the output table so the arithmetic is checkable. If a
qty-this-period figure is negative, flag it — "negative movement: check for a data correction or
remeasurement" (Pattern 12 estimate discipline) — never silently present it as ordinary progress.

---

## Step 5: Price the Measure (Pattern 14)

For each activity from Step 4:

- Match against `activity_rates` in the commercial profile (by item name). If matched: value =
  qty this period × rate, cited "rate per commercial profile".
- If the user gives a rate in-conversation instead: cite "user-supplied this session".
- **No match / no profile** → move the line to a **quantities-only annex**: activity, unit, qty
  this period, cumulative, value column reading "rate not in commercial profile" — point once to
  `$commercial-profile`. Never block the rest of the output on missing rates.
- State currency from the profile's `currency` field, or assume the user's stated currency /
  default GBP with the assumption stated once.

---

## Step 6: Prelims Line (Time-Based)

If `prelims.establishment_weekly` is in the commercial profile:

- **Weeks elapsed this period** = period length in calendar days ÷ 7 (state the divisor).
- **Prelims value this period** = weeks elapsed × `establishment_weekly`.
- **Prelims value cumulative** = weeks elapsed since the earliest recorded site date × the same
  weekly rate — state the site-start date used as the basis.

If `prelims` is absent from the profile: report "prelims weeks elapsed: [X] — rate not in
commercial profile" (quantities-only), point to `$commercial-profile`, and continue.

---

## Step 7: Retention and Summary Arithmetic

1. **Gross value this period** = sum of Step 5 priced lines + Step 6 prelims value this period.
2. **Gross cumulative** = sum of Step 5 priced lines at cumulative quantity + Step 6 prelims
   cumulative value. Reconcile against "previous cumulative gross + this period gross" (Pattern 9,
   ±0.5% tolerance) — flag any mismatch rather than silently resolving it.
3. **Retention** = `retention_pct` × gross cumulative (state the % and cite its source — profile
   or, if absent, ask and state the assumption).
4. **Net cumulative** = gross cumulative − retention.
5. **Net due this application** = Net cumulative − previously-applied net (from Step 1's resolved
   previous position).

Summary table: **Previous Cumulative (Gross) | This Period (Gross) | Cumulative (Gross) |
Retention Held | Net Cumulative | Net Due This Application**.

---

## Step 8: Contract-Aware Caveats (Option-Aware)

Read `main_option` per the Profiles note above. At this step, read
`references/option-caveats.md` and apply the matching row
per line item in the priced measure table.

---

## Step 9: Present the Application

Use this structure. Apply **Pattern 8** for the `AP-[NNN]` line (session-local; increment if a
prior `AP` ref exists in this conversation, else `001`).

```
APPLICATION FOR PAYMENT — [Project Name]
Ref: AP-[NNN]
Period: [Start Date] to [End Date]
Previous Valuation Date: [date / "none — first application"]
Contract Option: [A–F / "not confirmed"]
Generated: [today]
```

1. **Summary** — two sentences: total qty lines measured, gross/net values from Step 7, and the
   Option caveat headline from Step 8.
2. **Priced Measure Table** — Activity | Unit | Cum. Previous | Cum. This Period-End | Qty This
   Period | Rate | Rate Source | Value | Option Flag.
3. **Quantities-Only Annex** (Step 5) — omit the section if empty.
4. **Prelims Line** (Step 6).
5. **Retention & Net Summary** (Step 7 table).
6. **Evidence Schedule** — Date | Record ID | Summary | Photo ("yes — [asset ref]" / "none
   attached"), covering the period's key measured lines.
7. **Contract-Aware Caveats** (Step 8, verbatim per Option).
8. **Standing Caveat** — always include, unmodified:

> This is a records-backed measure and draft application for payment, prepared from Gather site
> data, for commercial review — **it is not a certified valuation**. Quantities, prelims, and
> retention arithmetic should be checked and agreed by the commercial manager/QS before formal
> submission. Ref: AP-[NNN] is a session-local sequence number for cross-referencing.

If Step 2 degraded to the aggregate-only path, repeat that limitation here instead of sections 2–3
and present only the narrative-based support list, the prelims line, and the caveats.

---

## Step 10: Shareable HTML Application Document (Generated by Default)

After presenting Step 9, generate a self-contained HTML application document by default — not
an optional extra. Read
`references/html-document.md` for the build steps, data
schema, and skip/fallback conditions.

---

## Related Skills

- `$commercial-profile` — capture the rates this skill prices against
- `$contract-profile` — capture the `main_option` that drives Step 8's caveats
- `$progress` — current-period output, variance and productivity (this skill only prices
  the movement, it does not analyse it)
- `$cost-to-complete` — the forward-looking counterpart to this backward-looking measure
- `$ce-quotation` — price a compensation event rather than the period measure
- `$subcontractor-check` — verify a subcontractor's own application against records
