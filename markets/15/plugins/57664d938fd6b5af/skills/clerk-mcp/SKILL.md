---
name: clerk-mcp
description: Use for Clerk SDK guidance or to manage applications, users, organizations, domains, billing, and instance configuration in a connected Clerk workspace through the Clerk MCP server.
---

# Clerk MCP

Use the bundled `clerk` MCP server for Clerk implementation guidance and connected workspace operations. Check the available tool list because authenticated tools depend on the connection and granted scopes.

For implementation guidance, use the public tools for:

- Adding Clerk authentication to a frontend or backend app.
- Choosing or applying Clerk SDK hooks, helpers, or components.
- Implementing B2B SaaS organization flows, organization switching, role checks, or billing patterns.
- Looking up Clerk quickstarts for Next.js App Router, React/Vite, Expo, Astro, Remix, Express, or Go.

Prefer MCP-provided snippets and quickstarts over guessing API shapes from memory. Start with `list_clerk_sdk_snippets` when the right slug is unclear, then call `clerk_sdk_snippet` for the specific snippet or bundle.

For workspace operations, use `whoami` to identify the connected account, active workspace, and granted scopes. When available, use the authenticated tools to inspect applications, users, organizations, domains, OAuth providers, and instance configuration, or to apply the requested application, user, and configuration changes. Check the target application and instance before a write. Use a tool's `dry_run` option to preview supported changes, and require the tool's explicit confirmation parameter for irreversible operations.

Authentication and scope upgrades happen through the MCP connection. If a tool is unavailable or a scope is denied, explain the missing access instead of assuming it was granted. Never include secret keys, tokens, or end-user personal data in `submit_feedback` reports.
