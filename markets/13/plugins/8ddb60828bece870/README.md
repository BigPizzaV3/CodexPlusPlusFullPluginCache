# Data4Traders OpenAI plugin package draft

Status: **draft; not submitted**. Verified against OpenAI and Agent Plugins
documentation on 2026-10-21.

## Package contents

- `plugin.json`: portable package identity, draft listing metadata, and five
  positive / three negative MCP review case drafts.
- `mcp.json`: one Streamable HTTP server at the verified public MCP endpoint,
  with OpenAI OAuth/DCR configuration matching the live Supabase discovery
  registration endpoint.
- `assets/data4traders-icon.svg`: existing square Data4Traders brand icon.

## Validation performed

- `plugin.json` validates against the official Agent Plugins 1.0.0 plugin
  manifest schema.
- `mcp.json` does **not** validate against the generic Agent Plugins 1.0.0
  MCP schema: that schema rejects the server-level `extensions` field required
  by OpenAI's current package guide for auth configuration. The two official
  docs conflict; OpenAI portal package validation is needed to determine which
  validator governs an actual upload.
- Listing URLs returned HTTP 200: website, imprint/contact, privacy, and terms.
- Icon has a square `viewBox` of 224 x 224.
- Positive case count: 5. Negative case count: 3.
- Short description length: 29 characters (maximum 30).

SHA-256:

| File | SHA-256 |
|---|---|
| `plugin.json` | `91f8136815bbd21c0530f11ef5ed318783e912d8a222b29fa051c528d491d593` |
| `mcp.json` | `6bf5795670aa63e58a2341c341109fccc6cced1f0fc5cc2c2ba516b9a5138abc` |
| `assets/data4traders-icon.svg` | `97432c86265db74ef0620e3129505ce9eb2f95efa0d6253166bd89ac7aea5e64` |

## Still required before submission

- Verify MCP tool metadata, OAuth behavior, permissions, and denial cases after
  prerequisite #1354/#1355 and WI-1 (#1362) are complete.
- Run all eight review scenarios against an isolated synthetic account/list;
  replace illustrative prompts/results if observed behavior differs.
- Record and host a reviewer-accessible walkthrough video, then add its URL to
  `extensions.com.openai.review.demo_recording_url`.
- Owner confirms the category, verified publisher identity, OpenAI project
  residency and Apps Management permissions in the dashboard.
- Owner/legal review updates the public privacy policy to accurately describe
  MCP data categories, purposes, recipients, retention, and revocation controls.
- Owner confirms the imprint/contact page as support URL and verifies listing
  claims and intended public countries.
- Connect and scan the public server in the protected portal; resolve findings.

The package contains no credentials. OAuth uses DCR discovered from the live
authorization-server metadata; no client secret, explicit endpoint override,
or server header is included. Do not describe the MCP manifest as validated
until OpenAI's upload validator resolves the schema conflict. No review
submission or publication has been performed.
