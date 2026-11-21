# S-Curve and Earned Schedule (progress Step 7)

## Step 7: S-Curve — Cumulative Progress and Earned Schedule

This step builds cumulative (to-date) planned and actual curves and derives an earned-schedule
read from them. **No engine runs here** — stored-baseline and recorded-actuals arithmetic only.
No CPM recalculation (`scripts/cpm.py`) is invoked, and no critical-path logic is used at any
point in this step.

### 7a: PLANNED Curve

Check for `programme/programme-baseline.json` (with its companion
`programme/programme-baseline.md`) per **Pattern 15**
(`../../../shared/patterns/15-programme-baseline.md`).

- **If it exists, the project matches, and one or more activities carry a user-confirmed mapping
  (Pattern 15 rule 5) to a baseline task:**
  - For each mapped activity, phase its planned quantity (or planned labour hours, per the
    weighting basis in 7b) across that task's **STORED** baseline start/finish dates (or, where
    the export carries no baseline distinct from the current plan, the current planned dates) —
    taken exactly as exported, never recomputed or adjusted (Pattern 15: STORED is the only
    admissible source for planned dates).
  - **Phasing assumption (state this in the output, every time):** quantity is spread **linearly**
    across the task's stored duration — an assumption, not a measured phasing profile. A mapped
    task with a 20 working-day stored duration and 200m planned quantity is treated as 10m per
    working day for that task's window.
  - Sum each mapped task's phased daily quantity across all mapped tasks to build one cumulative
    PLANNED curve, period end by period end.
  - Cite it: "planned curve per the imported programme ([revision], exported [date])."
  - Activities with no confirmed mapping are excluded from the planned curve and listed
    separately — never guess a mapping (Pattern 15 rule 5).
  - If the analysed date range (Step 1) starts after the earliest mapped task's stored start, the
    curve is partial; state the window covered and note a wider date range would show more of it.
- **If the file is absent, the project doesn't match, or no activity has a confirmed mapping:**
  degrade explicitly. State "Planned curve unavailable — run $programme-import" and
  present the ACTUAL curve alone (7b), with no planned line and no variance column.

### 7b: ACTUAL Curve

Build the cumulative ACTUAL curve from recorded output, period end by period end across the
analysed date range:

- Where the tracked activities share a single unit, cumulate actual quantity to date directly.
- Where activities use heterogeneous units, do **not** sum incompatible quantities — instead
  cumulate using the **same weighting basis already established in Step 6** (labour-hour
  weighting preferred, then single-unit quantity, then unweighted average) to produce one
  blended cumulative curve. Use one basis for both the planned and actual curves; state which
  basis is in use under the output table (Step 10).

### 7c: Earned Schedule

Only computable where a PLANNED curve exists (7a). If the planned curve was degraded to
"unavailable," skip this subsection entirely and state: "Earned schedule not computed — no
planned curve is available."

Where the planned curve exists:

- **ES(t)** ("earned schedule"): read off the two curves — the date at which the cumulative
  PLANNED curve first reached the value the cumulative ACTUAL curve has reached today (or at the
  data cut-off date, if the analysis is historic). This is a lookup against the curves built
  above, not a recomputation of the network.
- **Elapsed**: working days (per Step 4) from the earliest date covered by the curves to the
  data cut-off date.
- **SPI(t)** = ES(t) elapsed-equivalent / Elapsed.
- Report: "[X] working days ahead/behind schedule by earned measure" — the difference between
  the data cut-off date and the ES(t) date.
- **Standing caveat (always include, unmodified):** "Earned schedule is derived purely from the
  two cumulative curves above — no CPM engine runs and no critical-path logic is used here. It
  is a **trend indicator**, not a critical-path statement: a project can be SPI(t)-healthy (ahead
  by earned measure) while its true critical path is slipping, if the activities running ahead
  are not the ones driving completion. For a logic-driven answer, use `$programme-impact`."
