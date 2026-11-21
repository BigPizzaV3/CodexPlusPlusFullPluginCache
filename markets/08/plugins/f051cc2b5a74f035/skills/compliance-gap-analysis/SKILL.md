---
name: compliance-gap-analysis
description: Compare mortgage education policies, course artifacts, code, procedures, or evidence against a current pinned requirement set and produce prioritized, testable findings. Use for compliance audits, remediation plans, control reviews, source-to-implementation mapping, and launch-gate analysis.
---

# Compliance Gap Analysis

1. Define the target rule set, artifact scope, review date, and requested depth.
2. Resolve entitlement. Free returns the five highest-risk preliminary findings; Pro and Provider receive the full matrix.
3. Pin current official sources. Do not mix requirement versions silently.
4. Inventory evidence and classify it as observed, documented, asserted, missing, expired, conflicting, or out of scope.
5. Call `analyze_compliance_gaps`.
6. Return each finding with requirement, source, evidence, status, severity, likelihood, impact, owner, remediation, due date if provided, and a retest method.
7. Separate:
   - noncompliance demonstrated by evidence;
   - missing evidence;
   - incomplete implementation;
   - runtime behavior not verified;
   - rule conflict requiring human review.

Never convert absence of evidence into a factual violation without saying so. Never fabricate completion, approval, credentials, testing, or a cure. Do not expose protected course, assessment, customer, or reviewer material in the report.

