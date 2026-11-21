---
name: assessments
description: Run MockMentor assessment workflows when a student wants to take a mock, evaluate a completed mock or scorecard, check an MCQ or written answer, review results, or understand mistakes.
---

# Assessments

Use this skill for MockMentor assessment requests. Apply the guardrails skill and perform the account-and-access preflight once at the start of the requested assessment workflow. Use the student's current exam and feature access from that fresh preflight; do not ask again for known information or bypass a disabled, locked, or unavailable feature.

## Route the request

- For starting, presenting, submitting, grading, or reviewing a generated MockMentor mock, read [references/take-my-mock.md](references/take-my-mock.md).
- For evaluating a completed external mock, scorecard, OMR sheet, or uploaded result, read [references/evaluate-my-mock.md](references/evaluate-my-mock.md).
- For checking or explaining an individual MCQ, short answer, or written answer, read [references/check-my-answer.md](references/check-my-answer.md).

Load only the reference needed for the current request. A feature reference does not create tools or permissions. Use a workflow only when its required MCP tools are present and the server says the feature is accessible and operational. Otherwise state that the workflow is not currently available; do not substitute a different write tool, fabricate a saved result, or claim that analysis was persisted.
