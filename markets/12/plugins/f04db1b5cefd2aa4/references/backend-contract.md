# Backend work required (not implemented by this plugin update)

The plugin skill guides a session-only agent until AdNeuron MCP provides authoritative persisted state. Implement in Neon/Postgres with tenant-scoped authorization, row-level isolation, revisions, plan hashes, audit log, idempotency locks, expiration and provider reconciliation.

Proposed endpoints: `workflow_get`, `workflow_upsert_draft`, `workflow_validate`, `workflow_record_approval`, `workflow_execute`, `workflow_reconcile`, `workflow_get_audit`. None were exposed among 120 MCP tools when this package was prepared. Define schemas and permission gates before enabling.

Acceptance tests: cross-account isolation; preview-only performs zero writes; material change invalidates approval; creation paused does not authorize activation; ambiguous write cannot duplicate; Facebook-only excludes Instagram identity; Google conversion action existence is not tracking readiness; failed keyword research does not invent volumes; resume draft restores revision; actual provider readback shown after every write; account manager cannot be mistaken for serving customer.

UI integration: plugin skills can request progress cards and confirmation controls supported by the client, but cannot force a custom UI or install frontend components. A fully persistent web agent requires AdNeuron frontend implementation.
