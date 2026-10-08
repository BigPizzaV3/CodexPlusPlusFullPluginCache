# Mavixx Forge operating modes

## Determine the real project state

Inspect the active directory before choosing a workflow. A repository with application code, routes, components, or deployment configuration is an existing project even when it is incomplete. A blank folder, product brief, or untouched starter is a new project. If multiple repositories are present, identify the target from the user's request and repository instructions; ask only when the target remains ambiguous.

## Requested outcome controls the stopping point

| User request | Required outcome |
| --- | --- |
| Audit, review, explain, or plan | Evidence-backed findings or plan; do not mutate unless also asked |
| Set up or build a new project | Preflight, implementation, runnable result, and relevant verification |
| Upgrade, modernize, redesign, or finish an existing project | Baseline, implemented changes, rendered and functional verification, and concise handoff |
| Fix a known issue | Focused implementation and checks for the affected behavior |
| Prepare for release | Applicable quality gates, in-scope fixes, repeated checks, and release/rollback notes |

## Existing website route

Confirm that editable source is present. Inspect repository instructions, dirty files, package scripts, framework, routes, shared UI, styling system, data and authentication boundaries, environment-variable names, tests, and deployment configuration. Establish a working baseline, then use `$mavixx-project-upgrade`. For UI work, define a coherent direction with `$mavixx-design-system`, apply it to shared foundations and representative pages, and verify the rendered result with `$mavixx-quality-gates`.

## New project route

Use `$mavixx-project-bootstrap` to resolve material requirements and write only useful project guidance. If the user requested a build, continue into code after blockers are resolved; do not return a preflight document as though the product were complete.

## Stop conditions

Pause only for an actual blocker: missing source, destructive or irreversible data work without authorization, unavailable required credentials, mutually incompatible business rules, a brand conflict that cannot be resolved from approved assets, or scope that materially exceeds the request. A large but clearly requested implementation is not itself a blocker.
