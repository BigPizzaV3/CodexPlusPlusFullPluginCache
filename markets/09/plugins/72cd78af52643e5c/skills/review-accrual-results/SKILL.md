---
name: review-accrual-results
description: Review SnapAccruals bonus accrual totals, employee exclusions, prorations, and validation warnings after calculation. Use when the user asks why an amount or exclusion occurred; not for ledger reconciliation or financial-statement review.
---

# Review accrual results

Use the existing SnapAccruals calculation and confirmed settings. Follow the user's requested scope; do not process a different file or change the rule without authorization.

- Read the returned aggregate amount, period, calculated/excluded counts, `exclusion_reasons`, and `review_items`. Use returned amounts as authoritative. Separate validation errors that prevent calculation from warnings that require review.
- Prefer the existing workspace's Excluded view. If chat has a valid host-provided file reference and the user requests recalculation, use `calculate_bonus_pilot` or `calculate_bonus_file` with `view='excluded'`, retaining the same rate and, for files, the same confirmed file, mapping, period, units, eligibility method, and denominator. Use pagination when requested. This recalculates; file mode fetches and processes the authorized attachment again.
- Employee detail may be supplied only to the widget. Do not pretend that UI-only rows are available in conversation. Guide the user to the displayed row or request the specific detail needed to explain it.
- Explain the supported formula: annual salary × annual bonus target ÷ 12 × accrual rate × eligible days ÷ days in month. Percentage inputs are converted to fractions for arithmetic. Use actual returned inputs for examples; label hypothetical examples clearly.
- Highlight changed settings before recalculating. Do not silently alter mappings or rates to make totals match an expectation.
- End with the unresolved exceptions relevant to the request. Results are draft supporting schedules, not approved or posted journal entries.

## Keep the result source consistent

The workspace and chat may have different access to attachments. A missing file reference in chat does not prove that no file was uploaded or calculated in the widget. Use the current widget model context or the Discuss results in chat summary to identify the source and confirmed settings. Aggregate summaries omit employee rows and file references; never reconstruct a file or invent a download URL from them.

For an existing uploaded-file result, keep the same workspace and direct the user to Step 4: Review and download → Download Excel. Do not request another upload while the workspace still has the file. If the workspace was reset or the attachment expired, ask the user to reselect the file and confirm its settings. Never use the sample tools as a fallback for an uploaded-file request. If the source is unclear, ask whether the user means their uploaded file or the fictional sample.

When inputs are marked outdated, do not describe a previous result as current. Preserve the confirmed file, mapping, period, units, eligibility method, denominator and accrual rate. A returned result or generated link is not proof that a browser download completed.
