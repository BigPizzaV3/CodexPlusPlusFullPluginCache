# Public CLI access

Use this route when a terminal is available and the user requests the CLI or
already has an authenticated public Wilfie CLI. The CLI commands below perform
the same reads as the MCP workflow. They do not inherit the MCP connection's
credentials or grant permission for additional actions.

## Availability and sign-in

Check `wilfie --version` and command-specific `--help`. If the CLI is absent or
lacks a required command, use the public PyPI package in an isolated tool
environment when installation is permitted:

```bash
uv tool install --upgrade --index https://pypi.org/simple wilfie
wilfie --help
```

If `uv` is unavailable, use an existing Python virtual environment with
`python3 -m pip install --upgrade --index-url https://pypi.org/simple wilfie`.
Do not alter the system Python installation. If installation is unavailable,
use the connected MCP tools.

Use the user's existing production profile. If no environment is established,
ask before making API requests. This public skill targets `https://wilfie.ai`;
development, local-server setup and private platform administration are
separate workflows. Do not repoint an existing profile to a different server.

In the examples, replace `PROFILE` with that profile and `WORKSPACE` with the
selected workspace code. The remaining capitalized values stand for IDs,
queries or options resolved from results. Keep global options before the
command group. Use `--auth-mode oauth` consistently for account-linked reads.

```bash
wilfie --profile PROFILE --base-url https://wilfie.ai --auth-mode oauth auth status
wilfie --profile PROFILE --base-url https://wilfie.ai --auth-mode oauth auth login --client-id wilfie-cli
wilfie --profile PROFILE --base-url https://wilfie.ai --auth-mode oauth auth whoami
```

Run login only when needed. Let the user complete the normal browser sign-in;
do not read credential stores or ask for tokens in chat. Reuse a valid session.

## Read commands

Prefix each command below with:

```text
wilfie --profile PROFILE --base-url https://wilfie.ai --auth-mode oauth --output json
```

| MCP tool | CLI command after the prefix |
| --- | --- |
| `workspaces_list` | `workspaces list` |
| `workspaces_get` | `workspaces get WORKSPACE` |
| `wms_facilities` | `wms facilities --workspace WORKSPACE` |
| `wms_skus` | `wms skus --workspace WORKSPACE --query QUERY --include-on-hand` |
| `wms_inventory_availability` | `wms availability --workspace WORKSPACE --sku-id SKU_ID --facility-id FACILITY_ID` |
| `wms_inventory_balances` | `wms inventory-balances --workspace WORKSPACE --container-id CONTAINER_ID` |
| `wms_sales_orders_search` | `wms sales-orders search --workspace WORKSPACE --query QUERY` |
| `wms_documents_list` | `wms documents list --workspace WORKSPACE --kind KIND --search-query QUERY` |
| `wms_documents_detail` | `wms documents detail --workspace WORKSPACE --kind KIND --document-id DOCUMENT_ID` |
| `wms_documents_links` | `wms documents links --workspace WORKSPACE --kind KIND --document-id DOCUMENT_ID` |
| `wms_analytics_config` | `wms analytics config --workspace WORKSPACE` |
| `wms_analytics_dimension_members` | `wms analytics dimension-members --workspace WORKSPACE --dimension-key DIMENSION_KEY --query QUERY` |
| `wms_analytics_summary` | `wms analytics summary --workspace WORKSPACE --metric-key METRIC_KEY --period PERIOD` |
| `wms_analytics_timeseries` | `wms analytics timeseries --workspace WORKSPACE --metric-key METRIC_KEY --period PERIOD --granularity day` |
| `wms_analytics_leaderboards` | `wms analytics leaderboards --workspace WORKSPACE --metric-key METRIC_KEY --period PERIOD --group-by GROUP_KEY --limit 10` |

Use `--facility-location-id` instead of `--facility-id` for location-level
availability. Balances can also use `--facility-location-id`. List commands
accept `--limit` and `--offset`; sales-order search supports repeated `--status`.

For analytics, discover the catalog first. Repeat `--metric-key` for a summary
with multiple metrics, and use `--filter KEY=VALUE` for each supported filter.
Check installed help for optional grouping or scope arguments. Never invent a
metric key, substitute a period silently, or use a broader command to work
around missing analytics or permissions. Apply the main skill's result and
error interpretation rules to the returned JSON.

The public CLI has additional commands. They are outside this skill's read
workflow; do not use generic API-path commands, repairs or mutations here.
