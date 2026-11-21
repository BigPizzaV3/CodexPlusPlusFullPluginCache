# Plant & Equipment Report — Output Template

Load at Step 8. Use this **exact structure**. Fill every placeholder `[…]` with data. Do not
add, remove, or reorder sections.

---

```
PLANT & EQUIPMENT REPORT — [Project Name]
Ref: PL-[NNN]
Period: [Start Date] to [End Date]
Generated: [Today's Date]
```

Where `[NNN]` is a zero-padded sequential number. If a previous plant report exists in the conversation, increment by 1. Otherwise use `001`.

---

### 1. SUMMARY

| Metric | Value |
|---|---|
| **Total Plant Items** | [X] |
| **Active (≥60%)** | [X] ([%]) |
| **Underutilised (≥30% and <60%)** | [X] ([%]) |
| **Idle (<30%)** | [X] ([%]) |
| **Overall Utilisation** | [X]% (n/a if total days on site = 0) |
| **Mobilisations This Period** | [X] |
| **Demobilisations This Period** | [X] |
| **Total Idle Hire-Days** | [X] days |

After the table, write exactly 2 sentences:

> Overall plant utilisation for the period is [X]%, with [X] of [Y] items classified as active. [X] items are idle or underutilised, representing [X] hire-days of unproductive cost exposure.

---

### 2. PLANT REGISTER

| # | Description | Category | Days on Site | Days Used | Idle Days | Utilisation % | Status | Movement |
|---|---|---|---|---|---|---|---|---|
| 1 | [item] | [type] | [X] | [X] | [X] | [X]% | [Active/Underutilised/Idle] | [Present at start/Mobilised/Demobilised/Continuous] |

Sort by Utilisation ascending (worst first).

---

### 3. MOVEMENTS

#### 3.1 Mobilised This Period

**Utilisation Since** is defined as Days Used ÷ **days since mobilisation** (calendar days from the mobilisation date to the period end, inclusive), expressed as a percentage. Render "n/a" if days since mobilisation = 0.

| # | Item | Category | Date Mobilised | Utilisation Since | Purpose |
|---|---|---|---|---|---|
| 1 | [item] | [type] | [date] | [%] | [supporting activity name, if identifiable from narratives] |

For each mobilisation, write one sentence:

> [Item] was mobilised on [date] [to support [activity] / for [purpose from narrative]]. Since mobilisation, utilisation is [X]% — [satisfactory / below expectations, review requirement].

#### 3.2 Demobilised This Period

| # | Item | Category | Last Recorded | Utilisation Before Leaving | Reason |
|---|---|---|---|---|---|
| 1 | [item] | [type] | [date] | [%] | [if identifiable from narratives] |

If no movements: "No plant movements recorded during this period."

---

### 4. UTILISATION BY CATEGORY

| # | Category | Items | Avg Utilisation % | Active | Underutilised | Idle | Trend |
|---|---|---|---|---|---|---|---|
| 1 | [type] | [count] | [%] | [count] | [count] | [count] | [Improving/Stable/Declining] |

Sort by Avg Utilisation ascending.

_If only one category (or no category data) is present, state: "All plant falls in a single category — category comparison is not meaningful for this period." and skip the sentence below._

After the table, write one sentence:

> The [lowest-utilisation category] category has the poorest utilisation at [X]%, with [X] of [Y] items idle — [this warrants review / this is expected given [reason if identifiable]].

---

### 5. PLANT ISSUES

| # | Date | Issue Type | Item | Detail (narrative excerpt) |
|---|---|---|---|---|
| 1 | [date] | [Breakdown/Waiting/Wrong plant/Unavailable] | [item if identifiable] | "[quoted narrative excerpt]" |

If no issues: "No plant-related issues identified in diary narratives for this period."

For each breakdown, write one sentence:

> [Item] was reported as [issue type] on [date]. [Current status if known from later narratives, otherwise: "Status unknown — confirm whether repair has been completed or a replacement is required."]

---

### 6. RECOMMENDATIONS

Use these three sub-sections. Each lists **only the items that actually qualify** (up to all of them) — do not fabricate recommendations to reach a count. If a sub-section has no qualifying items, use its stated "no items" line. If none of the three sub-sections has any qualifying item, add a closing line: "No plant actions arise from this period's data — all equipment is adequately utilised with no breakdowns." For each qualifying item, use the prescribed sentence format.

#### 6.1 Off-Hire Candidates

For each Idle item:

> **[Item]** — on site [X] days, used [Y] days ([Z]% utilisation). Recommend off-hire unless required for upcoming works within the next [7/14] days. Estimated saving: [X] hire-days.

If no idle items: "No items recommended for off-hire — all equipment is at or above 30% utilisation."

#### 6.2 Utilisation Review

For each Underutilised item:

> **[Item]** at [X]% utilisation — review whether [a smaller/alternative item would be more cost-effective / this item can be shared with [other project if known] / the activity requiring this item is due to ramp up].

If no underutilised items: "No items flagged for utilisation review."

#### 6.3 Breakdown Follow-Up

For each breakdown identified in Section 5:

> **[Item]** reported as [issue] on [date] — confirm repair status and whether a replacement is required. If the item remains out of service, consider off-hire to avoid standing charges.

If no breakdowns: "No breakdowns recorded — no follow-up actions required."

---

### 7. ALLOCATION VARIANCE

_Include this section only if allocation data from Step 2b is available. Otherwise omit entirely._

**Divide-by-zero guard (Pattern 12).** Variance % = (variance ÷ planned) × 100. Where **planned = 0**, render Variance % as **"n/a"** with a data-quality flag — never a number or an error — and describe the item as "actual with no plan".

| # | Item/Category | Planned Days | Actual Days | Variance | Variance % | Flag |
|---|---|---|---|---|---|---|
| 1 | [item] | [planned] | [actual] | [+/−] | [%] | [Over/Under/OK] |

Flag items over-allocated (>20% above plan) or under-allocated (>20% below plan).

For each flagged item, write one sentence:

> [Item] is [over/under]-allocated by [X]% — [review whether additional plant was necessary / check if associated work has been delayed or descoped].

---

### Caveats

Always include — do not modify this text:

> **Notes:**
> - This report is based on plant data recorded in Gather. Items not recorded in shift diaries will not appear.
> - Utilisation is based on days recorded as used vs days on site. If usage is not recorded consistently, utilisation figures may understate actual use.
> - Financial costs (hire rates, standing charges) are not available through Gather. Idle hire-days are presented as a quantity — apply your own rates to calculate cost.
> - Movements (mobilisations/demobilisations) are inferred from first/last recorded dates. Actual mobilisation dates may differ if recording was delayed.
> - Ref: PL-[NNN] is a session-local sequence number for cross-referencing. It does not replace the project's own report numbering.
