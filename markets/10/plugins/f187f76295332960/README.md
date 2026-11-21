# Allo plugin

Allo connects ChatGPT to the Allo AI phone system for SMBs through Allo's remote MCP server.

The plugin uses the production MCP endpoint at https://mcp.withallo.com/mcp with OAuth handled by the MCP server's authorization flow.

Because the connection uses a hosted HTTPS MCP server rather than a local process, it is not desktop-only. It is designed for ChatGPT on web and desktop wherever plugins and remote MCP apps are available. Users still need to complete Allo account authorization, and availability can depend on their plan and workspace settings.

Support: https://help.withallo.com/en/support/

Before public submission, verify OAuth discovery, tool annotations, a reviewer-accessible demo account with sample data, and the Marketplace listing metadata.
