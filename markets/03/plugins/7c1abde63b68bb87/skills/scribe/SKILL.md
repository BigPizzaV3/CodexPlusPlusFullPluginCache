---
name: scribe
description: >-
  Create and manage Scribe email signatures, audit installs, read teammate and
  smart-field data, run marketing campaigns, and pull analytics through the
  Scribe MCP server. Use when the user wants to create, edit, preview, publish,
  or audit email signatures; manage reply and internal variants; add or look up
  teammates; read or set smart fields; organize folders or assets; run or report
  on marketing campaigns; or pull signature analytics, conversions, and visitors
  in Scribe.
---

# Scribe

Manage a Scribe workspace through the Scribe MCP server: signatures and their
reply and internal variants, teammates, smart fields, folders, assets,
integrations, marketing campaigns, analytics, and visitors.

## When to use this skill

Use it whenever the user wants to:

- create, edit, preview, publish, install, or audit email signatures
- add a reply or internal signature variant, or read the installed HTML
- assign signatures to teammates, org units, or rule-based audiences
- add, update, or look up teammates and their email aliases
- read or set smart fields (the merge fields that populate signatures)
- organize folders or upload assets (logos, banners, pictures)
- create, schedule, pause, or report on marketing campaigns
- pull signature analytics (views, clicks, conversions, revenue)
- look up identified visitors and where they came from

## Access

- Auth: OAuth sign-in as the user. Everything is scoped to the user's own
  workspace.
- Read tools run automatically. Write tools (create, update, delete, publish)
  ask the user for confirmation in the app.

## Core workflow: create a signature in the fewest calls

From a cold session, a complete signature takes three calls:

1. Call `get_content_schema` first. In one response it returns the strict
   block-tree schema, a flat lookup of every allowed enum value (including the
   non-obvious icon names such as `linkedin-in`, `facebook-f`), and a complete
   worked example with a populated social-icon row.
2. Adapt that example into a `draft_content` block tree and call
   `create_signature` with a `name` and the `draft_content`.
3. Call `publish_signature` to copy the draft into the live `content` and trigger
   installation.

To check the result before going live, call `preview_signature` on the draft and
read the returned HTML for layout and spacing, then publish.

Do not hand-write a block tree or guess enum spellings. Always call
`get_content_schema` before any `create_signature`, `update_signature`,
`update_signature_variant`, or marketing-campaign `content` write. An invalid
tree returns a 422 that names each offending field.

## Common patterns

- Audit installs: `list_signatures` (which templates are published and
  activated), then `list_signature_recipients` (who each one covers), then
  `list_integrations` (any failing connections).
- Verify a signature: `preview_signature` to check the draft layout before you
  publish, and `get_signature_html` to read what a specific recipient receives
  once it is live.
- Add a reply or internal variant: `get_content_schema`, then
  `update_signature_variant` to stage the variant draft, then
  `publish_signature_variant`. Variants need an active Microsoft 365 signatures
  integration.
- Look up teammate data: `list_teammates` (emails and smart-field values), with
  `list_smart_fields` for the field catalog.
- Fill gaps: read with `list_teammates`, then set values with `update_teammate`.
- Target a signature: `set_signature_recipient_rules` for auto-assign and
  conditions, `add_signature_recipients` for specific emails, or
  `add_signature_recipient_entities` for directory org units and groups.
- Run a campaign: `create_marketing_campaign`, then
  `schedule_marketing_campaign`.
- Report engagement: `get_analytics_views` and `get_analytics_clicks` for totals
  and a time series, or set `group_by` to rank signatures, teammates, campaigns,
  or countries. There is no clickthrough-rate field, so compute it as clicks
  divided by views.
- Report conversions: `get_analytics_events_summary` for conversion and revenue
  totals and rankings, and `list_analytics_events` to inspect the raw events.
- Attribute customers: `list_visitors` and `get_visitor` for identified
  end-users, and `get_visitor_breakdown` to rank which signature or teammate
  acquired the most.

## Tool reference

Access key: Read runs automatically, Write asks for confirmation, Delete asks for
confirmation and is destructive.

### Schema

| Tool | Access | What it does |
| --- | --- | --- |
| `get_content_schema` | Read | Returns the signature block-tree schema, all enum values, and a worked example. Call before authoring content |

### Signatures

| Tool | Access | What it does |
| --- | --- | --- |
| `list_signatures` | Read | List signature templates (block trees omitted unless you pass `include_content`) |
| `create_signature` | Write | Create a template, staged as `draft_content` until you publish |
| `update_signature` | Write | Update a template by id, staged as a draft until you publish |
| `preview_signature` | Read | Render a draft or published template to HTML with placeholder values to check layout |
| `get_signature_html` | Read | Get the real installed HTML of a published signature for a specific recipient |
| `publish_signature` | Write | Publish a template so the draft becomes live and installs |
| `install_signature` | Write | Install the current live content without publishing |
| `delete_signature` | Delete | Delete a template and unassign it from teammates |

### Signature variants

A variant is an alternate signature shown on reply emails or on internal
(same-domain) emails. Variants require an active Microsoft 365 signatures
integration; without it, variant writes return a 409 `variants_unavailable`.

| Tool | Access | What it does |
| --- | --- | --- |
| `list_signature_variants` | Read | List a signature's reply and internal variants with their state and content |
| `update_signature_variant` | Write | Create or update a reply or internal variant, staged as a draft until you publish |
| `publish_signature_variant` | Write | Publish a variant so its draft becomes live and redeploys |
| `delete_signature_variant` | Delete | Reset a variant back to the primary signature (the record is kept) |

### Signature recipients

| Tool | Access | What it does |
| --- | --- | --- |
| `list_signature_recipients` | Read | List who a signature is assigned to, with the targeting rules |
| `add_signature_recipients` | Write | Assign a signature to a batch of teammate emails |
| `remove_signature_recipients` | Write | Remove manually assigned recipients from a signature |
| `set_signature_recipient_rules` | Write | Set auto-assign and the smart-field condition rules |
| `add_signature_recipient_entities` | Write | Target a signature at directory org units or groups |
| `remove_signature_recipient_entities` | Write | Untarget directory org units or groups |

### Teammates

| Tool | Access | What it does |
| --- | --- | --- |
| `list_teammates` | Read | List teammates with their emails and smart-field values |
| `create_teammate` | Write | Add a teammate from an email and optional field values |
| `update_teammate` | Write | Set a teammate's smart-field values |
| `delete_teammate` | Delete | Soft-delete a teammate |

### Emails

| Tool | Access | What it does |
| --- | --- | --- |
| `list_emails` | Read | List teammate emails (primary and aliases) |
| `create_email` | Write | Add an alias email to a teammate |
| `update_email` | Write | Change an email address |
| `delete_email` | Delete | Soft-delete an alias email (a primary email cannot be deleted) |

### Smart fields

| Tool | Access | What it does |
| --- | --- | --- |
| `list_smart_fields` | Read | List smart-field definitions with kind and data source |
| `create_smart_field` | Write | Define a custom field, optionally synced from an integration |
| `update_smart_field` | Write | Update a custom field or its integration link |
| `delete_smart_field` | Delete | Delete a custom field and its values on every teammate |

### Folders

| Tool | Access | What it does |
| --- | --- | --- |
| `list_folders` | Read | List signature folders with their signature counts |
| `create_folder` | Write | Create a folder to organize templates |
| `update_folder` | Write | Rename a folder |
| `delete_folder` | Delete | Delete a folder (it must be empty first) |

### Assets

| Tool | Access | What it does |
| --- | --- | --- |
| `list_assets` | Read | List the image library (logos, banners, pictures) |
| `create_asset` | Write | Upload an image from base64 or a source URL |
| `update_asset` | Write | Update an asset's name or role |
| `delete_asset` | Delete | Delete an asset (in-use assets are soft-deleted so they keep rendering) |

### Integrations

| Tool | Access | What it does |
| --- | --- | --- |
| `list_integrations` | Read | List active integrations with status and any error details |
| `list_integration_entities` | Read | List directory org units and groups to target a signature at |

### Financial documents

| Tool | Access | What it does |
| --- | --- | --- |
| `list_financial_documents` | Read | List invoices and credit notes with downloadable PDF links |

### Workspace

| Tool | Access | What it does |
| --- | --- | --- |
| `get_workspace` | Read | Read the workspace plan, status, and invoiced seat count |

### Analytics

There is no clickthrough-rate field. Pair `get_analytics_views` with
`get_analytics_clicks` and compute clicks divided by views.

| Tool | Access | What it does |
| --- | --- | --- |
| `get_analytics_views` | Read | Signature views over a date range, as a time series or a ranked breakdown |
| `get_analytics_clicks` | Read | Signature clicks over a date range, as a time series or a ranked breakdown |
| `get_analytics_events_summary` | Read | Aggregated conversion and revenue numbers, as a time series or a ranked breakdown |
| `list_analytics_events` | Read | List the raw recorded conversion events behind the analytics |

### Visitors

Visitors are the workspace's own identified end-users (from `identify` calls),
not Scribe teammates.

| Tool | Access | What it does |
| --- | --- | --- |
| `list_visitors` | Read | List identified visitors with traits and first-touch attribution |
| `get_visitor` | Read | Get one identified visitor with traits, attribution, and lifetime engagement |
| `get_visitor_breakdown` | Read | Rank which signature or teammate acquired the most identified visitors |

### Marketing campaigns

| Tool | Access | What it does |
| --- | --- | --- |
| `list_marketing_campaigns` | Read | List campaigns with status, targeting, and content |
| `create_marketing_campaign` | Write | Create a campaign draft with a name and time window |
| `update_marketing_campaign` | Write | Update a campaign by id |
| `schedule_marketing_campaign` | Write | Activate or schedule a draft or paused campaign |
| `pause_marketing_campaign` | Write | Pause an active campaign |
| `resume_marketing_campaign` | Write | Resume a paused campaign |
| `delete_marketing_campaign` | Delete | Delete a campaign (an active one stops first) |

## Important notes

- Always call `get_content_schema` before writing any signature `draft_content`,
  variant `draft_content`, or campaign `content`. It is the fastest path to a
  valid block tree.
- Writes are staged. `create_signature` and `update_signature` set
  `draft_content`; the live `content` changes only when you call
  `publish_signature`. Variants stage and publish the same way through
  `update_signature_variant` and `publish_signature_variant`.
- `preview_signature` renders placeholder values for a layout check and needs no
  recipient. `get_signature_html` returns the real installed HTML for one
  recipient and is empty until the signature is published.
- Signature variants need an active Microsoft 365 signatures integration.
  Without it, variant writes return a 409 `variants_unavailable`.
- Analytics has no clickthrough-rate field. Compute it as clicks divided by
  views. Analytics ranges default to the last two months, and `hour` granularity
  is capped at a 31-day range.
- Some actions are blocked when a directory integration (Google Workspace or
  Microsoft Entra ID) manages the team list. Creating or deleting teammates and
  emails then returns a 409.
- Default and integration-synced fields are read-only. Setting them is skipped or
  returns a 422.
- List tools are paginated with `limit` (1 to 100); some use a `cursor` and
  others a `page`, and several support a bounded `auto_paginate` with `max_pages`
  (cap 20).
- Every write asks the user to confirm in the connected app, and every action is
  scoped to the user's own workspace.
