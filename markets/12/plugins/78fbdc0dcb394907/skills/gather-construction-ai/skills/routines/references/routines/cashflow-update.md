## cashflow-update

**Cadence:** Monthly, {{LEDGER_DAY}} plus 2 days (after monthly-cvr has imported the new ledger)
**Surface:** Desktop
**Prerequisites:** `contract-profile.md` with the payment-mechanics fields; `commercial/cost-ledger.md` kept current (monthly-cvr does this); per-head payment lags recorded in `{{FOLDER}}/routine-state/cashflow-update/last-run.md` on the first run
**Priority:** Standard

**Instructions:**
```
Run $cashflow for {{PROJECT}} over a 3-month horizon. Payment lags per head: use the
lags recorded in {{FOLDER}}/routine-state/cashflow-update/last-run.md (recorded at first
install as user-supplied); if none are recorded, state which heads run undated and ask for the
lags once — never assume a typical term.

Compare the end-of-horizon cumulative net against last month's saved curve. If it moved by
more than {{NET_MOVE_THRESHOLD}} (e.g. £25,000), lead with the movement and its mechanically
identified driver (the skill's sensitivity line); otherwise reply in three lines ("cash curve
within threshold of last month") and stop — silence is the feature, like eac-drift.
Retention release is never assumed; forecast rows stay labelled FORECAST.
Update routine-state/cashflow-update/last-run.md with this month's curve (monthly net and
cumulative net figures) and the confirmed lags for next month's comparison.
This output is internal — never issued to the other party.
```
