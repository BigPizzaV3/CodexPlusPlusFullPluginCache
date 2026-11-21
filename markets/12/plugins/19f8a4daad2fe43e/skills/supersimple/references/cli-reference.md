# Supersimple CLI Reference

Full docs: https://docs.supersimple.io/guides/managing-the-data-model/using-the-cli

Requires CLI **2.27.0 or later**. Install: `brew tap gosupersimple/cli && brew trust --tap gosupersimple/cli && brew install supersimple`. Direct macOS/Linux binaries are linked in the CLI docs. Check the installed command’s `--help` for current flags.

## Contents
- [Authentication](#authentication)
- [Export](#export)
- [Import](#import)
- [Validate](#validate)
- [Fix](#fix)
- [Discover](#discover)
- [dbt conversion](#dbt-conversion)
- [Entity management](#entity-management)

## Authentication

Run `supersimple status` to see the current account without prompting. Inspect the output; it always
exits 0, including not-logged-in, invalid-token, and failed-check results. Do not use its exit code
as an authentication check. An invalid token entered at an API command’s prompt can also exit 0.

`supersimple login` uses the saved configuration if present; otherwise it prompts for an API token
and stores it in `~/.config/supersimple/config.json`. `supersimple logout` removes that configuration.
For unattended use, supply `SUPERSIMPLE_TOKEN` through the environment. `SUPERSIMPLE_HOST` optionally
selects a different API host. The account is resolved from the token.

Environment-token authentication does not persist a login. Missing credentials on an API command
can trigger an interactive prompt; establish authentication first. Never echo tokens into logs.

## Export

### `supersimple export`

| Flag | Description |
|------|-------------|
| `-o, --output-dir <dir>` | Output directory (default: current dir) |
| `--stdout` | Print to stdout instead of files |
| `--force` | Overwrite existing files without prompting |
| `--models` | Include all models |
| `--metrics` | Include all metrics |
| `--explorations` | Include all explorations |
| `--agent-skills` | Include all workspace AI agent skills |
| `--ai-instructions` | Include general and per-source AI instructions |
| `--model-ids <ids>` | Comma-separated model IDs to export |
| `--metric-ids <ids>` | Comma-separated metric IDs to export |
| `--exploration-ids <ids>` | Comma-separated exploration IDs to export |
| `--agent-skill-ids <ids>` | Comma-separated workspace agent skill IDs |

With no filters, exports all accessible configuration. Any type flag or ID filter omits unrequested
types; combine flags to include several types. Explicit IDs take precedence over an all-of-type
flag. AI sections are included only for roles with Manage AI System Message permission.

Output structure: `models/*.yaml`, `metrics/*.yaml`, `explorations/*.yaml`, `agent_skills/*.yaml`,
`ai_instructions.yaml`, and `access_rules.yaml`. Model/metric filenames derive from IDs; exploration/skill filenames derive
from names. Export leaves obsolete files in place, so use a fresh destination when taking a complete
snapshot. `--force` overwrites local files without asking; it does not change server state.
`--stdout` and `--output-dir` are mutually exclusive.

## Import

### `supersimple import <paths...>`

| Flag | Description |
|------|-------------|
| `--delete-dangling` | Delete objects in Supersimple not present in config |
| `--skip-exploration-validation` | Skip exploration validation |
| `--skip-alert-validation` | Skip alert config validation |
| `--skip-answer-guidance-validation` | Skip answer guidance validation |
| `--validate-sql` | Check that model definitions produce valid queries against the connected database |

Import and validate require **Manage Models**, even for exploration-only input.
Always provide `*_id` in single-entity files; missing IDs trigger a prompt and rewrite the source,
including during validate. Map entries use their keys as IDs and must not repeat IDs in values.
Named access rules resolve only within the same import: include `access_rules.yaml` with subsets
(e.g. `supersimple import ./models ./access_rules.yaml`). This passthrough requires CLI ≥2.27.0.

Paths can be files, directories, or globs. Directories expand to `**/*.{yaml,yml}`. Quote globs when
the CLI should expand them. Import updates supplied entities and preserves unspecified entities
unless deletion is requested. Do not disable validation merely to make a failing import pass.

**Deletion scope:** `--delete-dangling` deletes missing models and metrics account-wide, even if the
input contains no models/metrics. It does not delete missing explorations. Workspace skills are
considered for deletion only when `agent_skills` is present; per-source AI instructions only when
`ai_instructions.sources` is present. Only use deletion with a complete, reviewed source of truth.
A restricted user’s export omits inaccessible models/metrics and hidden properties, so it is not
a complete source for `--delete-dangling`. Deleted per-source AI instructions are not printed in
the CLI summary. Use `validate --validate-dangling` to inspect consequences, and review AI sections separately.

## Validate

### `supersimple validate <paths...>`

| Flag | Description |
|------|-------------|
| `--validate-dangling` | Check for objects in Supersimple not in config |
| `--skip-exploration-validation` | Skip exploration checks |
| `--skip-alert-validation` | Skip alert validation |
| `--skip-answer-guidance-validation` | Skip answer guidance validation |
| `--validate-sql` | Check that model definitions produce valid queries against the connected database |

Validates against both the provided config and existing Supersimple account state.

## Fix

### `supersimple fix <paths...>`

| Flag | Description |
|------|-------------|
| `--format <format>` | Output format: `text` (default) or `yaml` |

**CLI 2.27.0 only handles `models:` map files. It crashes on `model:` files from discover/export.**
Also, `--format yaml` can incorrectly nest `relations.relations`; do not pipe it over source files.
Reports inferable missing reverse relations; does not edit files. It examines each YAML file
separately, so relations between models in different files can be missed. `--format yaml` prints
suggested configuration to stdout. Review output before applying it; it is not an in-place fixer.

## Discover

### `supersimple discover models`
Generate model YAML from the connected database via Supersimple API.

| Flag | Description |
|------|-------------|
| `--schema <schema>` | Database schema to introspect |
| `--catalog <catalog>` | Databricks catalog |
| `--connection <name>` | Named database connection (or `SUPERSIMPLE_CONNECTION`) |
| `--tables <tables>` | Comma-separated table include list |
| `--skip-tables <tables>` | Comma-separated table exclude list |
| `--skip-model-prefix` | Don't prepend schema name to model keys |
| `-o, --output-dir <dir>` | Parent output directory; files go under `<dir>/models/` |
| `--stdout` | Print to stdout |

### `supersimple discover schemas`
List available database schemas. Supports `--connection` / `SUPERSIMPLE_CONNECTION` and `--catalog`.

### `supersimple discover enum`
Discover enum values from a database column. Requires `--table` and `--column`. Optional: `--schema`, `--label-column`, `--limit` (default 1000), and `--connection` / `SUPERSIMPLE_CONNECTION`.

### Direct database discovery
`supersimple discover postgres models`, `supersimple discover bigquery models`, `supersimple discover redshift models` connect directly to databases without the Supersimple API and print YAML to stdout only. PostgreSQL
and Redshift require `--url`; BigQuery requires `--credentials`, `--project`, and `--dataset`.
Run with `--help` for flags.

## dbt conversion

### `supersimple dbt convert`

Convert matching `manifest.json` and `catalog.json` artifacts into Supersimple model YAML. Materialize the selected dbt
models first, then run:

```bash
dbt docs generate
supersimple dbt convert
```

By default, the command reads both artifacts from `target/` and writes `supersimple-models.yml`. Only dbt models with
`supersimple.enabled: true` in their model metadata are included. Supersimple annotations normally live under
`config.meta.supersimple` on models and columns; run `supersimple dbt convert --help` for the supported fields and older
dbt metadata locations.

| Flag | Description |
|------|-------------|
| `--artifacts-dir <dir>` | Directory containing both artifacts (default: `target`) |
| `-o, --output <file>` | Generated Supersimple YAML file (default: `supersimple-models.yml`) |
| `--force` | Overwrite an existing file not generated by this command |

Only the PostgreSQL, ClickHouse, and BigQuery dbt adapters are supported. Zero enabled models is an error.
Treat the output as generated. Make changes in dbt metadata, regenerate the artifacts, and rerun the converter. Full
workflow: https://docs.supersimple.io/guides/managing-the-data-model/using-dbt-models

## Entity management

| Command | Description |
|---------|-------------|
| `supersimple models list` | List all models |
| `supersimple models delete <id>` | Delete a model |
| `supersimple metrics list` | List all metrics |
| `supersimple metrics delete <id>` | Delete a metric |
| `supersimple explorations list` | List all explorations |
| `supersimple explorations delete <id>` | Delete an exploration |

Deletes run immediately without confirmation; ask the user first unless they already explicitly
authorized that deletion.

## Supersimple Apps

`supersimple app create`, `publish`, `list`, `delete`, `promote`, and `demote` manage Supersimple Apps.
Publishing, deleting, promoting, and demoting require **Manage Apps**.
Use the `supersimple-apps` skill for the Supersimple SDK and authoring workflow.
Run `supersimple app <command> --help` for the installed CLI's options.
