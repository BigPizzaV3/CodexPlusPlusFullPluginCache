---
name: engineer-test-and-regression-systems
description: Design and implement a durable test and regression system across unit, integration, contract, end-to-end, browser, responsive, accessibility, performance, security-relevant, migration, and visual verification. Use when the primary task is test architecture, coverage strategy, fixtures, CI quality gates, flaky-test control, or regression infrastructure rather than tests for one small feature.
---

# Engineer Test and Regression Systems

Build a test system that detects material failures without optimizing for raw test count or brittle snapshots.

Apply the shared [risk-adaptive assurance model](../../shared/expert-system/risk-adaptive-assurance-model.md). Test the required outcome and protected invariants with the smallest reliable system; do not encode an internal implementation path unless security, regulated behavior, protected architecture or an explicit deterministic contract requires it.

## Frame the assurance problem

1. Inventory architecture, critical user journeys, interfaces, data, environments, supported platforms, risks, incident history, current tests, CI, release gates, and observability.
2. Map requirements and protected behavior to failure modes, direct acceptance oracles, test layers, environments, evidence, owners, and release consequences.
3. Define what each test layer proves and explicitly does not prove.
4. Identify deterministic seams, fixtures, test data, mocks, clocks, randomness, external services, cleanup, isolation, and privacy requirements.
5. Classify tooling, dependencies, environments, and quality thresholds under the shared [decision-authority model](../../shared/expert-system/decision-authority-model.md). Do not introduce them silently.

## Test architecture

Select applicable layers:

- unit and property tests for local logic;
- integration for boundaries and persistence;
- API, schema, event, and consumer-driven contracts;
- end-to-end journeys and failure recovery;
- browser, device, responsive, and localization coverage;
- accessibility semantics and interaction;
- performance, capacity, reliability, and resource budgets;
- security-relevant permissions, abuse, input, and dependency checks;
- migration, rollback, backup, and restore verification;
- production smoke and synthetic monitoring;
- visual regression and human perceptual review.

When AI behavior is only one layer of a broader test system, include versioned representative and held-out evaluation datasets, expected outcomes/rubrics, prompt/model/retrieval/tool identities, tool-call trajectories and arguments, safety/adversarial cases, failure taxonomy and regression thresholds. Keep probabilistic evaluation distinct from exact deterministic assertions and preserve evaluator limitations. When behavioral AI evaluation is the primary task, route it to `$evaluate-ai-systems`; this skill owns the durable runners, fixtures, CI integration and cross-system regression infrastructure, not the independent AI verdict.

For material user-facing behavior, drive the real running application when unit or code-level tests cannot establish the outcome. Navigate, interact, trigger state, inspect output and errors, and exercise recovery. For sensitive adversarial or mutation testing, use a bounded isolated candidate copy when direct review could damage the accepted tree or data.

For visual regression distinguish strict pixel comparison, perceptual comparison, layout geometry, semantic assertions, and human visual approval. Use each only for the observable it can reliably protect. Apply the shared [perceptual quality gates](../../shared/expert-system/perceptual-quality-gates.md); technical tests cannot self-certify premium visual quality.

For representation-sensitive work, link each important perceptual observable to the representation proof and real runtime state that can establish it. A controlled offline reference render may serve as an art/material/form oracle, but never self-certifies browser pixel truth. Where applicable, test Source-Master-to-publishing-target lineage, representative views and screen-space states, defined versus user-controlled motion, approved publishing tiers and fallbacks, first-contact stability, resting/offscreen/hidden lifecycle behavior, and absence of drift from an authorized calibration checkpoint. Do not require these layers for ordinary DOM/CSS/image interfaces.

## Reliability and governance

- Define test ownership, naming, location, execution commands, runtime budget, parallelism, retries, quarantine, and failure triage. Record only environment factors that can materially change the measurement.
- Do not hide flaky tests behind unlimited retries. Measure flake rate, isolate the cause, set an owner and removal deadline, and preserve release risk visibility.
- Version deterministic fixtures and protect secrets and personal data.
- Define branch, pull-request, pre-release, post-deploy, and rollback gates with evidence retention.
- Keep the smallest suite that gives required confidence; delete or replace redundant tests only with authority and proof.

## Verification and output

Validate the test system against known seeded failures or safe mutation cases where feasible. Confirm that failures are actionable, reproducible, and linked to requirements. Report false positives, false negatives, runtime, maintenance burden, and uncovered risk.

Return the coverage and risk map, test architecture, tooling decisions and approvals, fixtures strategy, commands and environments, CI/release gates, visual assurance model, flaky-test policy, implemented assets, validation evidence, gaps, ownership, and rollout plan.
