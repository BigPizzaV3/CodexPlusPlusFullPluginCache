# Integration Suite engineering reference

Scope: SAP Cloud Integration (CPI/HCI), iFlows, API Management, Cloud Connector, Destinations, Connectivity service, adapters and integration flow steps. Confirm feature availability and authentication **per tenant/runtime and adapter**. Do not assume same feature across Cloud Foundry, Edge Integration Cell, or other runtimes.

Decision guide: Cloud Integration for multi-step integration, mediation, transformations, retry and protocol bridging; API Management for policy-based API exposure, authorization, quotas, lifecycle and analytics; API-Centric Integration for its specifically documented API development/deployment features; event middleware for asynchronous decoupling. MCP Gateway is an AI tool exposure/governance concern, not a replacement for integration data flows.

Patterns: request-reply, publish/subscribe, batch, event-driven, content-based routing, fanout/multicast, splitter/gather, sequential processing, idempotent consumer, dead-letter/exception flow. Favor Content Modifier (headers/properties/XPath/expression), Router, standard mappings, and Value Mapping over scripting for simple tasks.

When discussing B2B/EDI, assess trading partner onboarding, Integration Advisor, Trading Partner Management, message standard/version, acknowledgments, partner-specific mappings, secure connectivity, retries, non-repudiation and audit. For Event Mesh and Advanced Event Mesh, clarify they are distinct offerings, and validate broker/service compatibility and event contracts.

Operations: Message Processing Logs, correlation ID, exception subprocess, selective sensitive-payload logging, JMS vs Data Store persistence, retention, alerting, DLQ/recovery, redelivery and idempotency. Never assume an internal retry is automatically safe for non-idempotent target APIs.
