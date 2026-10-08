---
name: account-health-triage
description: Diagnose the current health of an authorised Google Ads account through Adszy MCP. Use for account check-ups, "what needs attention", budget-pacing, disapproval, anomaly, audit, or sudden-performance questions.
---

# Account Health Triage

Use Adszy's read-only tools to separate verified issues from healthy or unobserved areas.

## Workflow

1. If the account is ambiguous, call `list_ad_accounts` and ask the user to choose. Never guess an account.
2. Establish the requested window. Use `get_account_summary` for headline performance, then call only the relevant diagnostic tools:
   - `get_budget_pacing` for spend delivery.
   - `get_anomalies` for detected changes.
   - `get_disapprovals` for serving restrictions.
   - `get_account_audit` for the latest cached structural audit.
3. Treat a cached audit window as authoritative. If `windowMismatch` is true, state its actual window and use `get_account_summary` for the user's requested period.
4. Distinguish:
   - verified issue;
   - healthy observed surface;
   - no data or unvalidated surface.
5. Return a prioritised brief: issue, evidence, likely impact, and next safe action.

## Guardrails

- Never claim Adszy changed the account; every MCP tool is read-only.
- Do not infer causation from correlation. Label plausible explanations as hypotheses.
- State dates, currency, and material sample limitations.
- Do not describe an empty result as healthy.
- Keep account identifiers out of the prose unless the user needs them to disambiguate.
