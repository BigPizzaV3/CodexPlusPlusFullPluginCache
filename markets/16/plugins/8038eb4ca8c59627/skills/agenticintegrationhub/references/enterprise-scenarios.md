# Enterprise agent integration scenarios

## Agent and task routing

For a support request, authenticate the user and tenant, classify the bounded task, filter eligible agents by permissions and capability, and route to an approved support or operations agent. Define structured delegation, deadlines, maximum hops, completion evidence, and human escalation. An agent cannot expand its permissions by delegating.

## MCP gateway and tool routing

Expose narrow approved tools for CRM lookup, ERP order status, ITSM tickets, and document search. Filter discovery and invocation by caller and tenant. Resolve namespaced tools using registry metadata and contract versions. Route only to allowlisted healthy backends. Use distinct downstream credentials and prevent arbitrary URL routing. A gateway is optional when a direct server connection meets the requirement.

## API-to-AI workflow

Wrap a documented business API as a typed tool. Validate schemas, authorization, result limits, sensitive fields, pagination, and rate limits. Have the agent choose among approved operations while deterministic code enforces policy. Treat upstream content as data, not instructions.

## Events and long-running work

For asynchronous document or operational tasks, distinguish queue acceptance from completion. Use durable operation identifiers, correlation, bounded retries, cancellation where supported, deduplication, and observable terminal state. Do not promise exactly-once delivery across independent services.

## Cross-platform writes

Before creating a ticket or order, establish the authorized target, identity, validated input, write impact, idempotency strategy, and applicable approval. After an ambiguous timeout, reconcile with the original system before retrying. Failover must not duplicate a transaction in another business system.

## Acceptance checks

Check cross-tenant denial, unauthorized agent/tool discovery, invalid schema, tool-name collision, stale registry entries, upstream throttling, prompt injection in retrieved text, excessive delegation, cancellation, and ambiguous write outcomes. Label tests as proposed, run, passed, failed, or blocked using actual evidence.
