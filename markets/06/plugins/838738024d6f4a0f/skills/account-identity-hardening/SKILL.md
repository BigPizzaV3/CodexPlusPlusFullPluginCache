---
name: account-identity-hardening
description: Review Cloudflare account access, API-token scope, Access policies, and service credentials.
---

# Account and Identity Hardening

Review users, account roles, membership scope, authentication protections, session/security posture, Access applications and policies, service tokens, and API-token metadata where available. Use least-privilege recommendations: scope tokens to required account/zone resources and permissions, set appropriate expiration and IP restrictions when operationally feasible, separate automation identities, inventory stale credentials, and document rotation/revocation ownership.

Never request or display token or secret values. Do not infer MFA enrollment from unrelated account metadata. Distinguish an API token's configured scope from proof of where it is used. Flag Access Bypass rules because they disable Access enforcement for matching traffic; assess whether a narrower policy or Service Auth is appropriate. Before recommending changes, consider lockout, automation outages, emergency recovery, and staged validation. Read only; credential rotation, revocation, and policy edits require explicit per-action approval.
