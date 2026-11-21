---
name: connect-booklee
description: Connect a Booklee account, inspect its delegated access, or explain how to disconnect Booklee from an agent. Use when setting up this plugin or investigating a Booklee permission failure.
---

Use the connected Booklee MCP server. The user must be in a new chat on the
same host where Booklee was installed and select **Booklee** by typing `@` in
the composer. If only the skill is loaded, the MCP server is not attached and
tool calls will be unavailable. Tool names below are logical names; the client
may add a server prefix. Inspect the live tool schema before supplying
arguments.

When the user asks to connect, sign in, set up, test, or verify Booklee access, immediately call `get_access_context` with `{}` before answering. This protected read is the connection check: if the account is not connected, let the client start Booklee OAuth and consent. Do not substitute a public search or claim that the plugin works without this call.

Public discovery does not require sign-in. For an account-specific task, call `get_access_context`. If authentication is requested, use the client's Booklee OAuth flow. The flow has two required browser steps: the user signs in, then Booklee shows the **Connect an app to Booklee** `/mcp/authorize` consent screen where they select capabilities and business or location targets and click **Allow** or **Connect**. Sign-in alone does not create a connected app. Wait for the client to report that consent completed before calling `get_access_context` again. `/mcp/authorize` is the one-time consent page; `/mcp/connections` only lists, reviews, and revokes completed connections. If it is empty after sign-in, say that consent did not complete and restart the client's OAuth flow. Never ask for passwords, cookies, mobile tokens, or OAuth tokens in chat, and never build a consent URL from guessed OAuth parameters.

Explain the returned account, scopes, organizations, locations, and platform access in plain language. Resolve names with available authorized read tools when useful. Current Booklee permissions still apply on every call; a scope does not grant a role or ownership. Do not infer access to an organization from its public listing.

If a call needs additional access, explain the missing capability or target and use the client's reconnect or authorization flow. If the client says that the Booklee connector is unavailable, ask the user to open the plugin's Manage/Settings page for the selected host, enable or reconnect the `booklee` MCP server, start a new chat, and select **Booklee** with `@`; do not claim that sign-in succeeded or that access is connected until `get_access_context` returns. If the model reports capacity, ask the user to switch to an available model. Do not silently broaden the requested task, bypass a permission failure, or substitute a different account. A business role does not automatically support personal customer booking.

To disconnect, direct the user to Booklee account settings or https://booklee.app/mcp/connections. Disconnecting revokes Booklee access; the plugin may remain installed in the client until the user removes it there. Do not claim to have revoked access unless a supported tool or the user confirms it.

Respect the user's chosen client approval settings. Tool annotations describe effects; they do not prove that the server obtained human approval. This skill does not add a blanket confirmation requirement.
