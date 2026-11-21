# Connect the getimg plugin

1. Upload this package as a new version of the existing getimg plugin submission.
2. Under **MCPs**, select `getimg` and connect its MCP server.
3. Sign in to getimg and choose the team that will own generated media and pay its credit costs.
4. Ask the plugin to check the connected account or list available models.
5. Request media, for example, "Turn my selfie into professional headshots."

The plugin connects to the existing server at `https://getimg.ai/mcp`. This compatibility variant declares the Streamable HTTP transport and endpoint URL in its MCP entry. It omits authentication extensions so the host can discover the server settings. Portal acceptance of this entry has not been verified. The package contains no credentials.

To switch teams, reconnect and choose a different team in the OAuth consent flow. To change the connection or listing, edit `mcp.json` or `plugin.json`. Media workflow instructions live in `skills/create-media/SKILL.md`.

The icon is the existing 512 × 512 getimg artwork from `apps/web/public/icons/web-app-manifest-512x512.png`.

This archive contains the plugin, its media workflow, and the remote MCP connection. Public review also requires the separate review materials and dashboard checks.

## Verification

On 2026-10-21, the public server card confirmed the endpoint and transport. OAuth discovery confirmed CIMD, dynamic registration, and the four supported scopes. The existing authenticated connection passed `get_account` and `list_models` with `operation: create-speech`. Its 24 exposed tools match the bundled tool guide.

These checks did not spend credits. A new plugin's OAuth consent and paid generation still require verification through that plugin's own connection.

## Recreate the archive

Run this command from the repository root. Write the archive outside the plugin directory.

```sh
python3 -m zipfile -c /private/tmp/getimg-0.1.6.zip plugins/getimg/plugin.json plugins/getimg/mcp.json plugins/getimg/README.md plugins/getimg/assets plugins/getimg/skills
```
