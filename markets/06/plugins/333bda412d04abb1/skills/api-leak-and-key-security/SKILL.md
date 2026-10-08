---
name: api-leak-and-key-security
description: Detect API keys, service credentials, tokens, and privileged endpoints leaked to clients or repositories.
---

# API Leak and Key Security

Search source, history, bundles, source maps, logs, error responses, CI output, previews, browser storage, and configuration for secrets. Treat `NEXT_PUBLIC_*`, `VITE_*`, `PUBLIC_*`, client-exposed environment variables, and frontend bundles as public. Never expose Supabase `service_role`, secret keys, database passwords, signing keys, or provider secrets. Report location and rotation need without reproducing values.

Verify server/client boundaries, secret injection, redaction, rotation, least privilege, environment separation, and whether a leaked key remains usable after removal from source.
