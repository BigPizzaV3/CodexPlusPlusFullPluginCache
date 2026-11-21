# Production Engine for ChatGPT and Codex

This package connects an existing Production Engine workspace through 19 read-only MCP tools. Ask what is shooting, check crew responses and job health, compare budgets with recorded actuals, or review outstanding invoices, deliverables and bids. Answers come from the workspace you connect. The package contains no credentials.

## Connect in developer mode

Use ChatGPT's Developer mode to add the MCP server. Availability depends on the account and workspace policy. See the [connection guide](https://developers.openai.com/plugins/deploy/connect-chatgpt) for the current setup steps.

- Server: `https://production-engine.com/api/mcp/openai`
- Authentication: OAuth, predefined public client
- Client ID: `production-engine-chatgpt`
- Client secret: leave blank
- Redirect URI: `https://chatgpt.com/connector_platform_oauth_redirect`
- Scope: `read`

Sign in through Production Engine, including existing MFA if enabled, and explicitly allow access to the displayed workspace. Only an owner or admin can connect. Access tokens last one hour; rotating refresh credentials keep the connection for up to 90 days of inactivity. Revoke the connected assistant entry under Company Settings > Integrations to disconnect immediately.

## Build the ZIP

From the repository root:

```sh
node --import tsx scripts/package-chatgpt-plugin.mjs /tmp/production-engine-0.1.2.zip
```

This validates listing fields, the documented tool count, local PNG assets, package structure and review cases, then bundles only this plugin folder. It does not upload, submit or install the plugin.

## Release checks

Verify OAuth discovery and complete a real ChatGPT connection before submission. Test the five positive and three negative cases in `plugin.json` against a dedicated sample workspace. Record actual tool selections and results; packaged expectations are not test results.

The package uses a dedicated OAuth resource at `/api/mcp/openai`. It exposes the same 19 production read tools for ChatGPT callbacks and directly registered Codex loopback clients. It accepts only OAuth tokens issued for this exact resource, excludes bank feeds and third-party tools, and narrows requests for additional supported scopes to `read`. Existing connections to `/api/mcp` need a new authorization to use this package endpoint.

Verify the effective catalog and connection on both ChatGPT and Codex before submission. Local route tests establish resource isolation; they do not establish a successful connection in either host. Record live connection and review-case evidence separately.

The review cases require a synthetic project named **Spring Spot**, with representative shoot days, tasks, crew responses, budget lines, recorded actuals and client invoices in that sample workspace. Keep the fixture's dates and expected amounts explicit in the reviewer materials. Use synthetic records only. This package does not create the fixture or claim these scenarios have been executed.

Complete OpenAI's publisher identity and domain verification, enter reviewer account details privately in the portal, and provide the required walkthrough recording. Do not place reviewer credentials or the domain challenge in this package. Upload the ZIP at [the submission portal](https://platform.openai.com/plugins) after those materials are ready. Submission and publication require their own confirmation.

Support: [Production Engine support](https://production-engine.com/developers/support).

References: [authentication](https://developers.openai.com/plugins/build/auth), [plugin format](https://developers.openai.com/plugins/build/plugins), [submission](https://developers.openai.com/plugins/deploy/submission), and [submission validation errors](https://developers.openai.com/plugins/deploy/submission-errors).
