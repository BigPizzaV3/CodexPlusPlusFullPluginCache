---
name: performance-profiler
description: Assesses Dataverse forms, views, subgrids and volume against an explicit performance budget.
---

## Architect edition scope

This edition produces local plans, checks and review artifacts only. Instructions below describing provisioning, deployment, API calls, runtime tests or publishing are plans for an authorized operator, not actions to execute. Never connect to or modify an environment through this edition. No runtime test or deployment may be claimed from generated checklists.

# Performance Profiler
Run `python scripts/scan_unpacked_solution.py <unpacked-solution> --json`. Check form control count, view width, subgrids, scripts and representative volume. Recommend smaller forms/views and server-side filtering; report evidence rather than inventing timing numbers.
