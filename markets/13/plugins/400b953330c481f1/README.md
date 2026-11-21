# Beredskapguide ChatGPT plugin package

This portable Agent Plugins package connects ChatGPT to Beredskapguide’s one public, read-only Streamable HTTP MCP server:

`https://www.beredskapguide.se/mcp`

The declared publisher is Adrian Martén; public support and privacy questions use the existing contact route at [Beredskapguide](https://www.beredskapguide.se/om-guiden).

The server is intended to expose exactly three tools: `search_guides`, `get_preparedness_guide`, and `calculate_water_reserve`. It has no authentication, purchases, advertising, private household data, live-alert feed or medical-diagnosis capability.

## Validate and create the upload archive

From the repository root:

```sh
node scripts/check-chatgpt-package.mjs
mkdir -p dist
(
  cd integrations/chatgpt
  zip -r ../../dist/beredskapguide-chatgpt-plugin.zip plugin.json mcp.json assets README.md
)
```

The upload ZIP must extract with `plugin.json` and `mcp.json` at its root. It deliberately does not contain an `.app.json`, local command, lifecycle hook, credential or secret.

After the review page, walkthrough and captions are deployed, perform the boundary check:

```sh
node scripts/check-chatgpt-package.mjs --live
```

`--live` verifies public HTTPS responses, review-page metadata, the MP4 byte-range response and the WebVTT captions. It does not prove a directory submission, MCP scan, indexing, model tool selection or marketplace approval.

## Submission checklist

1. Complete OpenAI developer identity verification and ensure the selected organization has Plugins submission access.
2. Upload `dist/beredskapguide-chatgpt-plugin.zip`, select the verified publisher identity, and connect `https://www.beredskapguide.se/mcp` in the Plugins dashboard.
3. Complete the dashboard domain-verification challenge and resolve all MCP scan findings. The server must expose only the three declared read-only tools.
4. Run all five positive and three negative cases in ChatGPT against the deployed server. Record actual results in the review walkthrough; do not present expected behavior as observed evidence.
5. Confirm that the public review page, MP4 walkthrough and captions are accessible, then use the dashboard to submit the draft. No reviewer account or credentials are needed because the server has no authentication.

## Sources and limits

- [Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [Upload and submit your plugin](https://developers.openai.com/plugins/deploy/submission)
- [Plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines)
- [Beredskapguide privacy policy](https://www.beredskapguide.se/integritet)
- [Beredskapguide terms](https://www.beredskapguide.se/villkor)

This package declares a stable public endpoint but cannot establish that OpenAI accepts the package, verifies the publisher identity, scans the MCP server successfully, or approves publication. The walkthrough media and actual ChatGPT test evidence are pending until they have been recorded against the deployed service.
