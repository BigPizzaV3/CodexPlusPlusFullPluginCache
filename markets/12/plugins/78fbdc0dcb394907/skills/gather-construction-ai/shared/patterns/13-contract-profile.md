# Pattern 13: Contract Profile

Real contracts are amended: Z-clauses change notification periods, secondary options change
remedies, Contract Data fixes project-specific values. A **contract profile** captures this once
per project so every contract-touching skill applies the contract as executed, not the standard
form.

**File convention:** `contract-profile.md` in the working directory (one project) or
`contract-profile-<project-slug>.md` (multiple projects). Created and updated by
`$contract-profile`. Human-readable markdown with a fenced YAML block holding the
machine-readable fields:

```yaml
project: Westbury Viaduct Renewal        # must match the Gather project name
contract_family: NEC4 ECC                # NEC3/NEC4 × ECC/ECS/ECSC/ECSS, JCT SBC 2016, FIDIC ...
main_option: C
secondary_options: [X1, X5, X7, W2, Y(UK)2]
z_clause_amendments:                     # only entries that CHANGE the standard form
  ce_notification_weeks: 4               # 61.3 as amended (standard: 8)
  period_for_reply_weeks: 2
delay_damages_rate: "£8,500/day (X7)"
weather_measurements: [cumulative rainfall, days rainfall >5mm, days min temp <0C, days snow lying]
key_dates:
  - {condition: "Piers complete to deck level", date: 2026-03-31}
verified_against: "contract as executed, rev C2"
profile_date: 2026-07-07
```

**Rules for consuming skills:**
1. Before applying any contract timescale, remedy, or threshold, check for a contract profile.
   If present, its values **override** standard-form defaults, and outputs cite them as "per
   the contract profile (as amended)". Do not re-ask for values the profile states.
2. If absent, use the standard form, state the assumption prominently ("assuming the unamended
   NEC4 ECC — run $contract-profile to capture project amendments"), and continue.
3. Never invent or infer profile values. A missing field means "standard form + stated
   assumption", not a guess. Never write to the profile from a consuming skill — only
   `$contract-profile` edits it.
4. A profile whose `project` does not match the project being analysed is ignored (say so).
