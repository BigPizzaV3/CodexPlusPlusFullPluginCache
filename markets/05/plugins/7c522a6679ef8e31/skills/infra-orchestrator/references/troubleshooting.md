# Troubleshooting Module

## Method
Use: Symptoms -> Facts -> Scope -> Last-known-good -> Hypotheses -> Discriminating tests -> Evidence -> Conclusion -> Remediation -> Validation.

## Rules
- Evidence before conclusion.
- Isolation before remediation.
- Read-only before state-changing actions.
- One test should answer a specific technical question.
- State expected PASS and FAIL branches.
- Prefer high-information, low-risk tests.
- Do not restart, reboot, fail over, delete, change retention, activate zoning, upgrade firmware, or remove paths merely because it may clear the symptom.
- If root cause remains unproven, say so and define the next evidence needed.
- For vendor escalation, state exactly which logs, timestamps, job IDs, configs, dumps, or support bundles are required and why.
