---
name: solution-dependency-merge-resolver
description: Analyzes Dataverse solution dependencies and creates safe merge gates.
---

## Architect edition scope

This edition produces local plans, checks and review artifacts only. Instructions below describing provisioning, deployment, API calls, runtime tests or publishing are plans for an authorized operator, not actions to execute. Never connect to or modify an environment through this edition. No runtime test or deployment may be claimed from generated checklists.

# Solution Dependency & Merge Resolver

For parallel solution changes, compare components, dependencies, and IDs from unpacked exports. Generate the specialist pack and use `dependency-risk.md`. Block deletion, renaming, and hand-merging solution XML until migration, ownership, and rollback are reviewed.

```powershell
python scripts/generate_specialist_pack.py blueprint.json --output specialist-pack
```
