---
name: environment-drift-detector
description: Detects Dataverse solution drift between Dev, Test and Production using exported solution baselines.
---

## Architect edition scope

This edition produces local plans, checks and review artifacts only. Instructions below describing provisioning, deployment, API calls, runtime tests or publishing are plans for an authorized operator, not actions to execute. Never connect to or modify an environment through this edition. No runtime test or deployment may be claimed from generated checklists.

# Environment Drift Detector
Export/unpack the same solution from each confirmed environment and compare component inventories, versions, publishers, forms, views and relationships. Report drift; do not overwrite either environment automatically. Resolve by promoting the approved managed package.
