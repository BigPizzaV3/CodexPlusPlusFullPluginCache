# Cloudflare preparation and finalisation

The Worker source is in `cloudflare/`. Build/test locally as described in its
README. This ZIP's `mcp.json` contains `http://127.0.0.1:8787/mcp`, the endpoint
actually tested during preparation. It is for local verification only, and
the server is not left running after the preparation task finishes.

No Cloudflare account/project ID, production URL, developer-portal binding or
domain challenge is invented. `PUBLIC_ORIGIN` remains blank until a real
confirmed origin is selected. No deployment script or automatic upload is
part of the local test/build commands. The package is not public-upload-ready.

For a later separately authorised deployment:

- Confirm the intended Cloudflare account, Free plan and actual Worker name/
  hostname. Keep the full plugin and existing drafts intact.
- Prepare the exact origin config, then deploy through the authorised process.
  Use no AI/database/storage bindings. Measure real production CPU/availability
  and configure adequate, redacted operational diagnostics.
- Serve the portal's exact public domain-verification token from the supplied
  well-known route when prompted. A synthetic local token is not domain proof.
- Update the privacy/usage pages and complete the real host review/recording.
- Run the outer builder with `--public-endpoint <actual-HTTPS-MCP-URL>` and a
  fresh output directory. It probes that endpoint's health and actual tools
  against the saved local schema before generating the HTTPS upload copy.

The public builder does not deploy, connect to a portal, authenticate an
account, upload, submit or publish. A verified URL does not complete domain,
identity, scan, eligibility or recording requirements.

The current Worker includes per-IP and service-level request limiter bindings,
503 on unavailable protection, and 429 on excess requests before body parsing.
Production origin preparation now requires both --origin and --account-id.
Follow [the Worker deployment runbook](../cloudflare/DEPLOYMENT.md) and
[security controls](../cloudflare/SECURITY.md). Use the explicit account and
confirmed free workers.dev hostname; no credentials go into the package.
Limiter namespaces must not unintentionally collide with another Worker.
Preflight and dry-run checks are local; account ownership, Free-plan billing
and production CPU remain unverified until the actual deployment is inspected.

OpenAI currently does not support adding MCP to an existing Skills-only plugin.
Confirm the intended With MCP initial-submission identity/version path before
any portal action; do not delete or replace an existing draft to work around it.
