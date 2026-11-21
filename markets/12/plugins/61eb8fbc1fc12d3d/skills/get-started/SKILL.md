---
name: get-started
description: First-run guidance for the Leaf360 mortgage CRM plugin: confirm the connection, learn what the plugin can do, and set up a new loan officer.
---

# Get started with Leaf360

1. Confirm the connection by calling `leaf360_setup_status_get`. It returns the signed-in user's setup checklist, profile gaps, phone readiness, and workspace counts. If it fails with an authentication error, the user needs to sign in to Leaf360 through the plugin's connect flow.
2. Call `leaf360_config_get` with `sections: ["leadStatuses", "loanStatuses", "tags"]` so you use the workspace's exact status and tag names from the first answer onward.
3. Offer the three things people do most: find and update leads, open a loan file's conditions and rate lock, and draft follow-ups. Drafts are never sent without the user's approval in Leaf360.
4. For a new loan officer, follow `skills/leaf360-mcp-agent/references/getting-started.md`: show the checklist, do what can be done in chat, link the rest to the Leaf360 app, and offer the starter pack of templates and automations as drafts.

Never ask for passwords, verification codes, Social Security numbers, or card numbers. The plugin never returns them either.
