---
name: get-started
description: Use when the user wants to set up or operate Yodeck digital signage. Covers sign-in, bounded lists, and the limits of the production server.
---

# Yodeck

This plugin talks to the user's signed-in Yodeck account through the production MCP server at https://mcp.yodeck.com/mcp.

## Start

1. If a tool call is unauthorized, ask the user to sign in. Do not ask for a password.
2. List only what the user asked for. Pass limit 25 and an offset instead of requesting every record.
3. Read a resource before updating it.

## Limits

- Creating a user sends an invitation email only. Never collect or submit a password.
- A public media URL is fetched by Yodeck's servers.
- Changing a screen, takeover, or push changes a physical display.
- If delete is disabled, tell the user and do not retry.
