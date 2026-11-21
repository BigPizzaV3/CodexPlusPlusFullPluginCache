# Edit one relative Timer

Use this path only when the existing workflow and exactly one Timer are resolved and the user
requests a duration/unit change. The current timer must have `waitTime:true` and
`waitUntilDate:false`. Read the [Clock catalog](client/catalogs/blocks/Clock.md); no full design
manual or unrelated catalogs are needed. A mode, graph, start/stop or activation change uses
the full operating manual. Clarify an ambiguous target before writing.

1. Confirm the selected organization. Call `get_workflow_export` once, download the artifact
   with `<plugin-root>/scripts/transfer.py`, and retain its ID, organization, `modelHash`, graph
   and start/stop configuration. Resolve the Timer ID and expected old duration/unit from that
   downloaded workflow, preserving all unrelated nodes, connections, metadata and configuration.
2. Write a guarded SDK edit. Use `sdk.findShapes(ShapeType.CLOCK)` to confirm the exact target
   and `sdk.getShapeParams(id)` to assert its old mode and duration. Change only `duration`
   and `durationItem` with `sdk.updateShape`. Duration is a positive integer string; units are
   `Minutes`, `Hours`, `Days`, or `Months`. End with `sdk.finish()`.

```js
// Substitute the ID and old/new values resolved from this task's export and request.
const id = "<resolved-timer-id>";
const matches = sdk.findShapes(ShapeType.CLOCK).filter(shape => shape.id === id);
if (matches.length !== 1) throw new Error("Expected exactly one selected Timer");
const current = sdk.getShapeParams(id);
if (!current || current.waitTime !== true || current.waitUntilDate !== false ||
    current.duration !== "1" || current.durationItem !== "Days") {
  throw new Error("Timer changed or is not the expected relative wait");
}
sdk.updateShape(id, {duration: "2", durationItem: "Hours"});
sdk.finish();
```

3. Prepare the request with the local helper and the original export:

```sh
python3 <skill-dir>/scripts/run_workflow_editor_standalone.py prepare \
  --export <live-export.json> --workflow-id <workflow-id> \
  --organization-id <authenticated-org-id> --code <edit.js> --output <request.json>
```

Call the prepared `update_workflow` through MCP with the retained `expected_model_hash`.
Do not export again between preparation and save unless a conflict requires reconciliation.
Verify the receipt using the helper's `verify --response <receipt.json> --workflow-id <id>`.

4. Obtain a fresh export. Its hash must match the verified save receipt's `modelHash`.
   Compare graph nodes/connections by ID and compare start/stop configuration: only the
   requested Timer duration/unit may change. Also check paused/activation state remains as
   acquired. The editor may materialize previously omitted false defaults:
   `sendInTimeRange:false` on SendEmail and `useContactsTimeZone:false` on non-date Clock.
   Accept only those absent-to-false additions; do not ignore existing values, unrelated
   fields, missing nodes, rewiring or configuration changes. Report any unexplained change.

On a conflict, re-read and reconcile the requested edit against the new state. Never replace
only the hash and replay stale code. A structured response for the expected workflow with
`updated:false`, `failurePhase:"editor"`, `commitStatus:"not_committed"` and `retrySafe:true`
proves the save was not attempted; at most one client retry is allowed. MCP may already have
performed its bounded bootstrap recovery. For unknown or incomplete outcomes, inspect the
retained workflow before another mutation. If the change is already saved, verify and stop.
For `workflow_editor_at_capacity`, wait the supplied `retryAfterSeconds` and retry once.
Never create a replacement workflow, loop retries, activate or schedule it for this edit.
