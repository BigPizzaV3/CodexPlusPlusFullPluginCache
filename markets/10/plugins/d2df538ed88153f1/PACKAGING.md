# LogMeIn Resolve plugin submission package

This folder is the portable Agent Plugins package for the public LogMeIn Resolve MCP server. It is separate from the server deployment artifact and contains only listing, connection, and review metadata.

## Before uploading

- Confirm the production MCP URL in `mcp.json` is the endpoint to submit.
- The five positive and three negative cases are grounded in records from the OpenAI Demo account. Run them with the reviewer account before submission and confirm the expected tool names and results still match.
- Enter reviewer credentials and login instructions in the secure portal form. Do not put credentials in this ZIP.
- Confirm the icon paths in `plugin.json` point to included assets.
- Review the product name, publisher name, description, category, and license against the approved listing identity and company requirements.

## Package contents

- `plugin.json`: portable plugin manifest, listing metadata, draft review cases, and release notes.
- `mcp.json`: public HTTPS Streamable HTTP MCP endpoint.

The MCP server tools and their schemas/descriptions remain hosted in the server. Connect the endpoint in the Plugins portal and scan the live tools after uploading this package.
