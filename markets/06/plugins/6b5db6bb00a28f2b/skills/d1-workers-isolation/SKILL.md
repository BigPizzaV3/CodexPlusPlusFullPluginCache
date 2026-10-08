---
name: d1-workers-isolation
description: Review tenant and row authorization in Cloudflare Workers and D1 applications.
---
# D1 and Workers isolation

Apply when a Cloudflare Worker or Pages Function reads or writes D1 data, particularly for multi-tenant applications.

## Inputs

Prefer the relevant handlers, middleware/authentication code, schema and migrations, query helpers, Wrangler bindings/environments, and tests. If these are absent, give a general checklist and identify the evidence gap.

## Process

1. State that D1 is SQLite-based and does not provide PostgreSQL-style native RLS policies; do not suggest a D1 `CREATE POLICY` switch.
2. Trace the authenticated principal from verification to a server-derived tenant/user identity. Never trust a client-supplied tenant/user ID as authorization evidence.
3. Inspect every read and write path: direct lookup, update/delete, nested resources, joins, lists, pagination, search, aggregates, exports, bulk operations, and alternate endpoints.
4. Verify tenant predicates are applied in the data operation and that updates/deletes constrain both object identity and authorized owner/tenant. Use prepared/bound SQL values for injection resistance, while explaining that parameterization does not provide authorization.
5. Review schema constraints and indexes that support ownership invariants; verify creation and ownership transfer paths cannot assign arbitrary tenants.
6. Review environment separation and bindings; prefer preview/local D1 for development and ensure production data is not accidentally selected.
7. Produce attack-focused negative tests and positive controls.

## Output

Report each finding with file/route/query evidence, severity, cross-tenant impact, confidence, minimal remediation, and a test that should fail before the fix and pass after it.

## Boundaries

Do not call a D1 app secure based only on prepared statements, authentication middleware, or a binding. Do not assume complete route coverage from a partial sample. Do not run queries or migrations against live data unless separately and explicitly authorized.
