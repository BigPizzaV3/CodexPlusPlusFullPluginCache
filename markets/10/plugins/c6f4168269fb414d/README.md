# Noxi plugin

This repository is the source of truth for the Noxi Codex/ChatGPT plugin
scaffold. The plugin connects to one remote MCP server:
`https://mcp.noxi.ai/mcp`.

The package contains no credentials, API keys, embedded access tokens, or
local MCP process. Authentication is handled by the host against the OAuth
metadata advertised by the remote service.

## Included files

- `.codex-plugin/plugin.json` contains the reviewable listing metadata.
- `.mcp.json` pins the remote MCP URL plus the mandatory pre-registered Codex
  client and stable loopback callback. The OAuth resource is discovered from
  the server's Protected Resource Metadata; adding a duplicate explicit
  resource value would make the client send the parameter twice.
- `skills/noxi-presentations/SKILL.md` tells the model to discover actual Noxi
  capabilities and to avoid claiming unavailable account operations.
- `assets/noxi.svg` is copied from the repository-owned Noxi favicon.
- `.agents/plugins/marketplace.json` at the repository root makes this source
  available as a repository marketplace entry for development and review.

## Public references

| Purpose | Reference |
| --- | --- |
| Product | <https://noxi.ai/> |
| MCP server | <https://mcp.noxi.ai/mcp> |
| Privacy policy | <https://noxi.ai/privacy-policy> |
| Terms of service | <https://noxi.ai/terms-of-service> |
| Support | <https://noxi.ai/support> · `info@noxi.ai` |
| Security reports | `security@noxi.ai` |

The repository-owned canonical support page provides the real support and
security contacts, safe reporting guidance, and localized privacy and terms
links without asking users to disclose credentials. Verify the deployed
`https://noxi.ai/support` route before submitting the public listing.
Current OpenAI submission documentation recognizes `interface.supportURL`, but
the installed local plugin-creator validator rejects that property. Until E10B
runs the official ingestion/portal validator and resolves the compatibility
gap, `homepage` remains the package's support-URL fallback and the listing
draft carries the explicit support value. This local compatibility result is
not evidence that the current OpenAI validator rejects `supportURL`.
The optional public-source listing field remains omitted while the GitHub
repository is private; add it only after the cited URL is anonymously
reachable.

## Review and publication boundary

This scaffold and its repository marketplace entry do not publish Noxi to the
OpenAI Plugin Directory or the Claude Connector Directory. Public submission
still requires the platform-owned UI steps and review material documented in
[`docs/NOXI_CONNECTORS_PLAN.md`](../../docs/NOXI_CONNECTORS_PLAN.md): verified
publisher and domain, exact listing copy, remote-tool scan, reviewer account,
positive and negative test cases, the canonical support URL, screenshots where
required, and an explicit publish action after approval.

Claude uses the same remote MCP URL through its separate custom connector and
directory submission flow. Nothing in this Codex plugin manifest registers or
publishes a Claude connector.

The package now describes the deployed toolset (October 2026): reading
presentations and templates, creating presentations with the website engine,
AI edits through the real editor, and PDF/PPTX export
(`docs/architecture/connectors/E12_ENGINE_RUNNER.md`). Connection steps for
every host are in [`CONNECT.md`](./CONNECT.md). The release-gated listing
material and review cases still live in
[`docs/architecture/connectors/E10_PUBLICATION_PACKAGE.md`](../../docs/architecture/connectors/E10_PUBLICATION_PACKAGE.md)
and are refreshed after the live end-to-end runs.

## Local validation

From the repository root:

```sh
npx vitest run scripts/__tests__/noxiPluginScaffold.test.mjs
```

The committed test enforces the ingestion shape on a clean CI runner. Plugin
authors who also have the Codex plugin-creator skill installed may run its
`validate_plugin.py` as an additional local compatibility check. The current
private package passes that local validator and was imported successfully
from an isolated development marketplace; this is local ingestion evidence
only and does not represent an OpenAI portal validation, end-user installation
or directory publication.
