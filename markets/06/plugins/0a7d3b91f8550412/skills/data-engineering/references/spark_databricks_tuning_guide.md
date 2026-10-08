# Spark and Databricks Tuning Guide

## Purpose

Use for Spark/Databricks performance diagnosis, joins, shuffle/skew, memory pressure, partition sizing, file layout, and streaming state/checkpoints.

These are evidence-driven controls, not defaults.

# Diagnostic order

1. confirm correctness;
2. identify exact slow/failing stage;
3. compare known-good run;
4. inspect physical/runtime plan;
5. measure input, tasks, shuffle, spill, skew, files;
6. change one thing;
7. validate correctness, runtime, cost, stability.

# 1. AQE / skew

Before changing:
- verify AQE/skew behavior already enabled/current;
- inspect max vs median task sizes;
- check hot/null/default keys;
- inspect runtime join strategy.

AQE cannot fix wrong join keys or bad data modeling.

# 2. Shuffle partitions

Do not set a blanket number.

Measure:
- total shuffle bytes;
- post-shuffle tasks;
- p50/p95/max duration;
- spill;
- scheduler overhead;
- output file count;
- AQE coalescing.

Too many → overhead/tiny files.  
Too few → spill/stragglers/OOM.

# 3. Broadcast

Use only when one side is safely small after filters.

Check:
- post-filter size;
- plan;
- executor memory;
- stats.

Do not force broadcast because a table is called “dimension.”

# 4. OOM

Check before resizing:
- skew;
- oversized partitions;
- wrong build/broadcast side;
- wide rows;
- unnecessary columns;
- cache/persist;
- UDF/serialization;
- driver collect;
- concurrent workloads;
- streaming state growth.

Temporary compute increase is containment, not root-cause repair.

# 5. Repartition/coalesce

`repartition` adds shuffle and can rebalance.

`coalesce` mainly reduces partitions without full shuffle and can preserve imbalance.

Validate partition distribution and downstream file count.

# 6. File layout

Symptoms:
- slow scans;
- many tiny input tasks;
- large listing overhead;
- MERGE scans too much.

Check:
- file count/size;
- filter alignment;
- pruning/data skipping;
- clustering effectiveness;
- write frequency;
- target scan.

Use supported compaction/clustering only when evidence/access patterns justify it.

# 7. Cache/persist

Use only when an expensive result is reused enough to justify materialization/memory.

Avoid for one-use DataFrames or oversized intermediates.

Compare end-to-end runtime.

# 8. Structured Streaming

Check:
- input vs processed rows/sec;
- batch duration;
- backlog/offset lag;
- state rows/bytes;
- watermark progress;
- checkpoint duration;
- files/batch;
- sink duration.

Do not delete/relocate checkpoints casually.

Each query needs a unique checkpoint.

Validate compatibility before changing stateful logic or state-related configs.

# 9. Current Databricks behavior

Databricks runtime defaults/features can change.

Verify current docs before hardcoding:
- state-store provider defaults;
- changelog/asynchronous checkpointing;
- autoscaling guidance for streaming;
- serverless/job-compute recommendations;
- clustering/liquid clustering behavior;
- Lakeflow behavior.

# 10. Change record

For each tuning change record:
- symptom/evidence;
- old/new value;
- scope;
- expected mechanism;
- correctness guardrail;
- validation window;
- runtime/cost result;
- rollback trigger.
