---
name: mavixx-project-bootstrap
description: Prepare and begin implementing a new software project by resolving material requirements, establishing useful project guidance, and choosing an architecture and design direction. Use for a new build, an untouched starter, or a formally requested rebuild; route a functional or partially built existing codebase to `$mavixx-project-upgrade` and do not use for a narrow known fix.
---

# Mavixx Project Bootstrap

Complete a proportional preflight before material implementation. Preflight is a delivery phase, not the final result when the user asked to set up or build the project.

## Route the project

- Empty or starter-only folder: use **new mode**.
- Functional or partially implemented codebase: do not apply a new-project setup over it; use **existing mode** and route the work to `$mavixx-project-upgrade`.
- Unclear state: inspect files, Git status, manifests, routes, and build commands before deciding.

Read [references/preflight.md](references/preflight.md) and follow only the selected mode. Use [assets/AGENTS.template.md](assets/AGENTS.template.md) and [assets/PROJECT_BRIEF.template.md](assets/PROJECT_BRIEF.template.md) as adaptable output templates.

## Preflight contract

1. Classify known inputs as **confirmed**, **safely inferable**, **optional**, or **blocking**.
2. Ask only about blocking decisions whose answers materially change architecture, data handling, cost, brand direction, or user experience.
3. Offer a recommended choice whenever practical. Never invent credentials, legal claims, customer proof, brand assets, or business rules.
4. For a new project, create or update `PROJECT_BRIEF.md`, root `AGENTS.md`, and an implementation plan when they improve continuity. For an existing repository, preserve and extend current instructions instead of replacing them with generic templates. Invoke `$mavixx-design-system` when the product has a user interface.
5. Present a concise preflight summary: project mode, confirmed decisions, missing items, proposed defaults, risks, phases, and definition of done.
6. If the user already requested the build or setup, continue into implementation after actual blockers are resolved. Pause only for unresolved choices that materially change the product, architecture, data safety, cost, or brand identity; do not pause merely because the requested work is substantial.

## External resources

Do not silently install third-party skills or copy design systems. If an external skill, reference website, font, component, API, or asset library would materially improve the project, explain what it contributes, its source/license when known, and whether it is required or optional. Obtain approval before installation or external mutation.

## Completion

Preflight is complete when another Codex thread can understand the product, constraints, commands, architecture direction, and acceptance criteria from project files without relying on chat history. The user's build request is complete only after the implementation and relevant verification are also complete.
