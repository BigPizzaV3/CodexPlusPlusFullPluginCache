---
name: design-backend
description: Design and implement backends, data models, APIs, storage, authentication boundaries and integrations for web or mobile apps while preserving security and data integrity.
---

# Design Backend

1. Capture actual domain entities, read/write flows, consistency, data sensitivity, tenancy and permission levels. Read `../../references/backend-architecture.md` and `../../references/security-and-privacy.md`.
2. For existing systems inspect migrations, API contracts, constraints, indexes and current auth. Avoid destructive schema edits or broad data access.
3. Prefer simple typed APIs, explicit authorization per request, validated inputs, idempotency on retries, bounded pagination, standardized errors and auditability for consequential writes.
4. Choose storage based on query patterns and deployment needs; do not force Supabase/Firebase/Postgres on every project. Keep migrations reversible and test them with fixture data.
5. Use environment secret providers, never client-embedded privileged keys. Handle API errors, timeouts, retries and rate limits.
6. Integrate through real tests, confirm access controls and disclose unverified external credentials/flows.
