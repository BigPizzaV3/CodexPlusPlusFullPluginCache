# Po Once plugin 0.2.1

Po Once combines a hosted MCP connection, workflow instructions, and an optional
local CLI for social publishing and analytics. The hosted endpoint is
https://po-once.com/mcp and uses browser OAuth.

## Connect

Sign in to Po Once, select the workspaces and permissions the plugin may use,
and return to the chat client. Any workspace member can connect; each selected
workspace needs a plan with Agent API access. Manage grants on the AI Agent
page. Reauthorize existing connections to approve new scopes for account
connection links and saved-content deletion.

## Included

- `.codex-plugin/plugin.json`: package identity, listing, and review metadata.
- `.mcp.json`: hosted HTTP MCP endpoint.
- `skills/po-once/SKILL.md`: MCP-first workflows for multiple workspaces,
  saved content, scheduling, quota checks, analytics, comments, and discovery.
- `skills/po-once/references/cli.md`: CLI usage and provider details.
- `skills/po-once/scripts/po-once.cjs`: standalone CLI helper.
- `assets/`: Po Once icons.
- `LICENSE`: license for the bundled CLI and reference source.

The optional CLI needs Node.js 18+ and a separate organization API key. OAuth
credentials remain managed by the host. Keep credentials outside this package.
The media picker requires host support for MCP Apps.

## Updating the existing ChatGPT plugin

Upload `po-once-submission-0.2.1.zip` as a new version of the existing plugin,
complete applicable review steps, and publish the approved version. Hosted MCP
tool changes also require server deployment and an MCP rescan. Packaging does
not deploy the server or publish the plugin.

Local validation checks package structure, referenced files, CLI syntax, and
CLI behavior with mocked requests. Browser OAuth, actual MCP rendering, and
live publishing still need verification in the target client.
