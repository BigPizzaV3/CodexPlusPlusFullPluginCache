---
name: postgres-rls-hyperdrive
description: Design and review PostgreSQL row-level security policies used through Cloudflare Hyperdrive.
---
# PostgreSQL RLS with Hyperdrive

Apply when a Cloudflare Worker accesses PostgreSQL through Hyperdrive or another PostgreSQL connection.

## Inputs

Request schema, policies, grants/roles, migration code, query/transaction code, and Hyperdrive connection/pooling setup when relevant. Redact credentials and personal data.

## Process

1. Confirm PostgreSQL (not D1) is the database and identify tables and intended tenant/subject boundary.
2. Review RLS enablement and policy coverage for SELECT, INSERT, UPDATE, and DELETE as appropriate; reason about both `USING` and `WITH CHECK`, default-deny behavior, and policy composition.
3. Check ownership, superuser, `BYPASSRLS`, table-owner behavior, and whether `FORCE ROW LEVEL SECURITY` is appropriate. Verify the application role is not privileged enough to bypass the intended policies.
4. Trace how the Worker establishes request identity and passes it into a database transaction/query. Treat user-provided tenant claims as untrusted until validated.
5. Account for Hyperdrive transaction pooling: establish request context within the same transaction/query scope needed by policies; never assume connection session state persists when a pooled connection is returned. Prefer transaction-local context where supported and test pool reuse between tenants.
6. Review prepared statements, transaction boundaries, errors, and query paths so RLS is defense in depth rather than a substitute for sound application authorization.
7. Provide cross-tenant, anonymous, role-bypass, policy-operation, and pooled-connection contamination tests.

## Output

Provide policy snippets only when schema/identity details are sufficient; otherwise present a template with explicit placeholders. State assumptions, role bypass conditions, pooling caveats, and tests.

## Boundaries

Do not say that enabling RLS alone secures a database. Do not apply migrations or modify production roles without explicit authorization and a reviewed rollback plan. Never handle secret values.
