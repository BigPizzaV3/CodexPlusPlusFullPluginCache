# Connection behaviour evaluations

Run these in the intended host against this exact saved release. Static package checks are not live behavioural results. Use a dedicated sample-data organisation for authenticated checks; no record writes are needed.

| Case | Setup and action | Expected result |
| --- | --- | --- |
| Existing link | Fresh chat, valid authorised connection, Begin an 8D report | One authenticated read, connected-read, original task continues; no chooser or login. |
| No link | Fresh chat, no MCP tools/host link, Start process mapping | Exact question and two labels from modes.md; no fake connection or task reset. |
| Connect choice | Choose Get me connected | Actual host linking, provider credentials/consent, tools rediscovered, authenticated read before success. |
| Standalone choice | Choose Operate in standalone mode | Continue original task; no further Doctilla calls, signup, download or repeated prompt. |
| Explicit standalone | Valid link exists, initial request says standalone | No protected probe, chooser or live context; full standalone assistance. |
| Explicit connect | Initial request asks to connect | Skip redundant chooser; run linking/read verification. |
| Direct skill | Invoke car-8d, internal-audit or process-mapping directly | Same startup routine before its workflow; shared mode remembered. |
| Repeat in one chat | Switch from 8D to audit | No repeated setup or redundant connection probe. |
| New chat | Previous chat used standalone | Check new chat independently; no fabricated persistent choice. |
| Expired token | Read returns 401 | One supported reconnect when requested; authenticated read verifies recovery, task retained. |
| Refused access | Read returns 403 | Explain permissions/entitlements; no repeated login, REST fallback or broader access. |
| Cancellation | Cancel linking | Preserve useful standalone draft as unsaved; no login loop. |
| False success | User says connected but tools absent | No success claim; diagnose missing host wiring, retain task. |
| Public health only | Public endpoint/descriptor succeeds | Do not treat as authenticated record access. |
| Read-only account | Authenticated read succeeds, write unavailable | Connected-read remains useful; do not demand write access or make a test write. |
| Standalone then connect | Create a draft standalone, later link | Preserve draft; no automatic upload; exact approved save plan required. |
| Fresh installation | Install, run setup, choose connection | Remote server registered, OAuth completes, MCP tools exposed, authorised read succeeds. |
| Install without linking | Install, choose standalone | Skills usable without protected calls. If host blocks them, record installation blocker. |
| Token refresh | Let access token expire in a test account | Host refreshes or offers supported reauthorisation; subsequent authorised read succeeds. |
| Unsupported buttons | Host cannot render question widget | Same exact question and two numbered labels, accepting text; do not claim clickable buttons. |

Record host/version, release ID, time, actual tools, redacted result/error, observed outcome and pass/fail/pending. Never record tokens, passwords or authorisation codes.

## Authoring checks, 22 October 2026

After the server operator removed the Cloudflare Browser Integrity Check from the MCP subdomain, Python urllib retrieved protected-resource and authorisation metadata with HTTP 200. Unauthenticated initialize returned HTTP 401 and the expected protected-resource challenge. DCR, CIMD, S256, refresh_token and Doctilla scopes were advertised. No authenticated MCP tools were exposed in this rebuild chat. Fresh installation, selectable widget rendering, OAuth callback, authorised read, cancellation, standalone without linking and token refresh remain pending tests of the exact public host release. Historical 20 October results (five live record cases and three conversational policy checks) are retained as dated evidence, not rerun results for this release.


## Static design review requirements

Review authentication-design.md against current server source before declaring end-to-end implementation complete. Confirm per-tool securitySchemes, MCP authentication challenges, authenticated profile metadata, provider login continuation, refresh handling and the distribution-specific registered MCP integration. No new runtime tests were performed for the 3.0.8 design review.

## Non-technical customer scenarios (requirements; not run)

- No sign-in card: give a direct link to the existing plugin and conditional ordinary sign-in steps; do not assume a button exists.
- No connection option: explain owner/administrator action, supply a copyable support note, preserve standalone work; no custom-server setup instructions.
- Connected label but no chat access: at most one fresh-chat recovery with @DoctillaQM and an explicit continuation message; no claim that an unsaved draft transfers automatically.
- Non-technical user asks "what do I click?": one concrete next action grounded in known labels; no MCP/OAuth/client-ID explanation.
- User says "I've signed in": verify internally before confirming access, then continue the original quality task.
- User cannot connect: no credential collection, blame, repeated mode questions or indefinite sign-in retries.
