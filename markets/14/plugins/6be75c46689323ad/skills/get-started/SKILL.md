---
name: get-started
description: Set up or check The Buffers railway research plugin when the user asks to connect it, verify it works, or get started.
---

Use the bundled `buffers` MCP server at https://buffers.mikegtn.net/mcp.
It uses Streamable HTTP with no authentication; no API key or payment is needed.

Call `research_guidance` to verify the connection and inspect current coverage.
Report success only after receiving a successful tool result. Catalogue entries
and cached detailed reports are different coverage measures; do not describe the
catalogue count as fully indexed tour accounts.

If tools are unavailable, explain that this plugin's MCP connection must be
enabled in the host client. Do not change global settings or install unrelated
software. A directory listing or a ZIP alone does not prove installation.

After a successful check, briefly explain that the plugin can research dates,
locomotives, routes and timings, and draw source-based schematics. If the user
already supplied a railway question, continue with the railtour-research skill.
Otherwise give one example question without running an unsolicited research job.
