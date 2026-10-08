---
name: obi-entities
description: Identify and reconcile people, groups, locations, objects, structures, animals, and other reusable entities for an Open Bible Images project. Use before composition or character continuity work when scene elements need canonical OBI identity, or when review/feedback suggests the wrong entity or identity was used.
---

# OBI Entities

Build the project's entity set using [references/entity-record.md](references/entity-record.md). Reuse an existing OBI entity when it genuinely represents the same thing.

When a canonical project JSON file is supplied, preserve all other sections, update only `entities`, increment its artifact revision and the project revision, and append a history/capability-run entry. If the work was triggered by feedback or review, link the entity revision back to that finding. If no project file is supplied, label the result `unpersisted`.

## Workflow

1. Read the brief, Scripture scope, research claims, existing composition, available OBI entity records, and the exact feedback/review finding when applicable.
2. List every narratively or visually material person, group, place, object, structure, animal, and natural feature relevant to the question.
3. Search for canonical OBI matches using stable identifiers and relationships, not title similarity alone.
4. Record one of: matched, proposed_new, generic, uncertain, or excluded.
5. For people, preserve the distinction between Entity, Portrayal, Variant, and scene-specific Appearance.
6. Record time, age, location, ownership, part-of, and identity relationships when they affect continuity.
7. When responding to feedback, revise only the affected entity match or identity decision and preserve unrelated entity records.
8. Surface ambiguous matches and proposed new entities for human decision.
9. If an entity correction changes the intended scene, return disposition `needs_composition_revision`; if it only changes a person's portrayal/appearance, return `needs_entity_revision` with a handoff to `$obi-character-continuity`.

## Boundaries

- Do not create or merge canonical OBI entities without explicit authorization.
- Do not identify unnamed biblical figures more specifically than the text or evidence permits.
- Do not turn every incidental background item into a canonical entity.
- Do not define camera, lighting, or layout; those belong to composition.
- Do not invent a character appearance; route that work to `$obi-character-continuity`.
- Do not silently replace an existing entity merely because a review comment questions it; verify the identity first.

Completion means the composition can refer to stable entity records without hiding unresolved identity decisions, and any feedback-driven correction has a clear downstream handoff.

## User-facing response

Show only material entity matches, ambiguities, or decisions. For feedback-driven work, state whether the questioned identity was confirmed, corrected, or remains uncertain, and show the next action such as **Update character** or **Revise composition** when needed. Keep routine background entities and full record fields in the project file unless requested.
