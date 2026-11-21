# Weather Type Analysis, Lost-Hours Calculation, and Output Template

Read at Step 6 (after the classification and script aggregation in Step 3, and the labour/
progress retrieval in Steps 4–5). Covers weather-type breakdown, lost-time quantification for
CE/EOT claims, the exceptionally-adverse/1-in-10-year determination, and the exact 7-part
output template — fill every placeholder `[…]` with data, do not add/remove/reorder sections.

---

## Step 6: Analyse Weather Types and Patterns

Break down weather-affected days by weather type:

| Weather Type | Indicators |
|---|---|
| Rain / Heavy Rain | rain, heavy rain, rainfall, downpour, showers, wet, precipitation |
| Wind / High Wind | wind, high wind, strong wind, gale, gusting |
| Temperature / Heat | extreme heat, high temperature, heat |
| Frost / Ice | frost, ice, icy, frozen, frozen ground, black ice |
| Snow | snow, snowing, blizzard, snow cover |
| Flooding | flooding, flooded, waterlogged, standing water, water ingress |
| Storm | storm, thunder, lightning, thunderstorm |
| Combined / General | inclement weather, adverse weather, bad weather, unsafe conditions |

For each weather type:
- Count of affected days
- Total lost hours attributed to this type
- Percentage of total weather-related lost time

Identify temporal patterns:
- **Monthly / seasonal pattern** — which months had the most weather impact?
- **Consecutive run** — longest consecutive period of weather-affected days (important for cumulative disruption arguments)

Do **not** analyse weather by day of the week — weather is not correlated with weekday, so a day-of-week breakdown is meteorologically meaningless and any apparent pattern is coincidence.

---

## Step 7: Calculate Lost Time Quantification

Produce the key figures needed for CE claims and programme analysis:

### Total Weather Impact

| Metric | Value |
|---|---|
| **Total working days in period** | [count of all days with shifts] |
| **Full working days (FW)** | [count] ([percentage]) |
| **Restricted working days (RW)** | [count] ([percentage]) |
| **Non-working days (NW)** | [count] ([percentage]) |
| **Total weather-affected days** | [RW + NW count] ([percentage]) |

### Lost Hours Calculation

`Expected − Actual` measures the shortfall against a theoretical all-FW maximum from **every** cause (weather, access, resource, design, holidays, etc.) — it is **not** by itself the weather figure. Report it as such, then isolate the weather-attributable portion by cross-deducting hours already categorised to non-weather causes.

| Metric | Value |
|---|---|
| **Standard shift duration** | [median hours] |
| **Theoretical maximum hours (if all days FW)** | [total days x standard shift x avg crew] |
| **Actual hours worked** | [sum of all labour hours] |
| **Total shortfall vs theoretical maximum (all causes)** | [theoretical maximum − actual] |
| **Less: hours attributable to non-weather causes** | [access/resource/design/other, cross-deducted — see below] |
| **Weather-attributable shortfall (residual)** | [total shortfall − non-weather hours] |
| **Equivalent lost days** | [weather-attributable shortfall / (standard shift x avg crew); state the divisor] |

**Cross-deduction (Pattern 11):** the `weather-impact` register (WI) records **person-hours of shortfall vs the theoretical maximum (crew-scaled), weather-flagged** — it overlaps by design with the delay-analysis (DA) and access (AC) registers and uses a different unit, so **its total must not be summed with DA or AC** (state this in the output). Where a `$delay-analysis` (DA) register exists for the same period, deduct hours it has already attributed to access, resource, design or other non-weather causes on the same days, and cross-reference the DA Ref number. If no such register exists, state that the residual may still contain non-weather losses and has not been cross-deducted.

**Divide-by-zero guard (Pattern 12):** if the theoretical maximum is 0 (no working days or zero average crew), render the percentage figures as "n/a" with a data-quality flag rather than a number.

### Productivity Impact on Restricted Days

| Metric | Value |
|---|---|
| **Average output per FW day** | [value with unit] |
| **Average output per RW day** | [value with unit] |
| **Productivity reduction on RW days** | [percentage] |
| **Estimated lost output** | [RW days x (FW avg - RW avg)] |

### "Exceptionally Adverse" / 1-in-10-Year Determination

Whether weather was "exceptionally adverse" (JCT) or exceeded the **1-in-10-year threshold** (NEC clause 60.1(13)) **cannot be judged from site records alone** — site data shows only what happened, not what is climatically normal for the location. Establish a baseline before making any exceeds/within-normal statement:

1. **Obtain a climate baseline.** Use `WebSearch` for Met Office (or equivalent national meteorological service) **monthly climate averages** and, for the NEC test, **return-period / 1-in-10-year** rainfall, wind, snow or temperature data for the **site's location and month(s)**. If a reliable figure cannot be found, **ask the user** to supply the relevant Met Office / weather-station data.
2. **Compare** the recorded site conditions (days of rain, rainfall totals, wind, etc.) against that baseline for the same calendar month(s).
3. **Only then** may you state whether the weather exceeded or was within normal expectations — and cite the baseline source.
4. **If no baseline was obtained,** you must **not** assert either "exceptional" or "within normal". Force the neutral conclusion: **"Whether the weather was exceptionally adverse / exceeded the 1-in-10-year threshold cannot be determined from site data alone — independent Met Office climate data for the location is required."**

This determination gates the contractual-relevance branch in the KEY FINDINGS section.

---

## Step 8: Present the Weather Impact Report

Use this **exact structure**. Fill every placeholder `[…]` with data. Do not add, remove, or reorder sections. Apply **Pattern 8 (Report Numbering)** from `../../../shared/patterns/08-report-numbering.md`.

---

```
WEATHER IMPACT REPORT — [Project Name]
Ref: WI-[NNN]
Period: [Start Date] to [End Date]
Generated: [Today's Date]
Total Shifts Analysed: [X]
```

---

### 1. HEADLINE

Write exactly 2 sentences:

> Of [X] working days in the period, [X] ([X]%) were weather-affected — [X] restricted working days and [X] non-working days. Weather caused an estimated [X] hours ([X] equivalent days) of lost productive time, with **[top weather type]** accounting for [X]% of total lost time.

---

### 2. WEATHER IMPACT SUMMARY

| Metric | Value |
|---|---|
| **Total Working Days** | [X] |
| **Full Working Days (FW + FW-N)** | [X] ([X]%) — of which [X] weather-noted (FW-N) |
| **Restricted Working Days (RW)** | [X] ([X]%) |
| **Non-Working Days (NW)** | [X] ([X]%) |
| **Standard Shift Duration** | [X] hrs |
| **Theoretical Max Hours (all FW)** | [X] hrs |
| **Actual Hours Worked** | [X] hrs |
| **Total Shortfall (all causes)** | [X] hrs |
| **Weather-Attributable Shortfall** | [X] hrs |
| **Equivalent Lost Days** | [X] days (divisor: [median shift] hrs × [avg crew]) |

---

### 3. DAILY/WEEKLY BREAKDOWN

If ≤30 days, use daily:

| # | Date | Weather | Shift Duration | Category | Hours Lost | Notes |
|---|---|---|---|---|---|---|
| 1 | [date] | [conditions] | [X] hrs | [FW/FW-N/RW/NW] | [X] | [one-phrase note or —] |

If >30 days, use weekly:

| # | Week Commencing | FW Days | RW Days | NW Days | Hours Lost | Primary Weather |
|---|---|---|---|---|---|---|
| 1 | [date] | [X] | [X] | [X] | [X] | [type] |

---

### 4. WEATHER TYPE BREAKDOWN

| # | Weather Type | Days Affected | Hours Lost | % of Total | Avg Hours Lost/Day |
|---|---|---|---|---|---|
| 1 | [type] | [X] | [X] | [X]% | [X] |
| | **Total** | **[X]** | **[X]** | **100%** | **[X]** |

Sort by Hours Lost descending.

---

### 5. PRODUCTIVITY COMPARISON

| Metric | Clear Days (FW + FW-N) | Restricted Days (RW) | Reduction % |
|---|---|---|---|
| **Avg Shift Duration** | [X] hrs | [X] hrs | [X]% |
| **Avg Labour Hours** | [X] hrs | [X] hrs | [X]% |
| **Avg Daily Output** | [X] [unit] | [X] [unit] | [X]% |

If output data unavailable: "Daily output comparison not available — productivity impact is based on labour hours only."

After the table, write one sentence:

> On weather-affected days, labour hours reduced by [X]% and output reduced by [X]%, indicating [a proportional productivity impact / a disproportionate productivity impact beyond the lost hours, suggesting disruption to workflow and sequencing].

---

### 6. DISRUPTION FREQUENCY

| Metric | Value |
|---|---|
| **Disruption Rate** | [X]% of working days weather-affected |
| **Longest Clear Run** | [X] consecutive FW days ([start] to [end]) |
| **Longest Disrupted Run** | [X] consecutive weather-affected days ([start] to [end]) |
| **Avg Gap Between Disruptions** | [X] working days |

After the table, write one sentence:

> Weather disruptions occurred on average every [X] working days. [If longest disrupted run ≥3 days: "The [X]-day consecutive disrupted period from [start] to [end] is significant for cumulative disruption arguments — sustained weather impact prevents recovery of lost output." / If disruptions scattered: "Disruptions were scattered rather than concentrated, limiting their cumulative impact but creating repeated stop-start inefficiency."]

---

### 7. KEY FINDINGS

Write exactly 4 bullet points:

> - **Total impact:** [X] hours ([X] equivalent days) lost to weather — this represents [X]% of available working time in the period.
> - **Dominant weather type:** [Type] accounted for [X]% of all weather-related lost time ([X] hours across [X] days). [One sentence on whether this is typical for the season/location or exceptional.]
> - **Productivity effect:** On weather-affected days, output reduced by [X]% compared to clear days. [If reduction > hours lost %: "This exceeds the proportional lost time, indicating weather disrupts workflow beyond the direct time lost." / If proportional: "This is broadly proportional to the hours lost."]
> - **Contractual relevance:** Resolve the contract form via **Pattern 5** and use its terminology and the weather row of the **Pattern 7** clause mapping. This bullet is gated by the "Exceptionally Adverse / 1-in-10-Year Determination" in Step 7:
>   - [If a Met Office / climate baseline was obtained **and** the recorded weather exceeds it: "Against the [source] baseline, the recorded weather exceeded normal expectations for the location and period, which may support entitlement under the confirmed contract's weather mechanism (per Pattern 7 — e.g. NEC 60.1(13), JCT Relevant Event 2.29.8/2.29.6 (time only), FIDIC sub-clause 8.5 (EOT only)). Retain the baseline evidence to corroborate."]
>   - [If a baseline was obtained **and** the weather is within normal ranges: "Against the [source] baseline, weather disruption was within seasonally normal ranges — the threshold for 'exceptionally adverse' / the 1-in-10-year test does not appear to be met on the available data."]
>   - [If **no** baseline was obtained: "Whether the weather was exceptionally adverse or exceeded the 1-in-10-year threshold **cannot be determined from site data alone** — independent Met Office climate data for the location is required before any entitlement conclusion. Obtain it via WebSearch or from the user."]

---

### Caveats

Always include — do not modify this text:

> **Important notes on this weather analysis:**
> - Weather conditions are as recorded by site supervisors in shift records. If weather is not consistently recorded, the analysis will understate the impact.
> - Non-working days with no shift record are not included — if the site was closed due to weather but no record was created, those days are invisible to this analysis.
> - The productivity comparison assumes that weather is the primary cause of output reduction on affected days. Other factors (access, resource, design) may also contribute.
> - Lost hours are estimated based on the difference between standard and actual shift durations. This is an approximation — the actual productive time lost may differ.
> - For formal weather claims, this analysis should be supplemented with independent meteorological data from a recognised weather station.
> - Ref: WI-[NNN] is a session-local sequence number for cross-referencing.

---

## Related Skills

After presenting the weather impact report, suggest these related skills for deeper analysis:

- `$delay-analysis` — Build a comprehensive delay register including weather alongside all other delay causes
- `$programme` — Assess the programme impact of weather-related lost days
- `$narrative-search` — Search narratives for specific weather events or conditions in more detail
- `$measured-mile` — Establish baseline productivity on clear days to quantify the disruption effect
