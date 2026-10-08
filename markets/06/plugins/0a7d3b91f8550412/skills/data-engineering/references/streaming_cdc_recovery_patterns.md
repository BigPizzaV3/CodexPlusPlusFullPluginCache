# Streaming, CDC, and Recovery Patterns

## Purpose

Use for Structured Streaming, CDC ordering, checkpoints, watermarks, replay, and recovery.

# 1. Checkpoint semantics

A streaming checkpoint can contain:
- source progress/offsets;
- committed batches;
- stateful operator state;
- query metadata.

Changing/deleting it can cause the query to start fresh.

Treat it as production state.

# 2. Checkpoint rules

- unique durable checkpoint per query;
- never share one checkpoint across independent queries;
- preserve before troubleshooting destructive recovery;
- validate compatibility after stateful query changes.

If a new checkpoint is required, define replay source and duplicate handling.

# 3. Exactly-once nuance

End-to-end correctness depends on:
- replayable source/progress tracking;
- checkpointing;
- sink semantics;
- idempotency.

Do not say “Spark guarantees exactly once” without considering the sink and external side effects.

`foreachBatch` external actions may require their own idempotency.

# 4. Watermarks

Watermarks bound state and late-data handling.

Choose from:
- observed lateness;
- business tolerance;
- state/cost impact.

Do not widen/remove watermarks casually.

For stream-stream joins, event-time constraints and watermark design affect state cleanup and result behavior.

# 5. CDC ordering

Preferred ordering evidence:
1. source sequence/version/LSN;
2. source commit timestamp when reliable;
3. weaker processing/ingestion fields only as fallback.

Document limitations when no authoritative ordering exists.

# 6. Deletes

Handle delete/tombstone semantics explicitly.

Define whether:
- hard delete;
- soft delete;
- historical retention;
- downstream delete propagation.

Do not silently drop delete events.

# 7. Replay

A replay plan defines:
- source version/range;
- start/end offsets or dates;
- target scope;
- checkpoint strategy;
- idempotency;
- concurrent writers;
- validation;
- downstream reopening.

# 8. Recovery from incompatible/corrupt checkpoint

Options can include:
- compatible restart;
- selective recovery;
- backup + rebuild;
- new checkpoint + replay;
- full refresh.

Choose based on replayability, state size, RPO/RTO, and target semantics.

# 9. Backlog

If backlog grows:
- compare input vs processing rate;
- find slow stage/sink;
- inspect state/checkpoint cost;
- check source/file volume;
- check micro-batch sizing.

Scaling is justified only if efficient execution still cannot meet throughput.

# 10. Validation after recovery

Confirm:
- no lost source range;
- no duplicates;
- correct current state;
- delete/update ordering;
- backlog declines;
- state bounded;
- downstream reconciliation passes.
