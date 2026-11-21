# Output Template: Labour Analysis (labour Step 8)

## Step 8: Present Results

Use this **exact structure**. Fill every placeholder `[…]` with data. Do not add, remove, or reorder sections.

---

```
LABOUR ANALYSIS — [Project Name]
Ref: LA-[NNN]
Period: [Start Date] to [End Date]
Generated: [Today's Date]
```

Where `[NNN]` is a zero-padded sequential number. If a previous labour analysis exists in the conversation, increment by 1. Otherwise use `001`.

---

### 1. SUMMARY

| Metric | Value |
|---|---|
| **Total Labour Hours** | [X] |
| **Total Individuals** | [X] |
| **Working Days** | [X] |
| **Avg Hours per Working Day** | [X] |
| **Avg Hours per Person per Day** | [X] |
| **Peak Day** | [date] — [X] hrs |
| **Trough Day** | [date] — [X] hrs |

After the table, write exactly 2 sentences:

> Over the period [start date] to [end date], [X] individuals recorded [X] labour hours across [X] working days. The workforce trend is **[increasing/decreasing/stable/drifting/volatile]**, [with week-on-week change of [+/−X]% for the most recent two complete weeks / with insufficient data for week-on-week comparison].

---

### 2. TREND

Write one sentence:

> Labour hours are **[increasing/decreasing/stable/drifting/volatile]** over this period[, rising from [X] hrs/week to [X] hrs/week / declining from [X] hrs/week to [X] hrs/week / averaging [X] hrs/week with variation within ±15% / drifting with 15–30% variation between weeks / swinging between [X] and [X] hrs/week with >30% variation].

---

### 3. PERIOD BREAKDOWN

| # | Period | Total Hours | Headcount | Avg Hours/Person | Working Days |
|---|---|---|---|---|---|
| 1 | [date/week/month] | [X] | [X] | [X] | [X] |

Granularity: daily if ≤14 days, weekly if 15–60 days, monthly if >60 days.

---

### 4. BY PERSON

| # | Name | Trade/Role | Total Hours | Days Worked | Avg Hours/Day |
|---|---|---|---|---|---|
| 1 | [name] | [trade] | [X] | [X] | [X] |

Sort by Total Hours descending. If >20 individuals, show top 15 then:

> [X] additional individuals not shown (total [X] hours). Ask for the full list if needed.

---

### 5. BY TRADE/ROLE

| # | Trade/Role | Headcount | Total Hours | % of Total | Avg Hours/Person |
|---|---|---|---|---|---|
| 1 | [trade] | [X] | [X] | [X]% | [X] |

Sort by Total Hours descending.

If trade/role data unavailable: "Trade/role breakdown is not available — labour data does not include role classifications."

After the table (if available), write one sentence:

> The workforce is [predominantly [top trade] at [X]% of total hours / evenly distributed across [X] trades, with no single trade exceeding [X]% of total hours].

---

### 6. FLAGS AND ALERTS

Use this exact format for each flag. Group hours comparisons and workforce anomalies separately.

**Individual Flags:**

For each flag, write one line:

> ⚠️ **[Above daily comparison / Above weekly comparison]:** [Name] — [recorded hours, dates, comparison threshold].

**Workforce Flags:**

> ⚠️ **[Zero-hour day / Significant variance]:** [Date] — [detail: expected vs actual, or description].

If no flags: "No overtime or anomaly flags detected for this period."

---

### Caveats

Always include — do not modify this text:

> **Notes:**
> - This analysis is based on labour data recorded in Gather. Individuals not recorded in shift diaries will not appear.
> - Hours are as recorded — actual hours worked may differ if recording is approximate.
> - Commercial overtime comparisons use project-configured thresholds, or clearly labelled defaults of >10 recorded hrs/day and >50 recorded hrs/week. These do not establish overtime entitlement or assess health, fitness, safety or legal compliance.
> - Ref: LA-[NNN] is a session-local sequence number for cross-referencing.
