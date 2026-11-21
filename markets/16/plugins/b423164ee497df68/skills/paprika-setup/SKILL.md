---
name: paprika-setup
description: Connect or reconnect the Paprika plugin using the client's native OAuth flow, discover its read tools, and verify fleet access. Use only when the user asks to set up Paprika, sign in, or change granted scopes.
---

# Connect Paprika

Use the user-selected Paprika instance and its configured HTTPS `/mcp` endpoint.
The review example is `https://paprika-demo.benebsworth.com/mcp`; users select
their own deployment during setup. Do not treat the example as their fleet.
If Paprika tools are already available, call `fleet_status` once to verify
access. If authentication is required, open the client's native MCP OAuth
connection flow and let the user sign in and grant scopes there. Do not ask for
pasted credentials, bearer tokens, kubeconfigs, or secrets; do not store them
in the package or chat.

Start with `paprika:read` for fleet/application inspection. Add `paprika:write`
only when the user wants delivery actions. Scope grants and Paprika's RBAC are
both required; write access does not imply read access.

For the Codex CLI, add the selected HTTPS endpoint with `codex mcp add`
under a distinct connection name, then use `codex mcp login` with
`--scopes paprika:read`. Obtain the endpoint from the user’s existing
configuration or their explicit choice; never substitute another instance.

For a user-requested write connection, use the native consent flow with both
scopes (or `codex mcp login paprika_hosted --scopes paprika:read,paprika:write`).
In desktop clients use their MCP/plugin connection UI. If plugin installation
or reloading is needed, follow the host's supported flow; adding a raw MCP
endpoint alone may not load these packaged skills or an interactive view.

After connection, discover tools and call `fleet_status` once. Report the
returned fleet data or the actual error. Offer `open_fleet` when available in
a host supporting MCP Apps. If the deployed server lacks the new tools or the
host lacks Extensions support, retain normal read tools and state what remains
unverified. Editing this source package does not update the remote deployment.

## Connection diagnostics

Installation, account-owned cloud registration, OAuth, callable tools and a successful API read are separate checks. Verify the intended host account through supported native identity UI; a service email may differ. A connected computer or local CLI does not prove cloud access. If authoritative host evidence confirms a mismatched registration, say "This MCP was registered for another account. Connect it in this account." Otherwise mark account binding unverified; missing tools alone are not proof of expired credentials. When the user requests a new or renewed connection, use native OAuth with the requested permissions, then verify an actual read in the intended cloud chat. A 403 is a denied operation; do not expand scopes or create credentials to repair it. Do not extract tokens, copy another account’s App ID, broaden grants, or enable tracing to test setup.
