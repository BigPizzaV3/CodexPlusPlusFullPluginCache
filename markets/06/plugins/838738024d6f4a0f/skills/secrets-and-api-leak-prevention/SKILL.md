---
name: secrets-and-api-leak-prevention
description: Detect unsafe secret storage, credential leakage, overprivileged API use, and sensitive-data logging.
---

# Secrets and API Leak Prevention

Review tracked source and configuration for hard-coded credentials, tokens in client bundles, committed `.env`/`.dev.vars` files, secrets in build artifacts, unsafe CI variables, verbose request/exception logs, and credentials embedded in URLs. Prefer Worker secret bindings/Secrets Store for sensitive values, bindings for Cloudflare resources when suitable, and narrow short-lived credentials for external APIs.

Never print detected secret values. Identify only secret type, file/location, exposure channel, and a safely redacted fingerprint if essential. If a live credential may have escaped, recommend immediate owner-led revocation/rotation, scope review, audit-log review, and redeployment; do not attempt rotation. Inspect outbound API use for audience/scope validation, authorization checks, rate limits, timeout/retry bounds, and SSRF risks. Do not claim a scan proves no secrets exist; report scan scope and exclusions.
