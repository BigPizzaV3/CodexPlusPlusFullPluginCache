# Zorevo plugin for ChatGPT

Source of the plugin package submitted at platform.openai.com/plugins. Everything the ChatGPT directory lists comes from here plus the live MCP server at https://app.zorevo.io/mcp (tools, annotations and server instructions are read from the server when OpenAI scans it).

Files
- plugin.json: listing, review test cases, release notes. Keep the long description in sync with claude/zorevo-mcp-listing.md in the Zorevo project.
- mcp.json: the one remote MCP server, OAuth with dynamic client registration (no client id or secret).
- assets/icon.png (512) and assets/logo.png (1024): the Z mark on Violet Ray (#8936FE). icon.svg is the source.

Before uploading
1. Replace DEMO_RECORDING_URL in plugin.json with the reviewer video (Loom or similar, no sign-in needed).
2. Build the zip from inside this folder so plugin.json sits at the zip root:
   cd chatgpt-plugin && zip -r ../zorevo-plugin.zip plugin.json mcp.json assets README.md
3. Upload at platform.openai.com/plugins. Reviewer credentials (info+mcptest@zorevo.io) go in the dashboard's Review details form, never in this package.
4. Domain verification: the dashboard gives a challenge token; it is served as text/plain at https://app.zorevo.io/.well-known/openai-apps-challenge from OPENAI_APPS_CHALLENGE in the server .env (routes/web.php).

Rules from OpenAI's submission docs (Oct 2026)
- Metadata or skill changes need a new zip; MCP tool changes only need a rescan.
- The MCP URL can't change between versions.
- Five positive and three negative test cases are required for the first review.
- No headers, secrets or credentials in the package.
