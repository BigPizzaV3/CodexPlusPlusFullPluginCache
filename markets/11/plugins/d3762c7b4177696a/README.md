# Swarm For ChatGPT

A portable plugin package for the existing Swarm remote MCP service. It includes a connection descriptor, one workflow skill and Swarm branding. Authentication and authorization stay on the hosted service.

## Connect

Install the package through a supported local or private plugin source. Connect the bundled remote MCP server, sign in to Swarm and approve the selected Spaces. The package contains no API key, copied token, startup hook or local executable.

The workflow skill covers knowledge retrieval, durable decisions, Tasks, scheduling and agent delegation. Ordinary connected agents execute through the Foundation Task/Run queue without Core enrollment; enrolled devices and Swarm Cloud use a separate Core lane. Assignment, current permissions and human approvals remain enforced by Swarm. A connection does not make an inactive chat an always-on listener. On a UI-enabled Swarm service, `swarm_open_spaces` opens an embedded Space browser with Runs and Artifacts in compatible hosts. Tasks and schedules use the canonical tools; they are not additional embedded panels. The hosted service controls UI availability; installing this package does not change server configuration. Verify the actual connection and rendering in the target host before relying on them.

## Build And Review

From the repository root:

```bash
node --test test/chatgpt-plugin.test.mjs
node scripts/package-chatgpt-plugin.mjs /tmp/swarm-chatgpt.zip
```

The archive includes only this plugin's manifest, MCP descriptor, workflow skill, icon, README and license. No repository source, test fixtures, release receipts, social content or local registration IDs are packaged. Version `1.0.2` is the candidate package identity, independent of the Swarm platform and neutral MCP package versions, not a published release.

The icon is the owner-selected refined Swarm profile artwork on its original off-white background, imported unchanged as PNG rather than redrawn. Its SHA-256 is `6653003950334daef553b6ec82ffaeda13edb7be5ac9cd83291f863c75c26a8f`.

The manifest includes five positive and three negative reviewer cases, release notes and an anonymously accessible HTTPS walkthrough URL. The cases describe expected behavior, not completed acceptance results. The captioned recording demonstrates the production service using synthetic review data; it contains no account credentials. Dedicated test-account access and fixture instructions belong in OpenAI's secure reviewer form.

Upload the plugin ZIP in OpenAI Platform after selecting the verified publishing identity. Review the imported MCP configuration, automated findings and reviewer details before requesting human approval to submit. Native UI also needs its configured HTTPS origin and real-host validation. Local validation and packaging do not submit or publish the plugin.

## Separation

This folder is outside the npm `files` allowlist. The neutral `@blackscaletech/swarm-mcp` package remains a transport for any MCP-compatible client. Its local static resources are not a proxy for hosted UI resources. ChatGPT uses the remote connection in `mcp.json`, not the stdio bridge.

Future client integrations belong in their own `plugins/<client>` folders. Do not put host-specific behavior into neutral `src`, duplicate the remote tool catalog, or fork Swarm's OAuth and execution paths.

## References

- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/build/chatgpt-ui
- https://developers.openai.com/plugins/build/extensions
- https://developers.openai.com/plugins/deploy/submission
