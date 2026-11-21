---
name: setup
description: Connect the A1 Gallery MCP server and check it is working. Use when the plugin is first installed, when a tool returns 401 account_required, or when the user asks why A1 tools are not available.
---

# Connect A1 Gallery

The plugin uses one remote MCP server at `https://www.a1.gallery/api/mcp`. It needs an
A1 account — calls without one return `401 account_required`. There is no API key;
sign-in happens over OAuth in the browser.

## First connection

1. Connect A1 Gallery when the app prompts for it.
2. A browser tab opens on a1.gallery. Sign in to your A1 account.
3. Approve the consent screen. The tab closes and the tools become available.

If the user has no account, they can create one at https://www.a1.gallery/login.

## When a tool returns 401 account_required

The session is signed out or the token expired. Reconnect with the steps above. This is
the expected response for an unauthenticated call, not a fault in the server.

## Daily limits

Accounts have a daily call limit. A limit response arrives as a tool result, not an
HTTP error, so read its text and pass the message on.

## Checking it works

Call `get_design_filters`. It takes no arguments and returns the taxonomy, so it confirms
both the connection and the account in one call.
