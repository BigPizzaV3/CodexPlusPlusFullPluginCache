---
name: study-support
description: Run MockMentor study workflows when a student wants to create or revise a study plan, see today's tasks, report progress, find approved study material, or organize daily practice.
---

# Study support

Use this skill for planning, study-material, daily-task, and plan-progress requests. Apply the guardrails skill and perform the account-and-access preflight once at the start of the requested study-support workflow. Use fresh exam, evidence, access, and operational status from the server; do not invent availability, progress, sources, or saved state.

## Route the request

- For creating, replacing, revising, following, or reporting progress on a study plan, including today's persisted tasks, read [references/study-plan.md](references/study-plan.md).
- For finding or recommending study material, official resources, chapters, or practice sources, read [references/study-material.md](references/study-material.md).

Load only the reference needed for the current request. A feature reference does not create tools or permissions. Use a workflow only when its required MCP tools are present and the server says the feature is accessible and operational. Otherwise explain that it is not currently available; do not invent links, persistence, completion, or entitlement.
