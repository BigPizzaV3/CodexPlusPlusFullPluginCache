---
name: ai-governance-guard
description: Adds human-in-the-loop, confidence, prompt/output logging and deterministic fallbacks to AI-assisted Dataverse delivery.
---

## Architect edition scope

This edition produces local plans, checks and review artifacts only. Instructions below describing provisioning, deployment, API calls, runtime tests or publishing are plans for an authorized operator, not actions to execute. Never connect to or modify an environment through this edition. No runtime test or deployment may be claimed from generated checklists.

# AI Governance Guard
Treat AI output as untrusted draft. Validate against blueprint, require human confirmation for writes, log intent/change IDs without secrets, and fall back to a reviewed deterministic plan when confidence or evidence is insufficient.
