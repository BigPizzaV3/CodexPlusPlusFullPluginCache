# Isolation and adapters

## Before the first action

Default to an unauthenticated disposable context with inspected, copied resources at a virtual origin. Do not open the live HA origin for the isolated suite. No HA cookies, tokens, ingress sessions, real entity names or personal data are required.

The bundled Browserless template fulfills permitted HTTP requests from supplied bytes or aborts them. It never forwards requests. It also uses CSP, blocks workers/frames/forms, rejects native WebSocket/EventSource/worker creation before app loading, and logs blocked requests. This contains cooperative test code; it is not a sandbox for malicious code. If another transport is needed, model it or mark that path blocked. Never replace a denial with `request.continue()`.

If the permitted browser surface cannot install equivalent interception, use a separate fixture host with enforceable egress denial, or limit execution to proven-contained paths. A page-level stub alone does not prove comprehensive isolation.

Probe fetch, an unexpected GET action endpoint, POST, raw WebSocket, beacon and unsupported transports with inert reserved names. Separate probe attempts from app attempts. Verify probe records and the absence of an upstream-forwarding branch. Do not probe by making and undoing a live HA call.

## Mock HA surfaces

Inspect actual callers. Support explicit contracts and reject unknown ones:

- `hass.callService(domain, service, serviceData, target, ...)`: log service and target; return the installed version's expected shape.
- `hass.callWS(message)`: exact command types with separate read/write classification. A WS command is not inherently read-only.
- `hass.callApi(method, path, data)`: exact method/path match. Do not accept all GETs as harmless.
- `hass.connection.sendMessagePromise`, `subscribeEvents`, and other observed connection methods: explicit mocks with working unsubscribe/disposal.
- Raw fetch/XHR, ingress, todo, calendar, import/download, notification and browser APIs: model separately. No pass-through to original implementations.

Use realistic HA objects: string state, entity ID, attributes, timestamps, context IDs if used, and required locale/user/config fields. Publish fresh top-level and changed-entity identities. Include unavailable, unknown, missing and attribute-only updates. A synchronous setter loop is a burst test, not realistic asynchronous delivery.

Keep the mock store independent of app state. After Save verify submitted payload, store and UI. After Cancel verify store and intent count unchanged. Do not set the same app property subsequently asserted and call it an interaction test.

## Adapter bridge

| `window.__HA_AUDIT` member | Contract |
| --- | --- |
| `ready` | True only after actual target mount and required mock reads |
| `identity` | Observed tag/version and manifest fingerprint |
| `app` | Instance for permitted observation/labeled injection |
| `mock.intents` | Complete request ledger with explicit mutation flag and resolution status |
| `snapshot()` | Serializable route, draft, focus/selection, scroll, timer and store |
| `bump(...)` | Specified HA updates through the real frontend entry point |
| `redraw()` | Optional real redraw entry point; absent means unsupported |
| `settled()` | Optional app completion signal for pending work |
| `dispose()` | Remove owned listeners, subscriptions and timers |

Do not install bridge utilities into production. Missing adapter members are prerequisites to report blocked.

## Fault and data scenarios

Use synthetic data sufficient for branches: empty, one, many, long/Unicode labels, missing optional fields, duplicate labels with unique IDs, long scrollable lists and enough planner alternatives. Date-sensitive journeys need a controlled timezone/clock and a real-time timer smoke test.

Inject failures at the mock transport, not by setting DOM errors: latency, timeout, 401/403/409/429/500, invalid data, disconnect/reconnect, out-of-order reads and late saves. Record sequence/request IDs. Rejected writes must not falsely show success or discard recoverable drafts.

Clone state, not functions or real HA connections. Record synthetic payloads; use explicit allowlists for unavoidable live snapshots. Close only owned sessions. Do not restart shared Browserless after a timeout. Record cleanup failures. A whole live-backup restoration may overwrite unrelated activity.

Keep private manifests, backups and traces outside web-served directories. Public fixtures must contain only synthetic data. Keep reports private unless sharing was requested.

## Bundled starter

Run `scripts/new_audit.py <new-directory> --target <dashboard-name>` from the skill package. Copy all active target resources into that workspace, add their exact virtual mappings to `audit.json`, and implement `adapter.js` and `suite.js`. Load resources in the observed order. Add actual target resource paths to `sourcePaths`, provide `expectedTag` and source evidence, then set source verification and adapter configuration only after inspection. The starter refuses to build while unconfigured.

Run `scripts/build_payload.py <workspace>` to produce `payload.json`. Submit that JSON only through an available, authorized Browserless Function interface. Discover the local endpoint/version; the builder intentionally supplies no endpoint or authentication. Review payload size against provider limits. Binary assets are not handled by this text-resource starter; copy/encode them with an explicitly reviewed extension or report the gap. HTTP API simulation can be implemented inside the adapter using exact mock contracts; the static transport map does not pretend to be a generic dynamic backend.

The runner adds six explicit foundation gates to the user plan. Its default pass budget is configurable and its maximum helper budget is 55 seconds; this is a helper limit, not a Browserless/platform guarantee. It creates and closes its own context, and never closes the supplied shared page or entire browser.
