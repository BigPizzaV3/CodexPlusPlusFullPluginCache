# Research Notes — Data Engineering Copilot

Research date: 2026-09-23

## Recommended public name

Use **Data Engineering Copilot**.

The original internal name, “Production Data Engineering Copilot,” exceeds OpenAI's current 30-character final-directory display-name limit.

Keep the package name as:
`production-data-engineering-copilot`

Use the shorter skill identity:
`data-engineering`

This keeps the combined `plugin-name:skill-name` identity under OpenAI's 64-character limit.

## Recommended architecture

Use a **skills-only plugin** for v0.1.

The current value is architecture guidance, production debugging, recovery planning, tuning, implementation patterns, observability, and data-quality reasoning. No live Databricks, Spark, Airflow, or warehouse access is needed for the first version.

A later MCP-backed release would make sense only for controlled actions such as:
- reading job/run metadata;
- inspecting Spark or query metrics;
- querying table schemas and plans;
- reading Airflow DAG/task state;
- executing bounded validation queries;
- triggering approved replays/backfills.

## OpenAI package/submission rules checked

Current OpenAI documentation supports:
- a portable root `plugin.json`;
- skills in `skills/`;
- skills-only public plugins;
- display names up to 30 characters;
- short descriptions up to 30 characters;
- long descriptions up to 4,000 characters;
- up to 20 capabilities, each up to 120 characters;
- up to 3 starter prompts, each up to 128 characters;
- combined plugin/skill identity up to 64 characters;
- exactly five positive and three negative review tests for submission;
- bundled-skill safety/security scanning;
- verified developer/business identity and policy attestations.

Official references:
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors

## Current data-platform research

### Structured Streaming checkpoints

Current Databricks documentation states that checkpoints track source offsets, committed batches, stateful operator state, and query metadata. Deleting a checkpoint or switching to a new location causes the next run to begin fresh. Some changes to sources, stateful operations, state schema, and sinks require a new checkpoint.

This directly supports the skill rule: treat checkpoints as production state and never delete them casually.

### Current Databricks runtime behavior

Databricks documents current production guidance for Structured Streaming and runtime-specific checkpoint/state features. These defaults evolve, so the plugin should verify runtime-specific guidance instead of freezing configuration advice.

Examples of version-sensitive behavior include:
- RocksDB state-store defaults;
- changelog checkpointing;
- asynchronous state checkpointing;
- source evolution;
- state repartitioning;
- Lakeflow recommendations.

### Delta MERGE

Current Databricks documentation warns that MERGE can fail when multiple source rows ambiguously match a target row being updated. Preprocessing/deduplicating source rows is therefore a correctness requirement when source uniqueness is not guaranteed.

### Airflow

Airflow 3 exposes explicit backfill concepts including date range, reprocessing behavior, maximum active runs, backward ordering, and API/CLI operations. Backfill advice should therefore be version-aware and should not rely on legacy command behavior from memory.

### Spark

Current Spark Structured Streaming documentation continues to emphasize checkpointing/state for fault tolerance, while migration behavior changes across Spark releases. The skill therefore verifies exact Spark/runtime versions before recommending stateful-query or checkpoint migrations.

## Product decisions preserved

1. Correctness before tuning.
2. Preserve raw/replayable inputs where recovery matters.
3. Make writes and side effects retry-safe.
4. Use authoritative source ordering for CDC.
5. Treat checkpoint/state changes as production migrations.
6. Separate containment from permanent fixes.
7. Do not scale compute until the bottleneck is evidenced.
8. Backfills need explicit scope, concurrent-writer rules, validation, and rollback/repair.
9. Data quality needs an owner, threshold, action, and runbook.
10. Never claim a job, query, or fix was verified without actual results.
