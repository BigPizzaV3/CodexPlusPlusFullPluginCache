---
name: subcontractor-check
description: Verify a subbie's claimed hours, output and daywork lines against recorded
  attendance and deliveries; draft a factual response. Not the main contractor's own
  valuation (use valuation).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Subcontractor Check — Application Verification (Ref SV-NNN)

Verify a subcontractor's claimed hours, quantities and daywork lines against Gather records,
and produce a draft response ready for commercial review. Never asserts work was not done —
only what the records do or do not show.

Follow the shared patterns: `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Resolve Project, Subcontractor, and Period

1. Resolve the project using **Pattern 1** from `../../shared/patterns/01-project-resolution.md`.
2. Identify the subcontractor's name from `the user’s request`; confirm with the user if it could match
   a trade or a person rather than a company.
3. Parse the claim period using **Pattern 2**. Default to **last 4 weeks** if not given.
4. Check for `commercial-profile.md` (Pattern 14). If it matches the project, note the
   `subcontract_orders` entry (package, order value, rates basis) for Step 6 pricing. Mismatched
   project → ignore, say so. No profile → proceed quantities-only, point once to
   `$commercial-profile`.
5. Check for a contract profile (Pattern 13) — only needed for the Step 8 pay-less caution. If
   absent, note the unamended-standard-form assumption and continue.

---

## Step 2: Parse and Confirm the Claim

Parse the pasted/dictated claim lines into a table before doing anything else:

| # | Claim Line | Type | Claimed Qty/Hrs | Date(s) |
|---|---|---|---|---|
| 1 | [description] | Hours / Quantity / Daywork | [value + unit] | [date or range] |

Classify each line: **Hours** (labour attendance), **Quantity** (measured activity output), or
**Daywork** (an instructed task claimed time-and-materials).

Show the table back and get the user's confirmation or correction before verifying — a misread
line invalidates every downstream check.

---

## Step 3: Retrieve Supporting Records

Fetch only what the confirmed lines need (e.g. skip delivery notes if no materials are claimed).

**Labour (Hours lines).** `getCachedReport` (`dashboardResourceLabour`). **Pattern 12 gate:**
check (response or `getReportSchemas`) for a company/subcontractor field per row.
- Present → filter to the subcontractor's company, then the claimed trades.
- Absent → **degrade explicitly**: state this workspace's labour data has no company
  attribution, then verify by **trade** (all companies) plus **narrative naming** only — flag
  this in every affected verdict as weaker evidence, never presented as equivalent.

**Progress (Quantity lines).** `getCachedReport` (`dashboardProgress`), filtered to the
package's activities (ask the user which activities the package covers if unclear).

**Narratives (all lines).** As `narrative-search` does: `getCachedReport` (`dashboardNarrative`),
search for the subcontractor's name and trade, recording date, supervisor, and excerpt per hit —
primary support for Daywork lines and the fallback where labour lacks company attribution.

**Delivery notes (material lines).** As `delivery-notes` does: check `getReportSchemas` for a
delivery-capable report first; else fall back to shift records per Pattern 20
(`../../shared/patterns/20-evidence-retrieval.md`). Match delivered
quantities to materials claimed.

Any source returning no data for the period → apply **Pattern 3**, state it plainly; it feeds
the **NO RECORDS** verdict below, not an error.

---

## Step 4: Match Claim Lines to Records and Assign Verdicts

Compare each claimed value to recorded support and assign exactly one verdict:

| Verdict | Meaning |
|---|---|
| **SUPPORTED** | Recorded support within **±5%** of claim (state the tolerance in the output) |
| **PARTIALLY SUPPORTED** | Some support but outside ±5%, or support only from a weaker cross-check (trade-level, not company-attributed) |
| **NOT SUPPORTED BY RECORDS** | Records exist and positively contradict the claim (materially lower hours, no attendance/narrative on claimed dates despite records existing for the period) |
| **NO RECORDS** | No relevant records at all — a **recording gap**, never a rejection; do not infer the work was not done |

**Language discipline (table and letter):** write "records support / partially support / do not
support" or "no records found" — never "they didn't do it", "not done", or any phrasing that
asserts absence of work from absence of records.

| Claim Line | Claimed | Records Show | Variance | Verdict | Evidence Refs |
|---|---|---|---|---|---|
| [description] | [value] | [recorded value, or "none found"] | [+/−, %] | [verdict] | [record IDs / dates] |

`Evidence Refs` cites the specific record (shift ID, narrative date + supervisor, delivery note
ref) behind "Records Show" — never a bare assertion.

---

## Step 5: Daywork Cross-Check

For every Daywork line, cross-check the diary on the **exact claimed dates only** — do not
average across the period.

1. Search narratives on the claimed date(s) for the subcontractor and the claimed task.
2. Only resources the narrative **ties to the task** count as support; attendance alone (no task
   link) is listed as "attendance recorded, task attribution unconfirmed", not folded into
   either verdict direction.
3. Apply Step 4's verdicts unchanged — no narrative and no attendance on the date is **NO
   RECORDS**, not NOT SUPPORTED.

---

## Step 6: Value-at-Variance Summary

Where the commercial profile (Step 1) has an applicable rate — `labour_daywork_rates` for
Hours/Daywork, `activity_rates` for Quantity, or the package `order_value` for context — price
the variance for each non-SUPPORTED line:

| Claim Line | Variance (Qty/Hrs) | Rate | Value at Variance | Source |
|---|---|---|---|---|
| [description] | [+/− value] | [rate] | [£ value] | [commercial profile / user-supplied this session] |

Sum priced lines only; an unrated line shows "rate not in commercial profile" and is excluded
from the sum, not guessed — the total is a floor, and the output says so.

**Pattern 11:** never sum these totals with `delay-analysis` (DA), `access` (AC), or
`weather-impact` (WI) register totals — a daywork/standing-time line here may already sit in one
of those registers under different units and scope; cite the Ref where known instead of adding.

---

## Step 7: Present the Verification Report

```
SUBCONTRACTOR CHECK — [Project Name]
Ref: SV-[NNN]
Subcontractor: [name]
Period: [start date] to [end date]
Generated: [today's date]
```

`[NNN]` follows **Pattern 8** (increment if a prior SV report exists this session, else `001`;
include the session-local caveat line).

1. **Confirmed Claim** — the Step 2 table, as agreed.
2. **Data Basis** — one line per source used (labour company-attributed or trade-only degraded,
   progress, narrative, delivery notes), and any returning no data.
3. **Verification Table** — the Step 4 table.
4. **Value at Variance** — the Step 6 table, or "No commercial profile / no matching rates —
   quantities-only; run `$commercial-profile` to price variances".
5. **Verdict Summary** — one sentence: "[X] of [Y] claim lines are supported, [X] partially
   supported, [X] not supported by records, and [X] have no matching records — a recording gap,
   not a finding that the work was not carried out."

---

## Step 8: Draft Response Letter

Immediately after the report, draft a letter addressed to the subcontractor:

```
DRAFT — SUBCONTRACTOR APPLICATION RESPONSE
Ref: SV-[NNN]
To: [subcontractor]
Re: Application for [period], [project name]
Date: [today's date]
```

Line-by-line, in claim order:

> **[Claim line #]:** [Agree / Query / Withhold pending records] — [one factual sentence quoting
> the record: date, hours/quantity, or narrative excerpt]. [If NO RECORDS: "No record of this
> item has been located to date; please provide supporting evidence (delivery ticket, signed
> attendance sheet, or similar) for review."]

Map verdict → stance: SUPPORTED → Agree; PARTIALLY SUPPORTED → Query (state recorded vs
claimed); NOT SUPPORTED BY RECORDS → Withhold pending records, quoting the contradicting record;
NO RECORDS → Query, requesting evidence — never Withhold on a pure recording gap alone.

Close with this caution, unmodified in substance:

> This letter is a factual comparison against site records for commercial review and is **not**
> a formal pay-less notice. A valid pay-less notice is a distinct contractual step with its own
> content and timing requirements — see `$nec-contracts` (or the applicable contract
> knowledge skill) before withholding any sum. Where the contract profile shows **Y(UK)2**
> selected (or NEC is stated with no profile), the notice must be given no later than the
> prescribed period before the final date for payment — check the Contract Data date and
> `$nec-contracts` for current mechanics before relying on this letter alone.

---

## Caveats

Always include:

> **Notes:**
> - Verification is based on Gather records. Absence of a record is a data gap, not evidence
>   work was not carried out — see **NO RECORDS** above.
> - The ±5% **SUPPORTED** tolerance is a working default — state it explicitly; adjust only if
>   the user specifies a different figure for this project.
> - Where labour has no company attribution, verification fell back to trade and narrative
>   matching only — flagged per line above as weaker evidence.
> - Do not sum this report's Value at Variance total with DA/AC/WI register totals — Pattern 11.
> - This is a draft commercial response, not a formal contractual notice — it needs commercial
>   review before issue, and any withholding must follow the correct pay-less procedure and
>   timescale.
> - Ref: SV-[NNN] is a session-local sequence number for cross-referencing.

---

## Related Skills

- `$labour` — Full labour analysis for the subcontractor's trades over a wider period
- `$delivery-notes` — Deeper delivery/usage reconciliation for materials-heavy claims
- `$narrative-search` — Broader search for subcontractor mentions beyond the claim period
- `$commercial-profile` — Add or update subcontract order values and daywork rates
- `$nec-contracts` — Pay-less notice mechanics and Y(UK)2 timescales where NEC applies
