# Acquire and inspect the model

When repairing a draft created from a reference, retain its chosen Exact, Tailored, or Creative
regime and original PNG baseline. For Exact, preserve source choices, reuse existing assets or
crops before considering AI generation, and compare the repaired PNGs with the original source.
Do not reset the regime or adapt the branding during the repair.

## 1. Acquire and inspect

Call:

```text
get_email_model(message_id=<id>)
```

Treat the result as a manifest. Preserve its `modelHash` and download its short-lived
`downloadUrl` to a local JSON file through the host's authorized transfer path. Confirm the
downloaded byte count matches the manifest when `bytes` is present.

Inspect the model:

```bash
node <skill-dir>/scripts/inspect-editor-json.mjs \
  --input <downloaded-model.json> \
  --output <inspection.json>
```

If inspection reports no stripes or zero blocks, acquire and download again a bounded handful of
times. Never upload a blockless model or fall back to editing compiled HTML. If no populated model
becomes available, report a read failure and write nothing.

Use the inspection report to identify node ids, message areas, block types, visible text, links,
image sources, effective visibility, duplicate ids, and the before-edit census. Inspect relevant
source nodes directly when exact content matters. IDs belong to this acquisition only.

`moduleId` identifies a saved library module; it is different from a structural node `id`.
The pinned editor contract makes `moduleId` read-only. Preserve it during ordinary content
edits. Prefer a unique node id to address an edit; a `moduleId` selector also matches descendants,
so constrain its node kind and check cardinality before changing content.

### Requests to reuse a saved module

For an explicit saved header, footer, or other library-module request, call
`list_custom_blocks(query=<requested name or ID>)` in the selected organization. Match the
requested language and purpose to an actual result; never infer an ID or substitute a similarly
named invoice/transactional module. An absent or ambiguous match is unresolved.

Inspect the relevant node's own `moduleId` in the complete file from `get_email_model` and its
actual content. The existing JSON field is the source of module identity; no separate ID list or
write payload is needed. `synchronizable:true` in the library means the module supports sync,
not that this email instance is linked or up to date.

The current model API cannot replace a saved module by changing its read-only `moduleId`.
If the requested library ID differs, report that replacement is unavailable through the current
editor API. Complete independent supported edits, but report the overall request as partial.
Do not relabel an existing footer, translate its text and call it a library replacement, rebuild
it as a detached component, or patch HTML attributes to manufacture the requested identity.
If the requested ID is already present, verify its content before reporting that it is in use;
do not claim that synchronization was tested from the ID or library flag alone.
