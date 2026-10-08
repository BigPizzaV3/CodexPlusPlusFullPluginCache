---
name: pipeline-generator
description: Generates and validates Dataverse CI/CD quality-gate plans for versioned managed solution promotion.
---

## Architect edition scope

This edition produces local plans, checks and review artifacts only. Instructions below describing provisioning, deployment, API calls, runtime tests or publishing are plans for an authorized operator, not actions to execute. Never connect to or modify an environment through this edition. No runtime test or deployment may be claimed from generated checklists.

# Pipeline Generator
Generate assets with `python scripts/generate_delivery_assets.py blueprint.json --output delivery-assets`. Gate on lint, export/unpack, solution comparison, Solution Checker, automated tests, approval and managed import. Keep deployment credentials external to source control.
