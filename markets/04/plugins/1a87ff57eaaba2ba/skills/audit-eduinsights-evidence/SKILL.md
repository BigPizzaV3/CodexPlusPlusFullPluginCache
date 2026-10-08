---
name: audit-eduinsights-evidence
description: Audit an EduInsights answer, comparison, SQL result, or research method for source provenance, release and period alignment, entity resolution, level of detail, coverage, applicability, additive measures, and unsupported causal claims. Use when the person asks to verify, review, reproduce, challenge, or quality-check education or workforce evidence.
---

# Audit EduInsights evidence

Test whether each material claim is supported by the returned evidence. Do not rerun all research automatically; inspect the existing trace first and use tools only to fill a specific audit gap.

## Audit the claims

Read [audit-checklist.md](references/audit-checklist.md). Apply every section that matches the answer.

Build a compact claim ledger with:

- the claim;
- the measure and unit;
- the entity and level of detail;
- the period and release;
- the source;
- the evidence fit;
- the coverage reason;
- the audit result.

Use `edu_get_sources` for exact release details when the trace contains Source Release IDs. Use `edu_describe_data` for relation meaning. Use `edu_run_sql` only when a missing check requires a new query and focused tools cannot answer it.

## Rate findings

Use these results:

- **Supported:** the claim matches the source, period, entity, measure, and level of detail.
- **Supported with a limit:** the evidence answers the main question, but its population, geography, or level is narrower or broader.
- **Not established:** the evidence is relevant but does not measure the claimed outcome or relationship.
- **Cannot verify:** the trace lacks the needed source, release, period, or result rows.

Do not call a bounded source invalid merely because it does not cover every product or population. Assess whether it measures the concept asked about and state its scope.

## Report the audit

Lead with the most consequential issue. Separate correctness errors from disclosure improvements. Give the smallest concrete fix for each failed check.

Finish with a short list of claims that remain safe to use and claims that should be revised or removed.
