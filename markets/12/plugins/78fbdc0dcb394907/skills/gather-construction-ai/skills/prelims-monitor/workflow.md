---
name: prelims-monitor
description: Track prelims — weekly staff on site vs tender allowance, elapsed vs
  tender duration, and a projected overrun at current run-rate.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Prelims Monitor

Watch the prelims: staff-on-site against the tender allowance, site duration against tender
duration, and a projected time-related cost overrun at the current run-rate. This is a
run-rate extrapolation, not a critical-path or programme analysis.

Follow the shared patterns: `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

## Step 1: Resolve Project and Period-to-Date

1. Resolve the project using **Pattern 1**.
2. Parse the period-to-date using **Pattern 2**. Default (no period given): project start to
   today. Confirm only if the input needed non-trivial interpretation.
3. Determine the **site start date** — the earliest date across `dashboardResourceLabour` /
   `dashboardShiftTable` project-wide (not just the requested period), needed for elapsed
   duration in Step 5. Reuse the period-to-date start if it already predates all records.

## Step 2: Load the Commercial Profile (Pattern 14)

Look for `commercial-profile.md` (or `commercial-profile-<project-slug>.md`). If found and its
`project` field matches, read the `prelims` block: `staff_allowance`, `establishment_weekly`,
`tender_duration_weeks`. A mismatched `project` field is ignored — say so.

If no profile exists, or `prelims` is absent: proceed **weeks/quantities-only** — the headcount
and duration tables still run, but the allowance column, overrun cost, and variance pricing show
"not in commercial profile", with one pointer to `$commercial-profile`. Never invent an
allowance, weekly rate, or tender duration.

## Step 3: Schema Gate — Can Staff Be Distinguished from Trades? (Pattern 12)

Before computing any staff-only metric, check whether the workspace's fields support it:

1. Call `getReportSchemas` (or inspect the first `dashboardResourceLabour`/`getPeople` response)
   for a role, job-title, or company field distinguishing the main contractor's own
   staff/site-management from subcontract trade labour.
2. **If it exists:** filter to staff records for Steps 4–7 and state which field was used (e.g.
   "staff identified via company = [main contractor name]").
3. **If it does not:** **degrade explicitly** — state "staff identification is not supported by
   this workspace's fields — the staff/trade split is not available" and fall back to
   **total-headcount trend** (every distinct person on site, trades included) as the tracked
   series. Every downstream table header says "total on-site headcount", not "staff", in this
   mode. Never guess which individuals are staff.

## Step 4: Retrieve Weekly Headcount

Call `getCachedReport` (`dashboardResourceLabour`, `dashboardShiftTable`) for the period-to-date
(**Pattern 4**). Use `getPeople` only as optional role/company enrichment, as in `people` Step 2
— skip it if role/company already comes through the labour data.

Group into calendar weeks (Monday–Sunday); count distinct people in the tracked series from
Step 3 for each week. Label a week "(partial)" if the period starts or ends mid-week. Follow
**Pattern 3** if no data is returned.

## Step 5: Duration Position

**Elapsed site weeks** = (period-to-date end − site start date) ÷ 7, to 1 decimal. **Tender
duration** = `tender_duration_weeks` from the profile, or "not in commercial profile" — in which
case duration position is elapsed weeks only, with no forecast or overrun.

## Step 6: Forecast Remaining Weeks (Run-Rate Basis, Cost-to-Complete Method)

Mirror `$cost-to-complete`'s run-rate method:

1. Optionally call `getCachedReport` (`dashboardProgress`) for overall % complete.
2. **Basis A (preferred, needs % complete):** `Forecast Total Weeks = Elapsed Weeks / (%
   Complete / 100)`; `Forecast Remaining Weeks = Forecast Total Weeks − Elapsed Weeks`.
   **Divide-by-zero guard:** % Complete = 0 → "n/a", data-quality flag, no forecast.
3. **Basis B (fallback, no progress data):** state "no progress data available — forecast total
   weeks cannot be run-rate extrapolated; tender duration is shown for reference only" and omit
   Forecast Total Weeks and the projected overrun rather than inventing one (Pattern 12).

Always state which basis was used.

## Step 7: Projected Overrun and Cost Exposure

Only computable where the profile's `prelims` block is present **and** Basis A produced a
Forecast Total Weeks:

- **Projected overrun weeks** = `max(0, Forecast Total Weeks − Tender Duration Weeks)`.
- **Establishment exposure** = overrun weeks × `establishment_weekly`, cited "rate per
  commercial profile".
- **Staff variance-weeks**: per week from Step 4, variance = tracked headcount − allowance ("n/a
  — no allowance" if the profile is absent; "n/a — total headcount, not staff-only" if Step 3
  degraded). Sum the **positive** variance-weeks only — over-allowance weeks are not netted
  against under-allowance weeks; state this exclusion in the output.
- **Staff variance exposure** = positive variance-weeks × a **derived** per-head weekly rate
  (`establishment_weekly ÷ staff_allowance`, only where both are present and `staff_allowance` >
  0, else "n/a"). State plainly this is a derived rate, not a literal commercial-profile line,
  and cite the two source fields.
- **Total projected exposure** = the two lines above, summed and shown separately.
- Any unpriced or degraded input renders as weeks/quantities-only ("rate not in commercial
  profile") rather than blocking the rest of the output (Pattern 14 rule 2).

## Step 8: Present the Dashboard (apply Pattern 8 for the `PS-[NNN]` ref)

```
PRELIMS DASHBOARD — [Project Name]
Ref: PS-[NNN]
Period Assessed: [Start Date] to [End Date]
Generated: [Today's Date]
Tracked Series: [Staff-only, via <field> / Total on-site headcount — staff/trade split not supported]
```

### 1. HEADLINE

Exactly 2 sentences: current headcount position vs allowance (or "no allowance in commercial
profile"), and duration position (elapsed vs tender, plus the forecast basis used).

### 2. WEEKLY HEADCOUNT VS ALLOWANCE

| Week Commencing | Headcount | Allowance | Variance | Status |
|---|---|---|---|---|
| [date] | [X] | [X or "n/a"] | [+/−X or "n/a"] | [Over/At/Under/n/a] |

One row per week in the period. Bold weeks with positive variance.

### 3. DURATION POSITION

| Metric | Value |
|---|---|
| **Elapsed Site Weeks** | [X] |
| **Tender Duration (weeks)** | [X or "not in commercial profile"] |
| **Forecast Basis** | [A — run-rate on % complete / B — no progress data, reference only] |
| **Forecast Total Weeks** | [X or "not computable — Basis B"] |
| **Projected Overrun (weeks)** | [X or "n/a"] |

### 4. PROJECTED COST EXPOSURE

| Line | Basis | Value |
|---|---|---|
| **Establishment exposure** | Overrun weeks × establishment_weekly (rate per commercial profile) | [£X or "not in commercial profile"] |
| **Staff variance exposure** | Positive variance-weeks × derived per-head weekly rate (establishment_weekly ÷ staff_allowance) | [£X or "n/a"] |
| **Total projected exposure** | Sum of the above | [£X or "quantities-only — see caveats"] |

### 5. CAUSES

Cross-reference any delay-register refs already produced in this conversation (Pattern 11 —
cited, never summed):

> [X] delay-register entries in DA-[NNN] (and/or AC-[NNN]/WI-[NNN] if present) fall within this
> period and may explain part of the overrun — see the cited register for detail; its hours are
> not added into the cost exposure above. If no register exists: "No delay register (DA/AC/WI)
> has been produced in this conversation — run `$delay-analysis` to investigate causes."

### Caveats (always include, unmodified)

> **Important notes on this dashboard:**
> - This is a **run-rate extrapolation** from current headcount and progress trends, not a
>   programme or critical-path analysis — see `$programme` for schedule-risk ranking.
> - The staff/trade split depends on workspace fields (Pattern 12); where unavailable, all
>   figures are total on-site headcount, not staff alone.
> - Positive variance-weeks are summed without netting off under-allowance weeks — a conservative figure, not a true average.
> - Ref: PS-[NNN] is a session-local sequence number for cross-referencing.

## Related Skills

- `$people` — Full workforce roster, mobilisation/demobilisation detail
- `$cost-to-complete` — The labour-hours run-rate forecast this skill's basis mirrors
- `$programme` — Schedule-risk ranking and forecast completion dates (not this skill's job)
- `$delay-analysis` — Build or extend the delay register cited in Section 5
- `$commercial-profile` — Capture or update `prelims` allowances and rates
