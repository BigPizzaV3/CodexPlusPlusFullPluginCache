# Earned-Schedule Extrapolation (programme Step 5d)

### 5d: Earned-Schedule Extrapolation (Third Forecast Lens)

**No engine runs here** — this lens is stored-baseline and recorded-cumulative arithmetic only, exactly like Scenarios A/B. No CPM recalculation (`scripts/cpm.py`) is invoked, and no critical-path logic is used.

Only computable where the Pattern 15 baseline check above (5c) found a **confirmed activity/milestone mapping** — this lens needs a stored baseline start and duration, not just a planned finish date.

For each mapped activity/milestone:

| Field | Calculation |
|---|---|
| **Planned Duration (PD)** | The mapped task's STORED baseline duration (finish − start), taken exactly as exported — never recomputed (Pattern 15 rule 1: STORED is the only admissible source). |
| **Elapsed** | Working days (Step 3) from the mapped task's STORED baseline start to the data cut-off date. |
| **Earned Schedule ES(t)** | Under the same **linear-phasing assumption** used for the planned curve (state it — Planned%(t) = t / PD): ES(t) = PD × (Actual progress to date / Total Scope) — the point on the planned timeline that the actual cumulative achievement corresponds to. |
| **SPI(t)** | ES(t) / Elapsed. If Elapsed = 0, render "n/a" with a data-quality flag (Pattern 12). |
| **Earned-Schedule Forecast Duration** | Planned Duration / SPI(t). |
| **Earned-Schedule Forecast Completion** | Mapped task's STORED baseline start + Earned-Schedule Forecast Duration (skipping non-working days per the observed pattern, Step 3). |

Label this lens explicitly wherever it is presented: **"earned-schedule extrapolation — trend-based, not critical-path."**

**Unmapped activities:** this lens is not computable — state "Earned-schedule extrapolation unavailable — no confirmed baseline mapping for this activity (Pattern 15)."

This is a **simpler point-estimate variant** of the full period-by-period cumulative curve built in `$progress` Step 7 — it uses a single cumulative data point plus the stored baseline duration rather than a multi-period curve. For a fuller earned-schedule read (period-by-period table, cumulative S-curve chart), point to `$progress`.

**Never average the three lenses.** Present Scenario A (current rate), Scenario B (best sustained rate), and the earned-schedule extrapolation side by side in Step 8, each with its own stated assumption:
- Scenarios A/B assume the recent run rate (or best sustained rate) continues unchanged for all remaining work.
- The earned-schedule extrapolation assumes the *ratio* of earned progress to elapsed time (SPI(t)) continues unchanged, and it inherits the linear-phasing assumption used for the planned curve.

These are different models of the future — they will not agree, and averaging them into one number would imply a false consensus that the data does not support.

