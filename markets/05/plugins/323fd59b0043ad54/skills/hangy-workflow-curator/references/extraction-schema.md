# Workflow Extraction Schema

Create one record per candidate:

```text
Name:
Evidence:
Trigger examples:
Inputs:
Preconditions:
Decision points:
Ordered steps:
Supporting skills/capabilities:
Outputs:
Verification:
Safety/rollback:
Known failures:
Private details to remove:
Update existing skill or create new:
Priority:
```

## Evidence rules

- Use task IDs only in transient mining notes within the user-designated scope. Do not embed them in the finished skill, reusable outputs, or public logs.
- Use actual successful steps and validation results.
- Distinguish a one-off user preference from a repeated policy.
- Treat an impressive but unverified final claim as weaker than an artifact or log.
- Keep source-specific copy, media, and credentials outside the skill.

## Candidate thresholds

Prioritize a skill when at least two of these hold:

- the workflow occurred more than once;
- it took substantial time or repeated code;
- a missed guardrail could damage user data;
- it has a stable, testable output;
- the user explicitly asked to reuse it.

Create a reference variant rather than a new top-level skill when only formatting, domain vocabulary, or output sections differ.
