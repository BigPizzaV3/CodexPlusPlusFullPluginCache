# Changelog

## 1.0.0

- Add the required portable manifest schema and remove unsupported root fields.
- Add Codex `.mcp.json` wiring and synchronized compatibility metadata/onboarding.
- Declare OAuth dynamic client registration and the verified advertised endpoints and email scope in both MCP files.
- Ship a companion marketplace with authentication on install.
- Improve setup, retrieval, account-access, untrusted-transcript, and failure instructions.
- Remove the mobile screenshot and homepage demo declaration.
- Add installation requirements and owner-operated production acceptance checks.
- Preserve the hosted endpoint, publisher, brand assets, and review scenarios; target all supported countries as requested by the owner.

No server code was changed or executed locally. Public discovery and the unauthenticated login challenge were checked; full authentication and production behavior remain unverified.
