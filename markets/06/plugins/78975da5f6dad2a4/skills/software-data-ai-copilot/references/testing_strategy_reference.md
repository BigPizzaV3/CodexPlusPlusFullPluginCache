# Testing Strategy Reference

## Purpose

Use this file to choose the smallest set of tests that gives confidence in the change.

Do not apply a fixed unit/integration/E2E ratio mechanically.

# Test layers

## Unit / small tests

Best for:
- pure logic;
- validation;
- transformations;
- edge cases;
- deterministic business rules.

Properties:
- fast;
- isolated;
- deterministic;
- easy to diagnose.

Avoid mocking so much that the test no longer represents meaningful behavior.

## Integration / medium tests

Best for boundaries such as:
- database access;
- API clients;
- serialization;
- framework wiring;
- queues;
- filesystem;
- model/tool adapters.

Use them when failure can occur in the interaction between components.

## Contract tests

Use when independent components/services rely on:
- API schemas;
- events;
- files;
- database interfaces;
- model/tool output shapes.

Test the contract, not every internal implementation.

## End-to-end / large tests

Use sparingly for critical user journeys that smaller tests cannot fully establish.

Good targets:
- login and primary task completion;
- checkout/payment;
- critical data publishing path;
- major cross-system workflow.

Avoid relying primarily on E2E tests because they are slower and harder to diagnose.

## Regression tests

Every fixed bug should usually get the smallest deterministic test that would have caught it.

# Change-to-test mapping

## Local algorithm change
Unit tests + existing suite.

## API handler change
Unit tests + API/integration tests + contract check.

## Database change
Migration test + data-access integration + compatibility check.

## UI component
Component tests + accessibility checks; E2E only for important journey.

## Background job
Unit logic + integration with queue/store + retry/idempotency test.

## Data pipeline
Transformation tests + data-quality/reconciliation + replay/idempotency test.

## AI/LLM feature
Schema/validation tests + mocked tool/model boundary + evaluation set for behavior + safety/failure cases.

# Properties of good tests

Prefer tests that are:
- deterministic;
- isolated from unrelated systems;
- clear about expected behavior;
- independent of execution order;
- fast enough for their feedback loop;
- specific enough to identify the failure.

# Negative and edge testing

When relevant include:
- empty input;
- null/missing fields;
- min/max boundaries;
- duplicate input;
- malformed input;
- unauthorized user;
- timeout;
- dependency error;
- retry;
- concurrency;
- partial failure;
- rollback.

# Avoid

- testing implementation details with no behavioral value;
- huge snapshots with weak assertions;
- flaky timing sleeps;
- order-dependent tests;
- live production dependencies;
- duplicate coverage at every layer;
- E2E tests for logic already proven lower in the stack.

# Validation reporting

Never say “tests pass” unless test output is available.

If tests cannot be run, state:
- what should be run;
- expected result;
- highest-risk untested behavior.
