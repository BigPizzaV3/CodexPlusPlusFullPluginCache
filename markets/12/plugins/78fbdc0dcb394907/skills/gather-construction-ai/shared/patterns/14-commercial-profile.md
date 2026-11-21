# Pattern 14: Commercial Profile (Rates File)

The Gather API carries no financial data — rates, order values, and allowances must come from
the user. A **commercial profile** captures them once per project so money-shaped skills
(valuation, subcontractor verification, dayworks, off-hire, material reconciliation, prelims)
can produce priced outputs instead of quantities-only ones.

**File convention:** `commercial-profile.md` in the working directory (or
`commercial-profile-<project-slug>.md`). Created and updated ONLY by
`$commercial-profile`. Human-readable markdown with a fenced YAML block:

```yaml
project: Westbury Viaduct Renewal        # must match the Gather project name
currency: GBP
retention_pct: 3
main_option: C                            # cross-checked against contract-profile.md if present
activity_rates:                           # measure/valuation rates
  - {item: "Pier Construction (Piers 3-5)", unit: m3, rate: 385.00}
  - {item: "Deck Steel Fixing", unit: t, rate: 1240.00}
labour_daywork_rates:
  - {trade: "Steel fixer", unit: hr, rate: 38.50, basis: "CECA daywork schedule 2025 +12%"}
plant_rates:
  - {item: "50t crawler crane", unit: wk, rate: 2100.00, hire: hired, offhire_notice_days: 7}
subcontract_orders:
  - {subcontractor: "FormTech Ltd", package: "Falsework", order_value: 480000, rates_basis: "SC order 0042 rev 2"}
prelims:
  staff_allowance: 6                      # heads on site per tender
  establishment_weekly: 8500.00
  tender_duration_weeks: 42
material_norms:
  - {material: "C40/50 concrete", unit: m3, waste_allowance_pct: 5}
profile_date: 2026-07-07
```

**Rules for consuming skills:**
1. Rates come from the profile or from the user in-conversation — **never invented, never
   "typical rates"**. Every priced line cites its source ("rate per commercial profile" /
   "user-supplied this session").
2. No profile (or a line-item with no rate) → produce the full output **quantities-only**,
   with the value column showing "rate not in commercial profile", and point once to
   `$commercial-profile`. A quantities-only output is complete and useful — never
   block on missing rates.
3. Only `$commercial-profile` writes the file. Consuming skills read it.
4. A profile whose `project` does not match the project being analysed is ignored (say so).
5. The file contains commercially sensitive figures: the creating skill reminds the user to
   keep it out of shared repositories (add to `.gitignore` where relevant), and outputs
   destined for the other party carry only the priced lines, not the whole rates file.
6. Where both profiles exist, `main_option`/contract family come from `contract-profile.md`
   (Pattern 13) — the commercial profile defers to it on contract mechanics.
