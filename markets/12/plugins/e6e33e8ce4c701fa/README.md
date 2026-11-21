# Notely Voice plugin 1.0.0

Search and read existing voice notes, transcripts, summaries, action items, and folders through the hosted Notely Voice MCP service.

## Package status

The root manifest passes the published Agent Plugins JSON schema. The MCP base configuration passes its published schema; the documented OpenAI OAuth extension is validated separately because the published 1.0.0 schema does not yet allow that extension. Public OAuth metadata and the unauthenticated MCP login challenge have been checked. Full authenticated server behavior remains to be tested; this package is not a production certification.

The latest source review confirms improvements to registration, host PKCE, callback validation, and credential storage. Remaining client-binding, signing-key, secret-rotation and end-to-end acceptance checks are recorded in `SERVER-SECURITY-REVIEW.md`. Installing the files does not validate or repair the hosted server.

## Requirements

- A host supporting portable Agent Plugins or the included Codex compatibility format.
- Network access to https://mcp.notelyvoice.ai/mcp.
- A Notely Voice account and the server's OAuth connection. The package explicitly configures OAuth dynamic client registration, the supplied authorization/token/registration endpoints, and the advertised `email` scope.
- No local Node.js, Python, package manager, dependency installation, or build step is required for this plugin.

## Installation

Keep `plugin.json`, `mcp.json`, `.mcp.json`, `.codex-plugin/`, `skills/`, and `assets/` at the plugin root. Do not move MCP configuration or assets inside `.codex-plugin/`.

For local desktop installation, extract the ZIP into a dedicated plugin folder and register that folder in a personal or repository marketplace using the companion `marketplace.json`. Its `source.path` resolves relative to the marketplace root. The marketplace's `authentication: ON_INSTALL` requests account connection at installation; this marketplace policy is outside the plugin ZIP. Refresh/restart the host as required, select that marketplace in the Plugins Directory, and install Notely Voice. Follow the host's OAuth connection flow and sign in personally. A CLI install may prepare the package without opening an interactive login screen; in that case complete Connect in the host. Existing authorized accounts may not see a fresh login screen. Exact UI labels vary by host version.

For public submission, use the developer dashboard's **With MCP** flow for the production remote endpoint. A Skills only upload is unsuitable for this package. Complete the owner-operated checks in `RELEASE-CHECKLIST.md` before submission.

Portable hosts use root `plugin.json` and `mcp.json`. The OpenAI inline extension is canonical. Hosts consuming the Codex fallback use `.codex-plugin/plugin.json` and root `.mcp.json`; that file uses the Codex `http` transport spelling.

## First use and connection failures

Run the packaged getting-started workflow, then request "Give me an overview of my voice notes." Try recent notes, a topic search, a selected transcript, and folders. Use a test account for initial validation.

If tools do not appear, confirm the plugin is enabled, the marketplace path points to the correct folder, and the host supports the package format. If authentication fails, reconnect using connection settings. If access is denied, check the account's permissions; do not replace authentication with a service-role key. Service failures should be investigated by the Notely operator.

Disable/uninstall the plugin using the host's plugin settings. Disconnect the Notely account separately using connection settings and revoke its authorization with the provider where supported. Uninstalling is not evidence that existing tokens have been revoked.

## Data and limitations

Queries are sent to the configured hosted service; retrieved note content is available to the host for answering. Review the provider's privacy policy and terms before connecting. Those URLs are declared in the manifest but their content and service data handling have not been verified.

The package includes no server implementation, credentials, tool schemas, or local hooks. Its instructions cannot enforce backend authorization. It does not add recording, deletion, editing, or payment tools. No custom plugin UI is declared; the mobile screenshot has been omitted.

Publication targets all countries supported by the host. The explicit empty countries list removes plugin-specific country restrictions; platform availability and applicable service requirements still apply.

## Documentation

- Packaging: https://developers.openai.com/plugins/build/plugins
- Submission: https://developers.openai.com/plugins/deploy/submission
- Validation errors: https://developers.openai.com/plugins/deploy/submission-errors
- Authentication: https://developers.openai.com/plugins/build/auth

## Configuration update — 2026-10-14

Version 1.0.1 applies the owner-supplied notelyvoice.ai website/privacy/terms URLs, portable Streamable HTTP transport, and exact long description. Three starter prompts appear in the listing; all five are retained in SAMPLE-PROMPTS.txt and review test cases. CONNECTION-SPECIFICATIONS.json records discovery/OpenAPI URLs and requested token exchange settings as supporting information; hosts consume mcp.json, not that file. Current validation results accompany the ZIP. Previous endpoint and source-review statements above are historical supplied evidence, not current verification.
