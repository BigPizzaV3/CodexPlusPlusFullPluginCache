# Step 7: Present the Delay Register — Output Template

Use this **exact structure**. Fill every placeholder `[…]` with data. Do not add, remove, or
reorder sections.

---

```
DELAY ANALYSIS — [Project Name]
Ref: DA-[NNN]
Method: records-based delay register (screening) — not an SCL Protocol delay analysis; for as-planned vs as-built comparison see $asbuilt-programme
Period: [Start Date] to [End Date]
Generated: [Today's Date]
Total Delay Events: [X]
Total Estimated Lost Time: [X] shift-hours of delay ([X] days at [median shift] hrs/day)
```

Lost time is measured in **shift-hours of delay (event duration)**, not person-hours — this is the DA master-register unit under **Pattern 11**. The days figure always states its divisor (the median shift duration for the period).

Apply **Pattern 8 (Report Numbering)** from `../../../shared/patterns/08-report-numbering.md` for the `DA-[NNN]` reference.

This is the **master delay register** (all causes). **Do not sum its total with the AC (access) or WI (weather) registers** — they overlap by design and use different units (AC = person-hours; WI = shift-hours of shortfall vs theoretical maximum). See Pattern 11.

---

### 1. HEADLINE

Write exactly 2 sentences:

> [X] delay events were identified from site records for [Project Name] between [start date] and [end date], totalling an estimated [X] hours ([X] days) of lost productive time. The primary cause of delay is **[top category]**, accounting for [X]% of total lost time ([X] hours across [X] events).

---

### 2. CHRONOLOGICAL DELAY REGISTER

| # | Date | Code | Category | Description | Duration (hrs) | Resources Affected | Confidence | Evidence Ref |
|---|---|---|---|---|---|---|---|---|
| 1 | [date] | [ACC/WEA/DES/CLI/TPU/RES/REW/OTH] | [full name] | [one-sentence description drawn from narrative] | [X] | [X operatives, X plant] | [HIGH/MED/LOW] | [shift record IDs, access records] |

Sort by Date ascending.

For the Description column, use this sentence structure:

> [What happened] — [consequence for works].

Examples:
- "No possession granted — all track works suspended for the full shift."
- "Heavy rainfall from 10:30 — earthworks stood down, drainage gang redeployed to welfare area."
- "Awaiting revised drainage design — standing time for 4-person drainage gang."

---

### 3. CAUSE BREAKDOWN

| # | Category | Code | Events | Total Duration (hrs) | % of Total | Avg Duration (hrs) | Risk Owner |
|---|---|---|---|---|---|---|---|
| 1 | [category] | [code] | [X] | [X] | [X]% | [X] | [Employer/Contractor/Shared/TBC] |
| | **Total** | | **[X]** | **[X]** | **100%** | **[X]** | |

Sort by Total Duration descending.

"Risk Owner" assignment:
- **Employer:** Access/Possession, Client/PM Instruction
- **Design/Information — contract-dependent:** Employer risk on a traditional/employer-design contract (JCT SBC, NEC with Client-designed Scope, FIDIC Red Book). **Reversed to Contractor risk on design-and-build forms** — JCT D&B, NEC where the Contractor designs, and **FIDIC Yellow/Silver Book** — where design and information sit with the Contractor. Mark as **TBC** until the contract and who-designs-what is confirmed; do not default to Employer.
- **Contractor:** Resource Shortage, Rework/Rejection (typically)
- **Shared:** Weather (depends on contract), Third Party/Utility (depends on contract)
- **TBC:** Where category alone is insufficient to determine — note this requires contract review

After the table, write one sentence:

> Of the total [X] hours of delay, approximately [X] hours ([X]%) relate to Employer-risk events, [X] hours ([X]%) to Contractor-risk events, and [X] hours ([X]%) require further contractual assessment.

---

### 4. TIMELINE

| # | Week Commencing | Delay Events | Lost Hours | Primary Cause | Severity |
|---|---|---|---|---|---|
| 1 | [date] | [X] | [X] | [category] | [High >16hrs / Medium 8–16hrs / Low <8hrs] |

Sort by Week Commencing ascending.

After the table, write one sentence:

> Delay events [were concentrated in the week of [date] / were evenly distributed across the period / escalated in the final [X] weeks], suggesting [a specific incident / a systematic issue with [category] / an improving/worsening trend].

---

### 5. KEY OBSERVATIONS

Write exactly 5 bullet points using these templates:

> - **Largest single event:** [Description] on [date] — [X] hours lost affecting [X] resources. Category: [category]. Confidence: [HIGH/MED/LOW].
> - **Most frequent cause:** [Category] with [X] events totalling [X] hours. [One sentence on pattern: "These events [occurred on specific days suggesting a systematic issue / were weather-related and clustered during [period] / appear to be isolated incidents]."]
> - **Recurring pattern:** [Description of any pattern, e.g. "Access delays occurred on [X] of [Y] Mondays, suggesting a systematic possession scheduling issue" / "No recurring pattern identified — delay events appear to be independent."]
> - **Employer vs Contractor risk:** [X]% of lost time is attributable to Employer-risk events and [X]% to Contractor-risk events (context only — entitlement does **not** depend on the share of lost time). [If **any** material Employer-risk event exists, regardless of its percentage share: "[X] Employer-risk event(s) totalling [X] shift-hours are flagged for contractual follow-up — each may independently support a programme extension and/or compensation claim on its own facts, irrespective of the overall split. See `$ce-builder` and resolve the contract via Pattern 5." / If no Employer-risk events at all: "No Employer-risk events were identified; recorded delay is Contractor-risk or TBC — focus on resource planning and quality management, and confirm risk allocation via Pattern 5 before drawing conclusions."] Contractor-risk share is reported for context and does not extinguish entitlement arising from the Employer-risk events.
> - **Data confidence:** [X] of [Y] events are HIGH confidence (corroborated by multiple sources). [X] events are LOW confidence and should be verified before inclusion in formal submissions.
