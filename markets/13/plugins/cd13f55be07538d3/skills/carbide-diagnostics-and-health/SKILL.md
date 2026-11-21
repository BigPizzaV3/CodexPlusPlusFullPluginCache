---
name: carbide-diagnostics-and-health
description: Diagnose Carbide setup, booking, integrations, records, and background jobs using health checks and behavioral evidence. Use when explaining why Carbide behaved a certain way or what setup remains incomplete.
---

# Carbide diagnostics and health

1. Start with `list_health_check_issues` for setup gaps or the narrow evidence tool matching the reported behavior.
2. Use `search_behavioral_knowledge` to find the relevant Carbide rule, then `get_behavioral_knowledge` for the exact maintained explanation.
3. Correlate rules with current evidence using diagnostic record history, booking evidence, integration evidence, or background-job evidence. Keep organization and record IDs exact.
4. State whether each conclusion is a documented rule, an observed record, or an inference. Include missing evidence and asynchronous timing when relevant.
5. Diagnose first. Do not change settings or retry external work unless the user separately asks and the needed configuration scope is granted.

Diagnostic tools may be hidden by feature flags or role. Do not infer access to another organization when evidence is unavailable.
