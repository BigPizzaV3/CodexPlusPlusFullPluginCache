# Code Review Framework

## Purpose

Use this file to review code for correctness and engineering risk rather than style noise.

Prioritize defects that can change behavior, security, data, reliability, or maintainability.

# Review order

## 1. Intent and design

Ask:
- Does the change solve the intended problem?
- Does it fit the surrounding architecture?
- Is it more complex than necessary?
- Does it duplicate an existing abstraction?
- Does it introduce a new dependency/boundary without need?

# 2. Correctness

Check:
- happy path;
- edge cases;
- empty/null states;
- error paths;
- off-by-one/boundary behavior;
- type assumptions;
- state transitions;
- time/date handling;
- retries;
- partial failure.

For data code, also check:
- grain;
- keys;
- duplicate amplification;
- ordering;
- schema;
- idempotency;
- replay.

# 3. Security and privacy

Check when relevant:
- authentication;
- authorization/resource ownership;
- input validation;
- injection;
- XSS/CSRF/SSRF;
- path traversal;
- unsafe file handling;
- deserialization;
- secret leakage;
- PII logging;
- tenant isolation;
- destructive action controls.

Do not produce vulnerability theater: report issues only when supported by the code/context.

# 4. Contracts and compatibility

Inspect:
- API inputs/outputs;
- events/messages;
- database schema;
- public functions;
- configuration;
- CLI behavior;
- serialized formats;
- UI behavior.

Call out accidental breaking changes.

# 5. Concurrency and distributed behavior

When relevant:
- race conditions;
- atomicity;
- lock scope;
- duplicate delivery;
- idempotency;
- ordering;
- timeout/retry interaction;
- stale reads;
- cache invalidation;
- background job overlap.

# 6. Performance

Look for evidence-backed risks:
- repeated full scans;
- N+1 access;
- unnecessary network calls;
- unbounded memory growth;
- blocking work on hot paths;
- expensive serialization;
- oversized payloads;
- avoidable re-rendering;
- poor query/index use;
- large shuffle/collect in data code.

Do not request premature optimization without a plausible bottleneck.

# 7. Tests

Ask:
- Is the changed behavior tested?
- Is the bug regression covered?
- Are important boundaries tested?
- Are tests deterministic?
- Do tests assert behavior rather than implementation details?
- Is there unnecessary end-to-end coverage where a smaller test is better?

# 8. Maintainability

Check:
- naming;
- unnecessary complexity;
- duplicated logic;
- comments explaining why;
- dead code;
- confusing control flow;
- cohesion;
- ownership boundaries.

Do not block on personal style preferences when automated formatting/project conventions already define style.

# Severity

Use:

**Blocking**
Likely correctness, security, data-loss, compatibility, or production failure.

**Important**
Meaningful reliability, performance, test, or maintainability risk.

**Suggestion**
Non-blocking improvement with clear benefit.

Avoid inflating severity.

# Review output

A concise review can use:

## Verdict
One sentence.

## Blocking issues
Only actual blockers.

## Important issues
Ranked by impact.

## Suggestions
Only useful non-blockers.

For each issue include:
- location;
- problem;
- consequence;
- concrete fix or direction.

Praise is optional; accuracy is not.
