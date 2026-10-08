---
name: documentation-generator
description: Generates maintainable Dataverse app admin guides, user guidance, data dictionaries and release documentation from blueprints and solution exports.
---

## Architect edition scope

This edition produces local plans, checks and review artifacts only. Instructions below describing provisioning, deployment, API calls, runtime tests or publishing are plans for an authorized operator, not actions to execute. Never connect to or modify an environment through this edition. No runtime test or deployment may be claimed from generated checklists.

# Documentation Generator
Generate a concise baseline with `python scripts/generate_app_documents.py blueprint.json --output app-guide.md`. Supplement it with actual logical names from the validated export, security matrix, UAT evidence, deployment/rollback and known limitations. Never claim an untested feature works.
