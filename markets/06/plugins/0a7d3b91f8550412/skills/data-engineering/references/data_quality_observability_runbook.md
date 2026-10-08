# Data Quality and Observability Runbook

## Purpose

Use this file to define monitoring, reconciliation, alerting, and operational data-quality controls.

# 1. Pipeline signals

Useful baseline:
- run status;
- duration;
- retries;
- freshness;
- input/output/rejected counts;
- source lag;
- throughput;
- cost.

# 2. Data correctness signals

Depending on dataset:
- null required keys;
- grain uniqueness;
- duplicate rate;
- referential integrity;
- accepted domains;
- row-count reconciliation;
- financial/measure reconciliation;
- schema drift;
- delete/update counts.

# 3. Streaming signals

Monitor:
- input rate;
- processing rate;
- batch duration;
- backlog/offset lag;
- watermark;
- state rows/bytes;
- checkpoint duration/failures;
- sink latency.

A green job status is not enough.

# 4. DQ severity

Define checks as:
- blocking;
- quarantine;
- warning;
- informational.

Every production check should have:
- owner;
- threshold;
- action;
- notification route;
- recovery/runbook.

# 5. Freshness

Define freshness from business expectation, not arbitrary “latest timestamp.”

Example:
- source expected by 08:00;
- Silver by 08:20;
- Gold by 08:35.

Alert on the service-level expectation.

# 6. Reconciliation

For material pipelines capture:
- source rows/events;
- landed Bronze count;
- applied Silver changes;
- rejected/quarantined count;
- deletes;
- final published count.

For CDC also reconcile latest version/key state when feasible.

# 7. Anomaly detection

Use historical baselines for:
- volume;
- null rate;
- duplicate rate;
- processing time;
- reject rate;
- cost.

Do not block production solely on a noisy anomaly detector without defined policy.

# 8. Observability metadata

Useful run metadata:
- run ID;
- logical data interval;
- code/version;
- input artifacts/offsets;
- checkpoint/query ID;
- row metrics;
- environment;
- target version;
- replay/backfill ID.

# 9. Alert quality

Alerts should answer:
- what failed;
- impact;
- affected dataset/window;
- first check;
- owner;
- runbook.

Avoid alerts with no actionable threshold.

# 10. Post-change validation

After fixes/tuning validate:
- correctness;
- SLA;
- retries;
- cost;
- downstream state;
- repeated representative runs.

One successful run is not always enough for a recurring production issue.
