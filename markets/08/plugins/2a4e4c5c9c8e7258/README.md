# DataFlowr for Codex and ChatGPT

Registers the DataFlowr MCP server and its workflow skills in Codex, and the
same server in ChatGPT.

Getting started: <https://dataflowr.nl/en/claire> · Support: info@dataflowr.nl

> **The two halves authenticate differently.** ChatGPT signs in with OAuth and
> needs no credential. **Codex uses a connection token.** Once the Auth0
> migration lands, DataFlowr's authorization server supports neither dynamic
> client registration nor `localhost` redirect URIs — open registration is an
> attack surface and each registration consumes an Auth0 Application against a
> hard tenant cap, while Auth0 exact-matches redirect URIs with no port
> wildcard — and Codex needs both. Written up in full, with the per-vendor
> deviations, on that branch as `docs/mcp-oauth-compliance.md`.

## Install — Codex

Once listed, install it from the ChatGPT plugin directory, or run `/plugins`
in Codex and install the marketplace entry.

Then add the connection token. Open your connection in DataFlowr, copy its
`mcp_` token, and put it in the environment:

```bash
export DATAFLOWR_TOKEN=mcp_...
```

```toml
# ~/.codex/config.toml
[plugins."dataflowr".mcp_servers.dataflowr]
bearer_token_env_var = "DATAFLOWR_TOKEN"
```

`codex mcp login dataflowr` is **not** used. The token names exactly one
connection, so there is no connection to pick — to work in a different
administration, use that connection's token.

## Install — ChatGPT

Once listed, add it from the ChatGPT directory. Until then, ChatGPT web users
can add the same server by hand: **Settings → Connectors → Create** (developer
mode must be on for the workspace), with `https://app.dataflowr.nl/mcp` as the
URL and OAuth as the authentication. The connection picker appears in that
flow too. The plugin's skills are Codex-side only in that setup.

## Pointing at another deployment

The manifest pins DataFlowr's hosted endpoint, and Codex does not expand
variables in `.mcp.json`
([openai/codex#24401](https://github.com/openai/codex/issues/24401)). To test
against a development or self-hosted deployment, override the URL after
installing:

```toml
# ~/.codex/config.toml
[plugins."dataflowr".mcp_servers.dataflowr]
url = "https://dataflowr.internal.example/mcp"
oauth_resource = "https://dataflowr.internal.example/mcp"
```

## What is in it

### Listing languages and repository

The base listing text is English. Dutch (`nl-NL`) subtitle and description
alternatives are included in
`extensions.com.openai.publication.translations` in the manifest.
OpenAI currently validates and retains these translations in uploaded bundles,
but does not yet show them in the Plugins Directory or listing API responses.
Localized display names and starter prompts are not documented in this format;
unlike Copilot, it does not use language files with localization keys.
See [OpenAI's translation documentation](https://developers.openai.com/plugins/deploy/submission#translate-listing-text).

The source repository moved to <https://github.com/DataFlowrBV/DataFlowr> and
is private. The optional `repository` field is deliberately omitted from the
submission rather than pointing users to an inaccessible source repository.
The public product website remains in `homepage` and `interface.websiteURL`.

| Path | Purpose |
|---|---|
| `.codex-plugin/plugin.json` | Manifest — identity, component paths, install-surface metadata |
| `.mcp.json` | The bundled MCP server: `https://app.dataflowr.nl/mcp`, OAuth |
| `chatgpt-app-submission.json` | OpenAI submission-form import: app copy, tool-hint justifications, and review test cases |
| `skills/dataflowr-erp/` | Division resolution, reporting-vs-ledger choice, query guardrails, write confirmation |
| `skills/month-end-close/` | Delegate a close to the hosted closing agent, poll it, report findings, record decisions |
| `skills/cashflow-forecast/` | Delegate a forecast to the hosted forecasting agent and report it with its assumptions |

The skills name real MCP tools (`exact_online_divisions`, `financial_report`,
`closing_agent`, `forecasting_agent`); a renamed tool silently turns a recipe
into a wrong instruction, so keep them in sync with the server's tool surface.

The submission-form import is a review snapshot of the live MCP surface and is
uploaded to prefill the OpenAI review form; it is not runtime plugin
configuration. `plugins/__tests__/chatgpt-app-submission-sync.test.ts` pins its
tool census and safety annotations to the registry, so a tool-surface change
fails CI until the reviewer copy and test cases are refreshed together.

The directory listing is live, so the `plugin_asdk_app_…` id ChatGPT issues on
registration exists. The package name must retain the portal-assigned identity.
The `assets/` directory contains the owner's exact Licht (light) and Navy (dark)
PNG exports in seven resolutions. The manifest references 512px listing logos
and 96px composer icons in both themes. Always include this directory in uploads;
the icon reference alone is not sufficient.

The support URL is `https://dataflowr.nl/en/support`. The Productivity category
describes accounting work in Exact Online; the dashboard may require the owner
to reselect or confirm its category. The portal holds what the listing shows —
see `docs/marketplace-submissions.md` at the repository root.

## Download the submission archive

Signed-in users can download `/api/codex/agent-package.zip`. It calls the shared
`buildCodexPackage` builder, which packages this directory including hidden
configuration files and all original icon assets, and rejects missing icons.
Production builds copy this directory to `server/dist/codex-plugin` for the same
builder. Do not create separate ad-hoc ZIPs for submissions.
