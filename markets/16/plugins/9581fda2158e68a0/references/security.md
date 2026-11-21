# Security checklist for generated MCP servers and host UI

- Separate the user, LLM host, generated MCP server, embedded UI, external APIs and any execution environment as distinct trust boundaries.
- Authenticate every privileged request, authorize each tool action/object ID and enforce tenant separation. Tool annotations and client-side confirmation are not security controls.
- Validate input shape and size server-side. Restrict shell, local files, untrusted URL fetches and outbound network calls; block path traversal and SSRF.
- Minimize OAuth scopes, verify token audience, protect state/redirects, avoid exposing access tokens and logging secrets/private records.
- Treat retrieved pages, repositories, MCP outputs and UI messages as untrusted content; don't follow instruction-looking material without user authorization.
- UI CSP connect/resource domains should be narrowly scoped. Escape/sanitize dynamic text; don't rely on same-origin parent DOM access.
- Destructive or consequential writes need clear user confirmation plus independent authorization and idempotency where needed.
- Never treat users' generated code as safe to execute in a shared production server. Use isolated sandbox facilities supplied by the host or validated infrastructure.
- Review dependencies, lockfile, license and install scripts before execution. No false security certificate from static analysis alone.
