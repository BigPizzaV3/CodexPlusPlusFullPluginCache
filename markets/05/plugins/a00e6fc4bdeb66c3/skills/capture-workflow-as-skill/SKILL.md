---
name: capture-workflow-as-skill
description: Observe, extract, normalize, and convert a repeated real-world workflow into a reusable agent skill with triggers, inputs, decisions, tools, permissions, resources, quality gates, exceptions, and evaluation cases. Use when a user repeatedly explains the same task, asks to save a workflow as a skill, convert a conversation or SOP into a skill, learn from completed work, standardize a successful process, or improve a skill from usage history with explicit human review.
---

# Capture Workflow as Skill

Capture demonstrated work without silently learning unrelated behavior.

## Workflow

1. Confirm the workflow boundary, intended users, frequency, variability, risk, source material, and installation location.
2. Gather representative successful and failed examples. Do not treat a single run as a stable process.
3. Extract objective, trigger language, inputs, outputs, invariants, decisions, tools, permissions, external effects, failure modes, approvals, and completion evidence.
4. Separate organization-specific facts from general method and secrets from reusable configuration.
5. Decide whether the durable artifact should be a skill, prompt, SOP, agent, automation, hook, connector, or combination. Do not force every repetition into a skill.
6. Design the smallest reliable skill using `references/workflow-extraction.md` and `assets/workflow-intake.md`.
7. Reuse scripts, templates, and references when deterministic execution or progressive disclosure improves reliability.
8. Create realistic should-trigger, should-not-trigger, execution, missing-tool, and safety tests.
9. Obtain explicit approval before installing, activating, replacing, or granting new permissions.
10. Forward-test, repair demonstrated failures, version the result, and record provenance.

## Learning boundary

- Never retain private material or preferences beyond the authorized artifact.
- Never infer permission from observed user behavior.
- Never self-update an installed skill without a reviewable diff and approval.
- Exclude accidental workarounds, obsolete steps, credentials, and one-off exceptions unless intentionally generalized.

## Output

Return workflow model, artifact decision, proposed skill architecture, risks, evaluation set, approval points, and final package when creation is authorized.

For workflows that create downstream controlled artifacts, define an artifact contract: stable identity, version, lifecycle status, owner, sources, usage, precedence, dependencies, acceptance evidence, and replacement history. The captured workflow must be executable without hidden conversation context and include a clean-room test plus observable completion evidence.
