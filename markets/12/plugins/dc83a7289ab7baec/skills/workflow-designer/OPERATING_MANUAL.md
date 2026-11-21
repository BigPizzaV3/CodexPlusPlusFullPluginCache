# Reteno workflow operation contract

Resolve account entities through `get_organisation_info` and the appropriate MCP reads before
constructing code. The trigger examples are starting points, not authorization to change a
user's channel mix, contact eligibility, frequency or schedule. Adapt examples to the request
and available Reteno channels. Viber and Telegram are unavailable.

Read the exact matching files under `references/client/catalogs/blocks/` and `configs/`, the
trigger under `references/prompts/catalogs/triggers/` when relevant, and the SDK reference.
Use catalog schema values and public SDK methods. The existing Start block must be reused;
every new path must reach an End. Narrow edits preserve existing graph topology and settings.
Keep dynamic variables literal. Code cannot import packages, access DOM, perform network/file
operations or use timers. It must end with `sdk.finish()`.

## Prepare and save

```sh
python3 <skill-dir>/scripts/run_workflow_editor_standalone.py prepare \
  --export <live-export.json> --workflow-id <destination-id> \
  --organization-id <authenticated-org-id> --code <edit.js> --output <request.json>
```

Add `--created` for a newly created shell. The helper checks account/ID/hash and prepares
`update_workflow(workflow_id, expected_model_hash, code)`. Call that exact request through
the selected MCP tool. `prepared:true, persisted:false` is not a save receipt.

```sh
python3 <skill-dir>/scripts/run_workflow_editor_standalone.py verify \
  --response <save-receipt.json> --workflow-id <destination-id> --created
```

Omit `--created` for existing workflows. A valid receipt needs `updated:true`,
`verification.verified:true`, `modelHash`, and paused verification for a new workflow.
Fresh exports then verify the user-visible intent. Retain the returned destination even on
failure. There is no client-supplied idempotency key for workflow creation.

## Clone an inactive version

Export and download the source graph before creating a destination. Prepare unchanged graph
and start/stop settings locally:

```sh
python3 <skill-dir>/scripts/run_workflow_editor_standalone.py clone-files \
  --export <source-export.json> --workflow-id <source-id> \
  --organization-id <authenticated-org-id> --graph <source-graph.json> --output-dir <clone-dir>
```

Create the paused destination once and export its hash. Call `prepare_workflow_upload` for
that destination, upload `workflow.json` to kind `workflow` and `configs.json` to kind
`workflow-configs` using the plugin transfer helper and `application/json`. Prepare the update
with `--upload-session-id <session>` instead of `--code`, using the destination export and
`--created`. Call and verify that save before applying any further SDK edits. Unchanged
branches are imported, not recreated. Subsequent edits use the newly verified destination hash.

## Available catalogs

The checked-in catalog index is [catalog-index.md](references/catalog-index.md). These are
installed files; no install-time prompt generation or private repository access is needed.
