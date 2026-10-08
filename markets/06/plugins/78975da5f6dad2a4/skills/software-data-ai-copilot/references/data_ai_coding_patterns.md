# Data and AI Coding Patterns

## Purpose

Use this file for implementation-level data engineering, analytics, ML, and LLM code.

For deep production incidents or architecture, hand off to the specialized data engineering or RAG/agent workflow when appropriate.

# 1. SQL and transformations

Before changing SQL, identify:
- input grain;
- output grain;
- keys;
- join cardinality;
- NULL behavior;
- date/time semantics;
- deduplication rule;
- incremental boundary.

Do not use `DISTINCT` to hide an unexplained duplicate problem.

For dedupe, define winner and tie-breaker.

# 2. Spark / distributed transforms

Check:
- partitioning;
- shuffle;
- skew;
- collect-to-driver;
- UDF use;
- pruning;
- repeated scans;
- join strategy;
- output file behavior.

Correctness comes before tuning.

Avoid arbitrary repartition counts or forced broadcasts without evidence.

# 3. Pipeline code

Make retries safe.

Define:
- logical run/window;
- idempotency;
- source of truth;
- checkpoint/state;
- duplicate handling;
- schema evolution;
- late data;
- replay/backfill.

External side effects should not be duplicated by task retry.

# 4. Data-quality code

Prefer explicit checks tied to business grain and contracts.

Examples:
- required keys;
- uniqueness;
- referential integrity;
- freshness;
- accepted values;
- reconciliation;
- volume/change anomalies.

A quality check should define what happens on failure: block, quarantine, warn, or continue.

# 5. Notebook to production

Extract:
- reusable logic;
- configuration;
- IO boundaries;
- deterministic transforms.

Add:
- module/package structure;
- entrypoint;
- logging;
- validation;
- tests;
- dependency/runtime definition;
- secrets management.

Remove:
- hidden global state;
- manual cell-order dependency;
- embedded credentials;
- hardcoded local paths;
- exploratory display-only behavior from critical logic.

# 6. ML code

Separate:
- data preparation;
- feature logic;
- training;
- evaluation;
- artifact/version management;
- inference.

Check for:
- train/serve skew;
- data leakage;
- nondeterminism;
- reproducibility;
- metric misuse;
- model/version compatibility.

# 7. LLM integration

Treat model output as untrusted input.

Use when relevant:
- structured outputs/schema validation;
- bounded retries;
- timeout;
- rate-limit handling;
- fallback;
- prompt/tool injection defenses;
- redaction;
- eval cases;
- tracing;
- cost/latency measurement.

Do not parse free-form text when a reliable structured contract is available.

# 8. Tool/API wrappers

Centralize:
- authentication injection;
- timeout;
- retry;
- error mapping;
- logging/redaction;
- schema validation.

Avoid scattering provider-specific calls across business logic.

# 9. Current SDKs

LLM/ML/cloud/data SDKs evolve quickly.

When implementation depends on current syntax or behavior:
- check official docs;
- state version assumptions;
- avoid copying deprecated patterns from memory.

# 10. Handoff boundary

Use this coding skill for:
- local implementation;
- debugging;
- tests;
- refactors;
- SDK integration.

Use a specialized architecture skill when the main problem is:
- system-wide RAG design;
- agent topology/governance;
- production data-platform architecture;
- cross-pipeline incident recovery;
- organization-wide platform choices.
