## ce-quotation-chaser

**Cadence:** One-off, {{DEADLINE_DATE}} minus 5 days
**Surface:** Desktop
**Prerequisites:** `contract-profile.md` and `commercial-profile.md` (Pattern 14); `{{FOLDER}}/ce-register.md`
**Priority:** Standard (one-off — disables itself after firing)

**Instructions:**
```
This fires once, at {{DEADLINE_DATE}} minus 5 days. Read {{FOLDER}}/ce-register.md for the CE
referenced by {{CE_REF}} to confirm the quotation-instructed date, then run
$nec-deadlines against it (contract profile in this folder) to reconfirm {{DEADLINE_DATE}}
is in fact the live 62.3 deadline — do not assume the date passed to this prompt is still
correct if the register shows a later trigger.

Run $ce-quotation for {{PROJECT}} / {{CE_REF}} to check how far the quotation draft has
progressed. Price it from the commercial profile only — quantities-only for any line with no
rate, never an invented figure.
End with ACTION AVAILABLE NOW: "Draft the quotation now or agree a longer period under 62.5 —
PM silence after submission starts the 62.6 deemed-acceptance route; your own silence before
{{DEADLINE_DATE}} just loses the three weeks." No quiet-day exit — this prompt only fires once,
five days out, and the finding is always actionable by definition.
```
