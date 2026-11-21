# Output Template — Cost to Complete Forecast

At Step 8, use this structure verbatim (fill every `[…]`). Sections 1, 2, 4, 5, 6 and Caveats are always present; Section 3 is conditional (Method A only — see below).

Use this structure in this order — do not reorder or rename sections. Sections 1, 2, 4, 5, 6 and Caveats are **always present**. **Section 3 (Activity Breakdown) is conditional**: include it only if Method A (activity-based) was used; if Method B or C was used, omit Section 3 entirely and note under Section 2 "Activity breakdown not available — [Method B/C] used." This conditional omission is the **only** permitted deviation from the structure. Fill every placeholder `[…]` with data. Apply **Pattern 8 (Report Numbering)** from `../../../shared/patterns/08-report-numbering.md`.

---

```
COST TO COMPLETE FORECAST — [Project Name]
Ref: CC-[NNN]
Period Assessed: [Start Date] to [End Date]
Generated: [Today's Date]
Forecast Method: [A: Activity-Based / B: Percentage-Based / C: Trend-Based]
```

---

### 1. HEADLINE

Write exactly 2 sentences:

> Based on [Method A/B/C] using data from [start date] to [end date], the estimate at completion (EAC) for [Project Name] is **[X] labour hours**. [If planned baseline available: "This represents a variance of [+/−X] hours ([+/−X]%) against the planned total of [X] hours — the project is [under/over] budget in labour terms." / If no baseline: "No planned baseline is available for comparison — the EAC is presented as an absolute forecast."]

---

### 2. SUMMARY

| Metric | Value |
|---|---|
| **Actual Hours to Date** | [X] hours |
| **Working Days to Date** | [X] |
| **Average Daily Hours** | [X] hours/day |
| **Average Daily Headcount** | [X] |
| **Overall Progress** | [X]% complete |
| **Forecast Remaining Hours** | [X] hours |
| **EAC (Total Hours)** | [X] hours |
| **Planned Total Hours** | [X] hours or "No baseline available" |
| **Variance vs Plan** | [+/−X hours ([+/−X]%)] or "—" |
| **Forecast Method** | [A/B/C] |

---

### 3. ACTIVITY BREAKDOWN

_Include only if Method A was used._

| # | Activity | Unit | Planned Total | Achieved | Remaining | Hours/Unit | Forecast Remaining Hours |
|---|---|---|---|---|---|---|---|
| 1 | [activity] | [unit] | [qty] | [qty] | [qty] | [X] | [X] |
| | **Total** | | | | | | **[X]** |

Sort by Forecast Remaining Hours descending.

After the table, write one sentence:

> The largest remaining effort is [activity] at [X] forecast hours ([X]% of total remaining), followed by [activity] at [X] hours.

---

### 4. TRADE BREAKDOWN

| # | Trade | Hours to Date | % of Total | Daily Avg | Forecast Remaining* |
|---|---|---|---|---|---|
| 1 | [trade] | [X] | [X]% | [X] | [X] |

Sort by Hours to Date descending.

\* **Forecast Remaining per trade is a pro-rata apportionment, not a measured forecast.** Gather provides no per-trade remaining-work basis, so apportion the total Forecast Remaining Hours (from Step 5) across trades **in proportion to each trade's share of hours to date**: `Trade Forecast Remaining = Total Forecast Remaining × (Trade Hours to Date ÷ Total Hours to Date)`. State this method in the output. This assumes the future trade mix matches the mix to date — flag that trades whose work is front- or back-loaded (e.g. commissioning, finishing trades) will not follow this split. If the per-trade split would be misleading for the project's sequencing, mark this column "n/a — no per-trade apportionment basis" and report the total only.

---

### 5. PRODUCTIVITY TREND

| # | Period | Daily Output | Daily Hours | Hours per Unit | Trend |
|---|---|---|---|---|---|
| 1 | First half ([dates]) | [X] | [X] | [X] | — |
| 2 | Second half ([dates]) | [X] | [X] | [X] | [↑ Improving / → Stable / ↓ Declining] |

After the table, write one sentence:

> Productivity is **[improving/stable/declining]** — hours per unit [decreased from X to Y (X% improvement) / remained within ±15% / increased from X to Y (X% degradation)]. [If declining: "If productivity continues to decline, the EAC will increase beyond the current forecast." / If improving: "If the improving trend continues, the actual outturn may be better than forecast."]

**Scenario band (bounds on the EAC).** Using the first-half and second-half hours-per-unit already computed above as the bounding rates, recompute Forecast Remaining Hours (Step 5, Method A) at each rate to give a range around the central EAC:

| Scenario | Rate used (hrs/unit) | Forecast Remaining Hours | EAC (hours) |
|---|---|---|---|
| **Optimistic** (better of the two half-period rates) | [X] | [X] | [X] |
| **Central** (blended/overall rate) | [X] | [X] | [X] |
| **Pessimistic** (worse of the two half-period rates) | [X] | [X] | [X] |

> The EAC sits between **[optimistic] and [pessimistic] hours** depending on whether the recent productivity trend holds — the central forecast is [X] hours. Only compute this band where per-activity progress data (Method A) supports it; if not, state "scenario band not available — insufficient per-activity data".

---

### 6. RISKS TO FORECAST

| # | Risk | Source | Potential Impact | Likelihood |
|---|---|---|---|---|
| 1 | [description] | [narrative/access/trend data] | [+X hours if estimable from the data, otherwise "not quantifiable — monitor"] | [High/Medium/Low] |

Do **not** invent an hours figure for a risk. Quantify the impact **only** where the data supports a defensible derivation (e.g. a measured productivity decline that can be extrapolated, or an access loss with a known duration and crew) — and state that derivation. Where the impact cannot be derived from the available data, write **"not quantifiable — monitor"** (Pattern 12: estimate discipline). For each risk, write one sentence:

> **[Risk]** — [source evidence]. [If estimable: "Based on [stated derivation], if this materialises the EAC could increase by approximately [X] hours ([X]%)." / If not: "The hours impact is not quantifiable from the available data — flag for monitoring rather than a numeric allowance."]

If no risks identified: "No significant risks to the forecast were identified from the available data."

---

### Caveats

Always include — do not modify this text:

> **Important notes on this forecast:**
> - This is a **labour-hours forecast**, not a financial forecast. To convert to cost, apply your own labour rates, plant rates, and overhead percentages.
> - The forecast assumes future productivity will match the rates achieved to date. If conditions change (improved access, design completion, resource changes), the actual outturn will differ.
> - Progress data quality directly affects forecast accuracy. If progress percentages in Gather are high-level estimates rather than measured quantities, the forecast is correspondingly approximate.
> - No allowance is made for scope changes, variations, or compensation events not yet reflected in the programme.
> - This forecast covers direct labour only. Plant, materials, subcontract, and overhead costs are not included.
> - Ref: CC-[NNN] is a session-local sequence number for cross-referencing.

---

