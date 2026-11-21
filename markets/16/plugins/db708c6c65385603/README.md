# NewsMCP 1.0.0 — NewsCatcher

Live news, deduplicated into events.

Website: https://newsmcp.com | MCP endpoint: https://mcp.newsmcp.com/mcp

The .codex-plugin/plugin.json and .mcp.json files use the supported Codex compatibility layout. The MCP configuration explicitly declares OAuth DCR and omit endpoint overrides so discovery supplies the provider values. No credentials or invented callback URLs are included. The package version is independent of the live MCP server version (observed 0.7.0).

The ZIP places these files directly at its root, without an extra enclosing folder. Upload the ZIP under the public plugin workflow and connect the endpoint under With MCP. Inspect imported authentication and listing settings before proceeding. Portal acceptance and OAuth interoperability remain unverified.

The supplied original logo is unchanged. Reviewer cases are embedded in the manifest and documented in REVIEW_TEST_CASES.md. See PRE_SUBMISSION_CHECKLIST.md for remaining portal work. The supplied Google Drive demo URL is embedded in the manifest; reviewer playback access still needs confirmation. No .app.json is included because no registered plugin_asdk_app ID was supplied; public portal endpoint setup does not require inventing one.

References checked 2026-11-11:
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission

Validation limitation: the fetched Agent Plugins 1.0.0 MCP schema disallows extensions, conflicting with the OpenAI documentation OAuth example. Portable manifests are therefore omitted. Compatibility fields were checked against the official examples; no machine-readable compatibility schema or actual uploader result was available.
