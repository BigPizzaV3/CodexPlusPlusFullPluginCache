---
name: cybermirror-guide
description: Guide users through CyberMirror prospective admission and continuity-guard concepts, public integration boundaries, and policy-scoped result interpretation.
---

Use this skill when a user asks whether CyberMirror fits a proposed action, wants to understand its public control or connector contract, or wants an explanation of allow, warn, block, zero-state, readiness, or audit-trace meanings.

## Workflow

1. For a new suitability question, call `cybermirror_knowledge_map` first. Explain that a meaningful prospective review needs a declared current state, proposed step, and guard policy.
2. For integration or authentication questions, call `cybermirror_control_contract`. Explain which operations belong to a separate authenticated customer workflow.
3. For connector, service-role, or retention questions, call `cybermirror_manifest` and report the published metadata exactly as returned.
4. For allow, warn, block, zero-state, readiness, or trace questions, call `cybermirror_result_interpretation_contract`. Explain the result within the supplied state and declared policy.
5. If a request combines manifest and result interpretation, call the tools in that order and keep published service metadata distinct from callable public guidance.

## Boundaries

- The public CyberMirror tools provide guidance only. They do not authenticate customers, register connectors, make live admission decisions, actuate controls, issue safety certificates, or send messages.
- Do not request, accept, or forward API keys, passwords, MFA codes, private connector data, or login credentials.
- Allow, warn, and block are policy-scoped outcomes. An allow result is not safety certification; a block result is not proof of danger, malicious intent, or legal responsibility.
- Readiness metadata, audit traces, and integrity information do not establish independent certification.
- If the user asks to connect to a production controller, register a connector, block an action, issue a certificate, or deliver a report externally, explain that it is outside this public plugin and do not call a tool.
- If the request is unrelated to CyberMirror guidance, do not activate this skill.

## Response requirements

Use returned tool data as the source of truth. State the declared input and policy scope, the meaning of the outcome, and the limit of what can be inferred. Never invent a live decision, connector state, certification, or control action.
