---
name: findings-remediation
description: Produce prioritized, evidence-backed security findings, remediation plans, and verification checks.
---

# Findings, Remediation, and Retesting

Write concise but actionable findings with: ID/title, severity, confidence, affected resource, evidence/source/time, attack preconditions, impact, recommended fix, operational side effects, and verification/rollback. Prioritize exploitable exposure and identity/data-boundary failures before defense-in-depth gaps. Do not inflate severity or equate a missing best practice with a confirmed vulnerability.

For each fix, specify whether it is code, Cloudflare configuration, identity, CI/CD, or process work. Give a staged implementation order and tests that demonstrate the control. Retest the original condition, include regression cases (unauthenticated, wrong tenant/object, expired token, malformed input, preview route, cache cross-user), and record residual risk. Clearly state checks not performed and what evidence would close each gap. Never represent partial audit coverage as certification, compliance attestation, or “100% secure.”
