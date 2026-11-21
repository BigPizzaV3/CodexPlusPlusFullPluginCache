# Shared Format — Assumptions Table and Sensitivity Note

Used by `$cashflow`, `$cvr`, and `$cost-to-complete` wherever their
procedure says "read this file". Keep the wording and structure identical across the three so a
reader who sees one recognises the others.

## Assumptions Table

One row per parameter used anywhere in the forecast, with **exactly one** of three source
labels — nothing else: **profile** (contract or commercial profile), **user-supplied** (this
session), or **derived run rate** (calculated from the retrieved data, not stated by anyone). A
parameter with no source in one of these three categories is not a parameter this skill may use —
state it as "not stated" / "not supplied" and let the affected line degrade per that skill's own
rule, rather than inventing a value.

| Parameter | Value | Source |
|---|---|---|
| [name] | [value or "not stated"] | **profile** / **user-supplied** / **derived run rate** |

## Sensitivity Note (one line, mechanically identified — never speculative)

Identify the single parameter whose plausible one-step change moves the largest £ (or hours)
amount in the forecast — a lag shifting by one interval, a run rate recalculated on the next
period's data, a retention trigger being confirmed vs not. Compare the candidates and name only
the largest, with the amount it moves and over what change:

> The forecast is most sensitive to **[parameter]** — [one-step change] moves **[£X / N hours]**
> [between adjacent months / in the EAC], more than any other single parameter here.

If the data available cannot support this comparison (e.g. only one period of history, or no
confirmed lags/rates at all), say so plainly: **"sensitivity not computable — insufficient
[lag/run-rate/history] data"** — never name a parameter without a derivation behind it.

## "FORECAST vs recorded" labelling (state once, not per line)

State once, near the top of the output: every forward-looking value or cost figure in this
report carries the word **FORECAST** or is captioned "derived run rate"; every historical figure
it is built from is recorded/actual data. Do not repeat this caveat under every table — one
statement covers the whole document.
