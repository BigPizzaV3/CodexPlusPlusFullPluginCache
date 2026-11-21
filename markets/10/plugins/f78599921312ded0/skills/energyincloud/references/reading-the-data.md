# Reading the data

What is normal and looks like a fault, topic by topic, and which tool field decides. No threshold in
this file is ours: where a judgement exists, the tool returns it in a named field. Where no field
exists, there is no judgement to give.

## 1. Production

- Zero at night, low in winter, low on overcast days: normal, not a fault.
- A flat top on the production curve on a sunny day is usually an export or power limit at work,
  not a loss.
- Compare production only with the comparison the tool returns (`compare_to`, `comparison`,
  highlights with a delta). Never with "a typical plant" or with a size the user quotes.
- Production at zero through the daylight hours of a whole day while the plant kept reporting is
  worth stating as an observation, with the figures; it is still not a fault you declare.
- Fields: `energy.production` (kWh) in the energy summary; the curve in the power series.

## 2. Self-consumption and self-sufficiency

- `self_consumption_pct`: share of production used on site (directly or through the battery).
- `autarky_pct`: share of consumption covered by the plant. In Italian say "autosufficienza";
  "autarchia" only as a synonym, in the energy sense, never the historical one.
- High export with low self-consumption is not waste: it means production exceeded what the house
  and battery could absorb. The economics tool is where exported energy is valued.
- Fields: `self_consumption` block of the energy summary.

## 3. Battery

- A battery that sits at 100 % for hours on sunny days is full, not stuck.
- A battery that never goes below a floor is honouring its reserve: `soc_min_pct` shows the floor
  that was actually reached; the configured reserve is not in these tools.
- Cycles: `equivalent_cycles` and `equivalent_cycles_per_day` are measured on the period. Report the
  number; do not call it high or low.
- Depth of discharge: `dod.histogram` and `mean_dod_pct` describe how the battery was used, not how
  healthy it is.
- Capacity: `capacity.measured_kwh` against `nominal_kwh`; the verdict is `consistency`.
  `not_comparable` means the nominal figure is missing, nothing more.
- Health: `soh.now_pct` and `delta_pp` over the period. A delta of 0 over a week says nothing about
  ageing; that is a question for months.
- Temperature: `conditions[].mean_c` and `rise_c` against `threshold_c` returned by the tool. Report
  the margin; do not predict.
- Imbalance may come back `NOT_SUPPORTED_BY_PLANT`: this plant does not expose it. Say so, do not
  infer anything from the absence.
- Fields: all in the battery statistics tool.

## 4. Round-trip efficiency

- `rte.assessment` is the only judgement: `normal`, `above_reference`, `below_reference`,
  `not_assessable`. Translate literally.
- `soc_corrected: true` means the figure accounts for the battery being fuller or emptier at the end
  of the period; without it a week that ends full reads as inefficient.
- Short periods distort the figure; a `LOW_PRECISION_ESTIMATE` warning says the error cannot be
  bounded. Relay it.
- Fields: `rte` block of the plant KPIs.

## 5. Energy balance

- The check adds sources (production, import, discharge) against sinks (consumption, export,
  charge) and returns the residual after expected battery losses: `net_residual_pct` against
  `tolerance_pct`, with `within_tolerance`.
- This is an indication about the numbers, never a judgement about the plant. A residual outside
  tolerance often comes from how and where energy is measured, or from a corrupted sample; plants
  with no other sign of trouble show it day after day.
- Report the residual as a note on the figures, in one sentence, without the word "fault" and
  without a cause. Do not suggest support on it.
- Fields: all in the energy balance check.

## 6. Continuity

- `uptime_data_pct` is how much of the period data arrived; `uptime_connection_pct` how much of it
  the plant was reachable. They are not production uptime.
- `outage_ranges[]` lists the gaps with `ongoing`. Only an ongoing outage is a reason to mention
  support. A short gap at the same time every day is a pattern to describe, not a fault.
- `sla` is `null` unless the user gave a target; do not invent one.
- Fields: `availability` block of the plant KPIs.

## 7. Alarms

- You see `alarm_time` (share of the period with a blocking alarm open, number and length of
  episodes) and, in the period report, `episodes_by_severity` and `active_at_period_end`.
- No codes, no names, no descriptions. Zero blocking time is "no blocking alarm in the period", not
  "no alarms ever".
- Report `episodes_by_severity` with the severity names the tool gives (warning, alarm, fault).
  Never translate a severity into "guasto" or "rotto": a fault-severity episode is an alarm of that
  class, not a verdict on the plant.
- Anything about a specific alarm is in the portal.

## 8. Data quality

- `completeness_pct` and `days_with_gaps` describe the data, not the plant. A gap is missing data;
  the plant may have run normally through it.
- Energy totals come from meters in the field that keep counting: they stay right across gaps.
  Gaps affect power curves, state of charge and live readings, not kWh totals.

## 9. Economics

- `tariff_source: market_fallback` and the `MARKET_PRICE_FALLBACK` warning mean no tariff is on
  record and public market prices were used: the euro figures are an estimate. Say so once, clearly.
- `assumptions[]` lists what was inferred (customer class, committed power, VAT). Mention the ones
  that drive the figure if the user asks how it was computed.
- `export_revenue.eur: null` with `scheme: none` means no export scheme is on record, not that the
  energy was worth nothing. `energy_value_zonal` gives the market value of the same energy.
- `bill_impact` compares the bill with and without the plant for the period. No ROI, no payback, no
  recommendation on tariffs: the tool does not compute them and neither do you.
- Fields: all in the economics report.

## 10. Peak demand

- `max_import_kw` against `no_battery_peak_kw`: the battery's `avoided_peak_kw` is what it shaved.
  Report the kW here; the euro value is in the economics report.
- Fields: `peak_demand` block of the plant KPIs.

## 11. When data is missing

`availability` on a result names the reason. Translate it and stop:
- `NOT_SUPPORTED_BY_PLANT`: this plant does not provide this figure.
- `TEMPORARILY_UNAVAILABLE`: the source did not answer now; try later.
- `OUTSIDE_HISTORY`: the period is before the data this plant has.
None of them is a fault, and none is a reason to contact support.

## 12. Warnings

- `LOW_PRECISION_ESTIMATE`: approximate figure, error not bounded.
- `MARKET_PRICE_FALLBACK`: public prices used, no tariff on record.
- `TRUNCATED`: the result was cut; say the figures cover part of the request.
Relay each in plain words, once.
