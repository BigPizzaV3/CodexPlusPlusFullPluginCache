---
name: cognitivedb-manage-computes
description: >-
  Select, inspect, and manage CognitiveDB Compute resources, including
  workload-based CPU/GPU and specification guidance, connection details,
  monitoring, configuration, lifecycle transitions, and deletion.
metadata:
  version: "dev-1.13.4"
---

# Manage CognitiveDB Computes

Never invent fields, enums, force flags, IDs, or transitions. Never substitute
SQL, browser, or HTTP.

## Boundaries

- Own Compute selection, inspection, and lifecycle only; do not manage data,
  Catalogs, connections, ingestion, access, quotas, or SQL files. Route GPU
  query compatibility and table design to the matching GPU-workload guidance
  Skill.
- Return endpoint details only for one exact Compute and Catalog and never claim
  that credentials are included. Use monitoring only for the current activation;
  route cross-activation investigation to Query History.
- Resolve one immutable ID and current snapshot before mutating an existing
  Compute.

## Core Instructions

- Bind the current Space and gate the exact mutation. Describe a supplied
  immutable ID directly; otherwise list and disambiguate. Stop on conflicting,
  missing, or cross-Space evidence.
- Read [create](references/create.md) for create,
  [selection](references/selection.md) for workload, CPU/GPU, or specification
  recommendations,
  [update/default](references/update-and-default.md) for update or set-default,
  [transitions](references/lifecycle-transitions.md) for start, stop, or
  suspend, and [delete/recovery](references/delete-and-recovery.md) for delete
  or any ambiguous mutation result. Load a reference when its operation becomes
  the next proposal; do not preload later references or reload an unchanged one.
- For creation, reject a duplicate name and require compatible values returned
  by the current live configuration, type, and specification tools.
- Base every recommendation on current product, specification, availability,
  sizing-guide, and configuration evidence. Preserve the selected `specCode`;
  do not invent a separate GPU-count argument or promise a capacity limit.
- For update or default selection, validate the requested value against current
  live options and show the exact diff.
- For start, stop, or suspend, read fresh state and validate the requested
  transition. Each transition requires its own confirmation.
- Confirm the exact target, change, and cost or availability impact. Execute
  once and verify the same ID with describe/list, or verify absence after deletion.
- Inspect the exact ID before retrying an uncertain mutation. Report its ID,
  effective change, final observed state, impact, and any uncertainty.

## Allowed MCP Tools

- `cognitivedb_catalog_list`
- `cognitivedb_compute_create`
- `cognitivedb_compute_delete`
- `cognitivedb_compute_describe`
- `cognitivedb_compute_endpoint_details`
- `cognitivedb_compute_global_configuration_get`
- `cognitivedb_compute_list`
- `cognitivedb_compute_monitoring_list`
- `cognitivedb_compute_set_default`
- `cognitivedb_compute_spec_list`
- `cognitivedb_compute_start`
- `cognitivedb_compute_stop`
- `cognitivedb_compute_suspend`
- `cognitivedb_compute_type_list`
- `cognitivedb_compute_update`
- `cognitivedb_space_current_get`
