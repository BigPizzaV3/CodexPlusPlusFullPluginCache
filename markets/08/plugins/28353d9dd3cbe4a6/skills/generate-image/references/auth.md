# Login and Connection Troubleshooting

This skill is pinned to the single `enkio` MCP server. In Codex, its tool namespace is
**`mcp__enkio`** (Codex normalizes `-` in server names to `_`), and tool names themselves carry no
prefix -- for example `get_user_profile` refers to the tool of that name under the `mcp__enkio` namespace.

## First determine which state you are in

| Symptom | State | Handling |
| --- | --- | --- |
| No `mcp__enkio` namespace in the tool list at all | Server not connected (most often **not logged in**) | Follow "First login" below |
| `mcp__enkio` exists, but calls return 401 / say not logged in | Token expired or revoked | Follow "Log in again" below |
| `mcp__enkio` exists, but calls report connection refused / timeout | Service is not running or address is unreachable | See "Service unreachable" |

> **When not logged in, the entire namespace does not appear at all.** This is the state most easily
> misread as "the plugin isn't installed." Always handle it via "First login" below, and never fall
> back to a different tool as a substitute.

## Absolutely prohibited fallback behavior

When `mcp__enkio` is unavailable:

- **Do not** switch to another brand's MCP (`mcp__selfyz_ai` <-> `mcp__enkio`) just to "get the job
  done." They are different services, different accounts, and different credit pools -- cross-using
  them will really charge the wrong account.
- **Do not** mix a `task_id` / `job_id` / credit balance / artifact URL obtained elsewhere into this
  skill's calls.
- **Do not** fabricate model lists, credit prices, or task states from memory or guesswork.

The correct approach: truthfully tell the user that `enkio` is not connected, complete the login
yourself as described below, then stop and wait until it succeeds.

## First login

**Never ask a non-technical user to open a terminal and type a command.** Instead, run the login
command yourself, using your own shell/tool access:

```bash
codex mcp login enkio
```

This command prints a plain `https://` OAuth authorization URL to stdout (it also tries to auto-open
a local browser). Read that URL out of the command's output and hand it to the user as an ordinary
clickable link, for example:

> [Click here to log in to Enkio](PASTE_THE_HTTPS_URL_PRINTED_BY_THE_COMMAND_HERE)

**Do not lead with the `codex://mcp/login?server=enkio` deep link.** It only works if the client has
registered the `codex://` protocol handler (desktop app / IDE extension); in a plain terminal, a
remote/SSH session, or a browser-based client, clicking it silently does nothing and shows no error.
You may still mention it as a secondary shortcut for technical users, but the reliable path for
everyone else is always: you run the command, you extract the printed URL, the user only ever clicks
a normal https link.

The command keeps running while it waits for the OAuth callback, so start it in the background (or a
mode that lets you keep working) and check back on it rather than blocking on it. If you are on a
headless/remote machine with no local browser, the same printed URL can still be opened manually in a
browser on any other device -- the callback listener is still reachable over the network path Codex set up.

**After login succeeds, the user must open a new Codex conversation and retry.** The MCP tool table
in the current conversation is a snapshot taken when the session started and does not hot-refresh
after a successful login. Even once authorization is complete, `mcp__enkio` will still not appear in
this conversation. Do not keep retrying or switch to another tool in the current conversation --
directly guide the user to open a new conversation instead.

## Log in again

If the namespace already exists but tools report 401 / not logged in, the token is invalid. Run these
yourself (not the user), and relay the resulting login link the same way as in "First login":

```bash
codex mcp logout enkio
codex mcp login enkio
```

A new conversation is again required before retrying.

## Service unreachable

First confirm the plugin and service address:

```bash
codex plugin list           # should show enkio
codex mcp get enkio        # check its url and enabled status
```

This plugin points at the online service, so connection failures are mostly network or proxy issues:

```bash
curl -s -o /dev/null -w '%{http_code}\n' https://enkio-mcp.ufotosoft.com/healthz
```

A `200` response means the service itself is healthy; focus your troubleshooting on local network and
proxy settings instead.

## Confirm the service is correct

After receiving the return value of `get_user_profile()`, cross-check `brand` / `brand_website`
against `mcpServers.enkio.url` in this plugin's `.mcp.json`. If `brand` is not **Enkio**, the
current call has landed on a different service. **Stop immediately and tell the user** -- do not
continue with any credit-charging operation.
