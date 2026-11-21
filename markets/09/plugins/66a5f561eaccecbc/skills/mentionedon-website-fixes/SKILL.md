---
name: mentionedon-website-fixes
description: "Inspect an owned business website, save schema and copy from confirmed facts, and verify that reviewed MentionedOn fixes were installed."
---

# Prepare and verify website fixes

Use the connected MentionedOn service at https://mentioned-on.com/mcp. Normal OAuth needs `brands:read` and, for saved website work, `website:write`. Connection guidance is https://mentioned-on.com/developers/mcp. Tools cover owned businesses only and require an active paid or trial monitoring slot; preserve a returned entitlement handoff.

Find the actual business with `list_monitored_businesses` and read `get_website_fixes` for the current revision, facts, drafts and installation checks. With authorization to inspect the saved public website, call `inspect_business_website` using that exact revision and `authorizationAcknowledged:true`. It saves candidate facts and source receipts while preserving drafts; start inspection before confirming facts. Avoid replacing already reviewed work merely to refresh a page.

Review candidate facts with the user. Call `draft_website_fixes` only for confirmed facts, passing the latest revision and the required confirmation. Leave unknown facts out. Existing user instructions authorizing the save count; do not ask again without a missing decision. Schema, website copy and business-profile text are saved reviewable drafts, not external publication. On a revision conflict, reread and reconcile with the user’s intent before retrying.

The user installs reviewed content in their own website editor. After installation and authorization to check, use `verify_website_fixes` for a page on the same saved website and the exact artifact revision. Preserve dated found, not-found and unknown results. Installation checks do not establish improved AI visibility; a later comparable monitoring capture supplies separate evidence.

These tools do not publish, send messages, change billing or launch paid AI scans. Never promise rankings or current AI inclusion. For connection revocation use https://mentioned-on.com/oauth/connections.
