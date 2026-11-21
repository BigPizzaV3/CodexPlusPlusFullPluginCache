---
name: supersimple
description: Manage Supersimple dashboards and YAML model, metric, and exploration files with the supersimple command. Use for database discovery, dbt conversion, bulk configuration, and AI instructions. For data questions use Supersimple MCP; for Supersimple Apps development use supersimple-apps.
metadata:
  minimum-cli-version: "2.27.0"
---

# Supersimple configuration

Supersimple runs analytics against a connected warehouse. The CLI manages models, metrics,
explorations, and workspace AI instructions as YAML; importing changes the connected account.

## Choose MCP or the CLI

The [Supersimple MCP server](https://docs.supersimple.io/integrations/mcp-server) lets agents
ask analytics questions and inspect live explorations. Use an existing connection, or connect your agent to
`https://app.supersimple.io/mcp` using streamable HTTP and sign in through OAuth; the linked
guide has client setup and API-token instructions. Tools run with the connected user's access.

- Answer data questions with MCP `ask_supersimple`.
- Read shared explorations with `get_exploration*`; inspect results with `get_exploration_block_data`.
- Use the CLI for version-controlled or bulk models, metrics, dashboards, and AI configuration.
- Manage answer guidance through MCP.
- MCP `draft_app` creates a version of an existing app without publishing it; the target block
  must separately pin the returned `appVersionId`. See `supersimple-apps` for the edit workflow.

Tool availability depends on connection scopes and role permissions. If MCP is unavailable,
use the setup guide when live inspection would help; CLI configuration work can continue.

### Debug an existing exploration

Use `get_exploration` to find the block, then `get_exploration_block` to inspect its
`dereferencedPipeline` (including steps inherited from parent blocks). Run
`get_exploration_block_data` with the same variable values in `params` to check actual results
or query errors. Omitted variables use their defaults. Keep the account, user permissions,
filters, and date range consistent when comparing results; use `limit`/`offset` for bounded samples.
After changing and importing a model or exploration, rerun the affected block and compare a
specific expected value. For regressions, `get_exploration_history` and `get_exploration_version`
can help identify the changed definition.

## Start with the existing setup

CLI steps require terminal access and separate CLI authentication; otherwise use available MCP tools or prepare files for the user to apply.

1. Require CLI **2.27.0 or later**: check `supersimple --version`, `supersimple status`, and the project's existing configuration.
   If the CLI is missing, installation instructions are at
   https://docs.supersimple.io/guides/managing-the-data-model/using-the-cli.
   On macOS: `brew tap gosupersimple/cli && brew trust --tap gosupersimple/cli && brew install supersimple`.
   Direct macOS and Linux binaries are also linked from the CLI docs.
2. For unattended commands, use an existing `SUPERSIMPLE_TOKEN` environment variable. The account
   is derived from the token.
   `SUPERSIMPLE_HOST` optionally selects a different API host.
3. If credentials are missing, have the user run `supersimple login` in their terminal with a token
   from https://app.supersimple.io/settings/developers. Interactive login saves credentials under
   `~/.config/supersimple/config.json`; using an environment token does not save it.
   Do not print or commit tokens.

`status` reports the connected account without prompting. Read its output: the command always exits 0, including failed checks. Help, `fix`, and dbt conversion work without authentication.

If product behavior differs from this skill, compare `supersimple --version` with the latest
released CLI and check for skill updates using the
[skill installation guide](https://docs.supersimple.io/guides/ai-coding-agents#installation).
The minimum CLI version above is not a freshness check. Update the complete skill folder,
including its references, preserving local edits, then retry the affected step. If the mismatch
remains, report the observed behavior rather than assuming the skill is correct.

## Choose the source of truth

Follow the project's established workflow. Models and metrics are commonly version-controlled;
edit their source files, validate, then import. For dbt-managed models, edit dbt annotations and
regenerate the YAML. For explorations or AI configuration maintained in the app, export the current
entity before editing so unrelated content and settings survive. Do not overwrite uncommitted
configuration with an export; use a fresh temporary directory for inspection.

Read the relevant reference before authoring YAML:

- [CLI commands](references/cli-reference.md): flags, discovery, dbt, import/export, and deletion scope.
- [Models and AI configuration](references/data-model-yaml.md): properties, joins, metrics, access,
  workspace agent skills, and AI instructions.
- [Explorations](references/explorations-yaml.md): cells, pipelines, filters, charts, variables, and layout.

CLI configuration uses **snake_case keys**, with operation names such as `groupAggregate` unchanged.
The Supersimple SDK and GraphQL use camelCase (for example, YAML `metric_id` becomes SDK
`metricId`). Preserve arbitrary user-defined property keys and app state.

## Discover and edit models

```bash
supersimple discover schemas
supersimple discover models --schema public -o ./discovered
# Writes ./discovered/models/*.yaml. Review before copying into the project's model directory.
supersimple validate ./models --validate-sql
supersimple import ./models --validate-sql
```

Use `--connection <name>` for a named database connection. Discovery can prompt before replacing
files, so use a fresh destination. Check cardinality and keys before adding a relation.
Do not run `fix` on discovered/exported single-entity files: CLI 2.27.0 crashes on `model:` input.
Named access rules require `access_rules.yaml` in the same import, including subset validation.
For example: `supersimple validate ./models ./access_rules.yaml --validate-sql`.

For dbt:

```bash
dbt docs generate
supersimple dbt convert
supersimple validate supersimple-models.yml --validate-sql
supersimple import supersimple-models.yml --validate-sql
```

Materialize the selected dbt models before generating matching artifacts. Opt models in with
`config.meta.supersimple.enabled: true`. Treat the converter's output as generated; change the dbt
annotations and regenerate. See the CLI reference for options and limitations.

## Find and update explorations

```bash
supersimple explorations list
supersimple export --exploration-ids <id> --stdout
# Or export into a fresh directory for editing:
supersimple export --exploration-ids <id> -o ./sup-export
supersimple validate ./sup-export
supersimple import ./sup-export
```

For cross-entity searches, export the relevant types into a fresh directory and search the files.
Model/metric filenames use IDs; exploration and agent-skill filenames derive from names. Read the
ID inside a file before targeting it. `--force` overwrites existing export files; use it only when
that overwrite is intended. Export does not remove obsolete local files.

Exploration links: `https://app.supersimple.io/explore/<exploration-id>`.

Set `folder: Sales` alongside `name` to choose an exploration’s folder. Omitted or null `folder`
imports into the root. `visibility: personal` imports into the current user's personal space; omitted visibility defaults to `team`. Preserve both fields when
editing an existing exploration. Model sidebar sections still use `labels.section`.

## Keep data and instructions accurate

For categorical columns with a manageable set of values, consider `type: Enum` with
`enum_options: { load: distinct_values }`, or a static list with friendly labels. Dynamic enums are
cached (six hours by default) and capped at 1,000 values; they are not an exhaustive inventory for
high-cardinality columns. Avoid blindly converting every string column to an enum.

AI access to query results is controlled by account settings.

Workspace `agent_skills` and `ai_instructions` configure Supersimple's own AI. They are different
from this coding-agent skill. Their export/import requires **Manage AI System Message** permission; export silently omits these
sections without it. Import and validate also require **Manage Models**, even for exploration-only YAML.

## Validate and sync deliberately

Always set the `*_id` in a single-entity file. In map form, the map key is the ID; do not repeat it
inside the entry. Missing single-entity IDs trigger an interactive prompt and a source-file rewrite
in both validate and import, which can hang unattended commands.

`supersimple validate <paths...>` validates the proposed configuration against the existing account.
Use `--validate-sql` when table mappings, columns, joins, or SQL need warehouse validation. Review the
YAML diff before importing. After user-facing changes, open the affected exploration and check a
specific result, folder, filter, or chart that demonstrates the intended behavior. Use MCP
`get_exploration_block_data` to check a specific changed value after import.

Normal import updates the supplied entities. `--delete-dangling` can delete models and metrics
across the account even when importing only an exploration. Use it only for an explicitly intended
cleanup from a complete source of truth; a restricted user’s export omits inaccessible models,
metrics, and hidden properties and is unsafe for this round trip. See the CLI reference for scope.
Entity delete commands have no confirmation prompt: obtain explicit authorization before deleting.

Use the installed command's `--help` and actual API validation when documentation disagrees with
behavior. Report drift instead of retrying with validation disabled.
