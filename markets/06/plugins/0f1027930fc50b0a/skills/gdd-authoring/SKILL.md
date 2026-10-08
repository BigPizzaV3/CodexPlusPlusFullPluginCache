---
name: gdd-authoring
description: Create a new GDD or substantially revise a canonical game-design document with explicit rules, source ownership, evidence, and review gates.
---

# GDD Authoring Skill

Apply the [receiving-project contract](../../references/project-context.md). For substantial authoring, load the bundled [authoring standard](../../references/gdd-authoring-standard.md); use [templates](../../references/gdd-templates.md) for document structure and the [review checklist](../../references/gdd-review-checklist.md) before publication. Apply the receiving project's explicit policy where it differs.

## Goal
Produce canonical GDDs that are simultaneously readable by humans and reliably interpretable by AI agents, while keeping live numeric/config data and final visual assets in their designated owners.

## Trigger
Use for new GDDs or substantial GDD rewrites. For legacy-source migration, also activate `gdd-migration`. For any durable KB write, also apply `knowledge-steward`.

## Authoring principles
- One canonical owner per durable rule.
- Current design first; history belongs in decisions/archive.
- Separate design intent from runtime observations.
- Keep large/live numeric tables in designated Sheets/CSV; explain meaning, relationships, formulas, methodology, and intent in the GDD.
- Use progressive disclosure: orientation → normative design → evidence/operations.
- Essential meaning must remain understandable in text/structured form even when external visuals are unavailable.
- Unknowns remain explicitly unknown; do not smooth them into confident prose.

## Required workflow
1. Read the available project guide, current state and relevant domain context resolved through the receiving-project contract; load `knowledge-steward` once when writing durable knowledge.
2. Identify the canonical owner and scope. Avoid creating a new note if an existing canonical note already owns the concept.
3. Discover only the minimum source set needed: canonical KB, designated config, exact Figma frames, code/runtime evidence, analytics, or legacy material as applicable.
4. Separate accepted design facts, runtime observations, proposals, temporary assumptions, and open questions.
5. Map the intended content and artifacts to existing explicit approval. A complete approved brief or scoped update request is sufficient; do not require a new confirmation pack merely because the write is substantial. If material decisions or authority remain unresolved, consolidate those questions, recommended resolutions, assumptions and affected artifacts for the owner.
6. Write the authorized final state directly. Ask only about unresolved material decisions or a material departure from approved scope; use `review` for an actual unresolved checkpoint.
7. Apply required metadata and consistent terminology.
8. Add tables/diagrams/formulas only when they reduce ambiguity or reading time; do not force visuals.
9. Link external sources with explicit ownership meaning rather than copying volatile data.
10. Run the GDD review gate, read back all changed artifacts, then update context/index/state only when their current-state meaning changes.

## Document structure
Use sections as applicable:
- **Layer 1 — Orientation:** summary, player experience/design goal, scope/exclusions, at-a-glance facts, compact overview visual when justified.
- **Layer 2 — Normative design:** core rules, states/flow, inputs/conditions/outputs/failure handling, formulas, interactions/dependencies, edge cases.
- **Layer 3 — Evidence and operations:** structured-config ownership, exact Figma references, repo/runtime paths and drift, analytics/acceptance criteria, open questions and validation state.

## Metadata baseline
Use compatible YAML frontmatter for substantial new/reworked GDDs with `type`, `project`, `domain`, `feature`, `status`, `canonical`, `owner`, `validation`, `last_reviewed`, and optional `review_after`. Lifecycle state and evidence quality are independent.

## Visual and formula rules
Use Markdown tables for exact mappings, Mermaid for compact rule/state flows, charts generated from owned source data for trends, exact Figma frames for UI layout/prototypes, and owned visual references for art/VFX. Never encode essential meaning only through a visual. Define variables/units and evaluation order for non-trivial formulas and include a worked example when useful.

## Activation gate
A GDD may become `active` when material conflicts are resolved or excluded, design rules are separated from runtime observations, required source/visual context is present, essential behavior is understandable without hidden external context, owner approval exists for the approved scope, and changed artifacts pass readback.

## Project standards
The bundled references preserve the original reusable authoring workflow. If the receiving project maintains active local standards, reconcile differences against its agent guide and source-of-truth policy; installing the plugin does not silently replace those project standards.
