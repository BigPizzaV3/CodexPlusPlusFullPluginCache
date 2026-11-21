# SupMarTech Meta Ads Interest

This folder is a draft Agent Plugins package for the public ChatGPT/Codex Plugins Directory. It connects to the existing remote SupMartech MCP service with OAuth; it does not bundle server credentials or website source code.

## Package contents

- `plugin.json` — listing metadata, locale translations, and review test cases.
- `mcp.json` — remote Streamable HTTP URL and OAuth/DCR connection settings.
- `assets/mcp_icon.png` — SupMartech icon copied from the existing site asset.
- `REVIEW_NOTES.md` — portal checklist and annotation justifications.

## User-facing capabilities

- Search Meta ad-targeting interests using up to five terms.
- Separate direct results from related suggestions.
- Review approximate audience-size data returned by Meta.
- Score relevance, group supplied interests for testing, and estimate a budget scenario from user-provided assumptions.
- Generate a prompt for preparing a Saved Audience draft with a confirmation step.

The MCP tools do not access Ads Manager and cannot create or change ads, campaigns, ad sets, or audiences.

## Draft status

This package is not ready for final review submission until the production MCP metadata is updated and rescanned, the legal pages are deployed and verified, the listing name fits the 30-character public limit, and a reviewer account plus accessible demo recording are provided in the OpenAI portal. See `REVIEW_NOTES.md`.
