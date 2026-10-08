---
schema: tempest-risk-guidance/v2
auto_resolve_policies:
  - applicability: active
---

# Purpose

Codex Replay runs local replay comparisons and renders evaluation results.

# Risk Posture

Plugin-scoped changes are low risk and should be approved automatically unless they
introduce clear, concrete security vulnerabilities or destructive behavior.

# Required Inspection

Review the changed plugin files and relevant tests.
