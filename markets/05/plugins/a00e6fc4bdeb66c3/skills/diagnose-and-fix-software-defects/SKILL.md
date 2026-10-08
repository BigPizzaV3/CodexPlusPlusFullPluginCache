---
name: diagnose-and-fix-software-defects
description: Reproduce, isolate, diagnose, and repair a real software defect through evidence, competing hypotheses, root-cause analysis, a minimal controlled fix, focused tests, and regression verification. Use when existing software behaves incorrectly, crashes, fails a build or test, or has an observable regression. Do not use for speculative red-team critique, planned feature implementation, broad refactoring, or performance optimization without a defect.
---

# Diagnose and Fix Software Defects

Repair the verified root cause without hiding the symptom through a product change, weakened test, disabled check, or unrelated refactor.

## Diagnose before fixing

1. Define expected behavior, observed behavior, environment, affected scope, severity, and evidence.
2. Inspect repository instructions, recent changes, logs, stack traces, failing tests, dependencies, configuration, and relevant code.
3. Reproduce the defect with the smallest reliable case. If reproduction is impossible, state what remains unverified and gather safe diagnostics.
4. Establish a before-state and preserve user work.
5. Form competing hypotheses and list evidence that would confirm or falsify each.
6. Isolate the failure across input, state, component, interface, environment, timing, data, dependency, and deployment boundaries.
7. Identify the root cause and causal chain. Distinguish it from symptoms and contributing conditions.

Do not claim a root cause merely because one edit makes the symptom disappear.

## Authority and repair

Use the shared [decision-authority model](../../shared/expert-system/decision-authority-model.md). A bug report does not authorize changing intended product behavior, architecture, contracts, security, data semantics, visual direction, or scope. Stop on Class-1 ambiguity.

Implement the smallest coherent root-cause fix. Add or strengthen a regression test that fails before the fix and passes after it when feasible. Do not delete, skip, relax, snapshot-update, or mock away a meaningful failing test without explicit justification and authority.

If the repair requires broad structural transformation, route to `$refactor-and-migrate-codebases`. If the primary issue is measured runtime performance, route to `$optimize-runtime-performance`.

## Verification

Run the reproducer, focused tests, connected integration tests, relevant regression suite, type/lint/build checks, and applicable security, accessibility, browser, data, or deployment checks. Inspect the real behavior after the fix. Compare before and after evidence and check that the failure does not reappear under boundary conditions.

Use independent review for critical defects or risky fixes. Correct compliance with a defective specification is not success; if expected behavior itself is defective or contradictory, return the issue to its owner rather than coding around it.

## Output

Return reproduction evidence, root cause and causal chain, affected scope, fix manifest, decision class, tests and actual results, regression coverage, unrelated changes avoided, rollback, unresolved risks, and whether the defect is verified fixed, mitigated, not reproduced, or blocked.
