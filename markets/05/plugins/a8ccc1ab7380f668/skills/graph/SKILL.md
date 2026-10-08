---
name: graph
description: Orchestrate complex user-authorized work as an inspectable dependency graph with bounded parallelism, evidence-backed completion, adaptive approval gates, one repair cycle, and optional resumable checkpoints. Use only when the user explicitly invokes $graph, selects Graph Mode, or asks to apply the Graph Mode framework to research, audits, implementations, monitoring, or other multi-step work; never activate implicitly.
---

# Graph Mode

Graph Mode turns a complex request into an explicit execution graph: small nodes with declared dependencies, access levels, outputs, evidence requirements, and attempt limits. It schedules only ready nodes, joins parallel work deliberately, verifies the result, and stops with a clear terminal state.

It replaces an opaque “decide the next step and loop” workflow with visible control flow. The user can see what will run, what may run in parallel, what requires approval, how completion will be proved, and why the run stopped. Graph Mode changes orchestration, not the user's goal, permissions, or scope.

## How to use it

Invoke Graph Mode explicitly. Put the task after `$graph` in Codex, or select/mention Graph Mode in ChatGPT Work.

```text
$graph Audit this repository against its implementation plan.
$graph Implement the requested feature and verify it.
$graph Research these options using parallel evidence gathering.
$graph Monitor this process and report only material state changes.
```

Use it when work has meaningful dependencies, parallel research or inspection branches, a maker-reviewer handoff, deterministic verification, approval boundaries, or a need to resume. For a simple one-step request, an ordinary prompt is usually more efficient.

## How it works

1. **Bound the goal.** Preserve the requested deliverable, constraints, authority, and definition of done.
2. **Compile the graph.** Give each node an ID, dependencies, role, access level, expected output, evidence gate, and attempt limit.
3. **Announce the route.** Show the important branches, joins, verification gates, and approval boundaries before execution.
4. **Schedule ready work.** Run independent read-heavy nodes concurrently when useful; serialize overlapping writes and gated actions.
5. **Join and verify.** Reconcile branch outputs and prefer deterministic checks before model review.
6. **Repair once.** If a gate fails, diagnose it and allow one targeted repair/reverification cycle by default.
7. **Report the run.** Return the executed path, evidence, changes, skipped branches, uncertainty, and one terminal state.

Common shapes include sequential execution, parallel fan-out/join, maker-reviewer, bounded repair, human-gated actions, research synthesis, implementation, audit, and monitoring.

## Design rationale

Graph Mode is a practical, instruction-orchestrated adaptation of structured graph execution for Codex and ChatGPT workflows. Its design is aligned with the scheduler-theoretic framing in Hu Wei's paper [“From Agent Loops to Structured Graphs: A Scheduler-Theoretic Framework for LLM Agent Execution”](https://arxiv.org/abs/2604.11378): make dependencies inspectable, separate planning from execution and recovery, and bound escalation instead of relying on an open-ended agent loop.

The paper is a position paper and design proposal, not a production implementation or a report of empirical results. Treat it as conceptual grounding, not proof that every graph-shaped workflow is automatically better.

## Load the execution rules

Before constructing a graph:

1. Read [references/protocol.md](references/protocol.md) for node and state contracts.
2. Read [references/patterns.md](references/patterns.md) and select the smallest fitting pattern.
3. Read [references/verification-safety.md](references/verification-safety.md) before any write node or terminal verdict.

## Execute the graph

### 1. Bound the request

- Treat the text following `$graph` as the goal.
- Preserve stated constraints, deliverables, permissions, and definitions of done.
- Discover repository and environment facts before asking questions.
- Ask only when a missing decision materially changes the result or authority.
- Do not broaden the task merely because another graph branch would be useful.

### 2. Compile the execution graph

Create the smallest graph that can establish the requested outcome. Give every node:

- a unique ID and concise title;
- a kind, assigned role, and access level;
- explicit dependencies;
- an expected output and evidence requirement;
- an attempt limit and initial status.

Expand logical retries into new runtime node instances such as `repair-1` and `reverify-1`. Keep the executed dependency ledger acyclic even when the conceptual workflow contains a repair loop.

### 3. Announce the route

Before tool use, show a compact graph summary in commentary:

```text
Graph: scope -> [frontend-audit || backend-audit] -> reconcile -> verify -> review -> report
Gates: workspace writes allowed; external writes require approval; one repair round
```

Do not wait for graph approval when the route is safe, scoped, and already authorized. Pause only at an adaptive approval gate.

### 4. Schedule ready nodes

- Keep the root agent as controller, join owner, and final reporter.
- Run independent read-heavy nodes in parallel when doing so materially helps.
- Use no more than three worker subagents concurrently in addition to the root.
- Prefer built-in explorer behavior for investigation and worker behavior for implementation.
- Give each subagent a bounded task, allowed access, required evidence, and output contract.
- Do not let subagents delegate further work unless the graph explicitly requires it.
- Use one writer by default. Permit parallel writes only for proven-disjoint files or systems.
- Wait for every required dependency before running a join node.
- If subagents are unavailable or add more coordination than value, execute the same nodes sequentially.

### 5. Apply gates and repair bounds

- Run deterministic verification before model-based review when possible.
- Treat model review as an additional gate, never a substitute for available tests or source evidence.
- On a failed verification or review, diagnose the failure and allow one targeted repair round by default.
- After the repair allowance is exhausted, finish `FAILED` or `BLOCKED`; do not loop indefinitely.
- Pause before external writes, destructive actions, ungranted permissions, material scope expansion, or unresolved high-impact ambiguity.

### 6. Maintain state

For short runs, keep a compact ledger in the task context. Update it at joins and status changes.

For long, scheduled, resumable, or compaction-prone runs, create a checkpoint only when a suitable workspace location is already ignored by version control. Prefer `.codex/graph-runs/<run-id>/state.json` after confirming it with `git check-ignore`. Never edit ignore files solely for Graph Mode. If no safe checkpoint location exists, retain the state ledger in the task and disclose that file-backed resume is unavailable.

Validate any checkpoint with:

```bash
python3 <skill-dir>/scripts/validate_graph_state.py <state.json>
```

If the system Python cannot run the validator, use an available Python 3 runtime. The validator has no third-party runtime dependencies.

### 7. Finish with a run report

Return:

- final terminal state;
- executed path and node outcomes;
- evidence supporting completion or failure;
- changes and external actions actually performed;
- skipped, blocked, or unproven branches;
- remaining uncertainty and any required user action.

Use only `COMPLETE`, `BLOCKED`, `NEEDS_APPROVAL`, or `FAILED` as final states. Never report `COMPLETE` while required verification is missing or a required node remains unresolved.

## Keep authority explicit

- Ordinary repository reads and user-requested workspace edits may proceed under the active permission policy.
- External writes require explicit authorization in the request or a new approval at the relevant node.
- Destructive or difficult-to-recover actions require explicit authorization and exact target resolution.
- A subagent result is evidence input, not authority to expand scope or perform a gated action.
