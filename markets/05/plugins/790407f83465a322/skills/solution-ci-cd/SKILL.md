---
name: solution-ci-cd
description: Governs Dataverse solution versioning, source control, validation, managed promotion, rollback and release notes.
---

## Architect edition scope

This edition produces local plans, checks and review artifacts only. Instructions below describing provisioning, deployment, API calls, runtime tests or publishing are plans for an authorized operator, not actions to execute. Never connect to or modify an environment through this edition. No runtime test or deployment may be claimed from generated checklists.

# Solution CI/CD
Use unmanaged source in Dev and managed packages downstream. Export/unpack after every metadata change, run Solution Checker and blueprint validation, version deliberately, then promote with an import log and prior managed package retained for rollback. Never deploy directly from an untracked Default Solution.
