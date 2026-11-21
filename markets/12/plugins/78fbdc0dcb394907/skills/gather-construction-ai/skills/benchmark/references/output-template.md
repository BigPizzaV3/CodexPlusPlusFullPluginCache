# Output Template — Benchmark Comparison

Use this **exact structure**. Fill every placeholder `[…]` with data. Do not add, remove, or reorder sections. Apply **Pattern 8 (Report Numbering)** from `../../../shared/patterns/08-report-numbering.md`.

---

```
BENCHMARK COMPARISON
Ref: BM-[NNN]
Projects: [Project A], [Project B][, Project C, ...]
Period: [Start Date] to [End Date]
Generated: [Today's Date]
```

---

### 1. HEADLINE

Write exactly 2 sentences:

> [X] projects were benchmarked for the period [start date] to [end date]. **[Best project]** is the top performer overall (rank score [X]), while **[Worst project]** requires attention — [one-sentence reason: lowest productivity / most behind programme / declining trend].

---

### 2. COMPARISON TABLE

| # | Metric | [Project A] | [Project B] | [Project C] | Best |
|---|---|---|---|---|---|
| 1 | Working Days | [X] | [X] | [X] | — (context) |
| 2 | Total Labour Hours | [X] | [X] | [X] | — (context) |
| 3 | Labour Hrs/Working Day | [X] | [X] | [X] | — (context — scale metric, no direction) |
| 4 | Avg Daily Headcount | [X] | [X] | [X] | — (context) |
| 5 | Peak Headcount | [X] | [X] | [X] | — (context) |
| 6 | Output/Working Day | [X] | [X] | [X] | **[project]** if same activity+unit, else "— units differ (unranked)" |
| 7 | Output/Labour Hour | [X] | [X] | [X] | **[project]** if same activity+unit, else "— units differ (unranked)" |
| 8 | Plan vs Actual (Labour) | [X]% | [X]% | [X]% | **[project]** |
| 9 | Plan vs Actual (Progress) | [X]% | [X]% | [X]% | **[project]** |
| 10 | Allocation Accuracy | [X]% | [X]% | [X]% | **[project]** |
| 11 | Trend | [↑/→/↓] | [↑/→/↓] | [↑/→/↓] | — (context) |

Bold the best value only in **ranked** rows (rows 8–10, and rows 6–7 **only** where activity and unit match across projects). Context rows show "—" in the Best column and are never bolded. For output rows where units differ between projects, do not bold any value and mark the Best column "— units differ (unranked)". If >5 projects, split into two tables.

---

### 3. RANKINGS

| Rank | Project | Metrics Ranked (of 5) | Avg Rank Score | Strengths | Weaknesses |
|---|---|---|---|---|---|
| 1 | [project] | [X of 5] | [X] | [top 2 metrics] | [bottom 2 metrics] |
| 2 | [project] | [X of 5] | [X] | [top 2 metrics] | [bottom 2 metrics] |

Only projects ranked on **≥4 of the 5 rankable metrics** receive an overall rank. List any project below that threshold separately as **"insufficient data to rank — ranked on [X] of 5 metrics"** and exclude it from the ordering above.

---

### 4. NARRATIVE SUMMARY

Write exactly 4 sentences:

> **[Best project]** leads the portfolio with the highest [key metric] and a [improving/stable] trend. **[Worst project]** ranks lowest, primarily due to [specific metric at X% vs portfolio average of Y%]. [If any project improving: "[Project] shows the strongest improvement, with [metric] increasing by [X]% over the period." / If all stable: "No significant improvement trends were detected across the portfolio."] [If data gaps: "[X] projects had incomplete data — metrics marked N/A were excluded from rankings." / If no gaps: "All projects had complete data for all metrics."]

---

### Caveats

Always include — do not modify this text:

> **Notes:**
> - Projects may have different scopes, activity types, and complexity — direct comparison has inherent limits.
> - **Shift-pattern comparability:** projects on different shift patterns are not directly comparable. A 24/7 rail-possession project accrues hours and output on a different basis from a Mon–Fri civils project, so scale metrics (labour hours, headcount, shifts) and output-per-day figures can differ for pattern reasons alone, not performance. Confirm the projects are comparable before relying on any ranking.
> - **Output rankings** are valid only between projects performing the **same activity in the same unit**. Output metrics across differing activities/units are reported per project, unranked.
> - Scale metrics (labour hours, headcount, shifts/day) are shown for **context only** — they have no better/worse direction and are not ranked.
> - Metrics marked "N/A" or "No data" were excluded from rankings for that project. Projects ranked on fewer than 4 of 5 rankable metrics are shown as "insufficient data to rank".
> - Trends are based on the selected period only and may not reflect longer-term patterns.
> - Ref: BM-[NNN] is a session-local sequence number for cross-referencing.

---
