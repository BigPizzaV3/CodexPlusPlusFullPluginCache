# OnNetPulse plugin submission package

This directory is the portable OpenAI plugin package for the public OnNetPulse MCP server.

The package contains:

- `plugin.json` — portable plugin identity
- `mcp.json` — production Streamable HTTP MCP connection
- `skills/onnetpulse-job-search/SKILL.md` — job-discovery behavior

Create the upload ZIP from the contents of this directory so `plugin.json` and `mcp.json` are at the ZIP root. Do not include credentials, production environment files, or application build artifacts.
