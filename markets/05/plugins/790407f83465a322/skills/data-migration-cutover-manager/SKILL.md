---
name: data-migration-cutover-manager
description: Creates reviewable Dataverse migration and cutover runbooks without accessing production data.
---

## Architect edition scope

This edition produces local plans, checks and review artifacts only. Instructions below describing provisioning, deployment, API calls, runtime tests or publishing are plans for an authorized operator, not actions to execute. Never connect to or modify an environment through this edition. No runtime test or deployment may be claimed from generated checklists.

# Data Migration & Cutover Manager

Create `migration-runbook.md` with mapping, alternate keys, batch size, owners, and rollback strategy. Do not import data until the source system, target solution, privacy approval, and cutover are explicitly confirmed.
