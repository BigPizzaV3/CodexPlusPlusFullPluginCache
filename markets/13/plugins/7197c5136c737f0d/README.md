# AEvent – ChatGPT plugin package

Submission package for the ChatGPT / Codex plugin directory
(OpenAI Platform → Plugins → Upload new or existing plugin).

```
aevent-chatgpt-plugin/
├── plugin.json   # manifest, listing text, review test cases, release notes
├── mcp.json      # AEvent MCP server (staging, OAuth with DCR, scope mcp:use)
└── assets/
    ├── logo.png           # 512×512, light theme
    ├── logo-dark.png      # 512×512, dark theme
    └── composer-icon.png  # 256×256
```

This README is for the team only. Don't put it in the ZIP.

## Before uploading: fill in the TODOs in `plugin.json`

- `author.name`, `developerName`: registered company name, matching the verified
  developer identity (Business verification recommended; see below).
- `author.email`: support email.
- `privacyPolicyURL`, `termsOfServiceURL`: public HTTPS pages.
- `review.demo_recording_url`: a video walkthrough reviewers can open.

Already set: `websiteURL` https://aevent.com, `supportURL` https://help.aevent.com.

## Server

- `mcp.json` currently points at **staging**: `https://dev-api.aevent.com/mcp`.
  Production is `https://app-api.aevent.com/mcp`. OpenAI expects a stable public
  endpoint and may reject a staging/testing one, and the MCP URL can't be changed
  after submission without contacting OpenAI support, so switch back to
  production before the real submission.
- No client ID or secret is needed (DCR). Never put tokens or secrets in this package.

## Reviewer test account (entered in the dashboard, never in the package)

Login URL for reviewers: **https://dev.aevent.com** while `mcp.json` points at staging
(**https://app.aevent.com** for production). The account must exist on the same
environment as the MCP server.

A dedicated AEvent login that works **without MFA, email/SMS codes or magic links**, with:
- a campaign named **Demo Webinar** with a delivery integration connected
  (test cases 3 and 5 use it),
- at least one upcoming scheduled webinar (test case 2),
- some sample campaigns (test case 1).

Run all 5 positive and 3 negative test cases in `plugin.json` with this account
before submitting.

## Zip

From inside this folder (so `plugin.json` sits at the ZIP root):

```
cd ~/test/aevent-chatgpt-plugin
zip -r ../aevent-plugin.zip plugin.json mcp.json assets
```

## Upload and submit

1. platform.openai.com → **AEvent** organization → **Plugins** → **Upload new or existing plugin**.
2. Choose the verified developer identity and upload `aevent-plugin.zip`. Fix anything in **Issues** and re-upload.
3. **MCP server**: confirm the URL, choose OAuth (Dynamic Client Registration), connect and authorize.
4. **Domain verification**: serve the token OpenAI gives you as plain text at
   `https://<MCP host>/.well-known/openai-apps-challenge` on the MCP host in `mcp.json`
   (`dev-api.aevent.com` for staging, `app-api.aevent.com` for production; backend task).
5. **Review details**: reviewer test account, then **Save details**.
6. **Submit for review**, accept the policy attestations, watch **Review status** (feedback by email).
7. After approval, open the approved version and click **Publish plugin**.

## Developer identity

The AEvent organization is currently verified as **Individual**. Individual is
enough to submit, but the listing would show a person as the publisher. For
"By <company>" use **Business** verification (Organization settings → Verifications).

Docs: https://developers.openai.com/plugins/deploy/submission
