---
name: mavixx-forge
description: Orchestrate Mavixx Forge across a new or existing software project and carry the requested work through implementation and verification. Use when the user explicitly says Mavixx Forge, asks to set up or build a new project, or wants an existing website or app upgraded, redesigned, stabilized, or finished. Do not use for a generic coding question with no project work.
---

# Mavixx Forge

Turn the user's request into a working, verified project result. An audit, plan, `PROJECT_BRIEF.md`, or `DESIGN.md` may support the work, but none is a substitute for implementation when the user asked to build, fix, set up, modernize, redesign, or upgrade.

Read [references/operating-modes.md](references/operating-modes.md), inspect the active workspace, and select one route. On a compatible shell, `../../scripts/preflight_inventory.sh <project-root>` can provide an initial inventory; supplement it with direct inspection and never treat its output as verification.

- **New or starter-only project:** use `$mavixx-project-bootstrap`, then continue into implementation when the user requested a build.
- **Existing website or application:** use `$mavixx-project-upgrade`. For material interface work, also use `$mavixx-design-system` and follow its implementation loop.
- **Verification or release review:** use `$mavixx-quality-gates`.
- **Narrow known fix:** handle it directly with project-native conventions; do not inflate it into a broad redesign unless requested.

## Execution contract

- Treat an explicit request to build, set up, fix, upgrade, redesign, modernize, or finish as authorization to edit files within that scope. Do not ask for approval again merely because implementation is substantial.
- Ask only when a missing choice materially changes business behavior, architecture, data safety, cost, brand identity, or the requested outcome and cannot be inferred safely.
- If editable source is absent, explain that a URL alone permits inspection but not implementation, and ask the user to open or attach the repository. Do not claim the website was upgraded.
- Read repository instructions and Git status before editing. Preserve unrelated user changes, working behavior, data, public routes, integrations, analytics, and brand assets unless the request changes them.
- Prefer the existing stack and conventions. Do not replace a framework or introduce a new design library solely to make the result look different.
- Keep moving through safe, in-scope work while a non-blocking detail is unresolved. Record reasonable defaults instead of turning every preference into a question.
- Use rendered evidence for interface claims. Start the app when possible, inspect representative desktop and mobile states, exercise important interactions, fix observed issues, and rerun affected checks.

## Completion contract

Do not finish an implementation request with only recommendations. Finish when the requested code or configuration is changed, relevant checks have been run, critical flows are exercised, and UI work has been inspected in a rendered state. Report implemented changes, evidence, pre-existing failures, remaining blockers, and any deployment action that still requires separate authority.
