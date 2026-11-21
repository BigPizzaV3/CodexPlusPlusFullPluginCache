# Support and incident response

Triage: capture redacted correlation/message ID, UTC timestamp + timezone, iFlow/step, adapter, environment, status, sanitized error excerpt, target response, observed vs expected, first-occurrence frequency, recent deployment and affected volume. Never demand confidential payloads.

Classify error: transport/DNS/TLS, proxy/connectivity, client auth/authorization (401/403), 400 validation or malformed body, 404 endpoint/path, 408/429 throttling, 5xx upstream, XPath/XML namespaces, mapping, Groovy exceptions, asynchronous queue, expired tokens/certs, incompatible API schema, MCP authentication/transport/tool schema failures.

Response format: confirmed observations; ranked hypotheses; exact read-only diagnostics; minimal safe fix; proposed regression tests; monitoring/prevention. Differentiate failure site and response code from root cause. For retries, verify idempotency/duplicate protection and whether business transactions could already have been accepted downstream; approval required for write/replay.

Operational standards: correlation propagation, structured logs without secrets, response codes and latency distributions, alert thresholds, clear ownership, error subprocess, bounded backoff, poison-message containment and safe dead-letter handling. Never claim a live MPL inspection without an actual connected authorized tool.
