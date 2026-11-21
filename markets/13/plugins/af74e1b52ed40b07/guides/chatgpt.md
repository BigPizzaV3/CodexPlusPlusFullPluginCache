# ChatGPT

Upload this same ZIP in the OpenAI package flow. Do not extract it.

Skill/plugin version 0.1.41. The version in plugin.json is that release, not the Cofr app version.

MCP URL: https://09vyfnjv.mcp.cofr.io/mcp

## Tools

- run_aoa_mini_assessment: Public, no sign-in
- aoa_ai_opportunity_assessment: OAuth required
- create_aoa_discovery_guide: OAuth required
- run_aoa_full_assessment: OAuth required

A public tool can be called before sign-in. A protected tool asks ChatGPT to connect. Live tool metadata uses `noauth` or `oauth2`. This guide does not mark that behavior verified.

Schema validation, import, runtime, and directory approval are separate. An incomplete package is not submission-ready.

Last verified 2026-10-19: https://developers.openai.com/plugins/deploy/submission
