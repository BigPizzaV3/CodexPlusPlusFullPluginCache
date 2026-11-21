# Output Template: Progress Report (progress-report Step 8)

## Step 8: Present the Progress Report

Use this **exact structure**. Fill every placeholder `[…]` with data. Do not add, remove, or reorder sections.

---

```
PROGRESS REPORT — [Project Name]
Ref: PR-[NNN]
Period: [Start Date] to [End Date]
Generated: [Today's Date]
```

Where `[NNN]` is a zero-padded sequential number. If a previous progress report exists in the conversation, increment by 1. Otherwise use `001`.

---

### 1. EXECUTIVE SUMMARY

Write exactly 4 sentences using these templates:

> During the period [start date] to [end date], overall progress on [Project Name] reached [X]% complete, with [Y] of [Z] tracked activities on or ahead of programme. The principal achievement was [single biggest achievement — activity name, quantity, and unit]. The primary risk to programme is [single biggest concern — activity name, variance, and consequence]. The average daily workforce was [X] ([rising/stable/falling] across the period — the intra-period trend from Step 5, not a prior-period comparison), peaking at [X] on [date].

---

### 2. PERIOD NARRATIVE

For each week (or day if the period ≤7 days), use this repeating block:

> **Week [N]: [first working date] – [last working date]**
>
> Works concentrated on [primary activity] and [secondary activity]. [2–3 factual sentences drawn directly from diary narratives, quoting significant entries in "double quotes"]. [If weekend or night shifts occurred: note them explicitly — e.g. "Night possession worked [date]" or "Saturday working [date]" — do not assume a Monday–Friday day-shift pattern; this is a rail/possession product where weekend and night work is routine.] [If an event occurred: On [date], [event description] which [impact on works].]

---

### 3. PROGRESS

#### 3.1 Overall Status

| Metric | Value |
|---|---|
| **Overall Progress** | [X]% complete |
| **Activities On Track or Ahead** | [X] of [Y] |
| **Activities Behind** | [X] of [Y] |
| **Activities Critical (>20% behind)** | [X] of [Y] |

If a percentage-complete figure is not present in the progress data (no planned quantities to divide by), do not fabricate one — write for the Overall Progress row: "% complete not available — no planned targets configured; actual output is reported in the activity breakdown below" (Pattern 12).

#### 3.2 Activity Breakdown

| # | Activity | Unit | Planned | Actual | Variance | Var % | Status | Run Rate (/day) |
|---|---|---|---|---|---|---|---|---|
| 1 | [activity] | [unit] | [qty] | [qty] | [+/- qty] | [%] | [Ahead/On Track/Behind/Critical] | [qty] |

Sort by Status: Critical → Behind → On Track → Ahead.

#### 3.3 Achievements

For each of the top 3 activities ahead of plan, write one sentence:

> [Activity] achieved [actual qty] [unit] against a target of [planned qty], representing [+X]% above plan driven by [reason if identifiable from narratives, otherwise "sustained output throughout the period"].

#### 3.4 Concerns

For each of the top 3 activities behind plan, write one sentence:

> [Activity] delivered [actual qty] [unit] against a target of [planned qty] ([−X]% variance). At the current run rate of [rate] [unit]/day, recovery to programme requires [required rate] [unit]/day — [achievable with current resources / likely to require additional resources / unlikely without programme revision]. [If no planned finish date is available, replace the required-rate clause with: "the recovery rate cannot be computed without a planned finish date (not provided by the API)."]

---

### 4. WORKFORCE

| Metric | Value |
|---|---|
| **Average Daily Headcount** | [X] |
| **Peak Headcount** | [X] on [date] |
| **Total Labour Hours** | [X] hours |
| **Working Days** | [X] |
| **Trend** | [Ramping up / Stable / Ramping down] |

**Trade Mix:**

| # | Trade | Hours | % of Total | Avg Daily HC |
|---|---|---|---|---|
| 1 | [trade] | [hours] | [%] | [X] |

Sort by Hours descending.

After the table, write one sentence:

> The workforce was [predominantly composed of / evenly split between] [top 1–2 trades], accounting for [X]% of total labour hours.

---

### 5. ACCESS & POSSESSION

| Metric | Value |
|---|---|
| **Possessions Requested** | [X] |
| **On Time** | [X] ([%]) |
| **Late / Restricted** | [X] ([%]) |
| **Cancelled** | [X] ([%]) |

If the possession-timeliness fields (on-time / late / cancelled) are not present in `dashboardAccessPossession` for this workspace, do not infer them — show "not recorded" against those rows and add: "Possession timeliness is not captured in this project's access data — only the possession count is available" (Pattern 12). Verify field availability per Pattern 12 before populating these rows.

If any access issues occurred, write one sentence per issue:

> On [date], [description of access issue] resulting in [X hours / X operatives] of lost time.

If no access issues: "All possessions were granted on time with no restrictions recorded."

---

### 6. KEY EVENTS

| # | Date | Category | Event | Impact on Progress |
|---|---|---|---|---|
| 1 | [date] | [Weather/Access/Design/Client/Resource/Safety] | [one-sentence description] | [quantified impact: hours lost, operatives affected, or area inaccessible] |

If no key events: "No significant events recorded during this period."

---

### 7. LOOK-AHEAD

Write exactly 4 bullet points using these templates:

> - **Priority activities for the next period:** [Activity 1] and [Activity 2] require focus to [maintain programme / recover lost ground], targeting a combined run rate of [X] [unit]/day.
> - **Resource requirement:** Based on current trends, the workforce [is sufficient at current levels / may need to increase to support recovery on [activity] / can reduce as [activity] completes]. Only state a specific target headcount if it is derived from run-rate arithmetic (e.g. required rate ÷ current per-operative output) and show that derivation; otherwise write "a specific uplift figure is not quantifiable from the available data" (Pattern 12 estimate discipline). Do not invent a headcount number.
> - **Key risk:** [Risk description]. [Only quantify the delay if it is computable from run-rate arithmetic — i.e. shortfall quantity ÷ current run rate = [X] days behind — and show that working. Otherwise write: "The programme impact is not yet quantifiable from available data — it requires a planned finish date and formal programme analysis (`$programme`)."] Mitigation: [action].
> - **Recovery actions:** [Activity] requires an increase from [current rate] to [required rate] [unit]/day [only where a required rate is computable — this needs a planned finish date, which the API does not provide; if unavailable, state "the recovery rate cannot be computed without a planned finish date" rather than inventing one]. [Specific action: additional gang, extended shifts, revised methodology, or re-sequencing].

If no concerns exist, replace the risk and recovery bullets with:

> - **Key risk:** No material risks identified. Continue monitoring [highest-output activity] to maintain current trajectory.
> - **Outlook:** Current progress and resourcing levels are sufficient to meet programme targets for the next period.

---

### Caveats

Always include — do not modify this text:

> **Notes:**
> - This report is generated from Gather site diary data. It should be reviewed and supplemented with programme data, commercial information, and management commentary before formal submission.
> - Progress figures are based on data recorded in Gather. If recording is incomplete or delayed, the figures may understate actual achievement.
> - The look-ahead is based on observed trends, not a formal programme analysis.
> - Ref: PR-[NNN] is a session-local sequence number for cross-referencing. It does not replace the project's own report numbering.

---

