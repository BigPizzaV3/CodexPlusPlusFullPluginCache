# Workflow Patterns

## Contents

- Selection rules
- Sequential
- Fan-out and join
- Maker-reviewer
- Bounded repair
- Human gate
- Research, audit, implementation, and monitoring

## Selection rules

Choose the smallest pattern that proves the requested outcome. Combine patterns only when their control-flow benefit exceeds their coordination cost.

## Sequential

```text
scope -> execute -> verify -> report
```

Use for small tasks with one clear path. Do not spawn subagents merely to make the graph appear sophisticated.

## Fan-out and join

```text
scope -> [explore-a || explore-b || explore-c] -> reconcile -> report
```

Use for independent research, repository areas, documents, or risk dimensions. Give each branch non-overlapping scope and a common evidence-packet format. The root owns reconciliation.

## Maker-reviewer

```text
scope -> maker -> deterministic-check -> reviewer -> report
```

Use when correctness benefits from a fresh skeptical pass. Give the reviewer the task contract, produced artifact, and raw verification evidence; do not leak the maker's confidence or desired verdict.

## Bounded repair

```text
maker-1 -> verify-1 -> repair-1 -> reverify-1 -> report
```

Create repair nodes only after a specific failed gate. Make the repair target the diagnosed failure. Default to one repair round. Runtime node IDs remain distinct so the ledger is acyclic.

## Human gate

```text
prepare -> approval -> external-action -> verify-action -> report
```

Prepare a reviewable proposal before requesting approval. Include the exact target, effect, and recovery characteristics. Do not treat silence as approval.

## Research

```text
scope -> [source-streams] -> compare -> challenge -> synthesize
```

Separate source gathering from interpretation. Prefer primary sources for technical claims and current sources for unstable facts. Record uncertainty and disagreement.

## Audit

```text
authority -> [evidence-streams] -> reconcile -> deterministic-checks -> independent-review -> report
```

Keep audits read-only unless the user separately authorizes changes. Compare authoritative plans or requirements with actual evidence. Distinguish complete, partial, missing, blocked, and unproven work.

## Implementation

```text
scope -> inspect -> plan-route -> implement -> test -> review -> bounded-repair? -> final-test -> report
```

Use one writer by default. Parallelize read-only inspection and tests when independent. Never let review success replace final deterministic verification.

## Monitoring

```text
inspect -> classify -> no-change: stop
                    -> change: analyze -> notify-or-approval
```

Define cadence, change criteria, evidence freshness, stop condition, and authorized actions. Do not let monitoring silently become mutation.
