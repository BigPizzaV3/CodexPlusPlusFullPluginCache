# MCP fault isolation

| Symptom | Investigate | Evidence |
|---|---|---|
| initialize fails | SDK version, transport, stdout contamination (stdio), HTTP headers/session | startup logs + client handshake |
| tools/list empty | registration timing, server instance, client permission filtering | discovered server capabilities + raw tools/list |
| tools/call fails | schema/required fields, exceptions, provider timeout, auth scope | input, error code, test |
| UI not rendering | host support, `_meta.ui.resourceUri`, resource registration/read, MIME type | tools/list metadata, resources/read output |
| UI renders but events fail | bridge handshake, tool visibility, server auth, lifecycle | UI console + server call trace |
| works locally, fails remote | TLS, reverse proxy, CORS/origin, OAuth discovery/audience, timeouts | endpoint response + authenticated request |
| client regression | changed tool schema/name, transport/protocol mismatch | before/after contract diff |

Do not guess fixes from a screenshot alone when logs/tests are available. Keep user secrets out of evidence.
