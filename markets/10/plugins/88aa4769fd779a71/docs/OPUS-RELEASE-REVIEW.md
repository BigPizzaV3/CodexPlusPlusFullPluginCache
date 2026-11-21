# Opus release review

Independent reviewer: claude-opus-5, first-party provider, max effort. Completed October 4, 2026. This review covers the public hosting delta, not directory approval.

## HOSTING GO

No high-severity, exploitable runtime or security defect found in this delta. Host/Origin gating, the exact-match static routes, the 32 KB streaming cap, stateless per-request transport teardown, and the HTTPS-origin validators all hold up under review. Shipping is not blocked. Four concrete non-blocking findings follow.

---

**1. MEDIUM : `src/http.mjs:61` (`if (path === '/' || path === '/health' || path === '/mcp')`)**
*Trigger:* any `POST /mcp`. Every tool call synchronously `readFileSync`s and regex-scans the entire self-contained calculator HTML, then discards it : `html` is never read on the `/mcp` branch. Two effects: blocking event-loop work on every invocation under Fluid concurrency, and a truncated/missing build hard-fails `calculate_concentration` with 503 even though that tool needs no HTML.
*Fix:* drop `'/mcp'` from the condition (keep `/health` as the readiness probe), or cache the validated string and revalidate on `mtimeMs`.

**2. MEDIUM : `src/http.mjs:29` and `:36` (`localHosts`, `allowedOrigins`)**
*Trigger:* the guard at `src/http.mjs:120` permits `BIND_ADDRESS=0.0.0.0` when `PUBLIC_BASE_URL` is set. The loopback allowlist entries are keyed only on `req.socket.localPort`, never on peer address, so any LAN client can send `Host: localhost:4317` (and matching `Origin`) and pass both checks. No privilege is gained today : the service is anonymous, stateless, and has no auth or user data : which is why this is not a blocker.
*Fix:* add `localHosts` only when `req.socket.remoteAddress` is loopback.

**3. LOW/MEDIUM : `src/http.mjs:96` (`new StreamableHTTPServerTransport({ sessionIdGenerator: undefined })`)**
*Trigger:* `GET /mcp` with `Accept: text/event-stream`. Stateless mode passes the SDK's session validation, so the request reaches the SSE path and holds an open response plus a fresh `McpServer` until `server.setTimeout(20000)` destroys the socket. Bounded by that timeout and `maxDuration: 30`, but it consumes a concurrency slot for no protocol benefit (stateless mode sends no server-initiated messages).
*Fix:* return `405 Allow: POST, DELETE, OPTIONS` for `GET /mcp` before constructing the transport.

**4. LOW : `src/mcp-server.mjs:18` (`_meta.ui.domain`)**
*Trigger:* widget loaded from a preview or branch deployment. `domain` is hardcoded to `https://peptara-calculator.vercel.app` while `server.mjs:28` also admits `VERCEL_URL` / `VERCEL_BRANCH_URL` origins, so the declared domain won't match the serving origin on previews.
*Fix:* derive it from the same resolved origin, falling back to the canonical value.

---

**Residual live-check limits.** The 8 live checks cover the canonical production origin only. Unverified: Host acceptance on preview/branch URLs; `/privacy` and `/support` served from the standalone bundle on a cold start; both branches of `/.well-known/openai-apps-challenge`; and behavior under concurrent invocations sharing one instance, which is where finding 1 would actually bite. `HEAD /` returns 404 : confirm no uptime monitor depends on it.

## Release reconciliation

Ken explicitly waived the GLM audit for this release. Opus is the independent release gate; its verdict is HOSTING GO. No blocker or high-severity finding remains to reproduce.

- The repeated synchronous UI read and broad loopback-host allowance are present in the reviewed code. They are accepted non-blocking limitations for this anonymous, stateless calculator, with request-body and socket-time limits in place. No remediation is claimed.
- A hosted `GET /mcp` probe with `Accept: text/event-stream` returned HTTP 200 and no body before the client's 3-second timeout. This supports the open-stream observation. That probe does not independently verify the server's configured 20-second closure.
- The UI domain remains the stable canonical calculator domain. Preview embedding has not been verified. The configured preview host allowlist is not evidence that an embedded preview works.
- Separate checks verified both domain-challenge branches locally and static pages from a materialized standalone Vercel bundle. Production domain ownership and production ChatGPT integration remain unverified.

These notes do not claim load testing, directory eligibility, publisher verification, or OpenAI approval.
