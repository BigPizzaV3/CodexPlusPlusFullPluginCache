---
name: agent-tool-boundaries
description: Review AI agent tools, permissions, arguments, outputs, and action approvals for prompt-injection-driven misuse paths.
---

# Agent Tool Boundary Review

Use when an LLM can call tools, APIs, databases, browsers, code execution, or workflow actions.

## Review steps

1. Inventory tools, descriptions, authentication scopes, accessible resources, side effects, input schemas, output sensitivity, and user confirmation boundaries.
2. For each tool, ask whether attacker-controlled content can influence invocation, target, identifiers, query, body, recipient, or sequence.
3. Check authorization in deterministic application logic rather than relying on the model's decision; verify tenant/user binding, allowlists, schemas, bounds, and server-side policy.
4. Examine tool outputs as untrusted input. Check for secret minimization, provenance, cross-tenant exposure, and instruction-like output that could influence later steps.
5. Recommend least privilege, read-only defaults, narrow capabilities, independent action validation, explicit user approval for consequential changes, idempotency, audit logging with redaction, and rollback controls.
6. Design synthetic tests that prove denied operations remain denied even when context contains hostile instructions.

## Boundaries

Do not invoke tools against a live target or trigger side effects during a review. Do not expose tokens, credentials, hidden system prompts, or private records. Mark unknown enforcement as unverified rather than secure.
