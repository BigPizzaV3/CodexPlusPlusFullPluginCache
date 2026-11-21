# 1barn plugin for ChatGPT

The listing package for the ChatGPT Plugin Directory. The integration is
1barn's remote MCP server at https://api.1barn.com/mcp (OAuth); the portal
scans it from `.mcp.json`. `.codex-plugin/plugin.json` is the listing,
`skills/` tells the model how to work a barn, `assets/` holds the icon.

    make zip
