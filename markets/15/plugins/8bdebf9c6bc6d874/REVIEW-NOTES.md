# OAuth connection draft 1.0.4 — not ready for review

Native MCP URL: https://nest.promptowl.ai/mcp
OAuth discovery and the protected-resource challenge were verified on 2026-11-01. The authorization server advertises DCR, public clients, and S256 PKCE. No OAuth client has been registered by this build; registration occurs during connection setup. No secrets are included.

The portal previously requested a provided client ID. This draft explicitly selects DCR, supported in current package documentation. Portal acceptance and end-to-end sign-in have NOT been verified. If the portal still insists on a provided client ID, a real ContextNest-registered client and exact portal callback URI are required; do not reuse the legacy OpenAI client ID.

Preserved review cases and recipes describe the legacy wrapper. They must be revised against the native server tool inventory after connecting, before submission. All cases: Not run. Existing demo describes the old connector; a native-OAuth demo, reviewer account, policy coverage, listing URL verification, scans and attestations remain required.

This archive is for resolving draft connection setup, not submission for review. Changing the MCP hostname may require domain verification or may be rejected by the existing draft update route; use the portal feedback rather than assuming the old verification carries over.
