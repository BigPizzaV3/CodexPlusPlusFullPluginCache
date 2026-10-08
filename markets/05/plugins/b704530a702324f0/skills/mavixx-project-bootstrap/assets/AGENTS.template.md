# Project instructions

## Product source of truth

Read `PROJECT_BRIEF.md` before material product decisions. Read `DESIGN.md` before interface changes.

## Working rules

- Preserve user changes and established behavior unless the task explicitly changes them.
- Inspect before editing; prefer existing project conventions.
- Keep secrets out of source control and document only environment-variable names.
- Make changes in reviewable phases and verify each material phase.
- When an action is safely available within scope, perform it and verify the result instead of delegating routine steps to the user.

## Commands

- Install: `[project command]`
- Develop: `[project command]`
- Format/lint/typecheck: `[project commands]`
- Test: `[project commands]`
- Build: `[project command]`

## Definition of done

- Acceptance criteria in `PROJECT_BRIEF.md` are satisfied.
- Applicable checks pass or pre-existing failures are clearly documented.
- Critical journeys are verified, including responsive UI states when applicable.
- Material risks and deployment/rollback notes are reported.
