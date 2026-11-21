---
name: connect
description: Help the user connect VOY and understand the permissions needed for their requested taste, review, list or plan task.
---

Use the host's connection flow for the packaged VOY MCP server. Authentication
and account creation take place on VOY, not in this conversation. Never request
passwords, email verification codes, access tokens or API keys in chat.

If already connected, use only tools actually available with the granted scopes.
When Stay connected is approved using current consent, VOY can renew access
automatically while active, with up to 90 days between renewals. Access tokens
still last five minutes; this is not a five-minute human reconnection requirement.
Older grants keep their original expiry. The host may disconnect sooner, and
extra permissions always require new consent.
Ask for the narrow permissions needed for the user's task. Friendship permission
is separate from taste and review access. Date is not part of this release.

Explain a limitation when access or coverage is missing; do not imply that
installation grants all permissions. Users can manage or revoke their connection
in VOY settings. OAuth consent does not approve a later action.
