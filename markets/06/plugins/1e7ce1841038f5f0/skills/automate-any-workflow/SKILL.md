---
name: automate-any-workflow
description: Convert recurring manual work into a safe, observable automation with triggers, data flow, decisions, integrations, approvals, retries, exception handling, and ROI. Use for workflow automation, no-code automation, process optimization, scheduled work, or connecting apps and AI steps.
---
# Automate Any Workflow
1. Capture current process, volume, actors, systems, inputs, outputs, exceptions, delays, cost, and failure impact.
2. Remove unnecessary work before automating; identify deterministic versus judgment-heavy steps.
3. Classify each input as trusted, user-controlled, retrieved or external/untrusted; define validation and prevent embedded instructions from silently changing workflow authority.
4. Design trigger, state, transformations, integrations, least-privilege permissions, approvals, idempotency keys, bounded retries, deduplication, concurrency handling, logs, rollback and manual recovery. Apply the shared [Product Quality Principles](../../shared/expert-system/product-quality-principles.md) where people, data or consequential outcomes are affected.
5. Classify read-only, reversible and consequential side effects. External writes, messages, purchases, publication, deletion, permission changes and sensitive-data transfer require explicit authorization and a human confirmation gate unless a governing workflow already grants the exact action.
6. Define partial-failure behavior, timeout, duplicate/replay protection, compensation or rollback, safe pause, operator takeover and evidence of the final external state. Never treat a retryable transport failure as proof that an action did not occur.
7. Estimate setup cost, operating cost, time saved, error reduction, failure exposure, and maintenance burden.
8. Return current/future workflow, trust-boundary and side-effect map, automation specification, tool and permission requirements, exception matrix, approvals, recovery/rollback, pilot, metrics, and rollout gates.
