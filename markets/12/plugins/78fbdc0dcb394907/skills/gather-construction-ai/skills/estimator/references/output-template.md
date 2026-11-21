# Output Template — Estimator Rate Card

Use this **exact structure**. Fill every placeholder `[…]` with data. Do not add, remove, or reorder sections. Apply **Pattern 8 (Report Numbering)** from `../../../shared/patterns/08-report-numbering.md`.

---

```
ESTIMATOR RATE CARD — [Project Name]
Ref: ES-[NNN]
Period: [Start Date] to [End Date]
Generated: [Today's Date]
Based on: [X] progress records across [X] activities
```

---

### 1. HEADLINE

Write exactly 2 sentences:

> [X] activities were analysed for [Project Name] over the period [start date] to [end date], producing [X] derived unit rates ([X] high confidence, [X] medium, [X] low). [If planned rates available: "Against planned rates, [X] activities are slower than planned and [X] are faster, with an average variance of [+/−X]%." / If no planned rates: "No planned rates are available for comparison — rates are presented as actuals only."]

---

### 2. RATE CARD

| # | Activity | Unit | Total Output | Total Hours | Rate (hrs/unit) | Rate Range (min–max hrs/unit) | Confidence | Planned Rate | Variance % | Flag |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [activity] | [unit] | [X] | [X] | [X] | [min]–[max] | [HIGH/MED/LOW] | [X or —] | [+/−X% or —] | [Significantly slower >+50% / Slower >+20% / Faster <−20% / —] |

The **Rate Range** column shows the min and max per-record rate (from the Step 5 dispersion check) so each point rate carries its own spread. A wide range on a HIGH count is why an activity may be downgraded.

For any activity cross-referenced to `$measured-mile` or `$progress`, also state the reciprocal in units/hr (= 1 ÷ hrs/unit) in the observations, since those skills express productivity that way.

Sort: HIGH confidence first (by Variance descending), then MED, then LOW at bottom.

If no planned rates available, omit the Planned Rate, Variance, and Flag columns.

---

### 3. SUMMARY STATISTICS

| Metric | Value |
|---|---|
| **Total Activities Analysed** | [X] |
| **High Confidence (≥10 records AND rate ratio <2)** | [X] ([X]%) |
| **Medium Confidence** | [X] ([X]%) |
| **Low Confidence** | [X] ([X]%) |
| **Downgraded for dispersion** | [X] |
| **Activities Faster than Planned** | [X] |
| **Activities Slower than Planned** | [X] |
| **Average Variance** | [+/−X]% |

---

### 4. KEY OBSERVATIONS

Write exactly 3 bullet points:

> - **Largest variance from plan:** [Activity] at [+/−X]% — actual rate [X] hrs/[unit] vs planned [X] hrs/[unit]. [If slower: "This activity is consuming [X]% more labour than planned — investigate whether this reflects site conditions, resource mix, or scope change." / If faster: "This activity is outperforming plan — consider using this rate as a benchmark."]
> - **Best benchmark rate:** [Activity] at [X] hrs/[unit] (= [X] units/hr; HIGH confidence, [X] data points). This is the most efficient rate in the dataset and [can be used for labour-effort forecasting and benchmarking — converting it to a priced rate for a CE valuation requires user-supplied £/hr cost rates / should be validated against site conditions before wider application].
> - **Data quality flag:** [If any suspicious rates: "[Activity] shows [X] hrs/[unit] which is [unusually low/high] — this may indicate [output recorded without corresponding labour / labour not broken down by activity]. Verify before using." / If no flags: "No data quality concerns detected — all rates are consistent with recorded output and labour data."]

---

### Caveats

Always include — do not modify this text:

> **Important notes on these rates:**
> - Rates are derived from recorded data and assume labour hours are correctly attributed to activities. If labour is recorded at shift level but not broken down by activity, rates may be inaccurate.
> - LOW confidence rates (fewer than 5 data points) should not be used for pricing without additional validation.
> - Rates include all labour regardless of role — they do not distinguish between operative, supervisor, and engineer time.
> - Seasonal and site condition factors are not isolated — rates may vary significantly between summer and winter periods.
> - Ref: ES-[NNN] is a session-local sequence number for cross-referencing.

---
