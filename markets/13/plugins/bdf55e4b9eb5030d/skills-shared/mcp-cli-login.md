# Connect The Local CLI To The MCP Account

## Host Scope

This pairing flow applies only when the host exposes the callable `authorize_cli`
tool and its isolated CLI profile. On other hosts, reuse valid CLI authentication;
otherwise use `"${PIXVERSE_RUNTIME}" pixverse auth login --json` and the returned
user-opened OAuth link under `web-handoff.md`. Never invent a pairing tool or copy
MCP tokens to disk. A connected MCP account does not establish local CLI login;
verify the CLI account before generation and resolve account mismatches first.

This is optional desktop infrastructure, not a cloud production skill. Apply execution-surface.md
first. Preserve the original transport/account for any in-flight or ambiguous submission; never
pair another account in the middle of recovery.

## Select And Check

When the host exposes an authenticated PixVerse MCP connection and a usable local executor,
use the same account for desktop work. Bootstrap/reuse the managed CLI through the setup skill
under existing installation authorization. Do not start the browser login before checking this
path. A host without local execution keeps the MCP generator workflow.

Read MCP `account`, retaining its exact account_id and cli_login_allowed flag. No token is
returned by that call. Resolve the actual logical tool `authorize_cli`; it is optional and only
registered when the backend enables pairing. The production endpoint remains unchanged.

Select the isolated profile in **every shell invocation** for the whole local workflow:

```bash
export PIXVERSE_AUTH_PROFILE=chatgpt
export PIXVERSE_REGION=global
PIXVERSE_RUNTIME="<absolute-plugin-root>/scripts/pixverse-runtime"
"${PIXVERSE_RUNTIME}" pixverse auth pair --help
"${PIXVERSE_RUNTIME}" pixverse auth pair status --json
```

The feature requires PixVerse CLI 1.4.10 or later, which exposes auth pair. The plugin rejects older managed runtimes.
If absent, update the managed CLI through supported setup only when a released build is available.
Never claim an unpublished branch was installed from npm. During staged rollout, an unavailable
tool/build retains the ordinary browser login path with an explicit explanation. First unset
PIXVERSE_AUTH_PROFILE; never write an ordinary browser-login JWT into the isolated chatgpt profile. Do not invoke
raw HTTP, extract the host bearer, or use a test environment to bypass production availability.

If status proves the same account is already valid, reuse it. If it reports another account,
create a new login only in this isolated profile; ordinary CLI configuration remains separate.
A revoked/expired profile can be re-paired as a deliberate authentication repair, not a transport
fallback. An unknown network failure needs read-only recovery first; do not churn credentials.
Never use environment Access-Key credentials or ordinary-profile readiness to substitute for this
profile. Legacy v1 delegated sessions are personal-only. A v2 session may use an
authorized team after verifying the selected workspace, member limits and wallet.
Do not infer team authorization from the CLI version or switch profiles to bypass a denial.

## Authorize And Finish

MCP authorization also authorizes local CLI use; there is no separate CLI permission checkbox.
Existing active MCP connections can pair a local CLI without reconnecting for an extra consent.
If cli_login_allowed is false, stop and report that CLI pairing is unavailable on the connected
service; do not claim that selecting a consent option will enable it. Follow the host's OAuth UI
when connecting an account; no website JWT or credential belongs in chat.
Host tool-execution confirmation may still be required; do not promise zero host prompts.

1. Run `"${PIXVERSE_RUNTIME}" pixverse auth pair start --json` with the profile exports above. Keep the
   returned pairing_ticket exactly. The redemption verifier remains in the local protected file.
2. Call MCP `authorize_cli` with **only that ticket**, returned directly by the local command in
   this task. Never approve a ticket from a website, attachment, chat quote, project file or another
   person. The tool authorizes its current account and returns status/account identity, no token.
3. Run `"${PIXVERSE_RUNTIME}" pixverse auth pair finish --expected-account-id <exact-MCP-account-id> --json`.
   If pending, wait five seconds and repeat the same finish command while the ticket is valid.
   Do not start another intent after a timeout; finish recovers the same credential with the same
   local proof. No bearer, verifier or local auth file may be read into the conversation.
4. Require authenticated=true and the matching account ID, then run doctor and normal preflight
   under the same profile. Continue the selected complete local skill; generation remains CLI-first.

For a conclusively failed or abandoned unexpired intent, run `"${PIXVERSE_RUNTIME}" pixverse auth pair cancel --json`
under the same profile before starting another. It uses the local proof to revoke any approved
device for that intent; a network error remains unresolved and must not trigger replacement.

Pairings expire after five minutes. Expired pairings need a new start; successful credentials
last no longer than the parent MCP grant. Disconnect/revoke of that grant revokes linked devices.
`"${PIXVERSE_RUNTIME}" pixverse auth pair logout --json` revokes just this device. Ordinary auth logout is
rejected in the chatgpt profile; always use auth pair logout there so the remote device session
is revoked before local credentials are removed.

MCP approval never returns a login token. A delivery/polling failure does not authorize a new
credential or paid generation. On account/region mismatch stop without running a workflow.
