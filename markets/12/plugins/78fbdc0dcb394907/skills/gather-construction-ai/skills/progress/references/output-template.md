# Output Template: Progress Analysis (progress Step 10)

```
PROGRESS ANALYSIS — [Project Name]
Ref: PG-[NNN]
Period: [Start Date] to [End Date]
Generated: [Today's Date]
```

---

### 1. SUMMARY

| Metric | Value |
|---|---|
| **Total Activities** | [X] |
| **On Track or Ahead** | [X] ([X]%) |
| **Behind Schedule** | [X] ([X]%) |
| **Critical (>20% behind)** | [X] ([X]%) |
| **Weighted Progress %** | [X]% |

---

### 2. OVERALL ASSESSMENT

Write exactly one sentence using the appropriate template:

- If >80% on track or ahead: "Project is **on track** — [X]% of tracked activities are meeting or exceeding planned targets, with an overall weighted progress of [X]%."
- If 50–80% on track: "Project is **broadly on track** but [X] of [Y] activities require attention, most notably [activity name] at [−X]% variance."
- If <50% on track: "Project is **behind programme** — [X]% of activities are falling short of planned targets, with [X] activities in critical status requiring immediate intervention."

If planned data unavailable, use: "Progress is reported as actuals only — [X] activities recorded output during the period. Planned targets are not configured, so variance analysis is not possible."

---

### 3. ACTIVITY BREAKDOWN

| # | Activity | Unit | Planned | Actual | Variance | Var % | Status | Run Rate (/day) | Required Rate (/day) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [activity] | [unit] | [qty] | [qty] | [+/− qty] | [%] | [Ahead/On Track/Behind/Critical] | [qty] | [qty or — if on track] |

Sort by Status: Critical → Behind → On Track → Ahead.

"Required Rate" = the daily output needed over the remaining programme duration to recover to plan. Show "—" for activities on track or ahead, **and for every activity when no planned finish date is available** (the API provides no baseline programme, so remaining duration is unknown — see Step 5). When Required Rate is shown as "—" for this reason, add one line under the table: "Required Rate is unavailable — the API does not provide planned finish dates, so remaining programme duration cannot be determined (Pattern 12)."

---

### 4. CUMULATIVE PROGRESS (S-CURVE) AND EARNED SCHEDULE

Table (period end | planned cum | actual cum | variance) — one row per period end used in Step 7:

| Period End | Planned Cum. | Actual Cum. | Variance | Basis |
|---|---|---|---|---|
| [date] | [qty or —] | [qty] | [+/− qty or —] | [unit / labour-hour-weighted / single-unit / unweighted — per Step 7b] |

- If a planned curve was built (Step 7a): every planned figure cites the revision — "per the imported programme ([revision], exported [date])" — and the row immediately below the table states the linear-phasing assumption.
- If no planned curve (Step 7a degraded): omit the Planned Cum. and Variance columns and state: "Planned curve unavailable — run $programme-import. Actual cumulative curve shown alone."

Where the environment renders Mermaid, follow the table with an `xychart-beta` line chart of the same two (or one) curves; where it does not, present the table alone — never both a broken chart and a table claiming to be equivalent.

**Earned schedule** (only where a planned curve exists — see Step 7c):

> Earned Schedule: ES(t) = [date]. Elapsed: [X] working days. SPI(t) = [X]. The project is **[X] working days ahead/behind schedule by earned measure**.
>
> Earned schedule is derived purely from the two cumulative curves above — no CPM engine runs and no critical-path logic is used here. It is a trend indicator, not a critical-path statement: a project can be SPI(t)-healthy while its true critical path is slipping. For a logic-driven answer, use `$programme-impact`.

If no planned curve: "Earned schedule not computed — no planned curve is available."

---

### 5. PRODUCTIVITY

| # | Activity | Output | Unit | Labour Hours | Productivity | Unit |
|---|---|---|---|---|---|---|
| 1 | [activity] | [qty] | [unit] | [hours] | [qty/hr] | [unit]/hr |

If labour is not allocated by activity:

> Labour hours are not broken down by activity. Overall blended productivity: [total output] [unit] / [total hours] hrs = [rate] [unit]/hr.

If multiple activities with different units: "Productivity per activity cannot be calculated — labour is not allocated to individual activities and units are not comparable."

If no labour data: "Labour data is not available for this period — productivity rates cannot be calculated."

---

### 6. CONCERNS

Group by severity. Use this exact format for each.

**Critical:**

For each critical item:

> 🔴 **[Activity]** — [actual] vs [planned] [unit] ([−X]% variance). Zero progress recorded [for X days / since date] [if applicable]. At current run rate ([X] [unit]/day), recovery requires [X] [unit]/day — [X]x the current rate. [This is achievable with [action] / This is unlikely without additional resources or programme revision].

**Warnings:**

For each warning:

> 🟡 **[Activity]** — [description of concern: declining run rate, stalled progress, unrealistic recovery]. [One sentence with supporting data].

If no concerns: "No progress concerns detected — all tracked activities are on or ahead of plan."

---

### Caveats

Always include — do not modify this text:

> **Notes:**
> - Progress figures are based on data recorded in Gather. If recording is incomplete or delayed, figures may understate actual achievement.
> - Productivity rates are blended across all labour unless activity-level allocation is available.
> - "Required Rate" is only shown where a planned finish date is present in the progress data; the API does not provide baseline programme dates, so for many projects this column reads "—". Where shown, it assumes linear recovery over the remaining programme duration — actual recovery may require a non-linear approach.
> - The planned S-curve (Section 4) exists only where an imported programme baseline has a confirmed activity mapping (Pattern 15); it phases planned quantity linearly across each mapped task's stored duration — a simplifying assumption, not a measured phasing profile. No CPM engine runs to produce these curves — they are stored-baseline and recorded-actuals arithmetic only.
> - Earned schedule (ES(t), SPI(t)) is a trend indicator derived from the two cumulative curves, not a critical-path statement — see `$programme-impact` for logic-driven schedule impact.
> - Ref: PG-[NNN] is a session-local sequence number for cross-referencing.
