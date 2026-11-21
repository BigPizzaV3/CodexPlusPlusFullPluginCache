# Pattern 9: Commercial QA Gate (PM/QS Outputs)

For any skill output that reports quantities, rates, valuations, forecasts, or event cost/time effects, run this QA gate before presenting totals.

1. **Unit consistency**
   - Check that each measured quantity uses a recognised unit (m, m2, m3, t, item, hr, day).
   - Check unit-rate compatibility (e.g., m2 cannot be multiplied by m3 rate).
2. **Currency and tax basis**
   - State currency explicitly.
   - State whether values are net/gross and whether VAT/GST is included.
3. **Baseline vs current separation**
   - Keep baseline budget/target, current forecast, and variance in separate columns.
   - Tag the data cut-off date used for the analysis.
4. **Variation status discipline**
   - Keep proposed, instructed, approved, and rejected variations separate.
   - Do not roll unapproved value into "approved" forecast totals.
5. **Rounding and reconciliation**
   - State rounding convention (recommended: 2 decimals for money, 3 for quantity).
   - Report reconciliation tolerance at summary level (recommended ±0.5%).

If any check fails, include a **QA Warning** section in the output with the failed check(s) and likely impact.
