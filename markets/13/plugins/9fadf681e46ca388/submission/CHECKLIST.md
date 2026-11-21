# OpenAI public submission checklist

The package files are prepared, but the plugin should not be sent for public
review until every blocking item below is complete.

## Package and listing

- [x] `.codex-plugin/plugin.json` uses a stable kebab-case identifier and
  semantic version.
- [x] `.mcp.json` points to the production remote MCP endpoint.
- [x] Public listing copy and three starter prompts are prepared.
- [x] Five positive and three negative reviewer test cases are prepared.
- [x] Release notes are prepared.
- [x] Public website, help center, privacy policy, terms, and support contact are
  identified on the production domain.
- [ ] Confirm the support mailbox accepts and answers external mail.
- [x] Confirm that `https://moodlenstodo.com/mcp.html` is deployed and public.
- [x] Include the final 512 x 512 production logo and composer icon in the
  plugin package.
- [x] Host the reviewer walkthrough and include its verified public URL in the
  version 1.0.4 manifest.
- [ ] Upload the version 1.0.4 ZIP to import the recording URL in the portal.

## MCP server blockers

- [x] Implement MCP OAuth 2.1 protected-resource discovery.
- [x] Implement authorization-server metadata for the production issuer.
- [x] Support Dynamic Client Registration and require S256 PKCE for every MCP
  authorization.
- [x] Preserve the OAuth `resource` parameter through authorization and token
  exchange.
- [x] Bind every accepted MCP bearer to the exact production resource and
  issuer.
- [x] Preserve OAuth `state` exactly and return post-validation authorization
  errors to the registered callback.
- [x] Request the scopes the plugin's workflows need at first connect
  (`baseScopes` in `.mcp.json`). On 2026-10-20 ChatGPT reconnected with the same
  scopes instead of completing per-tool step-up, so every non-task tool failed.
  `integrations` stays opt-in.
- [x] Rotate refresh tokens and revoke the family atomically on reuse.
- [x] Retain rotated refresh records through their original expiry so replay
  remains detectable.
- [x] Apply pre-authentication abuse throttling and a stable per-family request
  limit that does not reset when access tokens refresh.
- [x] Return an appropriate `WWW-Authenticate` challenge for unauthenticated
  MCP requests.
- [x] Add accurate `readOnlyHint`, `openWorldHint`, and `destructiveHint`
  annotations to every exposed MCP tool.
- [x] Mark destructive and externally visible actions so the host can request
  user confirmation.
- [ ] Run initialization, tool-listing, read, write, authorization-expiry, and
  refresh-token tests against the production endpoint.
- [ ] Verify that error responses never expose credentials, stack traces, or
  data from another workspace.

## OpenAI account and portal fields

- [ ] Complete OpenAI individual or business verification for the publisher
  identity selected in the submission.
- [ ] Confirm the submitter has Apps Management write access in the owning
  OpenAI Platform organization.
- [ ] Verify control of the production MCP domain when requested by the portal.
- [ ] Register the production server in ChatGPT Developer Mode and complete all
  reviewer workflows in a new chat.
- [x] Keep `.app.json` and lifecycle hooks out of the public-submission ZIP;
  OpenAI currently rejects public packages containing either one.
- [ ] Create a dedicated reviewer workspace and provide demo credentials only
  through the portal's secure fields.
- [ ] Choose the supported countries or regions with the responsible business
  or legal owner.
- [ ] Complete policy attestations using verified product and data-handling
  information.
- [ ] Enter `support@moodlens-ai.com` and
  `https://moodlenstodo.com/help-center` in the portal's support fields.

## Reviewer package

- [ ] Populate the reviewer workspace with safe sample tasks, documents, a
  board, a sprint, and a meeting.
- [ ] Confirm the reviewer account has only the scopes required by the submitted
  workflows.
- [ ] Record expected tool calls and results for all cases in `TEST_CASES.md`.
- [ ] Submit the MCP server directly as a new MCP-backed plugin rather than
  referencing an existing integration.
