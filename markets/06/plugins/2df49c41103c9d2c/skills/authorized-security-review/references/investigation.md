# Investigation and validation

## Map the system

Identify real entry points and protected resources. For each relevant surface, record who can reach it, what inputs they control, which identity/tenant/object boundaries apply, and which control should enforce the intended restriction. In source review, follow actual callers, transformations, validators, and sensitive operations. In black-box review, distinguish observed behavior from inferred implementation.

Use forward tracing from input and backward tracing from sensitive operations. Examine related routes or operations when they share a suspicious control, while staying within scope. Suitable questions include whether object ownership is enforced, role transitions preserve restrictions, a parser changes interpretation, or an input reaches an unintended destination. Select questions from the target's evidence, not a mandatory exhaustive vulnerability checklist.

## Test a hypothesis

Record expected behavior, the smallest permitted comparison that could distinguish secure from insecure behavior, and the expected evidence. Prefer a baseline/control request and a narrowly changed request using controlled accounts and data. Inspect the application effect, not merely a success status. Rule out caching, account confusion, intended public access, documented sharing, and client-only behavior.

Bound execution by program constraints. Do not automatically escalate a limited result to shell access, persistence, credential collection, broad data extraction, or disruptive load. No exploit or payload catalog is bundled in this workflow; select a permitted validation technique based on the specific hypothesis and current authorization.

## Candidate record

- Stable local finding ID and concise title
- Asset, endpoint or source path, revision when known, and timestamp
- Attacker role, preconditions, and controlled input/action
- Expected security invariant and actual failed control
- Trace from entry point through relevant transformations to the effect
- Evidence locations, source line numbers or request/response references
- Baseline comparison, mitigations, and strongest counterevidence
- Observed impact versus unproven possible extensions
- Validation method, confidence, severity rationale, and proof gaps
- Status: confirmed / plausible / rejected / deferred
- Suggested remediation and a regression-check idea

Use the program's severity convention where provided. Base severity on demonstrated impact, prerequisites, reachable privilege boundaries, and realistic likelihood. Do not manufacture a CVSS vector or label unknown deployment assumptions as proven. Missing runtime reproduction does not invalidate a complete source-backed dataflow; it does limit claims about deployment.

Deduplicate by the broken control and effective fix, preserving distinct affected operations and evidence. Do not merge findings merely because they share a CWE. Maintain honest coverage: actually reviewed/tested surfaces, excluded surfaces, deferred work, and unresolved questions. Avoid claiming exhaustive assurance or guaranteed bounty eligibility.
