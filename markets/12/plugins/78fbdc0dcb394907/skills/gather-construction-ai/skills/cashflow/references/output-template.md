# Cashflow — Output Template (Step 5)

## Header block

```
PROJECT CASH FORECAST — [Project Name]
Ref: CS-[NNN]
Data Cut-Off: [date] | Horizon: [N] months | Currency: [GBP]
Contract Profile: [found / "not found — payment terms cannot be dated"]
```

## Section order

1. **SUMMARY** — two sentences: the net cash position at the end of the horizon, and the single
   biggest driver of that position (the Step 4 sensitivity line).
2. **CASH IN** — Step 2 build-up: value run rate and its basis, the assessment → certification →
   payment phasing table, retention held/released.
3. **CASH OUT** — Step 3 build-up: cost run rate by head and its basis (or the no-ledger
   degrade), payment lags by head (or "not supplied" per line), any user-supplied accruals.
4. **THE CURVE** — the Step 4 monthly table.
5. **ASSUMPTIONS** — the Step 4 assumptions table, every parameter, every source labelled.
6. **SENSITIVITY** — the one-line note.
7. **STANDING CAVEAT**

## Standing caveat (always, unmodified)

> This is a **forecast built from stated assumptions, not a prediction** — it is internal, and
> not the accounts. Value and cost run rates are trailing averages calculated from the data
> available to the cut-off date; they say nothing about future scope changes, new compensation
> events, remeasurement, or commercial settlement, and will drift as soon as any of those occur.
> Every timing parameter is either per the contract profile, user-supplied, or a derived run
> rate — a line with none of the three available is reported as undated, never assumed. This
> document is internal — do not issue it to the other party. Ref: CS-[NNN] is a session-local
> sequence number for cross-referencing.
