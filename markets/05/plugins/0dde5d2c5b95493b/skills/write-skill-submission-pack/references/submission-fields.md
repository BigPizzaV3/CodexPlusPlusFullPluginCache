# Skills-only submission field rules

- Rule snapshot: 2026-08-10 (Asia/Taipei)
- Scope: OpenAI public Skills-only plugin submission materials
- Source boundary: OpenAI official documentation only

## Route and package facts

- A Skills-only plugin can be submitted without an MCP server.
- The public package is a plugin bundle, not a bare `SKILL.md`.
- The bundle must contain `.codex-plugin/plugin.json` and at least one valid `skills/<skill-name>/SKILL.md`.
- A Skills-only ZIP must not include `mcpServers`, `.mcp.json`, `apps`, `.app.json`, or screenshot configuration.
- The package manifest requires a package `name`, semantic `version`, description, author name, and `skills` path.

Official sources:

- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors

## Final directory limits

Apply the stricter final-submission limits, not any wider upload-validation limit:

| Field | Rule |
| --- | --- |
| Package name | Required; at most 64 characters; begins with an ASCII letter or digit; only ASCII letters, digits, `_`, `-` |
| Version | Required semantic version; at most 64 characters |
| Display name | Required; one line; at most 30 characters |
| Short description | Required; one line; at most 30 characters |
| Long description | Required; at most 4,000 characters |
| Developer name | Required; one line; at most 80 characters |
| Category | Required; must be selected from the portal-supported list |
| Capabilities | At most 20; each non-empty, one line, at most 120 characters |
| Starter prompts | At most 3; unique after Unicode and whitespace normalization; one line; at most 128 characters; no plugin `@mention` |
| Skill description | Required; at most 1,024 characters |
| Combined identity | `plugin-name:skill-name` at most 64 characters |

## Review cases and evidence

The company production contract prepares exactly five positive and three negative cases for a Skills-only submission. Each case must stay tied to the current package version and include:

- user prompt;
- fixture or supplied input needed to reproduce it;
- expected activation;
- expected behavior;
- expected result shape;
- actual-result summary;
- direct evidence reference.

Positive cases must come from executed passing evidence. Negative cases must demonstrate the expected clarification, non-activation, refusal, or safe fallback. Do not convert a planned case into executed evidence.

## Other submission materials

- Prepare release notes for the submitted version.
- Preserve country or region availability as an owner/portal choice when not supplied.
- Preserve verified publisher identity, Apps Management permission, and policy attestations as owner/portal actions; do not infer them.
- Website, support, privacy-policy, and terms URLs are optional for Skills-only submissions under the cited error reference, but record whether they were supplied.
- Every bundled Skill must pass the portal safety/security scan. A local check is not the portal scan.
- A demo-recording URL is listed as an additional MCP-backed requirement, not a general Skills-only requirement. YouTube title and description are optional helpers unless current supplied portal rules say otherwise.
- Upload validation, safety scan, review, approval, and publication are separate states. Do not collapse or invent them.

## Evidence rules

- Treat an independent QA verdict as an input, not something this Skill can create.
- Treat an old-version result as version drift, not current evidence.
- When evidence is missing, leave the dependent field blank and mark the section `PARTIAL_MISSING_INPUT`. Use `BLOCKED_UNVERIFIED_EVIDENCE` only when the user asks to present an unexecuted test, QA, scan, review, or publication result as real or passed.
- When sources contradict, show both source labels and stop the affected section.
- Do not claim that a complete writing pack guarantees acceptance.

## Validation JSON shape

For a complete pack, create `submission-pack.json` with this top-level shape before running the bundled validator:

```json
{
  "pack_status": "DRAFT_COMPLETE_FROM_SUPPLIED_EVIDENCE",
  "artifact_use": "SUBMISSION_DRAFT",
  "submission_type": "skills-only",
  "package_name": "example-plugin",
  "skill_name": "write-example-pack",
  "version": "1.0.0",
  "package_digest": "supplied digest or evidence reference",
  "rule_snapshot": "2026-08-10",
  "display_name": "Example",
  "short_description": "One-line value",
  "long_description": "Evidence-bound description",
  "skill_description": "Required Skill description, at most 1,024 characters",
  "developer_name": "Supplied developer",
  "category": "Supplied portal category",
  "capabilities": ["Confirmed capability"],
  "starter_prompts": ["A realistic user request"],
  "positive_cases": [
    {
      "prompt": "Executed prompt",
      "fixture": "Fixture or reference",
      "expected_activation": "YES or NO",
      "expected_behavior": "Expected behavior",
      "expected_result_shape": "Expected result shape",
      "actual_result_summary": "Actual current-version result",
      "evidence_ref": "Received evidence reference"
    }
  ],
  "negative_cases": [
    {
      "prompt": "Executed boundary prompt",
      "fixture": "Fixture or reference",
      "expected_activation": "YES or NO",
      "expected_behavior": "Expected safe behavior",
      "expected_result_shape": "Expected result shape",
      "actual_result_summary": "Actual current-version result",
      "evidence_ref": "Received evidence reference",
      "reason": "Why this behavior is required"
    }
  ],
  "release_notes": "Supported version facts only",
  "independent_verdict": "Supplied verdict"
}
```

The complete file must contain five positive objects and three negative objects. Do not use placeholder text to satisfy the validator.

Use `artifact_use: TEST_ONLY_NOT_FOR_SUBMISSION` when the supplied source explicitly identifies itself as a fixture, sample, test-only artifact, or non-submission material. Use `SUBMISSION_DRAFT` only when no such restriction is present.

## Updating these rules

Recheck the official pages before releasing a new Skill version. If a route, field, limit, case requirement, or mandatory material changes, update this reference, the validator, the test fixtures, and the release notes together.
