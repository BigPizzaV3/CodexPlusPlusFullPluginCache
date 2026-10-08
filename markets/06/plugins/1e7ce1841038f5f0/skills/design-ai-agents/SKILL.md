---
name: design-ai-agents
description: Specify reliable autonomous or semi-autonomous AI agents with objectives, tools, permissions, state, memory, handoffs, approvals, retries, observability, evaluation, and safe failure. Use for agent architecture, multi-agent workflows, AI employees, tool-using assistants, or converting a process into an agent specification.
---
# Design AI Agents
1. Define observable objective, environment, inputs, outputs, authority, risk, and definition of done.
2. Separate reasoning/workflow from external capabilities; never assume unavailable tools or data.
3. Route the smallest useful expert group with one lead, necessary support, and an independent reviewer using the shared [expert routing model](../../shared/expert-system/expert-routing-model.md). Multi-agent does not mean maximum agent count.
4. Give every specialist an explicit role contract, decision classes, required evidence, handoff, evaluation, and stop conditions. Use the shared [decision-authority model](../../shared/expert-system/decision-authority-model.md); escalate controlled-source conflicts and Class-1 decisions.
5. Specify state machine, source of truth, memory retention, tool contracts, permissions, approval gates, retries, timeouts, idempotency, and recovery. Apply the shared [Product Quality Principles](../../shared/expert-system/product-quality-principles.md) where the agent affects people, data or consequential outcomes.
6. Threat-model untrusted user, retrieved, tool, document and inter-agent context. Preserve instruction/source boundaries; prevent indirect prompt injection, unauthorized data access or exfiltration, cross-user leakage and secret exposure. A model instruction is not an authorization grant.
7. Grant each agent and tool the least capability, data scope and duration required. Define authenticated/unlocked state where relevant, and require explicit human confirmation immediately before purchases, publication, external messages, deletion, permission changes or other consequential side effects unless separately authorized by a governing workflow.
8. Define safe failure, cancellation, recovery, bounded retries, duplicate-call protection, human takeover, observable tool/action logs and privacy-preserving diagnostics. Never imply unavailable tools, identity, permissions or state.
9. Define dynamic specialist activation, task-specific expert snapshots, independent reviewers, handoffs, cost/latency limits and escalation without multiplying agents by default.
10. Define versioned prompt/model/tool/retrieval evaluation requirements for normal, empty, conflicting, unknown, adversarial, stale and tool-failure conditions. Route independent behavioral evaluation to `$evaluate-ai-systems` and durable evaluation infrastructure to `$engineer-test-and-regression-systems`; architecture self-tests cannot ratify their own material gate.
11. Return architecture, threat model, agent and role contracts, routing matrix, state diagram in text, tool/permission matrix, approval and recovery policies, evaluation contract, observability plan, rollout plan, rollback and residual risks.
