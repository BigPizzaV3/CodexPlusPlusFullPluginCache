---
name: energy-analysis
description: Explain a clever-PV home's measured energy over a period, compare two periods, or analyse consumption and costs. Use when the user asks how much was produced, imported, fed in or consumed, what it cost, or how a month or year compares with another. Read-only.
---

Use the connected clever-PV MCP tools and their current schemas. Respond in the user's language. This skill only reads data: never call `set_automation_settings`, `set_home_location` or any device `set_*` tool as part of an analysis, even when a finding suggests a change. Offer the change and wait for an explicit request.

## Ground rules

- The only source for measured energy is `get_energy_data`. With `period` weekly, monthly or yearly it returns the period containing `date`: a `summary` with totals and `consolidatedIntervals` per day (weekly/monthly) or per month (yearly). Without `period` it returns one day with 5-minute power values.
- Prefer the returned `summary` for whole calendar periods. For other ranges, add up the energy values (Wh) of the consolidated day intervals that fall into the range, and say that you summed them. Never add up 5-minute power samples (W) as energy.
- Dates are calendar days in the home's time zone. Pick the period for relative dates such as "last month" from the current date and state the dates you used. `consolidatedIntervals[].date` is `dd-MM-yyyy`.
- Units: energy in Wh (convert to kWh or MWh for presentation, stating the unit), money in euro cents (ct; present as EUR with two decimals). `gridConsumptionCosts` includes energy price, grid fees and the prorated base fee and is 0 without a buy tariff. Report negative values as such; do not clamp them.
- A home or day without data returns zeros. A 0 can therefore mean "no data" as well as "nothing measured"; point this out when zeros look implausible (for example, zero consumption on a day) instead of presenting them as facts.
- A period that contains today is still running: say so and that totals will grow.
- These are measured values. Forecasts (`get_energy_forecast`, `get_solar_forecast`) are separate and must be labelled as forecasts.
- Do not compute a self-consumption rate, autarky or self-sufficiency figure. clever-PV has not defined how battery and grid charging enter this ratio; offer the underlying totals instead.

## Overview of a period

1. Call `get_energy_data` with the matching `period` and a `date` inside it.
2. Report production, grid import, feed-in, consumption and, if present, battery values from `summary`, plus costs.
3. State whether the period is complete or still running and point out days that are zero or look incomplete.

## Period comparison

1. Call `get_energy_data` once per period (for example `period: monthly` with a date in each month).
2. Compare only like with like. If one period is still running or has a different number of days with data, do not compare totals without comment: lead with per-day averages and state the day counts, for example "September so far (24 days) vs. August (31 days)".
3. Report differences as period B minus period A and percentages relative to period A. When period A is 0, give no percentage and say why.
4. Seasonal effects (PV in summer vs. winter) explain differences only as a hypothesis; say so.

## Consumption analysis

1. Take household consumption from `summary` of the matching period.
2. For which devices consumed what, read `devices` in the same response (energy in Wh, costs in ct). Device values need not add up to household consumption, because unmeasured loads are not listed.
3. For when consumption happens, use the daily view (5-minute power in W, UTC timestamps; convert to local time).
4. Separate observations (measured values) from explanations (hypotheses) and recommendations (optional, no automatic change).
