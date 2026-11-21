# Claude

Upload this same ZIP. Claude reads .claude-plugin/plugin.json and .mcp.json. Do not extract the archive first.

Skill/plugin version 0.1.41.

MCP URL: https://09vyfnjv.mcp.cofr.io/mcp

## Tools

- run_aoa_mini_assessment: Public, no sign-in
- aoa_ai_opportunity_assessment: OAuth required
- create_aoa_discovery_guide: OAuth required
- run_aoa_full_assessment: OAuth required

A public tool can be called before sign-in. A protected tool returns HTTP 401 with WWW-Authenticate so Claude can prompt to connect and retry. This package uses the same MCP URL. It does not require sign-in for public tools. This guide does not mark that behavior verified.

Accepting the ZIP into an account is not Claude directory approval. Directory submission uses a repository you own. Do not publish private skill files there.

Last verified 2026-10-19: https://claude.com/docs/plugins/submit
