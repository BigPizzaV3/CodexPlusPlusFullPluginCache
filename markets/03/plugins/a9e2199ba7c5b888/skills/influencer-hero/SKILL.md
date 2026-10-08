---
name: influencer-hero
description: Run an influencer marketing program through the Influencer Hero connector - discover creators, manage outreach campaigns, work the CRM pipeline, and read collaboration and campaign performance. Use whenever the user asks to find creators, review or update deals, add creators to a campaign, or pull campaign or collaboration results in Influencer Hero.
---

# Influencer Hero

Influencer Hero is an influencer marketing platform for consumer brands, covering
discovery, outreach, CRM, collaborations, content, affiliate performance, and
payouts. This skill explains how to use its tools correctly and safely.

The connector acts as the signed-in user. It inherits that user's role and brand
permissions exactly as the web app does, so it can only reach data and actions
that user could reach directly.

## Start here

Before a multi-step task, call `get_workflow_guide` with the matching activity.
It returns the recommended tools, their order, the identifiers involved, the
required role, and the safety notes. Available activities:

influencer_discovery, campaign_outreach, crm_management, performance_analysis,
campaign_reporting, email_onboarding, payout_review, content_wall,
application_pages, product_sending, bulk_tool, content_review,
profile_review_optional.

Follow the guide's steps rather than guessing a sequence.

## Two rules that prevent most mistakes

1. **Never invent identifiers.** Brand, campaign, board, deal, influencer, flow,
   and collaboration IDs must come from a previous tool result. When an ID is
   unknown, call the list or lookup tool that owns it first. Do not construct or
   guess an ID.

2. **Reuse IDs returned by earlier tools.** The workflow is a chain: a list tool
   returns IDs, a detail tool takes one of those IDs, and so on. Carry IDs
   forward from step to step.

## Identifiers and how they relate

- `brand_id` - a brand. Start with `list_brands`.
- `outreach_id` - an outreach campaign. From `list_campaigns`.
- `dashboard_id` / `dealflow_id` - a campaign board (a CRM pipeline whose columns
  are funnel stages). From `list_boards`.
- `deal_id` - an influencer's CRM record. From `list_crm_influencers`,
  `create_deal`, or `get_deal_details`.
- `collab_id` - one deal-brand collaboration. Request `return_collabs=true` from
  `get_deal_details` before using collaboration-performance tools.
- `flow_id` - an email flow. From `list_email_flows`.
- `user_id` - EITHER the current user, OR a platform-specific influencer ID
  returned by influencer lookup or search.

Do not substitute one identifier type for another.

## Credits: say so before spending them

These tools consume account credits. Tell the user before running them, and only
run them when the request clearly calls for it:

- Creator search (`search_influencers`) - search credits
- Full audience report (`get_influencer_analytics`) - report credits
- Contact detail lookup (`get_contact_details`) - contact credits

Everything else - CRM queries, campaign data, reporting, payouts - is free.

## Confirm before writing

Read-only tools (listing brands, campaigns, deals, reports, payouts) can run
without asking. Tools that change data must be confirmed with the user first,
immediately before running:

`create_deal`, `create_note`, `create_task`, `update_deal_stage`,
`add_influencers_to_campaign`, `send_product`, and any
`invoke_api_write_operation` or `invoke_api_delete_operation`.

Show the user exactly what will change, then wait for a yes.

## Common flows

**Discover and add to a campaign.** `get_workflow_guide(influencer_discovery)` →
`search_influencers` (warn about credits) → review candidates →
`add_influencers_to_campaign` (confirm first).

**Work the pipeline.** `list_boards` → `list_crm_influencers` for a board →
`get_deal_details` for a specific deal → log a `create_note` or move stage with
`update_deal_stage` (confirm the write).

**Report on performance.** `get_report` for campaign-level results across a date
range, or `get_deal_details(return_collabs=true)` then `get_collab_metrics`,
`get_collab_orders`, and `get_collab_top_products` for one collaboration.

## Less-common operations

For an operation with no first-class tool, call `search_api_capabilities` with a
short description of the goal. It returns matching operations, each with the
`invoke_with` tool to use - `invoke_api_read_operation`,
`invoke_api_write_operation`, or `invoke_api_delete_operation`. Read operations
run freely; write and delete operations need confirmation. Only reach for this
when no first-class tool or workflow step already covers the request.

## Empty or blocked results

- Empty lists usually mean the user is scoped to a brand without that data, or
  the filters are too narrow. Offer to list brands and campaigns first.
- "Insufficient permissions. Required role: ..." means the user's role is too low
  for that write; an account owner can raise it.
- A tool that fails right after a successful connection is usually a plan issue:
  connecting only checks the user is active, while individual tools enforce the
  account's plan.
