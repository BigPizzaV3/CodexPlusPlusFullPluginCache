# Reading and reporting results

## What the script reports

- **Effect**: observed KPI minus counterfactual over the measured window, in KPI units.
- **Lift**: effect divided by the counterfactual. For go-dark it is negative: the share of the treated geos' KPI the channel was producing.
- **Interval**: 90% by default. Built from in-time placebos (the same model run on past windows of the same length, where nothing was changed). When the history is too short for enough placebos, an AR(1)-corrected parametric interval is used and the output says so (`interval_kind`).
- **p-values**: `p_in_time` from the placebo windows; `p_in_space` from fake treated groups drawn from the controls. The smallest attainable p depends on the number of placebos.
- **iCPA**: spend change divided by the KPI change. For go-dark: spend saved per conversion lost. **iROAS**: value change divided by spend change.
- **Checks**: pre-period fit, placebo bias, number of placebo windows, agreement between the two estimators (TBR and synthetic control), and a shift in the control group's level.

## How to state the result

Lead with the number and its interval, then what it means for the decision:

- "Switching off brand search in the treated regions reduced total orders by 3.1% (90% interval: -5.0% to -1.2%). That is 410 orders over 28 days for 38,200 of spend saved: an incremental cost of 93 per order, against 21 per order reported by the platform."

Rules:

- Always give the interval. A point estimate without one is not a result.
- An interval that includes zero is "no detectable effect at this size", not "no effect". Say what size of effect the test could have detected (the design MDE).
- Report iCPA or iROAS next to the platform-reported CPA or ROAS. The ratio between them is the incrementality factor teams can apply to attribution.
- If the two estimators disagree in sign or by more than half, report both and do not pick the convenient one.
- If a check fails, say which, and what it means: low pre-period fit means a wide and less reliable interval; a shift in the control level means something happened to all geos (seasonality, tracking, national campaign) and needs explaining.
- Do not extrapolate a go-dark result in 20% of geos to a national budget change without saying so. The effect at a different spend level can differ.
- Do not combine results from different platforms' lift studies by adding them.

## Decision mapping

| Result | Typical decision |
|---|---|
| Effect significant, iCPA below target | Keep or scale; consider a heavy-up to measure the marginal return |
| Effect significant, iCPA above target | Reduce spend or restructure; test a holdback to find the efficient level |
| Not significant, MDE small relative to decision threshold | Evidence that the channel adds little at current spend; reduce and monitor |
| Not significant, MDE large | Inconclusive; redesign with more geos, longer duration or larger cell |
| Checks fail | Do not decide on this test; fix the cause and rerun |

## Using the result elsewhere

- Calibrate attribution: incrementality factor = iCPA reported by platform / iCPA measured (or measured iROAS / platform ROAS).
- Calibrate a marketing mix model: the lift and its interval are a prior for that channel's contribution (Meridian, Robyn, PyMC-Marketing accept experiment calibration).
- Repeat: incrementality changes with spend, creative and competition. Re-test key channels every 6 to 12 months.
