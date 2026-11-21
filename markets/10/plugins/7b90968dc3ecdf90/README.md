# TODAY ChatGPT Plugin

Config-only OpenAI plugin for the TODAY MCP server. This folder packages the
manifest (`.codex-plugin/plugin.json`) and MCP connection (`.mcp.json`) that
ChatGPT and Codex load. The MCP server, tools, and OAuth code live in
`today_app`; there is no application code here.

## Files

| File | Purpose |
| --- | --- |
| `.codex-plugin/plugin.json` | OpenAI/Codex plugin manifest (`name: today`): listing fields under `interface`, review/publication under `extensions.com.openai`, and `mcpServers: "./.mcp.json"`. |
| `.mcp.json` | Codex MCP config: one `http` server, `today`. |
| `assets/composer-icon.svg` | Square brand mark used for `composerIcon`. |
| `assets/logo.svg` | Square brand mark used for `logo`. |

## Keep aligned with `today_app`

This package must stay aligned with the MCP implementation in `today_app`:

- `today_app/mcp-app/` — MCP resource server exposing Streamable HTTP at `/mcp`,
  the read-only tool surface (`search`, `get_call`, `get_customer_extracted_data`,
  `get_customer_cumulative_facts`, `get_profile`), and the OAuth protected-resource metadata.
  `capabilities: ["Read"]` assumes every tool keeps `readOnlyHint: true`.
- `today_app/backend/api/oauth_server.py` — OAuth 2.1 authorization server
  (DCR + PKCE) that issues the scoped `connector:read` tokens the MCP server
  validates.

If a tool is added or removed, or the auth flow changes, update
`extensions.com.openai.review.test_cases` and the submission listing.

## MCP endpoint

| Environment | URL |
| --- | --- |
| Production | `https://mcp.usetoday.io/mcp` |

The production URL comes from `MCP_PUBLIC_URL` on the Azure app `today-mcp`
(`az webapp config appsettings list --name today-mcp --resource-group TODAY`).
Do not guess the host: re-read that setting before changing `.mcp.json`.

## Listing metadata

Confirmed values (verified reachable):

| Field | Value |
| --- | --- |
| `websiteURL` | `https://www.usetoday.io` |
| `supportURL` | `https://help.usetoday.io/` |
| `privacyPolicyURL` | `https://www.usetoday.io/legal/privacy-policy` |
| `termsOfServiceURL` | `https://www.usetoday.io/legal/terms-and-conditions` |
| `brandColor` | `#5932EA` |

## Submission status

Package metadata, icons, and all four listing URLs are in place. Remaining
items before submitting for MCP review:

- **Domain verification.** Host the portal challenge token as plain text at
  `https://mcp.usetoday.io/.well-known/openai-apps-challenge`. The MCP server
  serves `OPENAI_APPS_CHALLENGE` there when the env var is set (see
  `today_app/mcp-app/.env.template`).
- **Demo recording.** Set in `extensions.com.openai.review.demo_recording_url`
  (`https://youtu.be/DblWVeT5LwA`); it must show the main use cases and tools.
- **Test cases.** The five positive and three negative cases in
  `.codex-plugin/plugin.json` are drafts; run them against the reviewer test
  account and correct any drift before submitting.
- **Reviewer credentials.** Enter these in the submission dashboard, never in
  the package.

## `.app.json` — do not add to the submission package

OpenAI does not accept plugin ZIPs that contain app references (`apps` /
`.app.json`); such packages cannot be submitted. Declare the remote MCP URL in
`.mcp.json` and complete MCP setup in the dashboard instead.

`.app.json` (with a `plugin_asdk_app…` id from a developer-mode connection) is
only useful for local Codex/developer-mode testing. Do not add it to the root
`apps` field of `.codex-plugin/plugin.json` or commit it in a form that ships in
the submission ZIP. If you create it for local testing, keep it out of the ZIP
(for example, `cd chatgpt && zip -r ../today.zip . -x '.app.json'`) and remove
the `apps` field before submitting.

## Connect in ChatGPT developer mode

1. In ChatGPT, open **Settings** → **Security and login** and turn on
   **Developer mode**.
2. Go to [ChatGPT Plugins](https://chatgpt.com/plugins) and select the plus
   button.
3. Enter the MCP server URL above and complete the connection; sign in to TODAY
   when prompted (DCR + PKCE).
4. ChatGPT creates the connection and shows a technical ID in the browser URL
   beginning with `plugin_asdk_app`.

## Package

[chatgpt-package.yml](../.github/workflows/chatgpt-package.yml) builds
`today-plugin.zip` with `.codex-plugin/plugin.json`, `.mcp.json`, and `assets/`
at the ZIP root (`.app.json` excluded) and uploads it as a workflow artifact:

- Every push or PR touching `chatgpt/` (and manual `workflow_dispatch`): download
  the artifact from the run's **Summary**.
- Push/merge to `main`: also published as the `chatgpt-v<version>` GitHub
  Release asset.

To build locally (`cd chatgpt`):

```bash
zip -r -X ../today-plugin.zip . \
  -x '.app.json' -x '*.DS_Store' -x '*.zip' -x '**/__pycache__/*'
```

OpenAI does not deploy from this repo; upload the ZIP through the submission
portal. After publication, MCP tool changes are picked up automatically by
OpenAI's scans.

## Release a new version

The version lives in `chatgpt/.codex-plugin/plugin.json` (`version`) and is
independent of every other app in this repo. To cut a new version:

1. **Bump the version** in `chatgpt/.codex-plugin/plugin.json`:
   - Set `version` to the next [semver](https://semver.org/) (e.g. `0.1.0` → `0.2.0`).
   - Update `extensions.com.openai.publication.release_notes` to describe the change.
   - If the tool surface or listing changed, update
     `extensions.com.openai.review.test_cases` and the `interface` fields too.
2. **Build it.** Merge to `main` and let
   [chatgpt-package.yml](../.github/workflows/chatgpt-package.yml) run (or, to
   test first, run the workflow from the branch via **Actions → ChatGPT plugin
   package → Run workflow**).
3. **Download the ZIP.**
   - From the release: GitHub → **Releases** → `chatgpt-v<version>` →
     **Assets** → `today-plugin.zip`.
   - Or from the run: **Actions** → the run → **Summary** → **Artifacts** →
     `today-plugin-<version>`.
4. **Upload it** at [platform.openai.com/plugins](https://platform.openai.com/plugins):
   - First release: **Upload new or existing plugin**.
   - Update: open the existing plugin → **Upload plugin to make changes**, then
     publish the approved package version.
5. **Reviewer credentials** go in the dashboard's secure form, never in the ZIP.

Notes:

- The MCP server URL cannot be changed through the update flow; changing it
  requires contacting OpenAI support.
- Once published, **MCP tool changes are picked up automatically** by OpenAI's
  scans. Only metadata/skills changes need a new ZIP (steps 1–4).
- The workflow already excludes `.app.json` and `.DS_Store`; do not add app
  references to the submission package (see above).
