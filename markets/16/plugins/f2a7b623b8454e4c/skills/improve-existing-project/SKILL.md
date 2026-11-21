---
name: improve-existing-project
description: Refactor, redesign, modernize or extend an existing app repository while preserving working behavior, user data and current project conventions.
---

# Improve Existing Project

1. Before edits, inspect current tree, git status, scripts, packages, app entry points and expected user behavior. Read `../../references/execution-model.md` and `../../references/testing-and-evidence.md`.
2. Record baseline tests/build and identify user-requested scope. Keep changes surgical; do not upgrade unrelated frameworks or redesign adjacent screens.
3. For visual changes, study existing branding and compare before/after. For functionality, identify contracts, state persistence and error cases. Add a regression test for each fixed bug where practical.
4. Use isolation/worktrees for agents with overlapping edits. Preserve unrelated files and uncommitted work; no automatic commits/pushes.
5. Run focused tests then broad tests as feasible; report exact diffs, before/after evidence, regressions and limits.
