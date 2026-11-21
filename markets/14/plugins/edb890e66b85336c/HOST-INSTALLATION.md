# Private host synchronization & public package

Repository package: `sketchmonkey-design`, version **1.0.3**.
Submission package archive: `sketchmonkey-plugin-v1.0.3.zip` (`https://neuraldeepnet.adaptive.ai/cdn/sketchmonkey-plugin-v1.0.3.zip`).

Canonical server: `https://sketchmonkey-neuraldeepnet.on.adaptive.ai/api/mcp`.
The `/mcp` alias remains an active compatibility endpoint.

## Deployment Status (Live & Verified)

- **RFC 8414 OAuth Metadata:** Live at `https://sketchmonkey-neuraldeepnet.on.adaptive.ai/.well-known/oauth-authorization-server`
- **RFC 9728 Protected Resource:** Live at `https://sketchmonkey-neuraldeepnet.on.adaptive.ai/.well-known/oauth-protected-resource` and `.../api/mcp`
- **Tool Catalogue:** 16 tools advertised with input schemas, boolean annotations, and OAuth 2.1 scopes.
- **Skills:** 4 SEP-2640 skills with YAML frontmatter and live OAuth 2.1 guidance (`industrial-design`, `poster-campaign`, `industrial-cmf-board`, `brand-variant-system`).
- **First-party UI:** `/oauth/consent` and `/oauth/connections` are live and functional on the production origin.

## Portal & Reviewer Actions (Owner/Reviewer Scope)

1. **Private Installation Sync:**
   OpenAI Issue #2 and #3 note the owner's existing private installation (`sketchmonkey-design-studio` v0.4.3). To update it in-place without creating a duplicate listing:
   - In the OpenAI Plugin Creator / Developer Portal, open the existing private installation.
   - Point the MCP server URL to `https://sketchmonkey-neuraldeepnet.on.adaptive.ai/api/mcp`.
   - Re-scan tools to discover all 16 tools and OAuth scopes.
   - Save the submission (preserving portal-managed app bindings).

2. **Public Directory Submission:**
   - Manifests are provided in `plugin/` (`plugin.json`, `mcp.json`, `.codex-plugin/plugin.json`) with `publication.countries: []` (unrestricted country targeting).
   - Clean export archive available at `https://neuraldeepnet.adaptive.ai/cdn/sketchmonkey-plugin-v1.0.3.zip`.
   - Canonical brand icon: `assets/icon.png` (square 512x512 PNG).
   - Policy pages: `/support`, `/privacy`, `/terms` all return 200 on both `sketchmonkey.design` and `sketchmonkey-neuraldeepnet.on.adaptive.ai`.

3. **Billing Boundary:**
   - Website Stripe billing remains separate from directory connector actions.
   - Live Stripe EUR account is active; synthetic billing tests verify entitlement updates on webhook delivery. Real card charges were not made for preparation.
