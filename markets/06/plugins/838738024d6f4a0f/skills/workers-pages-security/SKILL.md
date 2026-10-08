---
name: workers-pages-security
description: Review Cloudflare Workers and Pages code, bindings, routes, previews, and application security boundaries.
---

# Workers and Pages Security

Inspect Worker/Pages source, Wrangler configuration, routes, bindings, environment separation, preview deployments, and request/response handling. Trace authentication before sensitive operations and enforce authorization at every object, tenant, and function boundary. Validate and bound untrusted input; assess SSRF, injection, path traversal, unsafe redirects, mass assignment, resource exhaustion, and error disclosure where applicable. Review binding capabilities as permissions and limit each Worker to the resources it needs. Prefer private service bindings for internal Worker communication when appropriate, while independently authenticating downstream operations: Access context does not automatically propagate through service bindings.

Check whether Pages previews expose non-production data or credentials; preview URLs are public by default unless protected. Review routes/custom hostnames and ensure staging is isolated. Report code-level evidence and distinguish static concerns from runtime-verified vulnerabilities. Do not deploy or modify production settings without explicit approval.
