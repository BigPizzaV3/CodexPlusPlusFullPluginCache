# Stockpress Library Plugin

Portable Agent Plugins v1 package for the Stockpress MCP server.

## Configure the server

Before connecting or uploading this package, replace the example URL in
`mcp.json` with the stable public HTTPS URL for the deployed Streamable HTTP
endpoint. The endpoint should be reachable at `/mcp`; do not put credentials or
secrets in the package.

## Public ChatGPT submission checklist

- Deploy the MCP server and its authorization server at stable public HTTPS
  URLs. The repository's mock/demo authentication is not suitable for public
  users; configure and test a production OAuth provider instead.
- Verify OAuth discovery, authorization-code flow with PKCE S256, token
  audience/resource handling, and per-request authorization against the
  requirements in OpenAI's authentication guide.
- Add OpenAI listing metadata to `extensions.com.openai` in `plugin.json`,
  including the verified developer name and real website, support, privacy, and
  terms URLs. Add the required app icon.
- Prepare five tested positive cases, three negative cases, an accessible demo
  recording, and reviewer test credentials. Enter credentials in the submission
  portal, not in this package.
- Upload the package ZIP through the OpenAI Plugins dashboard, connect and scan
  the MCP server, resolve findings, and submit it for review.

The manifest and MCP configuration use only the portable Agent Plugins v1
fields. The example MCP URL is intentionally non-production, so this package is
a standards-conformant scaffold, not a live or submission-ready plugin yet.