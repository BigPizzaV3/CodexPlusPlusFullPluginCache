# Electric State — submission package 1.3.0

This package creates a new Electric State plugin connected to the existing hosted MCP server. OpenAI asked for a new plugin (not a new version of the old one) so that the MCP server can be connected during setup. The hosted server reports version 1.2.0; the package version is independent.

- Endpoint: https://api.electricstate.app/mcp
- Transport: Streamable HTTP, stateless
- Authentication: None. The server is public and read-only, so reviewers need no account, API key or test credentials.
- Tools: `search_festivals`, `get_set_times`, `list_festivals`, `get_artist_schedule`. All four are read-only and first-party: Electric State's own festival catalog and schedules transcribed from official graphics.
- UI: tool results only; no widget resources are advertised.

## Upload

1. In Plugins, choose **Upload new or existing plugin**, pick the verified developer identity, select **Upload plugin**, and choose this ZIP.
2. Open **MCPs**, select the server, and choose **Connect**. Confirm the endpoint above and set authentication to **None**.
3. Complete the domain challenge. The portal shows the token and the URL it checks: https://api.electricstate.app/.well-known/openai-apps-challenge. That URL must serve the new plugin's token. If the token differs from the one it serves now, the site has to be redeployed before **Verify** passes.
4. Wait for the tool scan. Exactly the four tools above should appear, with no **Issues**.
5. Confirm the demo recording URL in review details. It is set in this ZIP as `review.demo_recording_url`: a public Google Drive copy of the September 4 walkthrough, which shows ChatGPT developer mode running the plugin. It predates `list_festivals`. Then set country availability and submit.

## Review cases

Five positive and three negative scenarios are included. Time-sensitive searches avoid fixed result counts. The `list_festivals` case asks for the next two weeks rather than fixed dates, so it stays valid whenever review runs.

## Validation scope

On October 20, 2026 (Pacific time), `initialize` and `tools/list` succeeded against production, and `tools/list` returned exactly the four tools above, each with `readOnlyHint: true`. Direct calls for every positive and negative data lookup returned the expected results. The domain-challenge URL returned HTTP 200 with the previous plugin's token. These checks do not substitute for the portal's connection, policy, or conversational review.

## Reference

Package format: https://developers.openai.com/plugins/build/plugins

Upload, connect, and review: https://developers.openai.com/plugins/deploy/submission
