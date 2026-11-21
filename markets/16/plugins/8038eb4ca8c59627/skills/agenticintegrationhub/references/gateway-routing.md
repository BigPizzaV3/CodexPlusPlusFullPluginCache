# Gateway and routing design

Specify the control plane (registration, policy, versions, secrets, lifecycle) separately from the data plane (discovery, invocation, streaming, errors). Do not expose management APIs as ordinary agent tools by default.

For each proposed route, record:

| Field | Required decision |
| --- | --- |
| Tool identifier | Unique namespace and operation |
| Contract | Approved schema and compatible version |
| Upstream | Approved endpoint and server identity |
| Eligibility | Caller, tenant, roles, scopes, environment |
| Data handling | Sensitivity, redaction, residency |
| Execution | Deadline, size limits, concurrency, quotas |
| Failure policy | Transient retry count, circuit breaking, fallback |
| Side effects | Read/write impact, backend idempotency, approval needs |
| Evidence | Trace ID, route version, decision, outcome, latency |

Use this decision sequence:

1. Authenticate the caller and establish trusted tenant context.
2. Resolve the approved tool identity and exact contract version.
3. Filter candidates by tenant isolation, permissions, policy, residency, and compatibility.
4. Validate input and enforce limits.
5. Select a healthy eligible route using deterministic rules where sufficient.
6. Authorize the concrete invocation and obtain appropriate downstream credentials.
7. Invoke with bounded execution and record an audit event without secrets.
8. Validate and sanitize the result; return protocol-compatible errors.

Apply health or latency ranking only after policy filtering. If no eligible route remains, return a controlled failure. Never select a more privileged route to improve availability. Treat the route registry as controlled configuration, not model-generated truth.

For sessionful or streaming versions, verify affinity, cancellation propagation, reconnect behavior, and state handling. For stateless versions, verify request-level metadata and authorization. Do not transpose assumptions between them.

Cache discovery only with identity/tenant/policy/version-aware keys and invalidation. Cache results only when authorization, data sensitivity, and freshness permit; avoid cross-tenant or sensitive response caching.

Test unauthorized discovery/invocation, tool collisions, stale contracts, wrong token audience, cross-tenant requests, prompt injection in tool results, malicious upstream destinations, expired credentials, throttling, cancellation, upstream outage, ambiguous write timeout, and duplicate execution. Use controlled environments and synthetic data.
