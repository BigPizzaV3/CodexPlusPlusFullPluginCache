---
name: app-change-delivery
description: Implements and delivers new or changed Dataverse model-driven apps with inventory, impact analysis, testing, publishing, and solution ALM evidence.
---

## Architect edition scope

This edition produces local plans, checks and review artifacts only. Instructions below describing provisioning, deployment, API calls, runtime tests or publishing are plans for an authorized operator, not actions to execute. Never connect to or modify an environment through this edition. No runtime test or deployment may be claimed from generated checklists.

# App Change Delivery

Use this skill after an approved design review. Work solution-first: inventory the existing app, tables, forms, views, navigation, security, automation, dependencies, and managed/unmanaged state. Create a change plan that names component ownership, expected impact, test cases, evidence, rollout, and rollback.

Implement only through supported maker, Dataverse, or ALM surfaces; do not hand-edit solution XML. Apply least-privilege security, Microsoft-aligned form and navigation patterns, and accessibility requirements. Before release, publish, export and unpack the solution, compare it to the approved blueprint, run role-based UAT and smoke checks, record the evidence, and promote a managed version through the approved pipeline.
