---
name: connection-permissions
description: Diagnose TrekMail OAuth connection, permissions, membership and feature availability without exposing secrets.
---

Use get_connection_permissions to inspect the current allowed capability set and constraints. Use get_account or drive_addon_get for applicable entitlement status. Visible tools are an intersection of selected tool families, scopes, current plan, membership and the domains the connection reaches; a selected family alone does not grant access. Full platform management uses the account's granted permissions, not a fixed small tool count.

When access is refused, distinguish an expired/revoked connection, missing scope, missing entitlement and an inaccessible resource. A host OAuth challenge may offer reconnection. Request only the permissions needed for the user's intended work and honor their refusal. Never work around a restriction using another account, arbitrary HTTP calls, pasted access tokens or a more privileged API key. Do not claim success for isError, requires_user_action or queued delivery.

For credential setup follow the authenticated TrekMail URL returned by the dedicated tool. Passwords, API keys and OAuth tokens are never collected in conversation. Changes to the connected grant may require reinitializing the MCP session. Reconnect or reinitialize using the host controls; do not ask the user to paste a token.

Do not call get_connection_permissions or get_account for a request that only needs domain names, a specific message or file. Routine account information is capabilities and limits, not the owner’s personal profile. Return only the requested fields in the final answer; do not echo resource IDs or delivery handles unless needed by the request.
