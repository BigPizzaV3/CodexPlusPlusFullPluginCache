# Verification and Handoff

## Test case contract

Each material test includes:

- test ID and linked requirement IDs;
- level and owner;
- preconditions and fixtures;
- action or stimulus;
- expected result and observable evidence;
- cleanup and isolation;
- pass/fail rule;
- automation status or manual reason.

## Regression baseline

Record protected behavior before implementation. Identify the existing tests, routes, interfaces, data invariants, user journeys, visual states, performance budgets, or security controls that must remain valid.

## Acceptance criteria quality

An acceptance criterion is valid when it:

- describes externally observable behavior or inspectable technical state;
- can be evaluated without guessing intent;
- includes conditions and expected result;
- avoids compound criteria where one part could pass and another fail;
- references the requirement and evidence source;
- does not claim exhaustive quality from a limited check.

## Implementation handoff checklist

- specification version and approval status are clear;
- blockers and assumptions are visible;
- affected and protected areas are listed;
- diagrams, schemas, designs, assets, and source links resolve;
- data handling and secret boundaries are explicit;
- test environment and commands are known or marked unknown;
- migration, rollout, rollback, and feature flags are defined where needed;
- code review ownership and required specialists are identified;
- completion report format is included.

## Completion report expected from developer

Require:

1. files and components created, modified, deleted, or deliberately preserved;
2. requirement IDs implemented;
3. deviations and rationale;
4. tests run with actual results;
5. untested areas and residual risks;
6. migration, deployment, rollback, or manual steps;
7. screenshots, logs, reports, or other acceptance evidence where relevant.
