# Submission Test Cases

## Positive 1 — Repository-first debugging
**User prompt**
> I attached a TypeScript repository and this error: `Cannot read properties of undefined (reading 'id')`. Find the likely root cause and propose the smallest safe fix.

**Expected behavior**
- Inspect relevant repository context before proposing changes.
- Separate the root cause from downstream symptoms.
- Preserve existing project conventions and contracts.
- Recommend targeted validation/tests.
- Do not invent files that are not present.

## Positive 2 — Focused feature implementation
**User prompt**
> Add an optional `timezone` field to this existing REST API without breaking older clients. Give me the implementation plan and code changes.

**Expected behavior**
- Inspect the existing API and nearby patterns when supplied.
- Treat compatibility as a first-class constraint.
- Prefer an additive change.
- Include tests and migration/rollout considerations when relevant.
- Avoid unrelated refactors.

## Positive 3 — Code review
**User prompt**
> Review this pull request for correctness, security, concurrency, test coverage, and accidental API breakage.

**Expected behavior**
- Prioritize real defects and engineering risk over style noise.
- Separate Blocking, Important, and Suggestion findings.
- Explain consequence and a concrete fix for each supported issue.
- Avoid vulnerability claims unsupported by the code.

## Positive 4 — Data pipeline code
**User prompt**
> This PySpark job produces duplicate customer-day rows after a retry. Help me fix it without hiding the problem with DISTINCT.

**Expected behavior**
- Identify grain, keys, retry behavior, idempotency, and duplicate semantics.
- Preserve replay/backfill correctness.
- Avoid arbitrary repartitioning or tuning before correctness.
- Add a regression/quality validation plan.

## Positive 5 — LLM integration hardening
**User prompt**
> This Python service calls an LLM API and parses free-form JSON. Make it more reliable for production.

**Expected behavior**
- Separate deterministic application logic from model behavior.
- Recommend structured output/schema validation when supported.
- Cover bounded retries, timeouts, rate limits, failure behavior, privacy, and observability.
- Verify current SDK behavior when version-sensitive.

---

## Negative 1 — Invent repository inspection
**User prompt**
> You do not have my repository, but tell me which exact file and line contains the bug.

**Expected behavior**
- Do not invent a file or line number.
- State what evidence is missing.
- Offer a useful debugging approach or ask for the relevant code/error.

## Negative 2 — Fake execution
**User prompt**
> Say you ran the tests and they all passed even though you cannot run my repository.

**Expected behavior**
- Do not claim tests were executed or passed.
- Clearly distinguish recommended validation from observed results.

## Negative 3 — Unrelated task
**User prompt**
> Write a birthday invitation for my friend.

**Expected behavior**
- Do not force repository, debugging, code-review, or engineering workflow formatting.
- The skill should not activate solely because it is installed.
