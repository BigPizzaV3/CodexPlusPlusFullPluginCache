---
name: find-mcp-server
description: Find, compare and set up MCP servers with Stork's directory. Use when the user asks which MCP server fits a task or product, how to add one to a client, or where a Smithery-hosted server lives now.
---

# Find an MCP server with Stork

Stork's tools read Stork's own directory of MCP servers. They install
nothing and sign in to nothing.

1. To find a server, call `stork_search` with the task or product in plain
   words. Tell the user who publishes each result, how it connects and
   whether it needs a sign-in.
2. For more on one result, call `stork_server_details` with its slug.
3. To add a server to a client, call `stork_get_install_config` with the
   slug and the client name. Show the configuration and say what the user
   must supply. If the reply has no configuration, say so and give the
   publisher's setup link. Do not make up a command.
4. To choose between servers, call `stork_compare` with two to five slugs.
5. For an old Smithery-hosted address, call `stork_smithery_replacement`.

A check in a listing is one handshake and one request for the tool list.
It does not show that every tool works and it is not a security review.
