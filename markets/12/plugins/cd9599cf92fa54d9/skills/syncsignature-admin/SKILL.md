---
name: syncsignature-admin
description: Manage a company's email signatures in SyncSignature: add teammates, audit missing details, edit group templates, manage banner campaigns, read click analytics and check integrations. Use whenever the user asks about their team's email signatures or SyncSignature.
---

# SyncSignature skills for AI assistants

Read this once after connecting. It is the workflow behind the SyncSignature MCP server (https://mcp.syncsignature.com/mcp).

## What SyncSignature is
A company email-signature manager. A workspace has **teammates** (people), **groups** (teams), **signature templates** (one per group), **banner campaigns** (a clickable banner added to signatures for a date range), **smart fields** (values synced from Google Workspace, Microsoft, Chili Piper or CSV) and **analytics** (views and clicks on signature links).

## Ground rules
- **Reads are safe.** `list_*`, `get_*` and `preview_signature` change nothing; call them freely.
- **Writes ask first.** Before any `create_*`, `update_*`, `delete_*`, `add_teammates_to_group`, `remove_teammates_from_group`, `pause_campaign` or `resume_campaign`, show the user what will change and wait for a clear yes.
- **Deletes are final.** Confirm each delete individually. Never delete in a batch from one confirmation.
- **Never invent ids.** Resolve teammates, groups, templates and campaigns by listing them first.
- **Before deleting a teammate,** call `get_teammate` and name the person the id belongs to.
- **Group template changes and group deletes reach everyone in the group.** Tell the user the `teammate_count` from `list_groups` before asking for a yes.
- **Start with `get_workspace`** to learn the workspace name, domain and seat usage.
- **A 403 means owner-only.** Tell the user which action needs a workspace owner; do not retry.
- **A 403 INSUFFICIENT_SCOPE means the connection is read-only.** The person turned off "Allow changes" when connecting. Lookups still work; for a change, tell them to remove and re-add the connector and leave "Allow changes" on. Do not retry.

## Workflows

### Add teammates
1. `list_groups` to find the target group (or ask which one).
2. `create_teammate` per person: name, email, job title, phone, department. Email must be unique.
3. `add_teammates_to_group` with the ids returned.
4. Tell the user the signature will be installed by the workspace's usual install path (Google/Microsoft sync or the invite email); the assistant does not install signatures itself.

### Audit missing data
1. `list_teammates` (paginated; page through everything).
2. Report who lacks a phone, title or photo. Offer to fill values the user provides via `update_teammate`.
3. If a field is a **smart field bound to a source**, say the next sync will overwrite a manual value; suggest fixing it at the source instead.

### Change a signature template
1. `list_workspace_templates` then `get_workspace_template` for the one in question.
2. `list_groups` to see which groups carry this template, then `list_teammates` and ask the user which of the teammates in those groups to preview with. Never pick one yourself.
3. `preview_signature` with `workspace_template_id`, that `teammate_id` and the proposed full `fields` array or `design` object. Nothing is saved.
4. Show the user the preview, the current and proposed values side by side (only the fields or design settings that change), the number of affected teammates the preview reports, and that the change goes live at once. Wait for a clear yes.
5. Only then `update_workspace_template` with the same `fields` or `design`. Report the number of queued updates it returns.

If the preview answers `unrenderable_signature`, the template's icons have not been uploaded yet: tell the user to open the template once in the SyncSignature app, and fall back to showing the current and proposed values and the affected count (add up `teammate_count` from `list_groups` for the groups carrying this template).

### Run a banner campaign
New campaigns are created in the SyncSignature app, because the banner image has to be uploaded there. If the user asks to start one, tell them to create it in the app. Here you can manage existing campaigns:
1. `list_campaigns` to find the campaign, its dates and its groups; `list_groups` to resolve group names.
2. `pause_campaign` / `resume_campaign` take effect immediately in teammates' signatures.
3. `update_campaign` changes the name, link, dates or groups; confirm the dates read back correctly.
4. `delete_campaign` removes the campaign and its banner everywhere.

### Report on analytics
1. `get_teammate_analytics` per teammate, or `list_signature_links` to see which links are tracked.
2. Summarise as a table: teammate, views, clicks, click-through rate. State the date range and the "as of" time from the reply's first line (no dates = all time). If it says OLD NUMBERS, tell the user.

### Check integrations
`list_integrations` shows Google Workspace, Microsoft, Chili Piper, Keka: connected or not and last sync. Sync is triggered from the SyncSignature app, not from here.

## Example requests
- "Add Priya Shah, priya@acme.com, Sales Manager, to the Sales group."
- "Which teammates have no phone number?"
- "Change the phone number on the Sales template. Preview it with Priya's details and tell me who it affects first."
- "Pause our webinar banner for the Sales group."
- "Which teammates got the most signature clicks last month?"
- "Is our Google Workspace sync connected?"
