# Security

## Reporting Vulnerabilities

If you discover a security vulnerability in this plugin, report it
privately:

- **Email**: plugin-support@lukka.global
- **Subject line**: `[PLUGIN-SECURITY] Brief description`


Do NOT open public issues for security vulnerabilities.

## Scope

**Plugin (report with [PLUGIN-SECURITY]):**

- Plugin code: skills, converted command/agent procedures and processors
- `mcp.json` configuration and OAuth flow

**Hosted MCP servers (report with [MCP-SECURITY]):**

- global.mcp.lukka.tech

- aml.mcp.lukka.tech, uda.mcp.lukka.tech, pricing.mcp.lukka.tech
- refdata.mcp.lukka.tech, analytics.mcp.lukka.tech, news.mcp.lukka.tech
- predmar.mcp.lukka.tech

## Authentication

Global MCP uses OAuth 2.0 with PKCE through Lukka Auth0. The public package
selects DCR in `mcp.json`. No client ID, secret or token is embedded in the
plugin. Authentication and token storage are managed by the host.

## Data Handling

The Claude audit-logging hook is not included in this public OpenAI package.
It does not create the original local usage log. This does not describe or
disable logging by the host or the remote service.
Requests and responses use the connected Lukka account and host environment.
See the [Lukka Privacy Policy](https://lukka.tech/privacy-policy/).

## Temporary File Processing

The `large-data-processing` skill writes intermediate files (AML reports,
transaction data) to `/tmp/` for processing. These files may contain
sensitive data (wallet addresses, risk scores, counterparty graphs). Files
are used ephemerally during command execution. On shared or multi-tenant
systems, ensure `/tmp/` has appropriate access controls.
