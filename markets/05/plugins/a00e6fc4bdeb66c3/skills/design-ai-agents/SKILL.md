---
name: design-ai-agents
description: Specify reliable autonomous or semi-autonomous AI agents with objectives, tools, permissions, state, memory, handoffs, approvals, retries, observability, evaluation, and safe failure. Use for agent architecture, multi-agent workflows, AI employees, tool-using assistants, or converting a process into an agent specification.
---
# Design AI Agents
1. Define observable objective, environment, inputs, outputs, authority, risk, and definition of done.
2. Separate reasoning/workflow from external capabilities; never assume unavailable tools or data.
3. Route the smallest useful expert group with one lead, necessary support, and an independent reviewer using the shared [expert routing model](../../shared/expert-system/expert-routing-model.md). Multi-agent does not mean maximum agent count.
4. Give every specialist an explicit role contract, decision classes, required evidence, handoff, evaluation, and stop conditions. Use the shared [decision-authority model](../../shared/expert-system/decision-authority-model.md); escalate controlled-source conflicts and Class-1 decisions.
5. Specify state machine, source of truth, memory retention, tool contracts, permissions, approval gates, retries, timeouts, idempotency, and recovery.
6. Define dynamic specialist activation, task-specific expert snapshots, independent reviewer agents, handoffs, logs, cost/latency limits, privacy, injection resistance, and human escalation.
7. Build role-specific and system-level evaluation cases for normal, empty, conflicting, adversarial, stale, and tool-failure conditions.
8. Return architecture, agent and role contracts, routing matrix, state diagram in text, tool matrix, policies, eval suite, rollout plan, and residual risks.
