# Behavior map: Cloudflare Data Security

| User input | Workflow | Output |
|---|---|---|
| “Enable RLS” for D1 | Correct the premise; identify D1/Workers boundary; request routes/schema/auth context as needed | D1-specific application-layer tenant isolation plan; no false claim of native D1 RLS |
| PostgreSQL RLS / Hyperdrive question | Identify database role, table, policy, transaction/pooling context | Policy and pooling review with missing evidence and bypass risks |
| Cloudflare architecture or code/config review | Inventory identity → authorization → data path → binding/storage → cache/background paths | Evidence-linked findings ranked by severity, impact, confidence, and remediation |
| Storage-specific isolation question | Route to applicable D1, R2, KV, Durable Objects, Vectorize/AI Search, cache, queue/job, or Access guidance | Product-specific controls and negative-test cases; distinguish authn from authz |
| Request to apply/deploy fixes | Explain proposed diffs and required approvals; do not mutate production unless user explicitly requests and scope is clear | Safe staged implementation plan or requested code changes, with validation and rollback guidance |
| Missing/ambiguous context | Ask only for details that materially change the assessment | Explicit assumptions; unknowns remain unknown rather than being silently treated as safe |
