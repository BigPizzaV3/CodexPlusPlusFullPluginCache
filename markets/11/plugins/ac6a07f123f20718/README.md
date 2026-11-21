# Diatech Make plugin

A private Agent Plugins 1.0 package connecting to
`https://make.diatech.ai/mcp/codex` using Streamable HTTP and the existing
Diatech OAuth discovery. An active CAD subscription is required.

Deploy the backend changes in this repository before connecting the plugin.
The endpoint is also available at `/api/mcp/codex`; development connections can
replace the origin in `mcp.json` with the running editor's origin.

The endpoint exposes the same 13 tools as `/mcp/claude`. It excludes and refuses
`diascript_setup`, so it cannot mint delegated CLI credentials or provide a local
CAD command. Rendering uses `diascript_render`. Reports, pricing, examples and
versioned publishing remain available under the caller's existing account rules.

Package this directory as the single `cad/` directory in a ZIP, keeping the
archive outside the source directory. Install through the host's plugin flow
and complete Diatech OAuth. Verify tool discovery, a harmless docs or validation
call, and a server preview after deployment. Account upload alone does not deploy
the backend or authenticate the connection.

## Product and policy links

- [Diatech Make](https://make.diatech.ai)
- [Documentation](https://make.diatech.ai/docs)
- [Support](https://make.diatech.ai/support)
- [Privacy Policy](https://make.diatech.ai/privacy)
- [Terms of Service](https://make.diatech.ai/terms)
