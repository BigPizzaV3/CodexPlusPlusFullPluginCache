---
name: improve-coverage-with-9to5
description: Improve pull request coverage with exact, read-only context from the 9to5 coverage MCP server. Use when asked to identify uncovered changed lines, add or refine targeted tests, investigate coverage regressions, compare coverage runs, or verify that a test change improved PR coverage in a repository with 9to5 coverage enabled.
---

# Improve Coverage With 9to5

## Overview

Use 9to5 coverage to find the smallest meaningful coverage targets, then work against the local checkout to add tests and verify the result. Treat MCP as coverage evidence only: it never returns source and does not prove that a test is behaviorally correct.

## Workflow

1. Determine the repository as `owner/name` from the checkout remote or user context. If it is uncertain, call `list_repositories`.
2. Resolve the current pull request number and call `get_pr_coverage` before any detailed query. Record the resolved commit SHA, report format, baseline, project conclusion, and patch conclusion.
   When the user wants a visual report, call `show_pr_coverage` with the resolved repository, PR number, format, commit, run ID, and run version. Its card keeps file queries and pagination bound to that snapshot. Uncovered file ranges include unchanged lines; use `get_uncovered_changed_lines` for changed-line test targets.
3. Call `get_uncovered_changed_lines`. Paginate until the relevant target set is complete. Prioritize:
   - uncovered changed lines in behavior-bearing code;
   - files with the largest uncovered changed-line count;
   - line regressions before older uncovered lines;
   - narrow, coherent behaviors that can be tested without broad rewrites.
4. Inspect the corresponding source and tests from the local checkout. Never ask MCP for source and never treat a line number alone as a test specification.
5. When a target needs more coverage detail, call `get_test_suggestions_context` for at most 200 exact lines. Use its nearby hit states to understand coverage boundaries, not to invent assertions.
6. Add focused tests that exercise observable behavior. Follow the repository's testing conventions and avoid assertions that merely execute lines.
7. Run the smallest relevant test command first, then the repository's required broader checks.
8. Produce and upload the new coverage report using the repository's existing 9to5 CI/upload flow. Do not expose or reuse MCP credentials as coverage-upload credentials.
9. Re-query `get_pr_coverage` and `get_coverage_regressions`. Report the before/after patch metrics and any remaining uncovered changed ranges. Do not claim improvement until a new coverage run has been resolved.

## Query Discipline

- Pass `repository` to every repository-bound tool.
- Preserve the resolved `format` across related queries.
- Use exact SHAs when available. A SHA prefix must contain at least seven characters and be unique.
- Pass signed cursors back unchanged and continue while `truncated` is true.
- If `baseline_unavailable` is returned, stop regression analysis and explain that the matching base run must be uploaded. Never guess another baseline.
- If `ambiguous_format` is returned, list runs and select the intended format from repository context.
- Treat `repository_not_found_or_forbidden` as deliberately ambiguous; do not probe for repository existence.
- See [references/mcp-tools.md](references/mcp-tools.md) for tool selection and stable errors.

## Safety Boundaries

- All 9to5 MCP tools are read-only. Make repository edits only when the user asked you to implement tests.
- Read source and tests only from the authorized local checkout.
- Do not log, print, commit, or pass OAuth/API tokens to test commands.
- Do not use coverage-upload tokens at MCP or MCP tokens for uploads.
- Coverage is line-based. Do not infer branch or condition coverage.
- A covered line does not establish test quality. Prefer tests of behavior and failure modes over execution-only assertions.

## Completion

Finish with a compact evidence summary: test files changed, test commands and results, the resolved before/after run SHAs and format, patch coverage delta, closed target ranges, remaining target ranges, and any baseline or upload limitation.
