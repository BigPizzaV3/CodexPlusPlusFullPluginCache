---
name: gdd-migration
description: Use when migrating legacy, fragmented, Figma-based, spreadsheet-based, or otherwise non-canonical game-design material into the receiving project's canonical KB.
---

# GDD Migration Skill

Apply the [receiving-project contract](../../references/project-context.md). Use the [migration brief and confirmation templates](../../references/gdd-templates.md) and [review checklist](../../references/gdd-review-checklist.md) when preparing publication.

## Goal
Migrate one bounded feature/system at a time into a clear canonical GDD without creating competing sources of truth or repeatedly re-reading entire legacy source sets.

## Trigger
Use for legacy GDD migration or consolidation of fragmented design sources. Also activate `knowledge-steward` and `gdd-authoring` when publishing or substantially rewriting canonical GDD content.

## Source routing
- Design intent, gameplay rules, formulas, states, conditions, edge cases, accepted decisions → canonical KB.
- Large numeric/config tables → the designated structured data/config source; link and explain meaning, do not duplicate.
- UI layout, wireframe, prototype, spatial visual flows → the designated visual-design source (for example, Figma); migrate behavioral rules and link exact frames.
- Implemented behavior/schema → the designated repository/runtime evidence; report drift against design.
- Analytics data → the designated analytics source; document definitions/usage, not raw data.
- Obsolete migrated material → archive/deprecate with replacement link; do not silently delete historical evidence.

## Required workflow
1. Define the migration brief: feature boundary, goal, exclusions, owner/reviewers, source list, known conflicts, target canonical owner.
2. Inventory source structure once. For Figma, record exact page/frame/node references and revisit only frames relevant to the current batch.
3. Extract atomic claims: intent, rule, state/transition, condition/outcome, formula meaning, edge case, UI behavior, config reference, runtime observation, decision/proposal/open question.
4. Classify every claim by knowledge state and destination.
5. Reconcile conflicts explicitly. If authority is unresolved, block that claim from canonical publication rather than guessing.
6. Match the migration scope and target artifacts to existing explicit approval. Reuse an approved brief or scoped migration request. If material conflicts or decisions remain, consolidate only the unresolved facts/questions, recommendations, assumptions and affected artifacts for confirmation.
7. Publish within that authorized scope once; do not require a new approval round for an already approved migration. Return only material departures or unresolved decisions to the owner. Update ownership/index/decision records only where materially needed.
8. Deprecate/archive superseded legacy material without deleting required evidence.
9. Read back all changed artifacts and verify links, metadata, ownership, and unresolved follow-up work.

## Efficiency rules
- Migration unit is one bounded feature/system, not an entire Figma file or legacy corpus.
- Inventory broadly once; then read narrowly.
- Do not re-read legacy material already compiled into an active canonical GDD unless validation/conflict investigation requires it.
- Prefer updating an existing canonical owner over creating another note.
- Keep a phase tracker only for long migrations; completed trackers move out of the active path.

## Definition of Done
A migration is complete when one canonical owner exists, relevant legacy sources were inventoried, durable claims were routed correctly, conflicts are resolved or explicitly open, external source ownership is linked correctly, significant accepted decisions are persisted, legacy material is deprecated/archive-routed as appropriate, owner approval is recorded, and changed artifacts pass readback.

## Project migration state
Use any active migration SOP and tracker designated by the receiving project. The source KB's legacy `GDD Migration SOP.md` was not present in the migration snapshot; this package does not claim to include it. The operational workflow here and bundled templates/checklist are available without that file. Resolve any project-specific migration gate from current project guidance.
