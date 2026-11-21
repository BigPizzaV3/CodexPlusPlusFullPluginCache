# Output Template — Commercial Report

Use this **exact structure**. Fill every placeholder `[…]` with data. Do not add, remove, or reorder sections.

---

```
COMMERCIAL REPORT — [Project Name]
Ref: CR-[NNN]
Period: [Start Date] to [End Date]
Comparison Period: [Prev Start Date] to [Prev End Date]
Generated: [Today's Date]
```

Apply **Pattern 8 (Report Numbering)** from `../../../shared/patterns/08-report-numbering.md` for the `CR-[NNN]` reference.

---

### 1. EXECUTIVE SUMMARY

Write a 5-sentence summary using the templates below. Sentences 1, 2 and 5 are always present. Sentences 3 (progress) and 4 (plant utilisation) are **conditional** — where the underlying data is missing, use the fallback sentence rather than inserting a placeholder or an invented figure (**Pattern 12: estimate discipline** — never fill a placeholder with a fabricated value).

> This report covers the operational commercial position for [Project Name] for the period [start date] to [end date]. Labour hours totalled [X] hours ([+/−X]% vs prior period), with an average daily headcount of [X] ([increasing/stable/decreasing]).

Sentence 3 — progress:
- If %-complete is available: "Overall progress stands at [X]% complete, with [Y] of [Z] activities on or ahead of programme."
- If %-complete is **not** available: "Progress is reported as actual output only — planned targets are not configured, so a percentage-complete figure cannot be stated."

Sentence 4 — plant utilisation:
- If utilisation data is available: "[X] plant items were on site with an overall utilisation of [X]%."
- If plant is recorded but utilisation (hours used vs available) is **not**: "[X] plant items were on site; utilisation could not be calculated as hours-available data was not recorded."
- If no plant is recorded: "No plant was recorded on site during the period."

Sentence 5 — always:
> [X] commercial issues were identified during the period, the most significant being [one-liner description of top issue]. (If none: "No commercially significant issues were identified during the period.")

---

### 2. LABOUR

| Metric | This Period | Previous Period | Change | Direction |
|---|---|---|---|---|
| **Total Labour Hours** | [X] | [X] | [+/− X] | [↑/↓/→] |
| **Average Daily Headcount** | [X] | [X] | [+/− X] | [↑/↓/→] |
| **Peak Headcount** | [X] on [date] | [X] on [date] | [+/− X] | [↑/↓/→] |
| **Working Days** | [X] | [X] | [+/− X] | [↑/↓/→] |
| **Hours per Working Day** | [X] | [X] | [+/− X] | [↑/↓/→] |

**Trade Breakdown:**

| # | Trade | Hours | Headcount | % of Total |
|---|---|---|---|---|
| 1 | [trade] | [hours] | [count] | [%] |

Sort by Hours descending.

After the table, write one sentence:

> The workforce [increased by X% / remained stable / decreased by X%] compared to the prior period, [driven by mobilisation of additional [trade] / reflecting completion of [activity] / consistent with current programme requirements].

---

### 3. PLANT & EQUIPMENT

| # | Equipment Type | Count on Site | Utilisation % | Status |
|---|---|---|---|---|
| 1 | [type] | [count] | [%] | [Active/Underutilised/Idle] |

Sort by Utilisation ascending (worst first).

After the table, write one sentence per movement:

> [Item/type] was [mobilised to / demobilised from] site on [date] [to support [activity] / following completion of [activity] / due to [reason]].

If no movements: "No plant movements recorded during this period."

---

### 4. MATERIALS

| # | Material | Unit | Quantity | Delivery Date(s) | Notes |
|---|---|---|---|---|---|
| 1 | [material] | [unit] | [qty] | [date(s)] | [note] |

If no materials data: "No materials data recorded for this period. If materials were used, recording should be reviewed."

---

### 5. PROGRESS

| # | Activity | Unit | Planned | Actual | Variance | Var % | Run Rate (/day) | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | [activity] | [unit] | [qty] | [qty] | [+/− qty] | [%] | [qty] | [Ahead/On Track/Behind/Critical] |

Sort by Status: Critical → Behind → On Track → Ahead.

After the table, write one sentence:

> Overall progress is [X]% complete. [X] activities are behind programme, the most significant being [activity] at [−X]% variance, which at current run rates [will / will not] recover without [additional resource / programme revision].

If planned data unavailable: "Planned targets are not available — progress is reported as actual output only. Variance analysis requires planned targets to be configured in Gather."

---

### 6. ACCESS & POSSESSION

| Metric | Value |
|---|---|
| **Possessions Requested** | [X] |
| **Possessions Granted** | [X] |
| **On-Time %** | [X]% |
| **Cancelled** | [X] |
| **Overrun / Restricted** | [X] |

For each significant access issue, write one sentence:

> On [date], [possession/access description] was [cancelled/delayed/restricted] [by X hours / for the full shift], affecting [X operatives] and resulting in approximately [X] hours of lost productive time.

If no issues: "All possessions were granted on time with no restrictions. Access performance was [X]% on-time for the period."

---

### 7. KEY ISSUES & RISKS

| # | Date | Category | Issue | Source | Commercial Implication |
|---|---|---|---|---|---|
| 1 | [date] | [Delay/Access/Design/Weather/Resource/Safety/Other] | [one-sentence description] | [supervisor name] | [one-sentence: potential claim, variation, cost impact, or programme impact] |

Sort by Date ascending.

After the table, write one sentence per issue flagged for commercial action.

**Before naming any contractual mechanism or clause**, resolve the contract form using **Pattern 5 (Contract Type Resolution)** from `../../../shared/patterns/05-contract-type-resolution.md` and map the event to a clause using **Pattern 7 (Common Event-to-Clause Mapping)** from `../../../shared/patterns/07-event-to-clause-mapping.md`. Use only the terminology and clause of the confirmed contract — never cite a specific clause number that has not been resolved through Pattern 7, and never invent a clause. If the contract form is not confirmed, use generic wording ("raise with the PM/CA/Engineer" / "log for period-end review") only.

> **Action required:** [Issue #X] — [description] represents a potential [change/entitlement event in the confirmed contract's terminology, per Pattern 5]. Recommended next step: [notify under the applicable clause from Pattern 7 for the confirmed contract / issue an early warning where the contract provides one / raise with the PM/CA/Engineer / log for period-end review].

If no issues: "No commercially significant issues were identified during this period."

---

### Caveats

Always include — do not modify this text:

> **Notes:**
> - This report is generated from Gather site diary data. It should be reviewed and supplemented with financial data, subcontractor accounts, and management commentary before formal submission.
> - All figures are based on data recorded in Gather. Where recording is incomplete, figures may understate actual position.
> - Commercial implications are indicative — formal contractual advice should be sought before issuing notifications or claims.
> - Ref: CR-[NNN] is a session-local sequence number for cross-referencing. It does not replace the project's own report numbering.

---
