---
name: captino-setup
description: Set up or troubleshoot the Captino MCP connection in Codex or ChatGPT - sign in to Captino with OAuth, choose which permissions to grant, re-authenticate after a revoke or expiry, check which tools the connection has, and fix 401, 403, "Not logged in", missing tools or connection errors. Use when Captino tools are unavailable or failing, or when the user asks how to connect Codex or ChatGPT to Captino.
---

# Captino setup

The Captino MCP server is `https://api.captino.io/mcp` (streamable HTTP). It
uses OAuth: the client finds the Captino sign-in from the server, registers
itself and stores and refreshes the tokens, so there is nothing to configure
in Codex or in ChatGPT. The plugin's `mcp.json` declares only the server's type
and URL.

The connection acts as the Captino user who approved it, in that user's
account. Access tokens last an hour and refresh on their own. The refresh token
lasts 30 days and is renewed each time it is used, so only a connection left
unused for 30 days has to sign in again.

## Permissions

When connecting, the user signs in on captino.io and sees a consent screen
listing these resources. They tick the ones the app may use. Write access
implies read.

| Resource | Access levels | OAuth scopes | Unlocks |
| :-- | :-- | :-- | :-- |
| Funnel | read, write | `funnel:read`, `funnel:write` | `list_funnels`, `get_funnel`, `list_funnel_steps`, `get_page_builder_reference`, `get_page_project`, `validate_page_project`; write adds `create_funnel`, `update_funnel`, `set_funnel_active`, `create_funnel_step`, `set_funnel_step_visibility`, `set_funnel_step_form`, `set_form_step_completion`, `delete_funnel`, `save_page_project`, `publish_page` |
| Contact | read, write | `contact:read`, `contact:write` | `list_contacts`, `list_leads`, `get_contact`, `get_contact_activity`, `list_contact_opt_ins`, `get_contact_pipeline_stats`, `get_contact_options`; write adds `update_contact`, `create_contact_meeting` |
| Performance | read | `performance:read` | `list_funnel_performance`, `get_funnel_performance`, `compare_funnel_performance_with_previous_period`, `get_funnel_step_performance`, `get_funnel_conversion_stats`, `get_form_step_performance`, `compare_funnels` |
| Subscription | read | `subscription:read` | `get_subscription`, `get_subscription_usage` |
| Form | read, write | `form:read`, `form:write` | `list_forms`, `get_form`, `list_form_responses`, `get_form_performance`; write adds `create_form`, `update_form`, `publish_form`, `delete_form` |

The server only lists the tools the granted permissions allow, so a missing
tool almost always means a box that was not ticked.

Recommended grants for the skills in this plugin: Funnel write, Contact write,
Form write, Performance read, Subscription read. Funnel read is enough if the
user will not build pages or change funnels; Form is only needed for forms.

## Connect from Codex

The plugin bundles the server as `captino`. It works in Codex CLI and in Codex
in the ChatGPT desktop app.

1. Install Captino from `/plugins`. Codex asks to authenticate the Captino
   server during install; continue.
2. If that was skipped, or to sign in again later, run:

   ```bash
   codex mcp login captino
   ```

   A browser opens on captino.io. Sign in, tick the permissions and approve.
   On a machine without a browser, add `--no-browser`: Codex prints the URL
   and asks for the callback URL. In the desktop app, choose **Authenticate**
   when the server asks for sign-in.
3. Start a new session. `/mcp` lists the `captino` server and its tools, and
   `codex mcp list` shows `OAuth` in the Auth column.

No config flag is needed for OAuth in current Codex versions. Tokens go to the
OS credential store, or a file under `~/.codex` when none is available.
`codex mcp logout captino` deletes them.

Without the plugin (for example in the IDE extension, which does not load
plugins), add the server by hand and sign in:

```bash
codex mcp add captino --url https://api.captino.io/mcp
codex mcp login captino
```

Do not do both: the plugin's server and a hand-added one with the same URL
list the tools twice.

## Connect from ChatGPT

1. Open **Plugins** in ChatGPT and install Captino.
2. When ChatGPT asks to connect Captino, continue. It opens captino.io; sign
   in, tick the permissions and approve.
3. Start a new chat and use Captino.

Without the plugin, the server can be added directly: **Plugins** → **+** →
**Add custom MCP server**, URL `https://api.captino.io/mcp`, authentication
OAuth. The account or workspace settings decide whether custom MCP servers are
allowed.

## Change permissions or disconnect

Connected apps are listed in Captino under **Settings → MCP**
(`/app/mcp-settings`), where the user can revoke one. Permissions cannot be
edited on an existing connection. To grant more or fewer, connect again and
tick different boxes:

- Codex: `codex mcp logout captino`, then `codex mcp login captino`.
- ChatGPT: disconnect Captino in **Plugins**, then connect it again.

Revoke the old entry under Connected apps if it is still listed.

## Troubleshooting

Match the symptom, then do the fix. Do not retry a failing call against a
different URL or with a token from somewhere else.

| Symptom | Cause | Fix |
| :-- | :-- | :-- |
| No `captino` tools at all | Plugin not installed or enabled, no new session since installing, or the plugin's server turned off by `enabled = false` under `[plugins."captino".mcp_servers.captino]` in `~/.codex/config.toml` | Install from the marketplace, check `/plugins`, remove that block, start a new session |
| `401`, or `Not logged in` in `codex mcp list` | Not signed in yet, the app was revoked under Connected apps, or the refresh token expired after 30 days unused | Codex: `codex mcp login captino`. ChatGPT: connect Captino again |
| `401` that persists after signing in, `Bearer token` in `codex mcp list` | A `bearer_token_env_var` or `Authorization` header set for `captino` in `~/.codex/config.toml` takes precedence over OAuth | Remove it from `[mcp_servers.captino]`, restart Codex, run `codex mcp login captino` |
| Tools listed twice | The plugin's server plus a hand-added `[mcp_servers.captino]` | Remove the hand-added block |
| Token refresh fails and signing in again is refused | The Captino user who approved the app, or the account, is deactivated | Ask a Captino admin to reactivate it, or connect as an active user |
| Some tools missing, others work | That resource was not ticked on the consent screen | Connect again and tick it (see Change permissions) |
| `403` on a tool call | Same as above, for a permission the call needs | Connect again and grant it |
| Connection refused or timeout | Network, VPN or proxy blocks `api.captino.io`, or the API is down | `curl -sI https://api.captino.io/mcp` (a 401 is the healthy answer without a sign-in); fix the network |
| `404 ... not found` on a specific id | The GUID belongs to another account or was deleted | Look the item up again with `list_funnels` or `list_contacts` |
| Contacts missing from lists, `hiddenContacts > 0` | Subscription contact limit reached | Not an auth issue. Upgrade the plan in Captino |

## Verify

After connecting, call `get_subscription` (or `list_funnels` if Subscription
is not granted). A successful answer confirms the sign-in, the account and the
permissions in one go. Report which resources were granted based on which
tools are listed.
