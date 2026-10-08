---
name: end-to-end-test-orchestrator
description: Designs and records reproducible Dataverse app end-to-end tests by role, device, and accessibility requirement.
---

## Architect edition scope

This edition produces local plans, checks and review artifacts only. Instructions below describing provisioning, deployment, API calls, runtime tests or publishing are plans for an authorized operator, not actions to execute. Never connect to or modify an environment through this edition. No runtime test or deployment may be claimed from generated checklists.

# End-to-End Test Orchestrator

Generate a role test plan with `generate_enterprise_assets.py`. Test launch, navigation, read, create, update, authorization boundary, and error paths for every role; include desktop, narrow/tablet, keyboard, 200% zoom, and relevant languages. Use only approved test data and link every run to solution version, data set, and evidence.
