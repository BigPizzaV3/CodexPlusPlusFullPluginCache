---
name: connect-first-site
description: Set up GoBuildWP after installing the plugin — sign in to GoBuildWP Cloud, connect the first WordPress site and try a first safe action. Use right after install, or when the user has no connected sites.
---

# Connect your first WordPress site

Goal: the user ends with at least one site connected and sees one real result from it.

1. Call `sites_list`.
   - If it returns sites, skip to step 4.
2. Explain in two sentences what GoBuildWP Cloud does: one connection reaches every WordPress site they connect, and each site keeps its own safety rules, confirmations and supported undo operations.
3. Walk them through connecting a site, one step at a time, waiting for them after each:
   - The site needs GoBuildWP, version 1.18.8 or newer. Install its release ZIP through WordPress admin → Plugins → Add New → Upload Plugin, or update the existing installation. Do not promise a WordPress.org listing before directory approval. Activate only one Free edition.
   - In WordPress admin: **GoBuildWP → Connect → GoBuildWP Cloud → Connect to GoBuildWP Cloud**.
   - They sign in or create a free account at GoBuildWP Cloud, pick **Read only** (recommended to start) or **Production safe**, approve, then click **Confirm** back in WordPress.
   Then call `sites_list` again to confirm the site appears.
4. Offer a safe first action on the new site, for example: "Want a quick health check?" If yes, read `operation_help` for `wp_system_status`, then call `wp_system_status` with `site` and `input: {}` and summarise the findings in plain language (no raw JSON).
5. Mention they can open the **GoBuildWP sites** panel from the sidebar to see all sites and recent changes, and undo changes that the site's ledger marks reversible.

Never ask the user to paste passwords, application passwords or access tokens into the chat. Connection always happens through wp-admin and GoBuildWP Cloud.

Use only the declared tools available on this connection. For other tasks, use `operations_list` to find the operation, then `operation_help` for its input schema and prerequisites. Every operation has its own named tool. For authorized Pro bulk, use the same tool with `sites` and `dry_run` instead of `site`. Every site operation takes `site` and an `input` object with its declared fields. If an integration is unavailable or its contract has changed, report that and ask the site administrator to resolve it; do not bypass the refusal through another operation.
