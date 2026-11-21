# LSEG AI - OpenAI Plugin Draft Bundle

Status: DRAFT / NOT READY FOR FINAL SUBMISSION

This bundle is the latest working package and submission handoff for LSEG AI.

## Confirmed

- Plugin name: LSEG AI
- Publisher: LSEG
- Subtitle: Data Analytics and Trading
- Category: Finance
- Submission type: Remote MCP / With MCP
- MCP URL model: Universal
- Production MCP URL: https://mcp.lseg.com
- UI: No
- Skills: No
- Authentication: OAuth 2.1
- Client registration method: Predefined OAuth client
- Authorization URL: https://login.ciam.refinitiv.com/as/authorization.oauth2
- Token URL: https://login.ciam.refinitiv.com/as/token.oauth2
- Registration URL: Not used for predefined OAuth client
- OAuth Client ID: PENDING
- OAuth Client Secret: PENDING if required; configure only in the OpenAI portal, not in this ZIP
- Token endpoint authentication method: PENDING
- Authorization server base: https://login.ciam.refinitiv.com
- Composer icon: assets/composer-icon.png (64x64)
- Directory icon: assets/directory-icon.png (256x256)
- Allowed countries/regions: all supported countries/regions
- Five positive and three negative review cases selected
- Original trading behavior and original public description retained at the user's request

## Public description retained

The LSEG connector provides real-time access to LSEG's institutional-grade market data, analytics and valuation capabilities, spanning across asset classes and domains, together with foreign exchange market coverage and order placement on LSE24 Exchange. It enables users to analyse instruments, perform complex calculations and move from analysis to execution through natural language interactions, governed by their existing LSEG account entitlements.

## Tool inventory

`submission/chatgpt-app-submission-draft.json` contains the 21-tool inventory and annotation justifications supplied by LSEG, with exactly five positive and three negative review tests selected. The unmodified supplied source JSON is preserved at `submission/source-chatgpt-app-submission.json`.

The raw production `tools/list` response from `https://mcp.lseg.com` is still required for final live verification of exact schemas, `_meta`, security schemes and scopes.

## Release notes draft

Initial release of LSEG AI, providing entitled users with access to LSEG market data, analytics and valuation capabilities, FX reporting and settlement-date calculations, and LSE24 RFQ and quote workflows through the LSEG MCP gateway. Access to data and actions is governed by each user's LSEG account entitlements and permissions.

## Demo recording

Record the demo in ChatGPT web with Developer Mode enabled and LSEG AI connected to the production MCP. Show OAuth sign-in, the five positive cases, the three negative cases, and explicit confirmation before the RFQ state-changing call. The final reviewer-accessible recording URL remains pending.

## Pending

See `submission/PENDING.md` for the current remaining items.

## Files

- `plugin.json` - working portable plugin metadata
- `mcp.json` - production MCP endpoint
- `assets/` - composer and directory icons
- `submission/portal-draft.md` - field-by-field portal handoff
- `submission/oauth-draft.json` - current OAuth configuration and placeholders
- `submission/chatgpt-app-submission-draft.json` - curated 5+3 test draft with supplied tool inventory
- `submission/source-chatgpt-app-submission.json` - unmodified source JSON supplied by LSEG
- `submission/PENDING.md` - remaining items

## Important

For a public remote-MCP submission, the OpenAI Platform portal and live production MCP are authoritative. This ZIP is a working package/handoff artifact and does not itself publish the plugin.
