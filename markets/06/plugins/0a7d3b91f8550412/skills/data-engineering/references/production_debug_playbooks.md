# Production Debug Playbooks

## Purpose

Use this file for active incidents, failed pipelines, data-quality regressions, Spark failures, Airflow scheduling problems, streaming backlog, and sudden runtime/cost changes.

These are diagnostic starting points, not universal answers.

# Incident method

1. Preserve evidence before restarting, clearing state, deleting checkpoints, or changing compute.
2. State one dominant working hypothesis.
3. Run the smallest decisive check first.
4. Separate reversible containment from permanent fix.
5. Before replay/backfill, assess duplicate, loss, ordering, and downstream risk.
6. Stop exploring lower-probability branches once evidence confirms the cause.
7. If correctness/SLA are unaffected, prefer monitoring over speculative change.

# 1. Executor OOM / join failure

## Most likely
Skewed/oversized partitions, unsuitable join strategy, or memory pressure from data shape.

## Check first
- Spark UI failed/longest stage;
- max vs median task duration;
- spill/shuffle/input size;
- physical plan;
- join-key distribution;
- null/default hot keys;
- broadcast/build side.

## Containment
- narrow the affected input window if semantics allow;
- isolate pathological hot keys;
- temporary compute increase only after evidence is preserved.

## Permanent fix
Choose evidence-backed action:
- AQE/skew handling;
- hot-key isolation/salting;
- earlier filtering/projection;
- correct join strategy;
- justified repartitioning;
- remove unnecessary cache pressure.

## Validate
No OOM/executor loss, reduced skew/spill, same business result, acceptable cost.

# 2. Spark job suddenly slow

Compare with the last known-good run.

Check:
- critical stage;
- physical plan changes;
- input rows/bytes;
- shuffle;
- spill;
- task/file count;
- lost pruning;
- changed stats/clustering;
- source growth.

Fix only the stage explaining the regression.

If SLA and cost remain acceptable, define an action threshold instead of tuning speculatively.

# 3. Duplicate target data

## Most likely
Non-idempotent retry, duplicate source keys, overlapping windows, replayed artifacts, or ambiguous MERGE input.

## Check first

```sql
SELECT business_key, COUNT(*) AS row_count
FROM target_table
GROUP BY business_key
HAVING COUNT(*) > 1
ORDER BY row_count DESC;
```

Then correlate duplicates with:
- retries/reruns;
- overlapping schedules;
- repeated files/events;
- source uniqueness;
- MERGE keys/order.

## Containment
Pause exact-count consumers, quarantine scope, stop retries if they amplify damage.

## Permanent fix
Deterministic source dedupe, stable key/version, replay-safe windows, processed-artifact ledger, idempotent side effects.

# 4. Missing late/out-of-order data

## Check
- event time;
- source commit time;
- ingestion time;
- lateness distribution;
- watermark/window;
- records outside boundary;
- sink correction capability.

## Fix
Set lateness from observed distribution/business needs and create a correction/replay path for beyond-threshold data.

Do not widen watermarks blindly; state and cost can grow significantly.

# 5. Streaming backlog

Check:
- input vs processing rate;
- batch duration vs trigger interval;
- source backlog;
- state size;
- watermark progress;
- checkpoint duration;
- sink duration;
- files/batch.

Potential causes:
- sink slower than source;
- unbounded state;
- checkpoint bottleneck;
- poor micro-batch sizing;
- skew;
- slow MERGE.

Containment should restore throughput without sacrificing correctness.

# 6. Checkpoint failure/incompatibility

Preserve the checkpoint and query config first.

Determine:
- query change;
- stateful operator change;
- state schema change;
- partition/state-store config change;
- corruption vs incompatibility;
- available replay source.

Do not delete the checkpoint as a first response.

Recovery may require:
- compatible restart;
- scoped checkpoint recovery;
- new checkpoint + replay/dedupe;
- full rebuild.

Choose based on source replayability and business recovery requirements.

# 7. Airflow DAG queued/stuck

Check:
- first blocked task;
- upstream state;
- pool slots;
- executor capacity;
- DAG/task concurrency;
- `max_active_runs`;
- scheduler logs;
- sensors/waits;
- overlapping runs.

Clear/retry only tasks proven idempotent.

Use deferrable/reschedule behavior for long waits where supported and appropriate.

# 8. Schema regression

Check:
- source schema change;
- parser/inference;
- nullable/type change;
- column rename/drop;
- Auto Loader/schema tracking behavior;
- downstream contracts.

Contain:
quarantine incompatible records or pin schema only if doing so preserves required data.

Permanent fix:
explicit schema contract/evolution rule and downstream migration.

# 9. Cost spike

Compare:
- runtime;
- input volume;
- cluster/serverless usage;
- retries;
- scans/shuffles;
- file count;
- autoscaling behavior;
- micro-batch frequency;
- failed/repeated work.

Do not optimize cost by reducing correctness or SLA without explicit trade-off.
