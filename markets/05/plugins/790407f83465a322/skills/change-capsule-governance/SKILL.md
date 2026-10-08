---
name: change-capsule-governance
description: Creates traceable Dataverse change capsules for approval, delivery, and rollback.
---

## Architect edition scope

This edition produces local plans, checks and review artifacts only. Instructions below describing provisioning, deployment, API calls, runtime tests or publishing are plans for an authorized operator, not actions to execute. Never connect to or modify an environment through this edition. No runtime test or deployment may be claimed from generated checklists.

# Change Capsule Governance

Run `python scripts/generate_change_capsule.py blueprint.json execution-manifest.json --output capsule`. A capsule binds the change ID, target, solution, approval, blueprint hash, and manifest hash to the same quality gates. Add the exported artifact hash and link the prior managed solution as the rollback reference.
