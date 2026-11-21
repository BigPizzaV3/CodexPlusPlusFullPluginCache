---
name: weather-impact
description: 'Quantifies weather impact on working time and productivity — lost days
  from shift weather records and programme impact. Triggers: weather delay, weather
  claim, seasonal impact.'
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Weather Impact — Quantify Weather Effects on Working Time and Productivity

Analyse weather conditions recorded in shift data to categorise working days, calculate lost time, measure productivity reduction, and identify weather patterns. Produces quantified weather impact data suitable for change/extension-of-time claims, programme analysis, and seasonal planning.

**Contract terminology:** Do not assume NEC. Before using any contract-specific term (e.g. "compensation event"), resolve the contract form using **Pattern 5 (Contract Type Resolution)** and use that contract's terminology throughout — the equivalent mechanism is a Relevant Event (JCT) or a Claim/EOT (FIDIC). See the weather row of the Pattern 7 mapping table for the applicable clauses.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Resolve Project and Date Range

Parse `the user’s request` for:

1. **Project name** — resolve using **Pattern 1 (Project Resolution)** from `../../shared/patterns/01-project-resolution.md`.
2. **Date range** — parse using **Pattern 2 (Date Range Parsing)** from `../../shared/patterns/02-date-range-parsing.md`. If no date range is specified, default to the last 4 weeks. For weather analysis, longer periods are usually more meaningful — suggest extending the range if it seems short:
   > "Weather impact analysis is more meaningful over longer periods. The default is the last 4 weeks — would you prefer to extend to the last 3 months or a specific season?"

Confirm the interpreted parameters with the user:
> "I'll analyse weather impact for **[project name]** from **[start date]** to **[end date]**. Does that look right?"

If the date range is unambiguous (exact dates provided), skip confirmation and proceed.

---

## Step 2: Retrieve Shift Data with Weather Conditions

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardShiftTable`
- **Project:** the resolved project UUID
- **Date range:** the parsed from/to dates

If no data is returned, follow **Pattern 3 (Empty Data Handling)** from `../../shared/patterns/03-empty-data-handling.md`. If only part of the range has records, do not stop to ask: analyse the covered period, state the covered and uncovered dates in a coverage line at the top of the report, and carry that caveat into every figure.

Extract from the response:
- Shift date
- Shift start and end times
- Shift duration (planned vs actual)
- Weather conditions recorded (rain, wind, temperature, frost, snow, etc.)
- Supervisor name
- Number of resources on shift

**Weather source and pagination:** This skill takes weather from the `dashboardShiftTable` dashboard report, which returns as a **single response with no pagination** (keep the date range to about one month per call — Pattern 4). No per-record fetch is required for the standard analysis. **Only if** the dashboard does not carry a weather field (verify per **Pattern 12**), or the user asks for per-shift weather detail, read `references/record-fallback.md` for the fallback procedure.

Save the raw response to a scratch file — it feeds both Step 3's classification and the
`shift_analytics.py` run below.

---

## Step 3: Categorise Each Shift by Weather Impact

Classify every shift into one of four categories based on the weather data and shift pattern:

| Category | Code | Definition | Criteria |
|---|---|---|---|
| Full Working | FW | No weather impact — full shift worked | No adverse weather recorded; shift duration matches or exceeds standard |
| Full Working, weather noted | FW-N | Weather mentioned but work proceeded normally | Weather recorded **and** shift worked full duration (>75% of standard) **and** no impact language — weather was merely noted, not disruptive |
| Restricted Working | RW | Weather present and work demonstrably curtailed | Adverse weather recorded **and** the shift was shortened (25–75% of standard) or the narrative describes reduced/disrupted output |
| Non-Working | NW | Weather prevented work entirely | Shift cancelled, actual duration below 25% of the standard shift, or narrative explicitly states weather stoppage |

**NW threshold — single definition:** a Non-Working day is one where the actual shift duration is **below 25% of the standard (median) shift duration** (or the shift was cancelled / the narrative explicitly states a weather stoppage). Use this 25%-of-standard test everywhere — do not use a separate fixed "2 hours" cut-off.

### Classification Rules

Apply these rules in order:

1. **Explicit non-working:** If the shift narrative or weather field explicitly states work stopped due to weather → **NW**
2. **Very short shift:** If actual shift duration is less than 25% of the standard shift duration and weather is recorded → **NW**
3. **Shortened shift:** If actual shift duration is 25–75% of the standard shift duration and adverse weather is recorded → **RW**
4. **Weather recorded, full shift, work curtailed:** If adverse weather is recorded, the shift duration is >75% of standard, **but** the narrative uses impact language (e.g. "reduced output", "gang stood down part-shift", "work slowed", "could not proceed with [activity]") → **RW**.
5. **Weather noted, full shift, no impact:** If weather is recorded and the shift worked full duration (>75% of standard) **with no impact language** — the supervisor merely noted the conditions → **FW-N (Full Working, weather noted)**, **NOT RW**. A bare weather mention does not itself curtail work and must not be counted as restricted (doing so inflates the claim). These days contribute **zero** weather-lost time.
6. **No weather issues:** If no adverse weather is recorded and shift duration is normal → **FW**

Calculate the standard shift duration as the median shift length across all shifts in the dataset. For all impact and lost-time calculations, treat **FW-N days as full working days (no lost time)** — only RW and NW days carry weather-lost time.

**Bulk classification via script.** Run:

```
python3 ../../scripts/shift_analytics.py <shifttable.json> --format md > <scratch>/shift-analytics-summary.md
```

The script applies the same 25%/75%-of-median-shift-duration test (rules 1–3 and 6 above) to
every shift and returns FW/FW-N/RW/NW day counts, weather-lost hours and day counts by weather
type, and calendar shift-coverage gaps — use these instead of counting rows by hand. It
**cannot read narrative text**, so it counts any day >75% of standard duration as FW-N
regardless of impact language. Apply **rule 4** yourself: for any day the script marks FW-N
that also carries adverse weather, check the narrative for impact language ("reduced output",
"stood down part-shift", etc.) and reclassify to RW if present, adjusting the script's totals
accordingly. State in the output which days (if any) were reclassified this way.

---

## Step 4: Retrieve Labour Hours for Productivity Comparison

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardResourceLabour`
- **Project:** the resolved project UUID
- **Date range:** the same from/to dates

Extract total labour hours for each day, then split into:
- **Labour hours on FW days** — total hours worked on full working days (FW **and** FW-N — weather-noted days count as full working per Step 3)
- **Labour hours on RW days** — total hours worked on restricted working days
- **Labour hours on NW days** — total hours worked (if any) on non-working days

Calculate:
- Average labour hours per FW day
- Average labour hours per RW day
- Labour hour reduction on RW days = ((FW average - RW average) / FW average) x 100%

**Divide-by-zero guard (Pattern 12):** if there are no FW/FW-N days in the period (FW average denominator = 0), or no RW days, render the reduction as **"n/a"** with a data-quality flag rather than a number — a percentage reduction cannot be computed without a clear-day baseline.

---

## Step 5: Retrieve Progress Data for Output Comparison

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardProgress`
- **Project:** the resolved project UUID
- **Date range:** the same from/to dates

Compare output on weather-affected vs clear days:

1. **Average daily output on FW days** — sum of progress quantities on FW days / number of FW days (treat FW-N days as FW)
2. **Average daily output on RW days** — sum of progress quantities on RW days / number of RW days
3. **Productivity reduction** = ((FW average - RW average) / FW average) x 100%

**Divide-by-zero guard (Pattern 12):** if there are no FW/FW-N days (denominator = 0) or no RW days, render the reduction as **"n/a"** with a data-quality flag — never as a number or an error.

If progress data is not available or not recorded at daily granularity, note this limitation and rely on labour hours alone for the productivity comparison.

---

## Step 6: Weather-Type Analysis, Lost-Hours Quantification, and Output

Read `references/weather-analysis-and-template.md`
for the weather-type breakdown, lost-time quantification (theoretical maximum, cross-deduction
against delay-analysis, equivalent lost days), the exceptionally-adverse/1-in-10-year
determination, and the exact 7-part report structure. Use the Step 3 script output (weather-lost
hours and day counts by type) as the source for the weather-type breakdown rather than
recounting from raw shift rows.

---

## Related Skills

After presenting the weather impact report, suggest these related skills for deeper analysis:

- `$delay-analysis` — Build a comprehensive delay register including weather alongside all other delay causes
- `$programme` — Assess the programme impact of weather-related lost days
- `$narrative-search` — Search narratives for specific weather events or conditions in more detail
- `$measured-mile` — Establish baseline productivity on clear days to quantify the disruption effect
