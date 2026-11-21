---
name: setup
description: Connect Booklee, complete sign-in and consent, and show the access granted to this agent.
---

# Connect Booklee

Use the Booklee MCP server already selected for this host. Before calling a
tool, make sure the user is in a new chat on the host where the package was
installed and has typed `@` and selected **Booklee**. Selecting a skill or
starter prompt without selecting the plugin does not load its MCP server. Do
not create a cloud environment, ask for credentials, or construct an OAuth URL
yourself.

Start by calling `get_access_context` with `{}`. If the client requests
authentication, let the user complete both Booklee sign-in and the
**Connect an app to Booklee** consent page. The user must choose the requested
capabilities and organization or location targets and click **Allow** or
**Connect**. Sign-in alone does not create a connection.

After the client reports that consent completed, call `get_access_context`
again. Explain the account, role, capabilities, organizations, locations, and
platform access returned by Booklee. Current Booklee permissions remain
authoritative; a connection cannot grant a role or target the account does not
have.

If the client reports that the Booklee connector is unavailable, explain that
the selected host has not loaded the MCP server. Ask the user to open the
Booklee plugin's Manage/Settings page for that host, enable or reconnect the
`booklee` MCP server, start a new chat, and select **Booklee** with `@` before
retrying. Do not claim that access is connected without a successful
`get_access_context` result. If the model itself reports that it is at
capacity, the user must switch to an available model before retrying.

Never ask for a password, cookie, mobile token, access token, or consent URL.
To review or revoke an existing connection, direct the user to
https://booklee.app/mcp/connections.
