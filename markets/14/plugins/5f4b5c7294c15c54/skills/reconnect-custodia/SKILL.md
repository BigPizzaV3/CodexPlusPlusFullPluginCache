---
name: reconnect-custodia
description: Reconnects or reauthenticates the Custodia connection in ChatGPT or Codex when tools are unavailable, authentication expired, or the user asks to reconnect.
metadata:
  product: Custodia
  operation: reconnect
---

# Reconnect Custodia

Restore access through the connection flow for the user's installation. Missing
tools can mean an unavailable connection or a conversation that has not loaded
the integration; they do not alone prove that credentials expired.

## ChatGPT or a registered plugin

1. Direct the user to Custodia's connection controls in the host application's
   plugin or app settings. Use a supported connection-management tool only if
   it is available and accepts the actual registered identity.
2. Ask the user to connect or reauthenticate Custodia in the provider's browser
   flow. Do not request passwords, MFA codes, tokens, or authorization codes in chat.
3. After the connection succeeds, check whether the required Custodia tools
   are available. If not, have the user open a new conversation with Custodia
   enabled and retry there. Do not promise a running conversation can refresh
   its tool catalogue.
4. If no connection controls are available, direct the user to the host's plugin
   management UI or Custodia support. Do not replace missing domain tools with
   direct HTTP calls or generic CRUD tools.

For a local selector such as `custodia-chatgpt-plugin@local-repo`, do not call
registered-app permission APIs with that selector. Never guess a registered
app or connector ID, or infer that the plugin is uninstalled from that API's
rejection of a local selector.

## Local Codex installation

Use this path only when the user is running a local installation and the host
provides a supported Codex CLI. Check the installed CLI's help before using
version-specific plugin or MCP commands. Never run local shell commands in a
ChatGPT-only environment.

1. Confirm that the Custodia plugin is installed and enabled and that its
   `custodia` MCP server is configured for HTTP with OAuth. If the server is
   absent, enable or reinstall the plugin before attempting login.
2. If authentication has expired, start the CLI's supported MCP login flow for
   `custodia`, requesting `mcp:execute` when scope selection is supported.
3. Clear stale credentials using the supported logout command only when the
   existing login is known to be stale and reauthentication is needed.
4. Keep any callback listener running while the user completes browser login.
   Let the CLI handle credentials; never inspect or echo them.
5. Wait for authentication success, then check tool availability. If the current
   conversation still lacks tools, ask the user to start a new conversation
   with Custodia enabled.

Reinstalling package files does not itself renew OAuth credentials. If browser
login selects the wrong account, stop and let the user switch to the intended
Custodia account before retrying. Never submit a spend request as a connection
test.
