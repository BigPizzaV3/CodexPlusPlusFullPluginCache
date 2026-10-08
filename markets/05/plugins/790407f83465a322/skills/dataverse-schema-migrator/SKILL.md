---
name: dataverse-schema-migrator
description: Plans safe Dataverse schema evolution, detects breaking changes and creates a reversible migration sequence.
---

## Architect edition scope

This edition produces local plans, checks and review artifacts only. Instructions below describing provisioning, deployment, API calls, runtime tests or publishing are plans for an authorized operator, not actions to execute. Never connect to or modify an environment through this edition. No runtime test or deployment may be claimed from generated checklists.

# Dataverse Schema Migrator
Inspect the exported baseline and intended blueprint. Classify each change as additive, data migration, breaking or destructive. Create additive components first, backfill and validate, switch consumers, then retire only with fresh explicit confirmation. Never delete fields/tables or edit solution XML by hand; export/unpack and validate after each migration.
