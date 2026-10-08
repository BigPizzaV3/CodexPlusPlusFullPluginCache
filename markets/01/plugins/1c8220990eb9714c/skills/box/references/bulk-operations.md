# Bulk Operations

The CLI and REST instructions in this reference apply only in Codex. In ChatGPT, use Box MCP and ignore the CLI/REST commands below. In Codex, use CLI for bulk actions only when `box users:get me --json` confirms it is installed and authenticated; use REST only when its authentication is already configured.

Read `references/auth-and-setup.md` first when the acting identity or SDK vs REST choice is unclear.

## When this applies

Use this reference for multi-item folder trees, batch moves, content classification, bulk metadata writes, or folder-structure migrations.

## Constraints

- Run CLI commands serially. See `references/box-cli.md`.
- Box requires unique item names within a parent folder. On `409 Conflict`, look up the existing item and reuse it only if it is the intended target.
- For pacing and `429` recovery, follow `references/troubleshooting.md`.

## Workflow

Use `Inventory → Classify if needed → Plan → Execute → Verify`.

### Inventory

Paginate through every source folder and capture each item's stable `id`, `name`, and `type`.

```bash
# CLI — increase max-items if the folder may contain more
box folders:items <SOURCE_FOLDER_ID> --json --max-items 1000 \
  --fields id,name,type > inventory.json

# REST — repeat with increasing offset until every page is returned
curl -sS \
  -H "Authorization: Bearer $BOX_ACCESS_TOKEN" \
  "https://api.box.com/2.0/folders/<SOURCE_FOLDER_ID>/items?limit=1000&offset=0&fields=id,name,type" \
  > inventory-page.json
```

### Plan

Classify by filename, extension, or existing metadata when possible. For content-based classification, use `references/ai-and-retrieval.md`. Map every item ID to a target and identify existing folders before execution.

If the user supplied an exact item-to-folder mapping, treat it as the approved plan. Otherwise present the generated file → folder map and any folders to create, then obtain one approval for the complete plan before creating folders or moving files. After approval, execute without per-item confirmations unless the plan must materially change.

Approval of the bulk plan satisfies the CLI/REST first-write confirmation for the folder creations and moves listed in that plan.

```json
{
  "folders_to_create": [
    {"key": "contracts", "name": "Contracts", "parent_id": "<PARENT_FOLDER_ID>"}
  ],
  "moves": [
    {"item_id": "<FILE_ID>", "item_type": "file", "target_key": "contracts"}
  ]
}
```

### Sample first

For large content-based classification, test the proposed categories on a small representative sample before building the full map. Use the results to correct the classification rule and flag ambiguous items, then include the resulting full map in the single plan approval above; do not add a separate sample-approval step.

### Execute

Create parent folders before child folders, record returned IDs, and process CLI writes serially. Resolve name conflicts rather than creating alternate folders implicitly.

```bash
# CLI — run once per plan entry, one command at a time
box folders:create <PARENT_FOLDER_ID> "<FOLDER_NAME>" --json
box files:move <FILE_ID> <TARGET_FOLDER_ID> --json

# REST
curl -sS -X POST \
  -H "Authorization: Bearer $BOX_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  "https://api.box.com/2.0/folders" \
  -d '{"name":"<FOLDER_NAME>","parent":{"id":"<PARENT_FOLDER_ID>"}}'

curl -sS -X PUT \
  -H "Authorization: Bearer $BOX_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  "https://api.box.com/2.0/files/<FILE_ID>" \
  -d '{"parent":{"id":"<TARGET_FOLDER_ID>"}}'
```

### Verify and recover

- Record each completed item ID and each failure as work proceeds. Continue independent items when safe, then resume using only the remaining IDs.
- After execution, compare the expected and actual IDs or counts in every source and target folder and report unresolved failures.

```bash
# CLI
box folders:items <SOURCE_FOLDER_ID> --json --max-items 1000 --fields id,name
box folders:items <TARGET_FOLDER_ID> --json --max-items 1000 --fields id,name

# REST
curl -sS \
  -H "Authorization: Bearer $BOX_ACCESS_TOKEN" \
  "https://api.box.com/2.0/folders/<SOURCE_FOLDER_ID>/items?limit=1000&offset=0&fields=id,name"
curl -sS \
  -H "Authorization: Bearer $BOX_ACCESS_TOKEN" \
  "https://api.box.com/2.0/folders/<TARGET_FOLDER_ID>/items?limit=1000&offset=0&fields=id,name"
```

For additional command and request patterns, use `references/box-cli.md` or `references/rest-calls.md`. Use `references/troubleshooting.md` for `429` handling or other failures.

## REST vs CLI for bulk work

| Factor | REST (direct API or SDK) | CLI (`box` command) |
| --- | --- | --- |
| Concurrency safety | Can handle controlled concurrency with proper rate-limit handling | Must run serially — no parallel invocations |
| Overhead per call | Lower — direct HTTP | Higher — process spawn per command |
| Error handling | Structured JSON responses, easy to parse and retry | Exit codes and mixed output, harder to automate |
| Best for | Last-resort fallback, or application code that already uses REST/SDK | Agent-driven operations when CLI is available |

For Codex agent-driven bulk operations, prefer CLI only when `box users:get me --json` succeeds. Use REST only when its authentication is configured and the fallback conditions in the main skill are met.
