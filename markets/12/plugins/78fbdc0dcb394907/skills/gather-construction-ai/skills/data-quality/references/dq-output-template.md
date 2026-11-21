# Data Quality Report — Output Template

Loaded at Step 11 (full-run report render). Use this **exact structure**. Fill every
placeholder `[…]` with data. Do not add, remove, or reorder sections.

---

```
DATA QUALITY REPORT — [Project Name]
Ref: DQ-[NNN]
Period: [Start Date] to [End Date]
Generated: [Today's Date]
```

Where `[NNN]` is a zero-padded sequential number. If a previous data quality report exists in the conversation, increment by 1. Otherwise use `001`.

---

### 1. OVERALL SCORE

| # | Check | Weight | Score (0–100) | Status |
|---|---|---|---|---|
| 1 | Shift Coverage | 25% | [X] | [Good/Fair/Poor] |
| 2 | Narrative Completeness | 25% | [X] | [Good/Fair/Poor] |
| 3 | Resource Recording | 25% | [X] | [Good/Fair/Poor] |
| 4 | Progress Recording | 25% | [X] | [Good/Fair/Poor] |
| | **Overall** | **100%** | **[weighted avg]** | **[Good/Fair/Poor]** |

Scoring thresholds — apply consistently (these bands match the Data Assurance agent's Pass/Conditional/Fail rubric):
- **Good** (85–100): Comprehensive; suitable for commercial analysis and claims evidence
- **Fair** (60–84): Usable with caveats; fix the listed gaps before high-stakes analysis
- **Poor** (0–59): Significant gaps; analysis reliability is compromised

Sub-score formulas — use these so repeated runs on the same data produce the same score:
- **Shift Coverage** = (days with at least one shift record ÷ expected working days) × 100
- **Narrative Completeness** = 0.6 × (% of records with a narrative) + 0.3 × min(average narrative word count ÷ 40, 1) × 100 + 0.1 × (100 − % boilerplate/duplicate narratives)
- **Resource Recording** = (records with labour data ÷ total records) × 100
- **Progress Recording** = (days with progress data ÷ expected working days) × 100

**Access recording (Section 9), Cross-source consistency (Section 8), the Per-Supervisor Quality Breakdown (Section 6), and the Quality Trend (Section 7) are all advisory-only — they are reported but do not feed the weighted score.** Rationale: access/possession is not configured on every project (its absence is often legitimate, not a data gap); consistency findings are qualitative flags rather than a coverage ratio; and the per-supervisor and trend sections re-slice the same four scored metrics by supervisor and by time chunk rather than introducing new measurements. Folding any of these into a fixed weighting would distort scores across projects with different setups or double-count data already in the four-check score. They are surfaced in their own sections for action but excluded from the score.

**Sampling caveat (state in the output):** the four scored checks use dashboard-report aggregates for the whole period, but any **field-level** statistics (e.g. average narrative word count, boilerplate detection, per-field completeness) come from the **single 25-record `getShiftRecords` page** sampled in Step 2 — this is a sample, not the population. Whenever a figure is derived from that page, label it, e.g. "based on a sample of 25 records" — do not present a 25-record field statistic as if it covered every record in the period.

After the table, write exactly 2 sentences:

> Data quality for [Project Name] over this period is **[Good/Fair/Poor]** with an overall score of [X]/100. [If Good: "The data is suitable for commercial reporting, delay analysis, and claims preparation." / If Fair: "The data is usable but gaps in [weakest area] should be addressed to strengthen commercial and claims analysis." / If Poor: "Significant gaps in [weakest area] and [second weakest area] undermine the reliability of analysis — immediate action is recommended."]

---

### 2. SHIFT COVERAGE

| Metric | Value |
|---|---|
| **Expected Working Days** | [X] |
| **Days with Records** | [X] |
| **Coverage** | [X]% |
| **Supervisors Active** | [X] |
| **Avg Records per Supervisor** | [X] |

**Gap Days:**

If gaps exist, list them:

| # | Date | Day | Notes |
|---|---|---|---|
| 1 | [date] | [Monday/Tuesday/…] | [Weekday with no record] |

If no gaps: "Full coverage — shift records exist for every expected working day in the period."

After the table, write one sentence — use the flag lookup table (workflow.md Step 3) for the wording.

---

### 3. NARRATIVE QUALITY

| Metric | Value |
|---|---|
| **Records with Narratives** | [X] of [Y] ([X]%) |
| **Average Word Count** | [X] words |
| **Very Short (<20 words)** | [X] records ([X]%) |
| **Potential Boilerplate** | [X] records ([X]%) |

After the table, write one sentence — use the flag lookup table (workflow.md Step 4).

---

### 4. RESOURCE RECORDING

| # | Data Type | Days Recorded | Coverage % | Items/Types | Status |
|---|---|---|---|---|---|
| 1 | Labour | [X] of [Y] | [X]% | [headcount range] | [Good/Fair/Poor] |
| 2 | Plant | [X] of [Y] | [X]% | [item count] | [Good/Fair/Poor] |
| 3 | Materials | [X] of [Y] | [X]% | [type count] | [Good/Fair/Poor] |

For each data type with coverage below 80%, write one sentence — use the flag lookup table (workflow.md Step 5). If all ≥80%: "Resource recording across labour, plant, and materials is at or above 80% — sufficient for reliable analysis."

---

### 5. PROGRESS RECORDING

| Metric | Value |
|---|---|
| **Activities Tracked** | [X] |
| **With Planned Targets** | [X] of [X] ([X]%) |
| **With Zero Actual** | [X] |
| **Update Frequency** | [Daily/Weekly/Sporadic] |

After the table, write one sentence — use the flag lookup table (workflow.md Step 6).

---

### 6. PER-SUPERVISOR QUALITY BREAKDOWN (ADVISORY — not scored)

| Supervisor | Records | % with Narrative | Avg Narrative Words | Assessment |
|---|---|---|---|---|
| [name] | [X] | [X]% | [X] / "n/a" | [assessment phrase, or "—, sample too small" if Records < 5] |

After the table, write one sentence:

> This breakdown is for coaching, not blame — it shows which supervisors would benefit from a conversation about recording habits, not whose records are less trustworthy. Narrative length is a proxy for engagement, not a measure of usefulness — treat thin narratives as a prompt to ask more, not as a defect in isolation.

---

### 7. QUALITY TREND (ADVISORY — not scored; may be omitted)

If fewer than 3 usable chunks exist (Step 9's small-sample guard), omit this section entirely and state: "The selected range is too short for a reliable trend."

Otherwise:

| Chunk | Coverage % | Narrative % |
|---|---|---|
| [week/month label] | [X]% | [X]% |

After the table, write one sentence:

> Recording quality over this period is **[improving/stable/declining]** [one clause naming the driver, e.g. "driven by rising narrative completion in the later weeks" or "held back by a coverage dip mid-period"].

---

### 8. CONSISTENCY ISSUES

For each inconsistency found in Step 10, use this format:

| # | Issue | Dates Affected | Severity | Detail |
|---|---|---|---|---|
| 1 | [Labour vs shifts mismatch / Progress without labour / Narrative mentions unrecorded event] | [date(s)] | [High/Medium/Low] | [one-sentence explanation] |

If no inconsistencies: "No cross-source consistency issues detected."

---

### 9. ACCESS RECORDING (ADVISORY — not scored)

| Metric | Value |
|---|---|
| **Possessions Recorded** | [X] |

If zero access data: "No access/possession data recorded. If this project operates under possessions or access windows, this gap should be addressed — access performance is critical for delay analysis and claims. If the project does not operate under possessions, this is expected and not a data gap."

If access data exists, write one sentence:

> [X] possessions are recorded for the period. [If recording appears consistent: "Access recording appears consistent." / If sparse relative to the project's possession regime: "Access records appear sparse — confirm all possessions are being logged."]

---

### 10. RECOMMENDATIONS

List exactly 3–5 prioritised actions. Use this exact format for each:

> **[Priority number]. [Short title]** (Impact: [High/Medium/Low])
>
> [One sentence describing the gap]. [One sentence describing the specific action to take]. [One sentence describing the benefit: "This will improve [specific skill/analysis] by [specific improvement]."]

Example:

> **1. Add narratives to all shift records** (Impact: High)
>
> [X]% of records lack narratives, which are the primary source for delay registers and event identification. Supervisors should record 2–3 sentences per shift covering: works undertaken, issues encountered, and instructions received. This will improve `$delay-analysis`, `$events`, and `$narrative-search` reliability.

---

After the Recommendations section, if this run is **not** already in Review Mode, add one sentence advertising it:

> Run `$data-quality [project] [range] review` for a record-level punch-list of exactly which records need fixing.

---

### Caveats

Always include — do not modify this text:

> **Notes:**
> - This assessment is based on what is visible through the Gather API. Some data may be recorded in Gather but not exposed through the dashboard reports.
> - "Expected working days" assumes a Monday–Friday working pattern. Adjust if the project operates a different shift pattern.
> - Field-level statistics (narrative word count, boilerplate, per-field completeness) are drawn from a **sample of up to 25 individually fetched records**, not the full population — treat them as indicative and read them alongside the stated sample size.
> - Access recording, cross-source consistency, the per-supervisor breakdown, and the quality trend are reported for action but are **advisory-only** — they do not contribute to the weighted quality score.
> - The quality score is indicative — it highlights gaps but does not assess the accuracy of the data that is recorded.
> - Ref: DQ-[NNN] is a session-local sequence number for cross-referencing. It does not replace the project's own report numbering.
