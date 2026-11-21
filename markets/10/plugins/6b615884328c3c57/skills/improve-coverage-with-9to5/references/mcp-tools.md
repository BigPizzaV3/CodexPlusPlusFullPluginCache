# 9to5 coverage MCP tool reference

Use the production Streamable HTTP endpoint at `https://coverage.9to5.software/mcp`.

| Tool | Use |
| --- | --- |
| `list_repositories` | Resolve an authorized `owner/name`. |
| `list_coverage_runs` | Resolve a run or disambiguate branch, PR, SHA, or format. |
| `get_pr_coverage` | Start a PR workflow; returns project, patch, baseline, conclusions, and changed files. |
| `show_pr_coverage` | Display an interactive PR card after resolving coverage; pass the exact run ID, version, SHA, and format. |
| `get_uncovered_changed_lines` | Get exact uncovered PR line ranges, optionally for one path. |
| `get_file_coverage` | Inspect covered/uncovered ranges for a file at a commit. |
| `compare_coverage` | Compare matching base/head runs; add `path` for exact line-state changes. |
| `get_coverage_regressions` | Return only regressions against the run's persisted baseline. |
| `get_test_suggestions_context` | Get target and nearby hit states for up to 200 lines; never source or test suggestions. |

All repository-bound tools require `repository` as `owner/name`. Page size defaults to 100 and is capped at 250. Continue with `next_cursor` while `truncated` is true.

Stable recoverable errors:

- `repository_not_found_or_forbidden`: verify the signed-in identity, installation, and token scope.
- `coverage_run_not_found`: verify selector, format, and whether CI uploaded the report.
- `baseline_unavailable`: upload the matching base commit and format; never substitute a guessed run.
- `ambiguous_format`: list runs and retry with an explicit format.
- `invalid_selector`: correct the PR, SHA, path, line bounds, status, or page size.
- `invalid_cursor`: restart pagination with the same selectors and no cursor.
