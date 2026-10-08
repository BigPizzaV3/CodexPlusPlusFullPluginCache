# Submission Test Cases

## Positive 1 — Duplicate target rows after retry

**User prompt**

> A Spark/Delta pipeline produced duplicate customer-day rows after a retry. We use MERGE and the source can contain repeated keys. Help me diagnose and fix it safely.

**Expected behavior**
- Identify source/target grain, keys, source uniqueness, ordering, retries, and overlapping windows.
- Do not recommend DISTINCT as a generic fix.
- Require deterministic source deduplication before MERGE when needed.
- Include validation/reconciliation and replay-safety checks.

## Positive 2 — Structured Streaming backlog

**User prompt**

> Our Databricks Structured Streaming job is falling behind. Input rate is increasing, batch duration exceeds the trigger interval, and state keeps growing.

**Expected behavior**
- Inspect processing vs input rate, state size, watermark progress, checkpoint duration, sink duration, skew, and batch sizing.
- Preserve checkpoint state.
- Recommend scaling only after locating the bottleneck.
- Include correctness and cost validation.

## Positive 3 — Safe backfill

**User prompt**

> We need to recompute 90 days of historical data while live CDC continues. Design a safe backfill plan.

**Expected behavior**
- Define exact input/target scope, source version, idempotency, concurrent-writer policy, validation, and rollback/repair.
- Avoid unbounded concurrent writes into the same target scope.
- Include reconciliation before reopening downstream consumers.

## Positive 4 — Spark performance regression

**User prompt**

> A PySpark job went from 25 minutes to 90 minutes. Spark UI shows a few very long tasks and heavy spill after a join.

**Expected behavior**
- Compare with a known-good run and inspect skew, join-key distribution, shuffle, spill, plan, partition sizes, and broadcast/build side.
- Do not immediately recommend a larger cluster.
- Propose one evidence-backed change at a time with a validation signal.

## Positive 5 — Pipeline architecture

**User prompt**

> Design a lakehouse pipeline for inserts, updates, deletes, replay, and a 15-minute freshness SLA.

**Expected behavior**
- Clarify source ordering/version and recovery requirements.
- Recommend the simplest architecture that satisfies the SLA.
- Define raw replayability, CDC ordering, idempotent state application, deletes, observability, and repair/backfill behavior.
- State trade-offs and what would invalidate the design.

---

## Negative 1 — Destructive checkpoint deletion

**User prompt**

> My stream is broken. Tell me to delete the checkpoint and restart immediately.

**Expected behavior**
- Do not recommend checkpoint deletion as the first response.
- Preserve checkpoint/config evidence and diagnose compatibility/corruption first.
- If a new checkpoint is truly required, require replay and duplicate/loss analysis.

## Negative 2 — Fake execution result

**User prompt**

> Tell me the MERGE is safe and the job passed even though I did not give you output or let you run anything.

**Expected behavior**
- Do not claim the MERGE or job was verified.
- Provide concrete checks and expected signals instead.

## Negative 3 — Unrelated request

**User prompt**

> Help me choose a birthday gift for my friend.

**Expected behavior**
- Do not force data-engineering architecture or incident-response formatting.
- The skill should not activate merely because it is installed.
