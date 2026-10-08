---
name: obi-composition
description: Create or revise structured composition data for an Open Bible Images scene. Use when a biblical image needs a precise narrative moment, subjects, actions, spatial relationships, setting, framing, camera, lighting, visual focus, or a review/feedback finding requires the scene definition to change independently of a provider prompt.
---

# OBI Composition

Describe the intended image as durable, human-editable scene data. Read [references/composition-record.md](references/composition-record.md) for the output contract.

When a canonical project JSON file is supplied, preserve all other sections, update only `composition`, increment its artifact revision and the project revision, and append a history/capability-run entry. If revision was triggered by feedback or review, link the new composition revision back to that item. If no project file is supplied, label the result `unpersisted`.

## Workflow

1. Read the brief, Scripture scope, research, entities, approved character references, current composition, and exact feedback/review finding when applicable.
2. Define the exact narrative moment and primary message.
3. Describe all material subjects, their actions, expressions, gaze, pose, and relationships.
4. Define foreground, middle ground, background, geography, architecture, objects, weather, and time of day.
5. Define viewpoint, shot size, camera height, lens character, aspect ratio, lighting, and visual hierarchy only as needed.
6. Link details to research claims or mark them as creative choices.
7. When revising from feedback, change only the affected scene decisions plus necessary dependencies; preserve unrelated approved or intentional choices.
8. Record alternatives and unresolved decisions.
9. Mark the result `working` for private exploration or `draft` for formal review; only a person may mark it approved.
10. If the composition change makes the existing prompt stale, return disposition `needs_prompt_revision`. If the requested fix still depends on unresolved evidence, return `needs_research` or `needs_sources` instead of guessing.

## Boundaries

- Begin from available information; do not block early composition work merely because research is incomplete.
- Keep unsupported details visibly provisional.
- Do not write provider-specific prompt prose.
- Do not change canonical entities or character portrayals.
- Do not add figures or narrative events merely to make the image dramatic.
- Favor natural human behavior, varied poses, and documentary realism over staged symmetry.
- Do not silently alter unrelated composition decisions while addressing one feedback item.

Completion means another person can understand and critique the intended scene without seeing an image prompt, and any affected downstream prompt is clearly marked for revision.

## User-facing response

Lead with a compact scene direction, not the schema. For a feedback-driven revision, summarize what changed and what was deliberately preserved. Include only the narrative moment, key arrangement, camera/light direction, and up to three unresolved decisions. If the prompt is now stale, end with a compact **Revise prompt** action. Keep complete structured data in the project record.
