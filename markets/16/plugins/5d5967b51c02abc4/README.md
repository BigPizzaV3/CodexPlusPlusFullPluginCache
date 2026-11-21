# Tejas Kumar for ChatGPT

The package uploaded to the ChatGPT plugins dashboard (platform.openai.com/plugins)
for the MCP server at https://tej.as/mcp. The server itself is
src/util/mcp/server.ts; this folder is only its listing.

Build the ZIP from this folder, bumping `version` in plugin.json first:

    zip -r tejas-kumar-chatgpt-<version>.zip plugin.json mcp.json icon.png README.md
