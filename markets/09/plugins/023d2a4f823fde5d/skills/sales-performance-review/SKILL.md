    ---
    name: sales-performance-review
    description: Analyze 33CRM sales performance using lead-cohort metrics, deal reports, owner breakdowns, and the current pipeline. Use for sales reviews, conversion reviews, owner/team performance, booked value, amount paid, and pipeline health questions.
    ---

    Use this skill for sales performance analysis.

Workflow:
1. Resolve the date window.
2. Call `sales_summary` for lead-cohort counts, conversion-related rates, source breakdowns, and stage breakdowns.
3. Call `get_sales_report` for period deals, booked value, current amount paid to date, by stage and owner.
4. Call `pipeline_summary` when the user asks about pipeline health or current stage distribution.
5. Call `list_sales_reps` only when you need the current active sales-rep directory for context.
6. If the user asks for a specific deal, use `list_deals` or `get_deal`.

Output:
- Sales summary
- Lead funnel metrics
- Deal and money metrics
- Owner/team breakdown
- Pipeline observations
- Risks / attention items supported by the data
- Metric caveats

Rules:
- Leads and deals are different entities; never merge their counts or rates as if they were the same cohort.
- `booked_value` is agreed deal value, not recognized revenue.
- `amount_paid_to_date` is not a dated cash-receipts metric.
- Current pipeline stages are a snapshot and are not necessarily the stage held during the selected period.
- Avoid subjective employee rankings unless the user explicitly asks for a factual comparison; present documented metrics rather than unsupported judgments.
- Reply in the user's language.
- Read-only only.
