# Larridin Work Context

A locally authored plugin package connecting to https://app.larridin.com/mcp/larridin. It is not represented as an official Larridin release.

## Connect and try

Install or import this plugin directory using a host that supports Agent Plugins or the Codex compatibility format. The ZIP contains one top-level plugin directory. Complete the host's Larridin OAuth connection flow, then try “What should I focus on today?” or “What changed in my work since yesterday?”

The portable `plugin.json` and `mcp.json` use the Agent Plugins schemas. `.codex-plugin/plugin.json` and `.mcp.json` provide the supported Codex compatibility layout. Keep both configurations aligned when editing the endpoint. No credentials are stored in this package.

OAuth uses server discovery. The server advertises CIMD and dynamic client registration; the package relies on the host's OAuth discovery and client registration flow. Your organization may still require a registered or approved client. If connection is refused, ask your Larridin administrator to approve the host client. Do not substitute a token into the package. An existing registered OAuth client can be configured using the host's connection settings.

Read and write capabilities describe the remote service. Reads retrieve context and analytics within the connected account's access. Writes can record observations or feedback when requested; installing the plugin does not itself write any context. This package installs no desktop sensor and adds no scheduled tasks or hooks.

## Verification and limits

On 2026-10-27, the endpoint returned HTTP 401 with an OAuth protected-resource discovery URL. The resource metadata identified `https://login.larridin.com` as its authorization server. Authorization metadata advertised PKCE S256, CIMD, dynamic client registration, authorization-code and refresh-token flows. Manifest JSON, local paths, portable schemas, bundled skill metadata, and ZIP structure were checked. Authenticated MCP initialization, tool discovery, and end-to-end calls through this new package have not been tested. The workflow is based on available Larridin tool descriptions; capabilities may differ by deployment and account.

## Submission preparation, version 0.1.1

Listing subtitle, publisher name shown in the supplied portal screenshot, existing publisher contact and policy URLs, and a PNG icon derived from the publisher's existing vector logo have been added. The existing policy URLs were retained at the creator's request. Those pages describe the public website and exclude customer-platform data; their applicability to Work Context requires publisher attention before public release.

The contact page provides a contact form and email fallback. The icon preserves the existing symbol and is centered on a square canvas. No new brand design is claimed.

This ZIP fixes the visible listing omissions; it is not submission-ready. MCP sign-in/configuration, demo recording, review cases and execution, reviewer access, country targeting, commerce declarations, scans, and attestations remain to be completed or verified in the existing portal draft. No credentials are included. The logo and policy pages were retrieved from the publisher's public site. No saved portal draft or app binding was changed.

## Sources

- Product and access model: https://larridin.com/work-context/
- MCP resource discovery: https://app.larridin.com/.well-known/oauth-protected-resource
- OAuth discovery: https://login.larridin.com/.well-known/oauth-authorization-server
- Plugin packaging: https://developers.openai.com/plugins/build/plugins


## Review case preparation, version 0.1.2

Five positive and three negative test cases are embedded in the manifest. They are draft expectations based on the connected development tool schemas, not executed test results. All eight are Not run against the submitted endpoint. Reviewer sample-data setup described in each case must be prepared and verified; the package does not seed that data. Tool availability and annotations on the submitted production endpoint remain unverified. The server owner must verify boolean readOnlyHint, openWorldHint, and destructiveHint annotations and correct them in the server source where necessary. No server code is included here.

Supporting content remains incomplete: no demo recording URL or commerce declaration has been supplied. Existing saved country targeting is preserved by omitting countries. Reviewer credentials belong only in the secure portal fields.
