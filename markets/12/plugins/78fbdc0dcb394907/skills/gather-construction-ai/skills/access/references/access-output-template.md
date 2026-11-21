# Step 7: Present Results — Output Template

Use this **exact structure**. Fill every placeholder `[…]` with data. Do not add, remove, or
reorder sections. Apply **Pattern 8 (Report Numbering)** from
`../../../shared/patterns/08-report-numbering.md`.

---

```
ACCESS ANALYSIS — [Project Name]
Ref: AC-[NNN]
Period: [Start Date] to [End Date]
Generated: [Today's Date]
```

---

### 1. HEADLINE

Write exactly 2 sentences:

> [X] possessions were recorded for [Project Name] between [start date] and [end date], with an access efficiency of [X]% and [X] hours total lost time ([X] overrun hours). [Band on **Total Lost Hours as a % of planned hours**, not on the raw efficiency ratio — an efficiency > 100% signals an **overrun regime**, not good performance. If lost hours < 5% of planned **and** no material overruns: "Access performance is **good** — possessions are being delivered close to plan with [X] hours total lost time." / If lost hours 5–20% of planned, or material overruns present: "Access performance shows **moderate disruption** — [X] hours lost across [Y] affected possessions ([X] overrun hours), with estimated standing time of [X] person-hours." / If lost hours > 20% of planned: "Access performance is **poor** — [X] hours lost across [Y] affected possessions, representing [X]% of planned access time." If efficiency > 100%: additionally state "Access efficiency exceeds 100% because possessions are overrunning the planned window — this is an overrun regime, not high performance."]

---

### 2. SUMMARY

| Metric | Value |
|---|---|
| **Total Possessions** | [X] |
| **Full Access** | [X] ([X]%) |
| **Affected** | [X] ([X]%) |
| **Missed** | [X] ([X]%) |
| **Total Planned Hours** | [X] |
| **Total Actual Hours** | [X] |
| **Total Lost Hours (late start + early handback)** | [X] |
| **Total Overrun Hours** | [X] |
| **Access Efficiency** | [X]% [if >100%: "— overrun regime, not high performance"] |
| **Avg Late Handover** | [X] mins |
| **Worst Late Handover** | [X] mins on [date] |
| **Avg Early Handback** | [X] mins |
| **Worst Early Handback** | [X] mins on [date] |
| **Est. Standing Time** | [X] person-hours |

---

### 3. POSSESSION DETAIL

| # | Date | Location | Planned Start | Actual Start | Late (mins) | Planned End | Actual End | Early Handback (mins) | Overrun (mins) | Lost Time | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [date] | [location or —] | [time] | [time] | [X] | [time] | [time] | [X] | [X] | [X hrs] | [Full/Partial/Missed/Overrun] |

Sort by Date ascending. Bold any row with Status = Missed. Late start and early handback are shown separately; Overrun is reported in its own column and is **not** netted against Lost Time.

---

### 4. NON-POSSESSION ACCESS

| # | Date | Type | Planned Window | Actual Window | Lost Time | Notes |
|---|---|---|---|---|---|---|
| 1 | [date] | [type] | [times] | [times] | [X hrs] | [note] |

If no data: "No non-possession access records were returned for this period."

---

### 5. LABOUR IMPACT

| # | Date | Status | Workers on Site | Late Handover (mins) | Est. Standing Time (person-hrs) |
|---|---|---|---|---|---|
| 1 | [date] | [Partial/Missed] | [X] | [X] | [X] |
| | **Total** | | | | **[X]** |

After the table, write one sentence:

> Estimated standing time is [X] person-hours across [X] affected possessions. This assumes workers could not be productively redeployed during delays — actual impact may be lower if alternative work was available.

If labour data unavailable: "Labour impact could not be quantified — labour data is not available for cross-referencing."

---

### 6. PATTERNS AND TRENDS

Write one sentence for each sub-section:

**Day of week:** "[Day] possessions show the highest average lost time at [X] minutes, suggesting [systematic issue]." / "No significant day-of-week pattern detected."

**Trend:** "Access performance is [improving/worsening/stable] — lost time [decreased/increased/averaged] from [X] hrs/week to [X] hrs/week."

**Repeat issues:** For each location/type with ≥3 delays: "⚠️ [Location/type] affected [X] times, losing [X] hours total — systematic issue requiring escalation." / "No repeat issues identified."

---

### 7. CONTRACTUAL RELEVANCE

If total lost hours >0: resolve the contract type using **Pattern 5 (Contract Type Resolution)** from `../../../shared/patterns/05-contract-type-resolution.md`, then cite only the confirmed contract's access/possession clauses from the **Pattern 7** mapping table (`../../../shared/patterns/07-event-to-clause-mapping.md`) (do not list all three contract forms — use the terminology of the applicable contract only). Then write:

> Access delays totalling [X] hours may give rise to entitlement under [the applicable clause(s) from Pattern 7 for the confirmed contract]. Cross-reference with `$delay-analysis` for a formal delay register or `$ce-builder` for a structured claim narrative.

If no lost hours: "All possessions delivered on time — no contractual access issues to report."

---

### Caveats

Always include — do not modify this text:

> **Notes:**
> - Access analysis is based on possession records in Gather. If possessions are not recorded or are recorded inconsistently, the analysis will be incomplete.
> - Standing time estimates assume workers could not be productively redeployed during delays, and — absent shift-level attribution — that the day's headcount relates to the affected possession. Actual impact may be lower.
> - Late handover and early handback are calculated from planned vs actual times. If planned times are approximate, variances may be affected.
> - **Register scope (Pattern 11):** this is the **AC (access) register** and its standing-time figure is measured in **person-hours**. It is a cause-specific deep dive that overlaps by design with the DA (delay-analysis) master register and the WI (weather-impact) register, which use different units. **Do not sum the AC total with DA or WI totals.** Cross-reference the DA register by its Ref number where one exists.
> - Ref: AC-[NNN] is a session-local sequence number for cross-referencing.
