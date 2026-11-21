# Reteno segment operation contract

For system select options, use the live semantic value or ID (for example `EMAIL` or
`COUNT_OPENED`), never a placeholder `profileInputOptionId: 0`. Custom profile selects still
serialize their real `profileInputOptionId`. Let the SDK resolve and validate both cases.
Activity and product-event date controls represent organization-local date-times even when
their live type is `DATE`; supply the requested local boundaries and the catalog timezone,
and let the SDK serialize UTC. Ordinary date-only profile fields remain date-only.
Build cross-channel Open/Click conditions as compatible OR aggregates using live option
values (`INAPP` where offered). Widget activity uses `AGGREGATED_WIDGET_ACTIVITY` separately.
Do not force an unsupported media/event pair through validation or enable excluded channels.

The installed plugin includes the compiled SDK, output schema and operator reference. It
needs Node.js 20.18.1 or newer and Python 3.11 or newer. No publisher session or proxy is used.
Authentication and tool calls belong to the host. Files are local working artifacts, not
alternative account data. Fetch a new catalog if it has expired or the account changes.

Read only the relevant live definitions. `uiContext` contains authoritative feature decisions,
timezone and application IDs. Do not synthesize missing decisions or silently enable features.
Use [operators](references/client/catalogs/condition-operators.md) to interpret the catalog and
 the [SDK](references/client/SDK_API_REFERENCE.md) to express the request. A failed SDK mutation
must stop the script. Do not edit JSON by hand to bypass a validation error.

```sh
node <skill-dir>/scripts/run_sdk.mjs \
  --catalog <catalog-manifest.json> --catalog-file <catalog.json> \
  --organization-id <authenticated-org-id> --script <mutation.mjs> \
  --output <segment.json> --request <request.json> --diagnostics <diagnostics.json> \
  --name <new-segment-name>
```

For an edit replace `--name` with `--segment-id <id> --input <get-segment.json>`.
For a count replace it with `--mode count`. Count mode takes no create metadata or segment ID.
The catalog must have been staged for that exact segment on edit, or without a segment ID
for creation/count. `--organization-id` comes from the same authenticated MCP account.

The generated request selects `create_dynamic_segment`, `update_dynamic_segment`, or
`count_segment_contacts`. Pass its `arguments` through the host-native MCP tool; do not call
HTTP tool endpoints, add headers, or request agent tokens. Keep the returned receipt with the
request for recovery. A successful local run never means the segment was saved or counted.

Preserve unaffected branches, parameters and exclusions. Be precise about relative vs absolute
dates, AND vs OR, event frequency, active-contact status, application and channel eligibility.
Use narrow selectors and assert cardinality before changing an existing condition. If a
requested definition is absent, report the missing prerequisite; do not substitute another
population silently. Aggregate counts are not evidence of which individual contacts matched.
