---
name: cloudflare-security-boundaries
description: Assess tenant isolation across Cloudflare identity, storage, caching, and asynchronous execution boundaries.
---
# Cloudflare security boundaries

Apply when an application spans multiple Cloudflare products or when the data path is outside a direct D1/Hyperdrive review.

## Inputs

Use only relevant code/configuration and user-provided architecture: identity provider, Access/JWT validation, bindings, routes, storage keys, cache rules, object ownership, queues/jobs, and environment layout.

## Review workflow

1. Draw the path from request identity through authorization to each storage read/write and response.
2. Verify Access/JWT validation at the Worker boundary where applicable, then separately verify object/row authorization. Access is not proof of ownership.
3. R2: check object-key ownership, upload/download authorization, signed URL scope and expiry, overwrite behavior, and whether bearer URLs leak through logs/referrers.
4. KV: check tenant-scoped key design, namespace/binding exposure, consistency assumptions, and authorization on reads/writes; do not treat an unguessable key as the only access control.
5. Durable Objects: ensure caller authorization before forwarding requests or invoking storage operations; validate object identifiers and tenant ownership on every path.
6. Vectorize/AI Search: derive namespaces and metadata filters from authenticated server-side identity; treat filtering as data selection, not as a complete authorization boundary.
7. Cache/CDN: verify tenant/auth context cannot collide across cache keys; bypass or explicitly scope caching for personalized responses and test cache hit/miss sequences across users.
8. Queues, Workflows, scheduled jobs, and retries: preserve and validate tenant context, authorize job creation, constrain payload-controlled resource IDs, and prevent one tenant's output from reaching another.
9. Review bindings and secrets for least privilege and environment separation. Never ask the user to disclose secret contents.

## Output contract

Map each finding to the specific boundary, evidence, attacker-controlled input, possible cross-tenant consequence, recommended control, and reproducible negative test. Mark uninspected products as out of scope.

## Boundaries

Do not infer that a product provides row-level policy enforcement unless official documentation supports it. Keep recommendations product-specific and current; for uncertain or version-sensitive behavior, consult official Cloudflare documentation. No deployment or account mutation without explicit scope and authorization.
