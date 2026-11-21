---
name: rate-library
description: Portfolio labour-norms library — sweeps recorded output rates (hrs/m,
  hrs/m2, hrs/m3, hrs/nr) across your projects into a versioned local library with
  per-norm provenance, compared against user-supplied tender norms. Hours only, no
  money.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Tender-Truth Rate Library (Ref RL-NNN)

`$estimator` derives labour-hour unit rates for **one** project. This skill sweeps the
**portfolio** and persists the result: what your sites actually achieve, in hrs/unit, versioned
run to run, so tendering can bid on achieved norms instead of guessed ones. Follow the shared
patterns: project resolution
(Pattern 1, `../../shared/patterns/01-project-resolution.md`), date parsing (Pattern 2, `../../shared/patterns/02-date-range-parsing.md`), pagination/call-volume warnings (Pattern 4, `../../shared/patterns/04-pagination-rate-limits.md`), and report
numbering (Pattern 8, `../../shared/patterns/08-report-numbering.md`).

**Scope note:** hours only. This is a labour-hour rate library, not a priced rate card — money
lives in `commercial-profile.md` (Pattern 14) and is never written here. Where a rate needs
pricing (a tender build-up, a CE valuation), the user supplies £/hr separately.

---

## Step 1: Scope — Which Projects, Which Window

1. Resolve the current project (Pattern 1). **Default sweep set = current project + up to 3
   comparable projects the user names** (by name, or "similar rail/highways/building work" —
   confirm the shortlist against `getMyProjects`). This default needs no extra confirmation.
2. **Wider than 4 projects** (an explicit longer list, or "all projects" / "the full portfolio")
   → warn before fetching: each project costs **3 `getCachedReport` calls**
   (`dashboardProgress`, `dashboardAllocation`, `dashboardResourceLabour` — the estimator Steps
   2–4 method), so N projects is **3 × N calls**. State the count and ask: "Sweeping [N]
   projects will make approximately [3×N] API calls. Proceed, or narrow the list to the default
   4?"
3. **Non-interactive runs** requesting a wider-than-default sweep: cap at the **3 most recently
   active projects** (ranked by most recent shift-record activity) plus the current project, and
   state the cap: "Non-interactive run — capped at [current project] + 3 most recently active of
   [N] named; re-run interactively to sweep others."
4. **Window:** parse `the user’s request` using Pattern 2. Unlike most skills' 4-week default, a
   portfolio norms sweep needs a longer look-back to accumulate enough shift records per
   activity — **default to the trailing 6 months** when no range is given, and state this
   override explicitly whenever the default applies.

---

## Step 2: Per-Project Norms — the Estimator Method, Swept

For each confirmed project, derive candidate norms using the `$estimator` method (that
skill's Steps 2–5): `dashboardProgress` for output quantities, `dashboardAllocation` and
`dashboardResourceLabour` for hours (recorded-labour precedence over allocated, per that
skill's hours-source rule), and the zero/near-zero output guard (Pattern 12).

**Qualification gate:** only activities with **both** a quantity record and an hours record in
the window qualify for a norm. An activity with one but not the other is listed as "quantity
only — no hours to derive a rate" or "hours only — no output to derive a rate", never
defaulted to zero or skipped silently.

**Records basis (rate-library's own threshold — distinct from estimator's HIGH/MED/LOW
confidence tiers):** for every norm, state the number of **distinct shift records** underlying
its quantity and hours data. Norms derived from **fewer than 10 shift records are flagged LOW
BASIS** next to the rate wherever it appears — in the per-project table, the consolidated
table, and the written library file. A LOW BASIS norm is never silently pooled into a range or
average without the flag travelling with it.

---

## Step 3: Consolidate Across Projects

For each activity type appearing in more than one project's Step 2 output:

1. **Side-by-side table** — one column per project, each cell showing that project's hrs/unit
   rate and its records-count/LOW BASIS flag.
2. **Range** — the min–max across projects' per-project rates (not a recompute from pooled raw
   data — the range of the already-derived project rates).
3. **Pooled average** — only where the **unit matches exactly** across every contributing
   project (m vs m vs m; never m vs m² vs m³) — labelled with its basis: total shift records
   pooled and which projects contributed.

**Never blend norms across different units, or across loosely-matched activity names, without
confirmation.** Where activity names differ across projects but plausibly describe the same
work (e.g. "Pier Construction (Piers 3–5)" vs "Pier Construction Piers 6–8"), **propose the
match and have the user confirm or reject it** before consolidating — the same discipline as
the programme-import activity mapping (Pattern 15). Rejected or unconfirmed matches are kept
**per project, unconsolidated**.

**Non-interactive runs:** consolidate **exact activity-name matches only**, and state this:
"Non-interactive run — only exact activity-name matches were consolidated; near-matches are
listed per project, unconsolidated, for interactive confirmation."

---

## Step 4: Tender Comparison

If the user has supplied tender norms this session (pasted figures), or the existing
`estimating/rate-library.md` carries a **Tender Norms** section from a previous run, build a
comparison table: tender norm vs achieved range (Step 3) vs delta. State the delta both in
hrs/unit and as a percentage, and note whether the tender norm sits inside or outside the
achieved range.

**No tender norms supplied or on file → skip this section and say so plainly.** Never invent a
"typical industry norm" to fill the gap — an absent tender norm is "no tender norm supplied",
not a benchmark substitute.

---

## Step 5: Write `estimating/rate-library.md`

**File convention:** `estimating/rate-library.md` in the working directory. Human-readable
markdown, containing:

- **Provenance header** — projects swept, window (from Step 1), generated date (**from the run
  context — never invented**), and the records-count basis convention used.
- **Achieved norms table** — per project, per activity: unit, rate, shift-records basis, LOW
  BASIS flag where applicable.
- **Consolidated table** — the Step 3 ranges, pooled averages (with basis), and which
  cross-project matches were confirmed.
- **Confirmed activity-name mappings** — the canonical activity name against each project's own
  wording, as confirmed in Step 3.
- **Tender Norms (user-supplied)** — if any were supplied this run (Step 4), so a later run can
  read them back.

**Overwrite discipline:** if `estimating/rate-library.md` already exists, show its existing
provenance (prior sweep date(s), projects, window) and ask: replace it, or **append** — a new
dated section below the existing ones, preserving history so norms are versioned run to run.
**Non-interactive runs default to append** (not replace, unlike a cost-ledger snapshot — the
whole point of this file is a version history of achieved norms over time): state "Non-
interactive run — appended a new dated section; prior sweeps preserved below" and continue.

**Sensitivity reminder (state once, every write):** this file is competitive data — your
achieved labour norms are commercially sensitive. Keep it local, out of shared repositories
(add to `.gitignore` where relevant), and never circulate it to the other party or a
subcontractor — the same handling as Pattern 14 rule 5.

---

## Step 6: Report

Apply Pattern 8 for the `RL-[NNN]` ref (session-local; increment on a prior `RL` ref, else 001).

```
RATE LIBRARY SWEEP
Ref: RL-[NNN]
Projects swept: [list, or "3 most recently active (non-interactive cap)"]
Window: [Start Date] to [End Date]
Generated: [Today's Date, from run context]
```

1. **HEADLINE** — 2 sentences: how many projects/activities were swept, how many norms
   qualified, how many are LOW BASIS.
2. **PER-PROJECT NORMS** — the Step 2 tables, one per project, each rate carrying its
   shift-records basis and LOW BASIS flag where it applies.
3. **CONSOLIDATED NORMS** — the Step 3 side-by-side/range/pooled-average table, and the
   confirmed (or non-interactive exact-only) activity-name mappings.
4. **TENDER COMPARISON** — the Step 4 table, or "No tender norms supplied — this section is
   skipped. This is not a substitute for a benchmark; no industry-typical figure has been
   invented in its place."
5. **LOW BASIS FLAGS** — a consolidated list of every norm with fewer than 10 shift records,
   restated plainly so none are missed in the tables above.
6. **WHAT THIS UNLOCKS** — `$estimator` can now cite this library instead of deriving
   from scratch each time; the next tender build-up bids on achieved norms, not assumed ones.
7. **CAVEATS** — hours only, no monetary rates (money lives in `commercial-profile.md`); the
   sensitivity reminder (Step 5); a LOW BASIS norm should not be relied on for a tender bid
   without further corroboration; Ref: RL-[NNN] is a session-local sequence number for
   cross-referencing.

---

## Hard Rules

1. **Hours only — never a monetary rate.** £/hr, daywork rates, and priced norms belong in
   `commercial-profile.md` (Pattern 14), never in this file.
2. **No cross-unit or fuzzy-name pooling without confirmation.** Units must match exactly for a
   pooled average; activity-name matches across projects are proposed and confirmed, never
   assumed (non-interactive: exact names only).
3. **Low-basis norms are always flagged** — fewer than 10 shift records is never silently
   pooled or presented as equivalent to a well-evidenced norm.
4. **No invented industry norms.** Absent a user-supplied tender norm, the tender-comparison
   section is skipped and says so — never filled with a "typical" figure.
5. **The file is competitive data.** State the keep-local/out-of-shared-repos reminder every
   time it is written (Pattern 14 rule 5 handling).
6. UK English throughout.

---

## Related Skills

- `$estimator` — the single-project method this skill sweeps and generalises; can cite
  this library once it exists
- `$benchmark` — portfolio performance comparison (productivity, utilisation, progress)
  alongside this library's norms
- `$labour` — the underlying labour-hours breakdown behind any norm's numerator
- `$progress` — the underlying output-quantity data behind any norm's denominator
