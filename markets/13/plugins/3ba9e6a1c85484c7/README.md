# PoultryLog Grower 1.0.0

New plugin identity: poultrylog-grower. New MCP entry: poultrylog-grower.
For platform.openai.com, upload this as a NEW plugin, not a new version of the
previous PoultryLog draft. The server URL and authorized OAuth client remain
unchanged. Verify the saved provided client ID before connecting.

# PoultryLog plugin 1.0.0

Connects to the existing OAuth-protected server at https://mcp.poultrylog.com/mcp.
The rebuilt server registers 381 tools; this package includes their complete
schema reference and updated workflow instructions. No credentials or account data
are packaged. The previous 0.3.6 release corresponded to the older 64-tool catalog.

The host imports executable tools from live MCP tools/list; it does not register
tools from the bundled reference JSON. After importing version 1.0.0, scan the MCP
connection and inspect the resulting tool list. Verify list_workspace_memberships,
read_account_preferences, discover_workflows and get_workflow_recipe appear before
claiming the expanded catalog is available. If the host still lists 64 tools,
registration remains incomplete even when get_user_context works.

Use skills/poultry-flock-analysis/SKILL.md and its references/tool-catalog.md for
workflow guidance and the complete registered names. Per-tool OAuth scopes, current
account permissions, confirmation and readback remain mandatory. Private preparation,
queued jobs and completed transport receipts have distinct meanings; do not claim
remote publication or deletion without the corresponding evidence.

This archive is a release package, not evidence that every tool has passed live
client acceptance or that public review/publication is complete. Keep the existing
OAuth identity and intended workspace. Never paste secrets into chat or this package.
Support and policy links: https://poultrylog.com/chatgpt.php.

OAuth setup uses the existing authorized ChatGPT client
`tpc_gCy7xGWZtGbcjB6PcSpfUC` in provided-client mode. No new client registration
is requested. In the platform plugin manager, select predefined credentials and
verify this exact client ID after import. Keep the token endpoint authentication
method matching this existing Auth0 application; the package does not force one.
Supply a client secret only through the secure portal field if that application
requires one. The callback shown by the portal must be allowed on the same client.
Updating a private ChatGPT plugin does not update a separate platform draft;
import this archive into that draft and save its MCP connection settings.
