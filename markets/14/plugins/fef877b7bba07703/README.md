# Perform.AI production plugin

Package identity: `perform-ai`, version `1.0.0`.
One Streamable HTTP connector: `https://mcp.perform.ai/mcp-invoke`, using OAuth with
client configuration discovered through the server's OAuth metadata.
No client credentials or existing app bindings are included.

This package uses `invoke_method_read` for read-only shipment and carrier
methods. Supply the named method and its parameters; use `describe_methods`
when its input schema is unclear. No operation-group skills are bundled. Sign in
with a Perform.AI account and select an authorized organization before
organization-scoped queries.

## Build

Run `bash package.sh` to create `perform-ai-1.0.0.zip`.
Requires Python 3, zip, and unzip. The archive includes only `plugin.json`,
`mcp.json`, this README, and the referenced icon. Research exports, old release
archives and local files are excluded. The script parses both JSON manifests,
checks required files and verifies ZIP integrity before replacing an existing
release archive.

## Review materials

Five positive and three negative cases are declared in `mcp.json` under
`mcpServers.perform-ai.extensions.com.openai.review`, using `testCases` and
`negativeTestCases`. There is no duplicate plugin-level case declaration.
Expected tool calls use `invoke_method_read`; the named business operations
are its method arguments. Prompts cover
carrier delays, shipment history, carrier configuration usage, yearly volume,
and filter discovery. Expected outputs must be derived from returned data;
historic fixture counts are not permanent assertions.

The supplied demo recording URL remains under
`extensions.com.openai.review.demo_recording_url`. No purchases or payments are
performed through the plugin. The supplied empty `publication.countries` list
means unrestricted targeting; confirm this is intended before submission.

## Readiness

Local packaging checks do not establish production OAuth, tool behavior or
submission acceptance. The earlier README records that five positive workflows
were exercised against a demo account; this is historical evidence and has not
been repeated against the submitted production draft in this cleanup.

Before submission:

- Verify the dedicated reviewer account can access the demo organization and
  fixtures named in the cases. Keep credentials and login instructions in the
  portal's secure reviewer fields, outside the package.
- Complete production OAuth sign-in and run all five positive and three negative
  cases against this exact endpoint and the saved draft. Verify pagination,
  accurate answers and organization permission boundaries.
- Inspect live tool schemas and boolean `readOnlyHint`, `openWorldHint` and
  `destructiveHint` annotations. Verify the portal discovers the invoke tools
  and that named business methods execute with the expected schemas.
- Play back the supplied demo and confirm it demonstrates this release and
  working production interactions. URL reachability alone is insufficient.
- Verify the intended business publisher, country targeting, domain ownership,
  portal scans, imported metadata and required attestations. Confirm the listing
  URLs and policies apply to the integration.

The website, support, privacy and terms URLs were fetched during the October 26,
2026 cleanup. The privacy policy explicitly covers MCP connections. These checks
are not legal approval. The bundled PNG is 512 × 512 pixels and under 5 MiB.
The `/mcp-invoke` endpoint was checked during the earlier cleanup:
unauthenticated MCP initialization returned HTTP 401 with OAuth resource
metadata, and discovery named `https://mcp.perform.ai/mcp-invoke` as the resource.
This verifies reachability and discovery, not successful OAuth sign-in or
authenticated method behavior. The previous generic-dispatch review objection
remains unresolved for this contract; changing the endpoint does not establish
review acceptance.

No portal upload, submission for review or publication was performed by this
cleanup. Submit and publish are separate actions.

Official requirements: [submission workflow](https://developers.openai.com/plugins/deploy/submission)
and [remote MCP review](https://developers.openai.com/plugins/deploy/app-review).
