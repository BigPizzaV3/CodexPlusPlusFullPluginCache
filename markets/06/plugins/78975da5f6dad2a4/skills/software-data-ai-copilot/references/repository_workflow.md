# Repository Workflow

## Purpose

Use this file when working in an existing codebase.

The repository is the primary source of truth for architecture, conventions, build/test commands, and implementation patterns.

# 1. Read before changing

Start with the smallest set of files needed to understand the task.

Typical order:

1. repository/project instructions;
2. README or relevant docs;
3. dependency/build manifest;
4. directory tree around the feature;
5. relevant implementation;
6. nearby tests;
7. config/schema/migrations if affected;
8. CI/build rules when validation depends on them.

Do not scan the entire repository mechanically when the task is narrow.

# 2. Instruction files

Look for files such as:

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `.github/copilot-instructions.md`
- `.github/instructions/*.instructions.md`
- repository-specific contribution docs

Respect their scope.

If multiple instruction files conflict, prefer the most specific applicable repository rule, then the user’s explicit request.

Do not copy conventions from a different subsystem when path-specific rules exist.

# 3. Find the existing pattern

Before creating a new pattern, search for a similar implementation.

Examples:

- similar API endpoint;
- sibling UI component;
- existing database migration;
- another background job;
- existing auth check;
- existing test fixture;
- existing model/tool wrapper.

Prefer consistency unless the existing pattern is demonstrably unsafe or the user requests redesign.

# 4. Task framing

Turn the request into:

## Desired behavior
What should become true?

## Non-goals
What should remain unchanged?

## Affected boundaries
Examples:
- API contract;
- database schema;
- UI state;
- event format;
- model output;
- batch job interface;
- CLI behavior.

## Risks
Examples:
- backwards compatibility;
- data migration;
- auth/security;
- concurrency;
- performance;
- deployment sequencing.

# 5. Minimal change principle

A good change:
- touches the fewest necessary components;
- preserves existing abstractions when adequate;
- avoids unrelated cleanup;
- has a clear validation path.

A small change is not automatically good if it duplicates logic or violates an established boundary. Choose the smallest coherent change.

# 6. New dependency test

Before adding a dependency, ask:

- Is the capability already present?
- Can the standard library/framework solve it?
- Is the dependency actively maintained?
- What is its runtime/bundle/security cost?
- Does the project already use an alternative?
- Is it compatible with current versions?

Do not add a dependency silently.

# 7. Configuration

Preserve the project’s existing configuration pattern.

Do not:
- hardcode secrets;
- invent environment variables without documenting them;
- change defaults with broad production impact without calling it out.

When adding config, define:
- name;
- purpose;
- default behavior;
- required/optional;
- validation;
- deployment impact.

# 8. Database/schema changes

Before changing schema:

- identify current migration tool;
- inspect nearby migrations;
- consider existing data;
- consider backwards compatibility;
- determine deployment order;
- define rollback/forward-fix strategy;
- test both fresh and upgraded states when relevant.

Avoid destructive schema changes without explicit scope and migration planning.

# 9. Validation

Use the repository’s actual commands when known.

Prefer:
- targeted tests first;
- type/lint/static checks for affected code;
- integration tests for changed boundaries;
- build/package check;
- broader suite only when warranted.

Never claim tests passed unless actual output is available.

# 10. Completion summary

For meaningful changes summarize:

- files/components changed;
- behavior added/fixed;
- tests/validation performed or recommended;
- compatibility/migration notes;
- remaining risks.

Do not claim implementation completion if the codebase was not actually modified.
