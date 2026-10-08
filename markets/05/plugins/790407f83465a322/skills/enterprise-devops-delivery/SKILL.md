---
name: enterprise-devops-delivery
description: Creates Azure DevOps or GitHub-compatible Dataverse release gates with approval, managed promotion, and rollback.
---

## Architect edition scope

This edition produces local plans, checks and review artifacts only. Instructions below describing provisioning, deployment, API calls, runtime tests or publishing are plans for an authorized operator, not actions to execute. Never connect to or modify an environment through this edition. No runtime test or deployment may be claimed from generated checklists.

# Enterprise DevOps Delivery

Generate a pipeline template with `generate_enterprise_assets.py`. Keep service connections and secrets out of the repository. Require blueprint linting, export/unpack, comparison, Solution Checker, E2E/UAT evidence, and environment approval before managed import. Use unmanaged Dev and managed Test/UAT/Production, with version, change ID, artifact hash, and tested rollback version for every promotion.
