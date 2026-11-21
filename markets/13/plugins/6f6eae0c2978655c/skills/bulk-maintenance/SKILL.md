---
name: bulk-maintenance
description: Run one reviewed WordPress operation across authorized sites, with a preview before changes. Use when the user asks for a task on several connected sites.
---

# Bulk maintenance across sites

1. `sites_list` to see which sites are available and their status. Skip sites that need reconnecting and say so.
2. Choose the reviewed operation for the task. Find its exact name with `operations_list`, for example `wp_system_status`. Read `operation_help` for the operation. Use this same named tool for one site or for bulk; there are no separate bulk operation tools. Follow the exact declared input schema and never invent an operation name or an execution selector.
3. If bulk access is unavailable, explain that this connection cannot run it in bulk. Offer single-site calls only for sites and actions the user authorizes.
4. Call the named operation with `sites` set to the requested site IDs, its declared `input` object, and `dry_run: true`. Omit `site`. This lists intended calls without executing the site operation; it does not prove the installed integration supports it. Show the user which sites will be touched.
5. After the user confirms, call the same operation with the identical sites and input and `dry_run: false`. Use `bulk_status` for progress, with longer intervals when unchanged. Summarise successes, approval requests and failures accurately. Site-specific approval must happen through the site's supported approval flow; do not insert confirmation fields without approval.
6. For write actions, review each site's change records and offer undo only where the ledger marks the change reversible ("review-and-undo"). Explain any irreversible operation or missing record.

Prefer read-only tools (audits, status) for bulk runs unless the user clearly asked for changes.
