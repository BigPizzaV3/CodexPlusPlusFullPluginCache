# Resource Analysis — Output Template

Load at Step 8. Use this **exact structure**. Fill every placeholder `[…]` with data. Do not
add, remove, or reorder sections.

---

```
RESOURCE ANALYSIS — [Project Name]
Ref: RA-[NNN]
Period: [Start Date] to [End Date]
Generated: [Today's Date]
```

Where `[NNN]` is a zero-padded sequential number. If a previous resource analysis exists in the conversation, increment by 1. Otherwise use `001`.

---

### 1. SUMMARY

Write exactly 3 sentences:

> This analysis covers plant and material resources for [Project Name] from [start date] to [end date]. Of [X] plant items on site, [X] are underutilised or idle, representing [X] hire-days of unproductive cost exposure. Material consumption across [X] tracked types is [steady/increasing/decreasing/mixed], with [X] anomalies detected.

---

### 2. PLANT EQUIPMENT

_If no plant data was returned for this project/period, replace this whole section with: "No plant equipment was recorded for [Project] between [dates]. Plant tracking may not be configured, or no plant was on site — see Step 2." Then continue to Materials._

#### 2.1 Plant Summary

| Metric | Value |
|---|---|
| **Total Plant Items** | [X] |
| **Active (≥60%)** | [X] ([X]%) |
| **Underutilised (≥30% and <60%)** | [X] ([X]%) |
| **Idle (<30%)** | [X] ([X]%) |
| **Long-Idle** | [X] |
| **Average Utilisation** | [X]% |
| **Total Hire-Days** | [X] |
| **Total Used-Days** | [X] |
| **Overall Utilisation** | [X]% (n/a if no days on site) |

#### 2.2 Plant Detail

| # | Description | Type | Days on Site | Days Used | Idle Days | Utilisation % | Status | Flag |
|---|---|---|---|---|---|---|---|---|
| 1 | [item] | [type] | [X] | [X] | [X] | [X]% | [Active/Underutilised/Idle/Long-idle] | [flag text or —] |

Sort by Utilisation ascending (worst first). If >25 items, show all flagged items first, then:

> [X] active items not shown (all ≥60% utilisation). Ask for the full list if needed.

#### 2.3 Cost Saving Opportunities

For each Idle or Long-idle item, write one line:

> **[Item]** — on site [X] days, used [Y] days ([Z]% utilisation). [X] idle hire-days represent unproductive cost. [Recommend off-hire / Review requirement for upcoming works].

If no idle items: "No plant items are classified as idle — no immediate cost saving opportunities identified."

---

### 3. MATERIALS

_If no material data was returned for this project/period, replace this whole section with: "No material usage was recorded for [Project] between [dates]. Material tracking may not be configured, or none was recorded — see Step 3." Then continue to Allocation Variance._

#### 3.1 Material Summary

| Metric | Value |
|---|---|
| **Material Types Tracked** | [X] |
| **Total Usage Records** | [X] |
| **Materials with Anomalies** | [X] |
| **Materials Increasing** | [list] |
| **Materials Decreasing** | [list] |

#### 3.2 Material Detail

| # | Material | Unit | Total Qty | Working Days | Avg Daily | Max Daily | Min Daily | Pattern | Anomaly |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [material] | [unit] | [X] | [X] | [X] | [X] | [X] | [Increasing/Decreasing/Steady/Sporadic] | [Yes/No] |

Sort by Total Qty descending.

#### 3.3 Material Anomalies

For each anomaly, write one line:

> ⚠️ **[Spike/Drop/Zero usage]:** [Material] on [date(s)] — [X] [unit] vs average of [X] [unit]. [Investigate whether this was a planned delivery/pour or a recording error / Check whether work requiring this material has paused or recording has lapsed].

If no anomalies: "No material usage anomalies detected for this period."

---

### 4. ALLOCATION VARIANCE

_Include this section only if allocation data is available. Otherwise state: "Planned allocation data is not available for this project/period. Analysis is based on actual usage only."_

#### 4.1 Plant Allocation

| # | Item/Category | Planned Days | Actual Days | Variance | Variance % | Flag |
|---|---|---|---|---|---|---|
| 1 | [item] | [X] | [X] | [+/−X] | [X]% | [Over >20% / Under >20% / OK] |

For each flagged item:

> [Item] is [over/under]-allocated by [X]% ([X] days variance). [If over: "Review whether the additional plant was programme-driven or indicates a planning error." / If under: "Check if associated work has been delayed or descoped."]

#### 4.2 Material Allocation

| # | Material | Unit | Planned Qty | Actual Qty | Variance | Variance % | Flag |
|---|---|---|---|---|---|---|---|
| 1 | [material] | [unit] | [X] | [X] | [+/−X] | [X]% | [Over >15% / Under >25% / OK] |

For each flagged material:

> [Material] consumption is [over/under] plan by [X]%. [If over: "Potential causes: wastage, rework, scope change, or planning underestimate." / If under: "Check whether associated work is behind programme or material has been substituted."]

---

### 5. RECOMMENDATIONS

List **up to 5** prioritised actions, each grounded in a specific finding above, using this format:

> **[Priority]. [Short title]** (Saving potential: [X hire-days / High / Medium / Low])
>
> [One sentence describing the issue]. [One sentence describing the recommended action]. [One sentence describing the expected benefit].

If the data supports no actions (e.g. all plant is well-utilised, no anomalies, no allocation variance), **state so** rather than padding to a fixed count: "No prioritised actions arise from this period's data — plant utilisation and material usage are within expected ranges." Do not fabricate recommendations to reach a quota.

---

### Caveats

Always include — do not modify this text:

> **Notes:**
> - Plant utilisation is based on days recorded as used vs days on site. If usage is not recorded consistently, figures may understate actual use.
> - Material quantities are as recorded in Gather. Actual consumption may differ if recording is approximate or delayed.
> - Financial costs are not available through Gather. Idle hire-days and material quantities are presented for the user to apply their own rates.
> - Ref: RA-[NNN] is a session-local sequence number for cross-referencing.

---
