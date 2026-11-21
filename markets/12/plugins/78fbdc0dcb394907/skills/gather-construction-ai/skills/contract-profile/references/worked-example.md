# Worked Example

**EXAMPLE ONLY — illustrates the output format, not a real project.** An NEC4 ECC Option C
project with a Z-clause amendment shortening the clause 61.3 notification window from 8 weeks
to 4 weeks would produce `contract-profile.md` containing the header below, followed by the
fenced YAML block:

> # Contract Profile — Westbury Viaduct Renewal
>
> Captured 2026-07-07 from the contract as executed (rev C2). This is a record for skill
> consumption, not legal advice — see the project's legal advisers for interpretation disputes.

```yaml
project: Westbury Viaduct Renewal
contract_family: NEC4 ECC
main_option: C
secondary_options: [X1, X5, X7, X18, Y(UK)2, W2]
z_clause_amendments:                    # only entries that CHANGE the standard form
  ce_notification_weeks: 4              # 61.3 as amended (standard: 8)
delay_damages_rate: "£8,500/day (X7)"
weather_measurements: [cumulative rainfall, days rainfall >5mm, days min temp <0C, days snow lying]
key_dates:
  - {condition: "Piers complete to deck level", date: 2026-03-31}
verified_against: "contract as executed, rev C2"
profile_date: 2026-07-07
```

> Notes: no amendment to the period for reply, programme submission interval, or payment
> periods was reported — standard NEC4 defaults apply. No pain/gain share percentages were
> provided — ask the commercial manager before running cost-share calculations.
