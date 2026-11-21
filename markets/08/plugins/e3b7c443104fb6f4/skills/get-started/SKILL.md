---
name: get-started
description: Onboard users to lit.onl MCP — connect OAuth, Growth+ workspace, and common short-link / document tasks.
---

# lit.onl MCP — get started

## When to use

The user installs the lit.onl plugin, asks how to connect, or wants a first short link / document action.

## Instructions

1. Confirm the user completed **Connect / Authenticate** (OAuth to litonl.com). Tools need a Growth or Premium workspace.
2. Prefer MCP tools over inventing URLs. Do not ask for or log client secrets or access tokens.
3. First useful actions:
   - Shorten a URL with `create_link` (slug, expiry, UTM as requested).
   - `list_links` to show existing short links.
   - `get_documents_quota` if they ask about document sharing limits.
4. Clarify deactivate vs delete: `deactivate_link` turns a link off; `delete_link` permanently removes it and click history.
5. Redirect rules / RediRL use `links:read` / `links:write` tools (`list_redirect_rules`, `create_redirect_rule`, or link fields `redirl` / `redirect_rule_set_id`).
6. If the org is Free or Core, explain they need Growth+ and point to https://litonl.com pricing / docs.
7. Docs: https://litonl.com/docs/ai
