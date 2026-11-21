# Install Statewright in Claude

## Claude chat and Desktop: remote connector

1. Open Customize > Connectors in Claude, select Add > Add custom connector.
2. Name: Statewright. Server URL: https://mcp.statewright.ai/mcp
3. Continue, review detected authentication, and select Sign in now.
4. Select a supported OAuth client mode. Statewright does not currently advertise dynamic client registration or Client ID Metadata Documents in its authorization-server metadata. Do not assume Register automatically or Claude's published identity works. Use your own registered OAuth client when required, with Claude's exact callback URL registered at Statewright.
5. Connect, complete Statewright sign-in and consent, then ask: List my available Statewright workflows. Do not start a workflow.

OAuth client ID statewright-codex was supplied for ChatGPT. It is not assumed to accept Claude callback URLs. Confirm/register a Claude-compatible public OAuth client before distribution; no secret or token is packaged.

## Claude Code: package compatibility

This folder includes .claude-plugin/plugin.json and .mcp.json using Claude Code's HTTP MCP configuration. Extract the ZIP, then preview from a terminal with:

```sh
claude --plugin-dir /absolute/path/to/statewright
```

Open /mcp to inspect the Statewright connection and authenticate. The configuration uses default OAuth discovery; because automatic registration is not advertised, it may require a preconfigured public client. Once its actual ID and approved loopback callback port are known, add oauth.clientId and oauth.callbackPort to the statewright entry in .mcp.json, or configure the server directly:

```sh
claude mcp add --transport http --scope user --client-id YOUR_REGISTERED_CLAUDE_CLIENT_ID --callback-port YOUR_REGISTERED_PORT statewright https://mcp.statewright.ai/mcp
```

Use /mcp to finish sign-in. Do not include --client-secret for a public client with no secret. Choose either the plugin connection or direct MCP setup to avoid duplicate server registrations.

## Verification status

Package structure and JSON checked. Claude is not installed in this build environment; Claude runtime validation, account installation, OAuth consent, tool discovery, and functional tests have not been run. Public Claude directory submission is separate and has not occurred.

## Official references

- https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/mcp
