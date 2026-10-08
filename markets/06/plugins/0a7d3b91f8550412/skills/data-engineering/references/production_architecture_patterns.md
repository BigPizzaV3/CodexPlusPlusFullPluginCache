# Production Architecture Patterns

## Purpose

Use this file for CDC, batch, streaming, replay, lakehouse layering, reliability, and cost trade-offs.

A pattern is a starting point, not a mandate.

# Selection questions

Ask only what changes the design:
- source/sink;
- volume/growth;
- freshness SLA;
- insert/update/delete semantics;
- source ordering/version;
- replay/backfill;
- RPO/RTO;
- downstream contracts;
- security/governance;
- cost constraints.

# 1. Replayable CDC

Flow:

`source CDC/log → immutable Bronze changes → ordered/deduped Silver state → Gold products`

Use when updates/deletes and replay matter.

Core guarantees:
- raw changes retained;
- deterministic winner/key;
- deletes explicit;
- replay of same bounded input reproduces state.

Required metadata:
- business key;
- operation;
- source sequence/version or commit time;
- ingestion time;
- source artifact/offset;
- run/replay ID.

Guardrails:
- dedupe before MERGE;
- prefer source ordering over ingestion time;
- reconcile Bronze vs Silver;
- scope backfills;
- prevent conflicting writers.

# 2. Deterministic batch

Flow:

`source snapshot/files/API → Bronze by data interval → validated Silver → publish`

Core guarantees:
- deterministic interval;
- rerun-safe;
- validate before publish;
- partial output not exposed as complete.

Use when batch is sufficient for SLA.

Avoid `now()`-driven business logic that changes on rerun.

# 3. Continuous streaming with durable raw landing

Flow:

`Kafka/Event Hubs/files → Structured Streaming → durable Bronze → incremental Silver → serving`

Use only when freshness justifies always-on complexity.

Core guarantees:
- durable raw landing;
- unique durable checkpoint;
- idempotent sink;
- explicit late-data behavior;
- observable backlog/state.

# 4. Triggered incremental streaming

Use `availableNow`/supported triggered patterns when:
- incremental processing semantics are useful;
- continuous always-on compute is unnecessary;
- bounded catch-up runs fit the SLA.

Verify runtime/source compatibility.

Do not combine features known to be incompatible without checking current docs.

# 5. Batch + streaming repair path

Streaming owns freshness.

Batch owns:
- historical recomputation;
- large repair;
- backfill.

Guardrails:
- shared business rules where practical;
- explicit table/scope ownership;
- no conflicting writers to the same scope;
- reconcile repaired state with stream progress.

# 6. Idempotent pipeline

Principles:
- deterministic input boundary;
- stable key;
- deterministic ordering;
- replayable raw data;
- stage/audit/publish;
- side-effect isolation.

Good patterns:
- deduped MERGE;
- bounded replace;
- output ledger;
- destination idempotency key.

Anti-pattern:
append on retry with no dedupe key.

# 7. Bronze / Silver / Gold

## Bronze
Raw, source-aligned, replayable.

## Silver
Validated, typed, deduped/conformed, correction-aware.

## Gold
Consumer-specific marts/aggregates/features.

Do not duplicate core entity-cleaning logic across every Gold product.

# 8. Cost-aware design

Major cost drivers:
- repeated full scans;
- large shuffles;
- unpruned MERGE;
- small files;
- over-partitioning;
- excessive micro-batches;
- repeated logic across layers;
- unnecessary always-on compute.

Optimize only after correctness and SLA are understood.

# Architecture decision format

**Recommendation**  
**Correctness invariants**  
**Failure/recovery model**  
**Trade-offs**  
**Cost/runtime**  
**What would invalidate the design**
