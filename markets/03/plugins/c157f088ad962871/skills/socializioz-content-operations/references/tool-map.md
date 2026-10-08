# Socializioz action map

Use only these 33 approved actions. Do not search for or invoke Base44 entity operations or unlisted backend functions.

## Orientation and context

- `invoke_get_user_profile`: session, selected workspace, plan, brand/account summaries, and capabilities.
- `invoke_list_user_workspaces`: friendly workspace choices for the authenticated user.
- `invoke_get_workspace_context`: role, readiness, plan, counts, and capabilities.
- `invoke_get_brand_profile`: identity, audience, voice, goals, guidelines, and profile completeness.
- `invoke_list_connected_accounts`: account identity, health, and capability flags.
- `invoke_get_mcp_help`: deeper rules for a topic or exact tool name. Treat the exposed 33-action list as authoritative if help mentions an unavailable action.

## Posts and lifecycle

- `invoke_create_draft_post`: create one DRAFT for one connected account; use a stable client request ID to avoid duplicates when available.
- `invoke_list_posts`: filter and paginate visible posts.
- `invoke_get_post`: full post details, lifecycle state, and current action flags.
- `invoke_update_draft_post`: update only a DRAFT.
- `invoke_send_post_for_approval`: move a DRAFT to PENDING_APPROVAL and create a human approval request.
- `invoke_approve_post`: approve a PENDING_APPROVAL post and schedule it at the supplied, existing, or ASAP time.
- `invoke_reject_post`: move a PENDING_APPROVAL post to CANCELLED without deleting its content.
- `invoke_schedule_post`: schedule a post for an exact future time; bypass pending approval only after an explicit user request.
- `invoke_reschedule_post`: change the future time of a SCHEDULED post.
- `invoke_cancel_scheduled_post`: cancel a scheduled post without deleting the post or media.
- `invoke_publish_now`: publish an eligible DRAFT or SCHEDULED post immediately; use explicit approval override only when requested.
- `invoke_retry_failed_publication`: retry only a FAILED publication after media validation.

Before scheduling, rescheduling, cancelling, or publishing now, obtain explicit confirmation for the exact post, account, and time or immediacy. Never infer that approval of content authorizes publication.

## Campaigns and plans

- `invoke_list_campaigns`: filter and paginate campaigns.
- `invoke_create_campaign`: create a campaign in the selected workspace.
- `invoke_update_campaign`: update only supplied campaign fields.
- `invoke_list_campaign_plan_items`: paginate a campaign's content plan.
- `invoke_create_campaign_plan_item`: add an idea or brief to a campaign plan.
- `invoke_update_campaign_plan_item`: update only supplied plan-item fields.
- `invoke_convert_plan_item_to_post`: convert a plan item into a DRAFT; approval, scheduling, and publishing remain separate.

## Media

- `invoke_list_workspace_assets`: paginate assets and optionally filter by type.
- `invoke_get_asset`: retrieve full details for one asset.
- `invoke_import_media_from_url`: securely copy a public HTTPS image or video into the selected workspace and return its Asset ID.
- `invoke_attach_assets_to_post`: attach existing Asset IDs or an actually supplied file/file URL to the authenticated user's DRAFT.
- `invoke_detach_assets_from_post`: remove selected attachments while retaining library assets.
- `invoke_reorder_attached_assets`: reorder the same attached Asset IDs.
- `invoke_media_preflight`: validate the post's media for its platform and content type before scheduling, publishing, or retrying.

Never fabricate a local file path, host file reference, asset ID, or public URL. Derive the workspace for attachment operations from the intended post whenever the tool does so.

## X research

- `invoke_x_live_read`: verified read/search operations for posts, mentions, users, followers/following, and specifically authorized DM-event retrieval.

This action reads only. It cannot publish, delete, follow, unfollow, like, reply, or send a DM.

## Result handling

- Follow pagination fields instead of assuming the first page is complete.
- Treat tool errors and warnings as authoritative.
- Use returned IDs only for follow-up calls; present friendly names to the user.
- Do not claim that a scheduled post is published.
- Do not claim provider success unless the publication action confirms it.
- Do not use `get_publish_status`; it is not one of the approved actions.
