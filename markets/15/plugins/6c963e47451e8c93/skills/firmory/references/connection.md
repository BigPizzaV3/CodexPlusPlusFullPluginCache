# Connect and reauthorize Firmory

Use this reference for missing authorization, an explicit connection request, a website connection check, or a team change. Keep the original task pending and resume it after verification. Connected starter questions run directly; there is no standalone setup skill.

## Identify the connection

Discover tools on this plugin's `firmory_cloud` connection and use their actual schemas. Call `workspace({})` to verify the authorized team. A missing tool requires discovery or refresh when available; it does not prove that credentials expired.

For missing or expired authorization, use the host's Firmory Connect or Sign in action. Let the user authenticate, choose a team, and consent in the browser. Do not request credentials, copy tokens, fabricate callback URLs, or substitute a generic website sign-in page. A direct CLI login does not reconnect the hosted ChatGPT plugin.

Check `isError` before interpreting workspace results. Verify access after authorization, then resume the original read-only task without requiring the user to repeat it or say "Connected". If the host requires a new turn, explain that limitation. For a connection-only request, show the verified team and accessible projects; for verification-only requests, omit unrelated browsing. Report partial listings honestly.

A permission error or outage is not a reason to loop through sign-in. Stop on declined authorization.

## Change the authorized team

Team changes require new consent on the existing connection. Project changes within that team do not.

1. Read `workspace` and identify the current team. If it already matches the requested team and the user did not explicitly request reauthorization, continue without another prompt.
2. Discover `request_team_authorization`. Do not use obsolete `list_teams`, `get_current_team`, or `switch_team` tools from stale metadata. Team selection happens on the consent page.
3. Check any explicitly reported host policy. In Codex desktop, `approval_policy=never` blocks native OAuth prompts even when authorization elicitation is enabled. When this policy is confirmed, ask the user to select **Default permissions** instead of **Full access**, verify the effective policy changed, and then proceed. Do not infer the policy merely from a missing prompt, edit permission files, or bypass security controls.
4. For the hosted Firmory plugin, call `request_team_authorization` once with `currentTeamId` from `workspace`. Use the host's native reauthorization action for the existing account and connection. The user chooses the intended team and approves access. Do not add an account, send a settings link, or render a custom card. The optional legacy `authorize` argument is not a second user step.
5. An auth-required response does not prove that an entry appeared or a browser opened. If the host shows no action, report that authorization has not started and stop retrying. Preserve the current connection; do not revoke credentials or uninstall the plugin to force a prompt.
6. After consent, read `workspace` on the same connection and confirm the intended team. Refresh available tools if supported. If the old team remains, report it without automatically restarting authorization. Discard the previous team's node IDs and cursors only after a verified switch.
7. Resume the original task in the verified team. If the user only requested a team change, report the verified team briefly. Cancellation preserves the original connection.

For directly configured Claude Code MCP connections, use the existing Firmory connection in `/mcp`. For a directly configured Codex CLI server, use the fallback below. Neither changes the hosted ChatGPT connection.

## Verify a connection requested by the Firmory website

Only when the user supplies a Firmory connection challenge, complete the normal authorization/workspace check and call this connection's `verify_connection` with the supplied `challenge`. Do not generate, alter, echo, or send the challenge to another connection.

A successful response with `connectionCheck.status: "verified"` confirms the website check. Report its returned team and project when present, then continue the original task. Workspace access alone does not complete this check. An expired challenge requires a new website check; a permission or team mismatch requires the intended connection, not repeated login attempts. Report unavailable tools or errors without claiming verification succeeded.

## Direct Codex CLI fallback

Use this only for a directly configured CLI MCP server with terminal support. Prefer `codex` on PATH; otherwise check the current macOS app executable at `/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex`. Older installations may use `/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex`. Use a path only after confirming it exists.

```sh
codex -c 'mcp_servers.firmory_cloud.url="https://firmory.ai/mcp"' mcp login firmory_cloud --scopes user:org:read --oauth-client-registration cimd
```

This temporary URL override avoids a second persistent server entry. Let the CLI generate the OAuth flow, open the browser, and store credentials. Keep the process alive while the user consents; do not start overlapping attempts or retry a decline. On timeout, report that the attempt expired before offering a new one.

A zero exit status confirms authorization, not workspace access. Reload the host's MCP connection when supported and verify `workspace` before continuing. If tools remain unavailable, report the loading error without sending the user through login again. Never read credential files, copy tokens, construct callback URLs, or substitute another provider's CLI.
