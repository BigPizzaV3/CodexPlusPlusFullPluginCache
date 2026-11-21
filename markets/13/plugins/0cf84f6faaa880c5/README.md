# Blackbird Concierge

This is a ChatGPT plugin package adapted from the Cursor Marketplace
plugin at https://github.com/blackbird-labs-inc/blackbird-plugin.

The plugin connects to Blackbird's protected remote MCP endpoint:

```json
{
  "mcpServers": {
    "blackbird-concierge": {
      "type": "streamable-http",
      "url": "https://concierge.api.blackbird.xyz/mcp"
    }
  }
}
```

The server advertises OAuth protection for `birdie:read` and `birdie:write`.
Users must complete Blackbird sign-in in ChatGPT before live tools can be
discovered or used.
