---
name: get-started
description: Describes what the Influee tools cover in an Influee brand account, from campaigns and creators to messages, tasks and content review, and how a typical campaign moves through them.
---

# Get started with Influee

Influee is a platform where brands and agencies run UGC and creator campaigns. A brand posts a campaign with a brief, creators apply with a proposal, the brand picks creators, ships the product and reviews the content they deliver. Influee holds the payment and pays the creator when the work is approved.

The Influee tools act on the user's own Influee brand account. They return only the brands, campaigns and creators that account can see. Explicit instructions from the user take priority over anything in this skill.

## How a campaign moves through the tools

1. **Set up.** A brand and its products exist in the account. A campaign starts as a draft with a brief and creative assets, and is submitted for review when it is complete.
2. **Recruit.** While recruitment is open, creators apply with proposals. The brand can also search creators, keep them in lists, and prepare and send offers to chosen creators.
3. **Run.** Each collaboration produces tasks for the brand: shipping the product, adding tracking links or creator codes, and reviewing delivered content or raw footage.
4. **Use the content.** Approved videos and photos land in the content library with transcripts, and can be shared with a public link.

The signed-in user, company and workspace are available from `get_viewer`. Pending action items across all campaigns are available from `list_tasks`. Questions about how Influee works are answered from the Influee help docs by `ask_docs`.

## What the tools cover

| Area | Read | Change |
|---|---|---|
| Campaigns | `list_campaigns`, `get_campaign` | `create_campaign`, `update_campaign`, `submit_campaign`, `duplicate_campaign`, `open_campaign_recruitment`, `close_campaign_recruitment`, `remove_campaign` |
| Creators and lists | `list_creators`, `get_creator`, `list_lists`, `get_list` | `create_list`, `edit_list`, `toggle_list_creator`, `remove_list`, `blacklist_creator` |
| Collaborations and offers | `list_collaborations`, `get_collaboration` | `create_collaboration`, `update_collaboration`, `send_collaboration`, `decline_collaboration`, `withdraw_collaboration`, `update_collaboration_deadline`, `launch_dispute` |
| Messages | `list_conversations`, `get_conversation`, `ask_conversations` | `send_message`, `create_draft_message`, `send_draft_message` |
| Tasks | `list_tasks` | `confirm_shipment`, `confirm_delivery`, `add_tracking_link`, `add_promo_code`, `review_content`, `review_creative_asset` |
| Content library | `list_delivered_content`, `get_delivered_content`, `list_share_links` | `create_share_link`, `revoke_share_link` |
| Briefs and creative assets | `list_creative_assets`, `get_creative_asset`, `get_creative_asset_document`, `list_ad_script_sources`, `get_ad_script_source` | `add_creative_asset`, `update_creative_asset`, `duplicate_creative_asset`, `remove_creative_asset`, `add_creative_asset_document`, `upload_creative_asset_document`, `remove_creative_asset_document` |
| Brands, products, workspaces | `list_brands`, `get_brand`, `list_products`, `get_product`, `list_workspaces`, `list_payment_methods` | `create_brand`, `update_brand`, `create_product`, `update_product`, `remove_product`, `update_workspace` |
| Documents and skills | `list_documents`, `get_document`, `list_skills`, `get_skill` | `save_document`, `create_skill`, `update_skill`, `delete_skill` |
| Invoices and payments (company admins) | `list_invoices`, `get_invoice`, `list_payments`, `get_payment` | none |

## Things to know

- Many tools accept a name or an ID. When a name matches more than one record, the tool returns candidate IDs and the user picks one.
- A new collaboration is a draft. Nothing reaches the creator until the offer is sent.
- Sending a message or an offer reaches the creator right away, and deletes cannot be undone. The user sees what will happen and confirms before these run.
- A message draft waits in the Influee dashboard for the user and is never sent automatically.
- Whether the account can message a creator depends on its Influee access. If sending is refused, saving a draft still works.
- A creator's username and contact details can be hidden (`hideSensitiveInformationReason`). The creator is then referred to by first name.
- Proposal acceptance, collaboration sign-off, rewards and payments are handled in the Influee dashboard, not through these tools.
- Invoices and payments are readable by company admins only.
