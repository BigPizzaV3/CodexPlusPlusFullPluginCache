---
name: setup
description: Connect the Casually directory integration through native OAuth and check access with read-only project tools.
---

# Connect Casually

Use the client's native Connect or Authenticate action for the installed Casually plugin. The directory endpoint is `https://api.casually.marketing/api/v2/mcp/directory`. Sign-in and consent happen on Casually's browser page. Never request credentials, tokens or OAuth callback URLs in conversation.

After connection, read the available Casually tool definitions and call `list_creative_projects` to check access. Connection checks must not create drafts, spend credits, submit forms, request review or send email.

This edition supports project preparation, LP/email drafts, existing media, human review and reports. It does not expose AI image/video/audio generation, generic API execution, self-approval or purchases. Do not register the broader legacy endpoint or use another connector to bypass these limits.

For expired/revoked access, reconnect through native OAuth. The user can revoke grants in Casually's /dashboard/plugins connection guide. Report permission/plan/setup failures as returned; do not claim successful authentication based only on a preview page or tool listing.

Use only the brief and selected resources required for the user's task. Do not request full conversation history or inspect unrelated local files.
