# Technical Interview Frameworks

## Purpose

Use these frameworks to run realistic technical preparation across different role families.

Do not apply every framework to every role. Route by the JD and candidate profile.

---

# 1. Coding interview

## Interview flow

1. Clarify the problem and ambiguous requirements.
2. State input/output and constraints.
3. Give a straightforward approach.
4. Improve the approach when needed.
5. Write syntactically valid code if the interview expects coding.
6. Test normal, edge, boundary, empty, duplicate, and invalid cases as relevant.
7. State time and space complexity.
8. Handle follow-up constraints.

## Evaluate

- correctness;
- reasoning;
- communication;
- data-structure choice;
- edge cases;
- testing;
- complexity;
- readability;
- maintainability.

Do not over-focus on the final algorithm while ignoring communication and testing.

## Feedback pattern

- Correctness issue
- Missed edge case
- Complexity issue
- Communication issue
- Stronger approach
- Minimal corrected code when requested

---

# 2. Debugging interview

## Flow

symptom → reproduce → isolate layer → gather evidence → hypothesis → smallest test → fix → validation

Probe:
- what changed;
- scope;
- logs/metrics;
- recent deploy/config/data changes;
- dependency failures;
- rollback;
- prevention.

Evaluate whether the candidate distinguishes evidence from guesses.

---

# 3. System design

## Core flow

1. Clarify users and functional requirements.
2. Define scale/latency/availability/security constraints.
3. Identify core entities and interfaces.
4. Draw the high-level architecture.
5. Trace one important request/data flow.
6. Deep-dive into the critical bottleneck.
7. Cover reliability and failure handling.
8. Cover security and observability.
9. Discuss trade-offs and alternatives.
10. State what changes at 10x scale.

## Role-specific emphasis

Backend:
- APIs, storage, cache, queues, consistency, scaling.

Data:
- ingestion, processing, storage, partitions, freshness, replay, quality, orchestration.

AI:
- model/tool/retrieval flow, evals, guardrails, latency, cost, fallback.

Frontend:
- client architecture, state, rendering, caching, performance, accessibility.

Platform/SRE:
- deployment, networking, observability, HA/DR, capacity, failure domains.

Mobile:
- client/server boundary, offline state, sync, lifecycle, releases.

---

# 4. SQL / Data interview

## Flow

1. Confirm table grain.
2. Identify join keys.
3. Clarify expected output grain.
4. Write the simplest correct query.
5. Check duplicates and NULL behavior.
6. Check date/time boundaries.
7. Add windows/CTEs only when they improve correctness/readability.
8. Validate with a small example.
9. Discuss performance only after correctness.

Common areas:
- joins;
- aggregation;
- windows;
- deduplication;
- top-N;
- gaps/islands;
- running totals;
- date logic;
- slowly changing dimensions;
- incremental logic;
- data quality.

For data-engineering roles, follow with architecture or failure-recovery questions.

---

# 5. Data pipeline design interview

Clarify:
- sources/sinks;
- volume/growth;
- latency;
- batch/streaming;
- insert/update/delete semantics;
- ordering;
- schema evolution;
- backfills;
- RPO/RTO;
- consumers.

Then cover:
- raw landing;
- transformations;
- idempotency;
- dedupe;
- CDC;
- orchestration;
- quality;
- observability;
- replay;
- security;
- cost.

Follow-up failures:
- late data;
- duplicate events;
- source replay;
- schema break;
- partial failure;
- sink outage;
- backfill during live writes.

---

# 6. Cloud / platform design interview

Clarify:
- workload;
- traffic;
- regions;
- availability;
- compliance;
- data sensitivity;
- cost constraints.

Cover:
- network boundary;
- identity and least privilege;
- compute;
- storage;
- deployment;
- secrets;
- observability;
- scaling;
- HA/DR;
- cost.

Follow up with:
- region failure;
- credential compromise;
- traffic spike;
- bad deployment;
- dependency outage.

---

# 7. SRE / incident interview

Use:
impact → detection → triage → hypothesis → containment → recovery → root cause → prevention

Probe:
- first metric checked;
- rollback criteria;
- communication;
- data-loss risk;
- customer impact;
- post-incident changes.

Good answers prioritize restoration and correctness before speculative redesign.

---

# 8. AI / ML interview

## ML systems
Cover:
- data;
- features;
- training;
- evaluation;
- serving;
- monitoring;
- drift;
- retraining;
- latency;
- failure cases.

## GenAI systems
Cover:
- use-case suitability;
- model choice;
- structured outputs;
- retrieval/tools;
- context;
- evaluation;
- hallucination;
- safety;
- observability;
- latency/cost;
- fallbacks.

For agents, ask:
- why an agent is needed;
- tool permissions;
- state;
- retries;
- termination;
- approvals;
- tracing;
- evals.

Do not reward “use an agent” as architecture by itself.

---

# 9. Frontend interview

Possible focus:
- JS/TS fundamentals;
- async/event loop;
- component/state design;
- browser/network behavior;
- performance;
- accessibility;
- testing;
- frontend system design.

Design flow:
requirements → component/state model → data fetching/cache → rendering → errors/loading → accessibility → performance → testing.

---

# 10. Mobile interview

Possible focus:
- lifecycle;
- concurrency;
- state;
- networking;
- persistence;
- navigation;
- offline behavior;
- testing;
- performance.

Design flow:
requirements → screen/state flow → client/server boundary → persistence/cache → offline/sync → errors → observability → release compatibility.

---

# 11. Take-home / practical assessment

Before solving, inspect:
- instructions;
- time expectation;
- allowed dependencies;
- submission format;
- testing requirements;
- evaluation hints.

Prioritize:
1. correctness;
2. required scope;
3. clear structure;
4. tests;
5. README/assumptions;
6. polish.

Do not over-engineer a small assignment.

---

# 12. Technical concept question

For “What is X?” interview prep, answer in layers:

## 20-second
Definition + why it matters.

## 60-second
Definition + mechanism + practical use.

## Deep follow-up
Trade-offs, failure modes, implementation detail, and where not to use it.

Use only the depth the user asks for.
