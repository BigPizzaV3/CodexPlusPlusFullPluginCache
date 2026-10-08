# MCP Design Reference

## Purpose

Use this file when designing an MCP server/client integration.

MCP evolves quickly. Verify the current specification and SDK documentation before implementation.

As of the 2026-07-28 specification, the protocol moved to a stateless core and introduced/strengthened extension-based capabilities and authorization changes. Do not assume older session/transport guidance remains current.

# Core server primitives

## Tools
Executable functions the model can invoke.

Use for:
- actions;
- live lookups;
- external APIs;
- controlled mutations.

Design tool schemas carefully and enforce authorization server-side.

## Resources
Structured/contextual content provided to the application/model.

Use for:
- documents;
- repository data;
- reference content;
- structured context.

Resources are not a substitute for write tools.

## Prompts
Reusable user-invoked prompt/templates.

Use when the product wants curated interactive workflows/templates.

Do not expose an operation as a prompt when it is really a tool.

# MCP design questions

Before building, define:
- host/client;
- server responsibility;
- local vs remote server;
- capabilities needed;
- tools/resources/prompts;
- authentication/authorization;
- tenant/user boundary;
- schema contracts;
- caching/freshness;
- rate limits;
- errors;
- observability;
- long-running work;
- compatibility/spec version.

# Stateless core

For current implementations, verify the latest spec behavior for:
- request metadata;
- discovery;
- transport;
- routing headers;
- caching;
- server-initiated interactions;
- task extensions.

Do not copy pre-2026 session assumptions without verification.

# Authorization

Treat auth as a first-class architecture concern.

Define:
- resource server;
- authorization server;
- client identity;
- user identity;
- scopes;
- tenant/resource ownership;
- credential storage;
- token refresh;
- issuer validation where required.

The model selecting a tool is not authorization.

# Tool schemas

Use explicit JSON schemas.

Define:
- required inputs;
- enums/bounds;
- output schema;
- errors;
- side effects;
- idempotency;
- approval needs.

Keep tool catalogs understandable.

When the tool surface becomes large, use discovery/search/deferred loading mechanisms supported by the host/runtime instead of pushing everything into model context.

# Long-running work

For jobs that cannot finish within a normal tool call, use the current protocol/runtime's supported long-running task pattern.

Define:
- task identity;
- status;
- progress;
- cancellation;
- resumability;
- result retrieval;
- retention.

Do not invent a custom asynchronous protocol when a supported extension exists.

# UI / apps

If the host supports MCP Apps or another UI extension, keep UI responsibilities separate from the underlying tool/resource contract.

The server should still have clear authorization and data contracts without depending on presentation.

# Errors

Return errors that clients/agents can act on:
- invalid parameters;
- unauthorized/forbidden;
- not found;
- conflict;
- rate limited;
- transient dependency failure;
- permanent failure.

Avoid leaking internal secrets or stack traces.

# Compatibility

Record:
- MCP specification version;
- SDK/runtime version;
- optional extensions;
- deprecated features relied upon.

Test against the actual target host because hosts may support different subsets/extensions.

# Observability

Capture:
- request/tool name;
- authenticated principal;
- outcome;
- latency;
- sanitized parameters;
- error category;
- rate-limit/approval events.

Do not log credentials or sensitive resource contents by default.
