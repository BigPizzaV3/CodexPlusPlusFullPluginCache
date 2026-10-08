---
name: architecture-review
description: Review a proposed architecture for security, reliability, operability, and fit.
---

# Architecture Review

Apply when reviewing a supplied design, proposal, or architecture artifact.

1. Establish scope and evidence. Separate explicit design facts, missing details, and inferences; do not claim code or infrastructure inspection unless actually provided.
2. Trace important user/data flows, trust boundaries, identities, authorization, dependencies, failure paths, recovery, observability, and operational ownership.
3. Assess risks against explicit quality attributes and known threat model. Prioritize by plausible impact and exposure; provide concrete evidence and mitigations.
4. Check resilience patterns for their failure modes too (retries, queues, caches, replicas, circuit breakers, fallbacks). Identify cascading-failure and data-consistency risks.
5. Use current primary framework/documentation sources for factual platform/security requirements. Treat architecture patterns as context-dependent rather than guarantees.
6. Recommend targeted validation: threat modeling, prototype, load/fault test, cost estimate, or expert review.

Return prioritized findings and unknowns. Do not certify security, compliance, scalability, or production readiness from a diagram alone.
