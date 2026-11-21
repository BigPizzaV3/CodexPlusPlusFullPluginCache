# Output Template: Programme Health Summary (programme Step 8)

## Step 8: Present the Programme Health Summary

Use this **exact structure**. Fill every placeholder `[…]` with data. Do not add, remove, or reorder sections. Apply **Pattern 8 (Report Numbering)** from `../../../shared/patterns/08-report-numbering.md`.

---

```
PROGRAMME ANALYSIS — [Project Name]
Ref: PM-[NNN]
Period: [Start Date] to [End Date]
Generated: [Today's Date]
Programme Health: [ON TRACK / AT RISK / BEHIND]
```

---

### 1. HEADLINE

Write exactly 2 sentences:

> Programme health for [Project Name] is **[On Track/At Risk/Behind]** — [X] of [Y] activities are on or ahead of programme, with overall progress at [X]% against a planned [X]%. [If On Track: "No activities require immediate intervention." / If At Risk: "[X] activities are behind by 5–20%, most significantly [activity] at [−X]% variance." / If Behind: "[X] activities are significantly behind (>20%), with [activity] at [−X]% variance requiring urgent intervention."]

---

### 2. PROGRAMME STATUS

| Metric | Value |
|---|---|
| **Overall Progress** | [X]% actual vs [X]% planned |
| **Working Days in Period** | [X] |
| **Working Days Lost (Access)** | [X] |
| **Net Effective Working Days** | [X] |
| **Activities On Track/Ahead** | [X] of [Y] |
| **Activities Behind** | [X] of [Y] |
| **Activities Critical** | [X] of [Y] |

Programme health thresholds:
- **On Track:** All activities within ±5% of plan
- **At Risk:** Any activity 5–20% behind, or run rate ratio <0.85
- **Behind:** Any activity >20% behind, or overall progress >10% behind plan

---

### 3. ACTIVITY BREAKDOWN

| # | Activity | Unit | Planned | Actual | Variance | Var % | Status | Run Rate (/day) | Required Rate (/day) | Forecast Finish |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [activity] | [unit] | [qty] | [qty] | [+/−X] | [X]% | [Ahead/On Track/Behind/Critical] | [X] | [X] | [date] |

Sort by Status: Critical → Behind → On Track → Ahead. Bold Critical rows.

---

### 4. ACTIVITIES AT RISK

For each Behind or Critical activity, write one sentence:

> 🔴/🟡 **[Activity]** — [X] days behind programme. Current rate [X] [unit]/day vs required [X] [unit]/day (ratio [X]). [Cause: access restrictions accounted for [X] of [Y] days / productivity shortfall / resource under-manning / cause unknown — investigate with `$delay-analysis`].

If none: "No activities are behind programme."

---

### 5. ACCESS IMPACT

| Metric | Value |
|---|---|
| **Possessions Requested** | [X] |
| **Possessions Granted** | [X] |
| **Missed/Cancelled** | [X] |
| **Working Days Lost** | [X] |

After the table, write one sentence:

> Access restrictions account for [X] of the [Y] working days of delay across all behind-programme activities. [If significant: "This is an Employer-risk impact — cross-reference with AC-[NNN] (if available) for detailed access analysis." / If minimal: "Access is not a significant contributor to programme delay in this period."]

If no access data: "No access/possession data available — programme analysis is based on progress data only."

---

### 6. RUN RATE ANALYSIS

**Conditional (Pattern 12):** Required Rate and Ratio depend on a planned finish date, which the API does not provide. If planned finish dates are **present** in the data, use the full table. If they are **absent**, drop the Required Rate, Ratio, and Assessment columns and present run rates only — do not fill placeholder values.

If planned finish dates are present:

| # | Activity | Current Rate | Required Rate | Ratio | Assessment |
|---|---|---|---|---|---|
| 1 | [activity] | [X] [unit]/day | [X] [unit]/day | [X] | [On track / Needs acceleration / Critical] |

Thresholds: On track ≥1.0, Needs acceleration 0.7–0.99, Critical <0.7. Where the ratio denominator is 0, render "n/a" (Pattern 12).

If planned finish dates are absent, use instead:

| # | Activity | Current Rate | Best Sustained Rate |
|---|---|---|---|
| 1 | [activity] | [X] [unit]/day | [X] [unit]/day |

> Required rates and run-rate ratios are not shown — the API provides no planned finish dates, so remaining programme duration is unknown (Pattern 12). Rates are presented as observed run rates only.

---

### 7. FORECAST SUMMARY

**Conditional (Pattern 12).** All forecasts are anchored to the **data cut-off date [end date]** (the last date with recorded output), not today. Three lenses are presented side by side — run-rate Scenario A, run-rate Scenario B, and the earned-schedule extrapolation (5d) — and are **never averaged into one number**; each carries its own assumption.

If planned finish dates are present:

| # | Activity | Planned Finish | Forecast Finish (A — current rate) | Forecast Finish (B — best sustained) | Forecast Finish (C — earned-schedule) | Variance vs Plan (A) | Status |
|---|---|---|---|---|---|---|---|
| 1 | [activity] | [date] | [date] | [date] | [date, or "— no baseline mapping (Pattern 15)"] | [+/−X days] | [Early/On Time/Late] |

Column C is labelled **"earned-schedule extrapolation — trend-based, not critical-path"** wherever it appears, and is populated only for activities with a confirmed Pattern 15 baseline mapping (5d); unmapped activities show "—" with the reason.

After the table, write one sentence per lens — do not blend them into a single verdict:

> [X] of [Y] activities are forecast to finish on time or early on the current-rate (Scenario A) basis. [If any late: "The most significant forecast delay is [activity] at [+X] days late — at current rates, completion is forecast for [date] (best sustained rate: [date]) against a planned [date]." / If all on time: "All activities are forecast to complete within programme."]
>
> On the earned-schedule extrapolation (mapped activities only): [X] of [Y] mapped activities show SPI(t) ≥ 1.0 (ahead or on pace by earned measure). [If any behind: "[activity] shows SPI(t) [X] — earned-schedule extrapolation forecasts completion [date], [+/−X] days vs the stored baseline finish." / If none mapped: "No activities carry a confirmed baseline mapping — the earned-schedule lens is not available this run (Pattern 15)."] This lens is trend-based, not a critical-path statement — see `$programme-impact` for logic-driven schedule impact.

If planned finish dates are **absent**, output a **run-rate-only forecast** instead — do not emit placeholder planned/variance values:

| # | Activity | Remaining Work | Forecast Finish (A — current rate) | Forecast Finish (B — best sustained) | Forecast Finish (C — earned-schedule) |
|---|---|---|---|---|---|
| 1 | [activity] | [X] [unit] | [date] | [date] | [date, or "— no baseline mapping (Pattern 15)"] |

> Planned completion dates are not available from the API, so variance vs plan cannot be computed. Forecasts are run-rate projections from the data cut-off date [end date]: Scenario A uses the current run rate, Scenario B the best sustained rate, and Scenario C (earned-schedule extrapolation, trend-based not critical-path) is shown only for activities with a confirmed Pattern 15 baseline mapping. Where remaining scope is unknown, the forecast is omitted rather than estimated (Pattern 12).

---

### Caveats

Always include — do not modify this text:

> **Notes:**
> - Programme analysis is based on progress data recorded in Gather. If recording is incomplete, figures may understate actual achievement.
> - Forecast completion dates are anchored to the data cut-off date (end of the analysed window), not today, and are presented as three lenses (current run rate, best sustained rate, and — where a confirmed baseline mapping exists — earned-schedule extrapolation), never averaged into one number. Actual completion depends on future conditions.
> - Run rate calculations use working days from shift records. If the working pattern changes, forecasts will shift accordingly.
> - The earned-schedule extrapolation is stored-baseline and recorded-cumulative arithmetic only — no CPM engine runs, and it is a trend indicator, not a critical-path statement. It assumes linear phasing of the planned curve (Pattern 15) and requires a confirmed activity mapping; unmapped activities show it as unavailable.
> - Without the Accepted Programme (the API provides no logic links or float), this is a schedule-risk ranking, not a critical-path analysis. Activities flagged as high risk are not confirmed to be on the critical path.
> - Ref: PM-[NNN] is a session-local sequence number for cross-referencing.

---
