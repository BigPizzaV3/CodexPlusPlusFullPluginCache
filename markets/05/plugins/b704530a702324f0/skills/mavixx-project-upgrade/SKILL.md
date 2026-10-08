---
name: mavixx-project-upgrade
description: Implement and verify an end-to-end upgrade of an existing website or software project while preserving working behavior, user changes, data, routes, integrations, and brand intent. Use for broad modernization, UI or UX improvement, redesign, stabilization, inherited projects, or completing a partially built codebase; do not use for an audit-only request or a narrow known fix unless explicitly invoked.
---

# Mavixx Project Upgrade

Use an audit-first, checkpointed upgrade that continues into implementation. Never treat modernization as permission to rewrite the project, and never treat the audit as completion when the user requested an upgrade.

Read [references/upgrade-protocol.md](references/upgrade-protocol.md) before changing code. For any user-facing website or interface upgrade, also read [references/ui-upgrade.md](references/ui-upgrade.md).

## Authorization and mode

- If the user asks only to audit, review, explain, or plan, inspect and report without changing files.
- If the user asks to upgrade, modernize, redesign, improve, set up, finish, or fix the existing project, that request authorizes implementation within the stated scope. Do not stop for a redundant approval after presenting the audit or plan.
- If the editable repository is not present in the active workspace, stop and request the source. A live URL is not an editable project.

## Required behavior

1. Locate the real project root. Read applicable repository instructions, Git status/history, manifests, architecture, routes, data models, environment-variable names, tests, and deployment configuration.
2. Establish a baseline with safe project-native checks. For UI work, run the application and inspect representative pages at desktop and mobile widths before editing. Record pre-existing failures separately.
3. Map critical user journeys and invariants. Identify what must remain stable, what is broken, what is incomplete, and what is merely dated.
4. Create a concise prioritized working audit covering only relevant functionality, setup, UX, visual consistency, responsiveness, accessibility, performance, security, maintainability, dependencies, and release risk. Separate **must fix**, **recommended**, and **optional redesign** work.
5. Make a recoverable Git checkpoint when safe and useful. Never overwrite unrelated dirty changes or user-owned files.
6. Implement the authorized scope in reviewable phases. Prefer shared foundations before page-by-page patches. Keep data, APIs, URLs, analytics, SEO, authentication, and deployment compatibility stable unless the request changes them.
7. For visual changes, use `$mavixx-design-system` to establish direction and apply it to the code. A `DESIGN.md` file alone is not an upgraded UI.
8. After each material phase, use `$mavixx-quality-gates`, fix in-scope failures, and repeat affected checks. Visually inspect the rendered UI rather than inferring quality from source code.

Stop and request direction only when the upgrade requires destructive data changes, unavailable required credentials, an uncertain business rule that changes behavior, a brand conflict that approved assets cannot resolve, missing editable source, or a materially expanded scope. Continue all safe work that is not blocked.

## Completion gate

Do not hand off an upgrade while safe in-scope implementation remains. Completion requires actual source or configuration changes, relevant build and test evidence, exercised critical journeys, and rendered desktop/mobile evidence for UI work. Clearly distinguish remaining blockers and pre-existing failures from the completed upgrade.
