---
name: vibe-code-security-reviewer
description: Route fast-built application reviews into focused threat, code, dependency, data, deployment, and remediation workflows.
---

# Vibe Code Security Reviewer

Use this plugin to review AI-generated, low-code, prototype, and production application code for security weaknesses.

## Review workflow

1. Establish scope: repository, routes, APIs, identities, data, deployment, external services, and environment.
2. Identify trust boundaries and attacker-controlled inputs.
3. Trace authentication, authorization, data access, mutations, uploads, outbound requests, and privileged operations.
4. Route to focused skills under `skills/`.
5. Report findings with severity, confidence, affected path, exploit preconditions, impact, evidence, fix, and verification test.
6. Separate confirmed findings from hypotheses and missing evidence.
7. Re-review the exact changed path after remediation.

Always run the API leak, authentication, and data-access checks for any application that exposes a client-side API or database. For Supabase projects, always run the Supabase RLS and Supabase API checks together; RLS alone does not determine whether a table or function is exposed through the Data API.

## Severity

Use practical severity based on exploitability, impact, exposure, privilege required, affected users, and compensating controls. Do not inflate every issue to critical. Call out attack chains when individually medium findings combine into serious risk.

## Boundaries

- Review defensively and only within the user's authorized scope.
- Do not exploit real systems, exfiltrate data, bypass controls, or create persistence.
- Never expose secrets found in code; report location and rotation need without reproducing values.
- Do not claim a clean security audit from a limited review.
