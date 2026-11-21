# API-Centric Integration, MCP Gateway and agentic AI

First verify current product names, license/service plan, region, runtime, release maturity and documented features. Never assert a feature exists because it is a plausible design.

API-Centric Integration: document actual artifact types, deployment environment, connectivity to backend, transformations, API policies, lifecycle/versioning, traffic control, observability and artifact promotion only after verifying docs. Compare with Cloud Integration iFlows and API Management proxies at responsibility boundaries, rather than asserting universal equivalence.

MCP: a protocol for AI clients to discover/invoke tools provided by MCP servers. Gateway is an intermediary policy and exposure component **where officially supported**. A2A is agent-to-agent coordination; REST/OData/SOAP are backend API protocols; iFlow orchestration moves business messages. They are not interchangeable.

Illustrative flow (not a guaranteed SAP-supported topology): agent client → authenticated MCP interface / gateway → policy and scope enforcement → approved tool connector or backend API → SAP service; audit invocation metadata with redaction, request id, actor, scope, policy decision, tool and backend outcome. Check MCP transport, auth, endpoint URLs and tool schema fields from documentation rather than inventing.

Tool contract checklist: name/description, JSON schema inputs and outputs, errors, pagination, timeouts, limits, idempotency key, dry-run option, tenant boundary, data classification, scopes, audit and human-approval policy. Default to read-only list/get/status tools; segregate production write tools.

Agent governance: explicit allowlist; policy engine before action; least-privilege tokens and tenant isolation; tool calls subject to confirmation for writes; tamper-evident audit log is a design goal, not something automatically provided; protect against prompt injection through tools and retrieval content. Treat tool discovery as untrusted metadata.

For Copilot Studio, ChatGPT, Joule and custom agents, validate each client's actual transport/auth capabilities and licensing, and identify any bridge as a custom component. Do not imply native connectivity merely because a standards-based approach is possible.
