---
name: privacy-telemetry-ingestion
description: Captures and aggregates data-minimized usage and quality events without credentials or field contents.
---

## Architect edition scope

This edition produces local plans, checks and review artifacts only. Instructions below describing provisioning, deployment, API calls, runtime tests or publishing are plans for an authorized operator, not actions to execute. Never connect to or modify an environment through this edition. No runtime test or deployment may be claimed from generated checklists.

# Privacy Telemetry Ingestion

Use `telemetry_store.py ingest` to store only allowed event types and hashed actor IDs. Reject tokens, passwords, prompts, email addresses, and field values. Use `summary` for aggregates. Apply the same server-side filters to Application Insights or SIEM exports, and enable them only after retention, access controls, and privacy approval are defined.
