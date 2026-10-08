# Lint runtime and project profiles

Use the read-only script for mechanical checks. Semantic correctness, deletion
decisions and source authority still require the workflow's review.

## Runtime

Python 3.9+ and the dependencies in [requirements.txt](../requirements.txt) are
required. Use the host's existing Python environment if it provides them;
otherwise prepare an isolated environment using the host's dependency policy.
Installing the plugin alone does not install Python packages. Do not modify the
plugin cache or a project's dependencies just to run an audit.

Example after resolving these placeholder paths:

```sh
python3 -m venv /temporary/path/kb-lint-venv
/temporary/path/kb-lint-venv/bin/python -m pip install -r /installed/kb-maintenance/requirements.txt
/temporary/path/kb-lint-venv/bin/python /installed/kb-maintenance/scripts/kb_lint.py /target/vault --json
```

If the host cannot execute Python or obtain the dependencies, provide a manual
review with that limitation. Do not report a script pass that did not run.

## Select the project conventions

The script reads `<vault>/.kb-lint.json` when present. `--config /path/profile.json`
selects another profile, including a temporary profile for an audit-only task.
Do not write a profile into the project without authorization for that change.
Values supplied in the profile replace the corresponding defaults.

For a plain Markdown project, a possible profile is:

```json
{
  "work_dirs": ["work/active"],
  "decision_dirs": ["docs/decisions"],
  "archive_dirs": ["docs/history"],
  "archive_names": [],
  "hot_names": ["AGENTS.md", "CLAUDE.md", "index.md"],
  "context_names": ["index.md"],
  "required_metadata": [],
  "decision_id_fields": ["decision_id", "id"],
  "decision_id_pattern": "ADR-[0-9]+",
  "link_types": ["wikilinks", "markdown"]
}
```

Use actual project conventions, not this example blindly. An empty directory list
disables the corresponding layout-specific check. With no profile the original
KB layout remains the default; coverage always includes the effective settings.

| Profile key | Default / meaning |
| --- | --- |
| `work_dirs` | `00_System/Work/Active`; scan these relative subtrees for stale active work |
| `decision_dirs` | `00_System/Decisions/Records`; scan these relative subtrees for record definitions |
| `archive_dirs` | `99_Archive`; archive subtrees are exempt from required metadata and current-owner uniqueness |
| `archive_names` | `Archive`; directory basenames treated as archive at any depth |
| `hot_names` | `AGENTS.md`, `CLAUDE.md`, `PROJECT_STATE.md`, `_Context.md`; warn on links to archive |
| `context_names` | `_Context.md`; check for a sibling Markdown owner |
| `exclude_dirs` | `.git`, `.obsidian`, `.agents`, `.claude`, `.codex`, `.venv`, `node_modules`, `Library`, `Temp`, `Logs`; basenames at any depth or exact relative subtrees |
| `required_metadata` | `type`, `project`, `status`; `[]` allows plain Markdown without frontmatter |
| `valid_statuses` | `draft`, `review`, `active`, `temporary`, `deprecated`, `superseded`, `archived` |
| `inactive_statuses` | `deprecated`, `superseded`, `archived`; exclude retired owners from uniqueness and stale-work checks |
| `canonical_key_fields` | `domain`, `feature`; fields defining a canonical owner's identity |
| `decision_id_fields` | `decision_id`, `id`; defining ID metadata, preferred over a first H1 or filename starting with the ID |
| `decision_id_pattern` | `DEC-` followed by four digits, a hyphen and three digits; use a regex matching the complete project record ID |
| `link_types` | `wikilinks`, `markdown`; select the local link dialects to inspect |

Lifecycle fields (`status`, `canonical`, `replacement`/`superseded_by`,
`review_after`, `last_updated`/`last_reviewed`) retain those names. Projects with a
different schema need an explicit mapping/adaptation; this profile is not an
arbitrary schema translator. Structured reviewer/owner metadata is allowed, while
identity, lifecycle and date fields must be scalar.

## Interpret findings and coverage

- A missing/non-directory vault, invalid profile or missing runtime dependency
  exits 2. Errors such as duplicate owners/IDs or invalid YAML exit 1. Warnings
  exit 0; callers must inspect `issues`, not just the exit code.
- An empty scope produces an `empty-scope` warning and `coverage.status: empty`.
  It is not a successful assessment of project knowledge.
- Inspect `coverage.matched_files` before interpreting the work/decision checks.
  Zero matching files does not establish that a differently named directory was
  inspected. Confirm or change the profile before claiming that coverage.
- Current canonical owners exclude inactive lifecycle statuses. A historical
  record can retain `canonical: true` with its superseded status and replacement.
- Decision body references never define record IDs. Use defining metadata, the
  first H1 starting with the ID, or an ID-prefixed filename. Unknown definitions
  receive a warning rather than silently passing duplicate-ID coverage.
- CommonMark inline links, images and defined reference links are checked as
  local paths. Percent-encoded paths are decoded; `/path` is vault-relative.
  Wikilinks support note names, vault-relative/source-relative paths and explicit
  attachment filenames. Code fences and inline code are excluded.
- Remote URLs, heading fragments, raw HTML links and undefined Markdown reference
  labels are not validated. Local paths outside the vault are reported, not read.
- `--skip-unresolved-links` suppresses missing targets in partial materializations
  and reports reduced coverage. It does not suppress ambiguous wikilinks or outside-vault Markdown links.
- `--stale-work-days N` overrides the 30-day threshold. Findings are mechanical
  observations; a review date or old work note is not permission to archive it.
