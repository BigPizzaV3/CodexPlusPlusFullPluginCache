---
name: setup
description: Connect Hoot Lens and choose an authorized website to investigate without changing capture settings.
---

# Set up Hoot Lens

1. Connect the packaged `hootlens` MCP server through the host's sign-in flow. The user signs in and chooses sites and permissions. Start with read and replay. Never ask for a pasted token.
2. Call `whoami` and `list_projects`. Confirm the site the user intends. Ask them to choose if several sites could match. If none are reachable, explain the access state without inspecting another account.
3. For an existing site, begin with `review_findings` and one supporting `get_session_narrative`. Cite observed behavior, IDs and sample sizes. A connection does not prove recording works.
4. If the owner requests a new site, use the packaged Hoot Lens workflow. Creation needs explicit `sites:create` approval for all sites, an available slot, a stable retry key, balanced or strict privacy and required visitor consent.
5. Missing permissions require the user's decision to reconnect and approve them. Setup does not automatically change capture, grant visitor consent or authorize writes.
