---
name: obi-image-review
description: Score and review an Open Bible Images draft for biblical fidelity, historical plausibility, material realism, continuity, and publication readiness. Use when an actual image or external feedback needs visible, evidence-based review; identify the earliest responsible artifact and the next capability, but do not grant final human approval.
---

# OBI Image Review

Review the actual image, not merely its prompt. Treat Scripture as authoritative for what it states without turning artistic tradition or one plausible reconstruction into biblical fact. Read [references/review-rubric.md](references/review-rubric.md) before scoring and use [references/review-record.md](references/review-record.md) for stored findings.

When a canonical project JSON file is supplied, preserve all other sections, update only `reviews`, increment its artifact revision and the project revision, and append a history/capability-run entry. If review was triggered by user, collaborator, consultant, or external feedback, link the review finding back to that feedback item. If no project file is supplied, label the result `unpersisted`.

## Workflow

1. Inspect the image at sufficient detail.
2. Identify the subject, passage, narrative moment, approximate period, location, culture, and image type. Load the exact composition, character records, prompt snapshot, references, approved research, and triggering feedback when available.
3. Review in this order: central action and people against Scripture; historical and cultural grounding; visible clothing, architecture, objects, activities, geography and environment; character continuity; then materials, construction, scale, anatomy, lighting, text, and generation artifacts.
4. Report only issues that materially affect publication, normally no more than five. Combine related problems and do not double-count.
5. Score from 100 using only visible, supported High- or Medium-confidence deductions. Put debated, speculative, low-confidence, cropped, obscured, or unassessable details in Research Notes without deduction.
6. Verify consequential specialized claims with reliable sources when research tools are available, especially before deducting eight or more points. If the evidence is insufficient, do not force a deduction; mark the finding `needs_research` or `needs_sources` and state the precise question.
7. For every material finding identify the earliest likely root cause: research, sources, entity, character, composition, prompt, or generation.
8. Assign a recommended next capability: `research_context`, `find_sources`, `define_entities`, `character_continuity`, `revise_composition`, `build_prompt`, `generate_draft`, or `human_decision`.
9. Provide a localized edit prompt only for findings whose root cause is already sufficiently supported. Do not use an edit prompt to paper over an unresolved research, entity, character, or composition problem.
10. If invoked through the Image Project front door and the user's request is broad enough to investigate the cause, allow the orchestrator to follow `needs_research` or `needs_sources` findings automatically and then update the review finding with the result.

## Feedback handling

External or human feedback is evidence of a concern, not proof that the concern is correct. Preserve the original comment and reviewer identity when supplied. Review the relevant image region and project context, then classify the feedback as supported, partly supported, unsupported, or inconclusive. Route supported concerns to the earliest responsible artifact and preserve the lineage from feedback → review finding → follow-up capability → revision.

## Boundaries

- Do not claim to see details that cannot be inspected.
- Do not invent a biblical or historical rule to justify an aesthetic preference.
- Do not approve your own output or replace consultant review.
- Do not edit the image unless the user separately requests revision or explicitly asked to fix/revise it as part of the same request.
- Do not hide uncertainty when references or approved artifacts conflict.
- Do not deduct for uncertainty or merely because another plausible reconstruction exists.
- Do not manipulate deductions to force a pass or failure.
- Do not claim an inscription is correct unless it is legible; transcribe exact writing or recommend specialist verification when it matters.

Completion means a creator can act on each finding without guessing what is wrong, where the problem originated, or which capability should handle it next.

## User-facing response

Return the scored format defined in the rubric: verdict and score, confidence, consultant recommendation, context, transparent deductions, priority feedback, strengths, research notes, optional artistic feedback, overall assessment, and localized edit prompt. For each material unresolved finding, add one compact next action such as **Research this**, **Find more sources**, **Update character**, **Revise composition**, **Revise prompt**, or **Generate revision**. Keep it direct and limit scored issues to those that matter.
