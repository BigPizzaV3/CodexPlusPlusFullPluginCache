# XMemo brainstorming and review playbooks

Use these playbooks when ChatGPT helps shape reasoning or review work produced
in ChatGPT, Claude Code, Codex, GitHub Copilot, Kiro, or another agent.

## Contents

- [Brainstorm and converge](#brainstorm-and-converge)
- [Review a plan](#review-a-plan)
- [Audit progress](#audit-progress)
- [Reconcile multiple agents](#reconcile-multiple-agents)
- [Cross-agent review receipt](#cross-agent-review-receipt)

## Brainstorm and converge

1. Recall relevant goals, constraints, prior decisions, failed approaches, and
   open questions.
2. Separate divergent exploration from convergent planning.
3. Organize options by benefits, costs, risks, assumptions, reversibility, and
   evidence needed.
4. Identify contradictions with saved decisions instead of silently replacing
   them.
5. Define decision criteria and recommend a direction only when evidence
   supports one.
6. Label unresolved ideas as tentative.
7. Save only the confirmed direction, rationale, unresolved questions, and
   concrete actions; do not save the full brainstorm.

Output:

```text
Brainstorm Review
- Objective
- Relevant prior context
- Options and tradeoffs
- Assumptions requiring validation
- Risks and reversible experiments
- Recommended direction
- Unresolved questions
- Proposed XMemo updates
```

## Review a plan

Establish the source agent and artifact/version when known. Review the plan
against the user's goal, current XMemo decisions, and current evidence.

Check:

- Objective, scope, and explicit non-goals.
- Compatibility with prior decisions and constraints.
- Ordered dependencies and whether phases are independently verifiable.
- Missing edge cases, failure recovery, security, privacy, and destructive
  actions.
- Required permissions, external coordination, and deployment boundaries.
- Acceptance criteria, tests, evidence, rollback, and handoff readiness.
- Whether the plan confuses a proposal, implementation, deployment, and
  verified production outcome.

Return one verdict:

- `approved`: coherent and ready to execute; not evidence of implementation.
- `changes_requested`: direction is viable but named issues must be fixed.
- `blocked`: required facts, access, or decisions are missing.
- `rejected`: the approach conflicts with the goal or unacceptable constraints.

```text
Plan Review
- Source: <agent and artifact/version>
- Verdict
- What is strong
- Critical findings
- Missing evidence or decisions
- Required revisions in priority order
- Acceptance gate
- Recommended next action
```

Save the approved plan or durable review decision only when it will guide future
work. Record the review occurrence as an event when its history matters.

## Audit progress

Do not accept a progress summary as proof by itself.

1. Recover the approved plan, latest working state, prior reviews, and relevant
   TODOs.
2. Map each claimed completion to current evidence: files, diffs, tests, logs,
   review results, deployment state, or user confirmation.
3. Mark each item `verified`, `partially verified`, `claimed`, `stale`,
   `conflicting`, or `blocked`.
4. Distinguish local implementation, commit, push, deployment, and production
   verification.
5. Detect scope drift, skipped gates, newly introduced risk, and stale next
   actions.
6. Update working state only from the reconciled result.

```text
Progress Audit
- Source: <agent and checkpoint/version>
- Overall status
- Verified completed work
- Claimed but unverified work
- Conflicts or stale state
- Remaining acceptance gates
- Risks and blockers
- Exact next action
```

## Reconcile multiple agents

- Compare claims concept by concept, not agent by agent.
- Prefer direct evidence and explicit user decisions over confidence language.
- Prefer newer evidence only when it addresses the same scope and has not been
  superseded.
- Preserve material disagreement and ask the user when no authoritative source
  resolves it.
- Keep source attribution readable, but never treat an agent label or instance
  identifier as authentication or authorization.
- Do not expose raw boundary hashes, tokens, traces, or private metadata.

## Cross-agent review receipt

```text
XMemo coordination update
- Sources reviewed: <agents/artifacts>
- Verdict or reconciled status
- Durable decisions saved or updated
- Working state updated
- TODOs created or changed
- Conflicts left unresolved
- Next review or execution gate
```
