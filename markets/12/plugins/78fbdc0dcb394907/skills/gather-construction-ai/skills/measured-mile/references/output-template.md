# Output Template: Measured Mile Analysis (measured-mile Step 8)

```
MEASURED MILE ANALYSIS — [Project Name]
Ref: MM-[NNN]
Baseline Period: [Start Date] to [End Date] ([X] working days)
Impacted Period: [Start Date] to [End Date] ([X] working days)
Generated: [Today's Date]
```

---

### 1. HEADLINE

Write exactly 2 sentences:

> Productivity in the impacted period was [X]% lower than the baseline, representing a loss factor of [X]. This equates to [X] [unit] of lost output and [X] additional labour hours attributable to disruption.

---

### 2. SIDE-BY-SIDE COMPARISON

| # | Metric | Baseline | Impacted | Variance % |
|---|---|---|---|---|
| 1 | Working Days | [X] | [X] | — |
| 2 | Total Labour Hours | [X] | [X] | [+/−X]% |
| 3 | Average Daily Hours | [X] | [X] | [+/−X]% |
| 4 | Average Headcount | [X] | [X] | [+/−X]% |
| 5 | Total Output | [X] [unit] | [X] [unit] | [+/−X]% |
| 6 | Output per Labour Hour | [X] [unit]/hr | [X] [unit]/hr | [+/−X]% |
| 7 | Output per Day | [X] [unit]/day | [X] [unit]/day | [+/−X]% |
| 8 | Weekly Rate Range (min–max [unit]/hr) | [min]–[max] | [min]–[max] | — |

Row 8 shows the spread of weekly productivity rates within each period (compute per-week output-per-hour and take the min and max). If the two periods' ranges **overlap**, add a note: "The weekly rate ranges overlap — the apparent loss may partly reflect normal week-to-week variation rather than disruption; treat the point loss factor with caution." This guards against reporting noise as a productivity loss. If weekly granularity is not available, show "—" and note the point comparison carries no dispersion evidence.

---

### 3. DISRUPTION IMPACT

| Metric | Value |
|---|---|
| **Loss Factor** | [X]% productivity reduction |
| **Expected Output (at baseline rate)** | [X] [unit] |
| **Actual Output** | [X] [unit] |
| **Lost Output** | [X] [unit] |
| **Hours at Baseline Rate** | [X] hrs |
| **Actual Hours** | [X] hrs |
| **Additional Hours** | [X] hrs |

After the table, write one sentence:

> At baseline rates, the impacted period should have produced [X] [unit] in [X] hours. The actual [X] [unit] took [X] hours — [X] additional hours ([X]%) attributable to disruption.

---

### 4. PER-ACTIVITY BREAKDOWN

| # | Activity | Unit | Baseline Rate | Impacted Rate | Loss Factor % | Lost Output | Additional Hours |
|---|---|---|---|---|---|---|---|
| 1 | [activity] | [unit] | [X] [unit]/hr | [X] [unit]/hr | [X]% | [X] | [X] |

Sort by Loss Factor descending.

If unavailable: "Per-activity breakdown not available — analysis based on aggregate labour hours and output."

---

### 5. CONFIDENCE ASSESSMENT

| Check | Assessment |
|---|---|
| **Similar activities** | [Yes/Partially/No — detail] |
| **Similar conditions** | [Yes/Partially/No — detail] |
| **Sufficient data** | [Yes/Marginal/No — [X] and [X] working days] |
| **Similar resource levels** | [Yes/No — [X]% headcount difference] |
| **Baseline validated (no recorded disruption)** | [Yes — no disruption in baseline narratives/access / No — baseline shows [disruption]; loss factor is understated] |
| **Learning-curve position** | [Representative steady-state / Early-project — understates loss / Late post-learning — overstates loss] |
| **Overall Confidence** | **[HIGH/MEDIUM/LOW]** |

After the table, write one sentence:

> Data confidence is **[HIGH/MEDIUM/LOW]**. [If HIGH: "Both periods are comparable — the loss factor is reliable." / If MEDIUM: "Broadly valid but [limitation] may affect precision." / If LOW: "[Limitation] significantly affects reliability — treat as indicative only."]

---

### Caveats

Always include — do not modify this text:

> **Important notes on this measured mile analysis:**
> - The measured mile method assumes the baseline period is representative of unimpacted performance. If the baseline was itself partially impacted, the loss factor will be understated (this is checked via the Step 2 baseline validation).
> - Learning-curve position matters: a baseline taken early in the project (crews still ramping up) understates achievable productivity and the loss; a baseline taken at post-learning peak overstates it. A representative steady-state baseline is preferred over the single best period, which is cherry-picking that tribunals reject.
> - This analysis uses data from Gather dashboard reports. If progress data contains only high-level metrics, the analysis is based on labour hour comparison only.
> - The loss factor quantifies the productivity difference but does not by itself prove causation. Cross-reference with `$delay-analysis` to identify what caused the disruption.
> - Seasonal effects (weather, daylight hours) may explain some productivity variation independently of disruption.
> - Ref: MM-[NNN] is a session-local sequence number for cross-referencing.
