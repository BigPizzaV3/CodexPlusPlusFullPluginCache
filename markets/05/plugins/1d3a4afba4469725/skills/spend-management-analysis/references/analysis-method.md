# Analysis method

Use this method after identifying the input type and audience.

## Identify the data shape

In-house or legal-ops exports usually include a firm/vendor, matter, matter type, timekeeper role, hours, rate, billed amount, and sometimes a budget or estimate.

Law-firm internal exports usually include a practice group, matter type, timekeeper role, hours, rate, billed amount, collected amount or realization, and sometimes a budget or estimate.

If the type is ambiguous, infer from the columns when the evidence is strong. A firm/vendor field usually indicates outside-counsel spend; practice-group or realization fields usually indicate firm-internal economics. Otherwise ask.

## Normalize

Map source columns to the fields the data actually supports:

- `entity`: outside firm or internal practice group
- `matter_id` and, when present, matter name
- `matter_type`
- `timekeeper_role` and optionally timekeeper name
- `hours`
- `rate`
- `billed_amount`
- `budget_estimate`, when present
- `collected_amount` or realization fields, when present
- task/activity codes and line-item descriptions, when present
- dates or period fields, when relevant to pacing or trends

Do not force a mapping where the source does not support one. Keep blanks visible and explain which analyses they prevent. Exclude expense rows from staffing ratios while retaining them in total spend.

## Staffing mix

For each comparable matter type or phase, calculate the share and ratio of partner/senior hours versus associate, paralegal, or other leveraged hours. Flag outliers only when supported by the data, such as one routine matter using materially more partner time than peer matters.

Connect the pattern to the work when line descriptions or task codes allow it. Partner-heavy strategy or negotiation may be appropriate; partner-heavy first-pass document review is more likely a leverage issue.

## Budget variance and pacing

Where a budget or estimate exists, aggregate actual spend at the correct matter or engagement level and calculate absolute and percentage variance. Rank material overruns and notable underruns.

For active matters with elapsed-time data, compare the percentage of budget consumed with the percentage of expected time elapsed. Use transparent scenarios such as flat run-rate or current-period run-rate; label projections and assumptions. Do not present a projection as an actual outcome.

If no budget exists, say budget variance cannot be assessed. A missing budget field may itself support a process recommendation, but not an invented overrun.

## Allocation patterns

Assess which firms or practice groups handle which matter types, whether routine and complex work are allocated intentionally, and whether rate or realization patterns suggest mismatched work allocation. Distinguish a matter-specific outlier from a firm-wide or systemic pattern.

## Diagnose the likely driver

For each finding, separate the observed fact from the likely explanation. Plausible drivers include:

- staffing mix or insufficient delegation
- scope expansion or estimate mismatch
- rate-to-work mismatch
- intake, scoping, or budget-control gaps
- process inefficiency
- realization or collection issues for firm-internal data

Use cautious language when the data cannot distinguish between explanations. Recommend what to confirm before acting.

## Frame for the audience

- Internal review: provide granular detail and every material flagged item.
- Outside-counsel conversation: use terse, specific, non-accusatory negotiating points and acknowledge plausible complexity or scope explanations.
- Executive or board: lead with business impact and decisions in plain language; minimize billing jargon.

## AI-leverage assessment

Assess AI fit only for work categories identified in task codes, activity codes, or line-item descriptions. Do not infer AI fit from a matter name, matter type, practice area, staffing ratio, or rate alone. When task-level evidence is absent, state that AI leverage was not assessed and identify the detail needed for a future review.

- High potential: first-pass document/discovery review, legal research summaries, and contract or clause review against a playbook.
- Medium potential: routine/template drafting, correspondence, and summarizing large document or transcript sets.
- Low potential: negotiation, court appearances, client relationship work, and case-specific strategy or judgment.

For each opportunity, name the applicable task or matter, explain why the work is or is not a fit, and state that attorney quality control and the organization’s confidentiality, privilege, and AI-use policy still apply. Never fabricate a savings estimate from billing data alone.

## Quality checks

- Reconcile reported totals to the normalized rows used in the analysis.
- Avoid double-counting matter-level budgets repeated on line-item rows.
- Check whether expenses, credits, or adjustments need separate treatment.
- Verify percentage denominators and time-period assumptions.
- Make sure each recommendation traces to a supported finding.
