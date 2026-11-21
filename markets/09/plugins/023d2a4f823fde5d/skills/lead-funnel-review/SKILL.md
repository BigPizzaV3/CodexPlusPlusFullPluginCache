    ---
    name: lead-funnel-review
    description: Review the 33CRM lead funnel, lead sources, qualification/win/loss outcomes, pipeline-stage distribution, and recent lead records. Use when the user asks about lead generation quality, funnel health, conversion, sources, or leads needing operational attention.
    ---

    Use this skill for lead-funnel questions.

Workflow:
1. Resolve the requested period.
2. Call `sales_summary` first for lead-cohort totals, qualified/attended/won/lost metrics, by-stage and by-source breakdowns.
3. Use `list_leads` when the user needs the underlying recent leads, workflow status, source, stage, or owner.
4. Use `get_lead` only after identifying a specific lead and when stage history is needed.
5. Use `pipeline_summary` only as supplemental current deal-pipeline context; do not present it as the lead funnel.

Output:
- Funnel overview
- Source mix
- Stage / outcome mix
- Leads needing follow-up based on returned workflow state when requested
- Data quality / pagination notes
- Clear distinction between lead funnel and deal pipeline

Rules:
- Do not infer ad attribution from a lead source beyond what the CRM explicitly stores.
- Do not infer reasons for won/lost outcomes from fields that are not returned.
- Do not expose or imply clinical information.
- Reply in the user's language.
- Read-only only.
