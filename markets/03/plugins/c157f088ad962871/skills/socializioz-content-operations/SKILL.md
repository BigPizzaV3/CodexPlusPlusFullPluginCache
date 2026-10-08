---
name: socializioz-content-operations
description: Plan, draft, review, schedule, publish, and organize social media work through Socializioz. Use for Socializioz workspace and brand orientation, connected-account selection, evidence-safe campaign strategy, platform and content-format decisions, campaign plans, post drafts, media preparation, approval workflows, scheduled publishing, immediate publishing, publication retries, and authorized X research.
---

# Socializioz Content Operations

Use Socializioz as the source of truth for the active workspace, brand, connected accounts, posts, campaigns, media, approvals, and publication state.

Read [references/tool-map.md](references/tool-map.md) before a multi-step operation or whenever exact action boundaries are unclear. Read [references/marketing-practice.md](references/marketing-practice.md) when planning strategy, choosing platforms or formats, writing content, selecting timing, or evaluating claims.

## Orient before acting

1. Call `invoke_get_user_profile` before a multi-step workflow.
2. If the active workspace is unclear, use `invoke_list_user_workspaces` and ask the user to choose by friendly workspace name.
3. Read `invoke_get_brand_profile` and `invoke_list_connected_accounts` before creating brand-specific content or choosing a publishing target.
4. If the requested client or brand conflicts with the active Brand Profile, ask whether to continue for the external client or switch to the connected brand.
5. For an external client, plan without binding content to the active connected brand. Bind or publish only after the user chooses the intended connected account.
6. Use account capability and health flags as authoritative; never assume a platform connection can publish.
7. Do not expose raw internal identifiers. Retain returned identifiers only for follow-up tool calls.

## Decide before creating

1. Identify the objective, audience, offer, campaign or one-off scope, target platforms, language, and available evidence.
2. Choose platforms and formats from the objective and available assets; do not mechanically duplicate identical copy across every channel.
3. Use campaigns and campaign plan items for coordinated initiatives. Use a direct draft for a one-off post.
4. Preserve explicit user wording, language, audience, constraints, and blocked terms.
5. Never invent performance metrics, customer results, case studies, certifications, market facts, trends, or competitor behavior.
6. Mark unsupported claims with an explicit verification placeholder and ask for evidence before presenting them as facts.
7. Treat proposed posting times as hypotheses unless supported by the user's own verified data. State the timezone.

## Draft and review

- Create an unpublished draft before approval, scheduling, or publishing unless the user explicitly requests an immediate eligible publication.
- Create one draft per connected destination account. Adapt the hook, length, CTA, hashtags, and format to that platform.
- Keep campaign planning, plan-item conversion, drafting, approval, scheduling, and publishing as distinct lifecycle steps.
- After a write, report only what the tool result confirms. Never describe a draft as scheduled or a scheduled post as published.
- Before another lifecycle action, use `invoke_get_post` when the current post state or available action flags may have changed.

## Prepare media

1. Prefer existing workspace assets found with `invoke_list_workspace_assets` and `invoke_get_asset`.
2. For a public HTTPS media source, use `invoke_import_media_from_url` before attaching it.
3. Attach media only to the intended draft with `invoke_attach_assets_to_post`.
4. Run `invoke_media_preflight` before scheduling, publishing, or retrying a media post.
5. Never assume a chat attachment is automatically available to an MCP tool. Use a host-provided file reference only when the tool call actually receives one; otherwise request a public HTTPS URL or use an existing workspace asset.
6. Treat asset detachment and reordering as edits to the draft, not deletion of the library asset.

## Approve, schedule, and publish safely

- Send a draft for review with `invoke_send_post_for_approval` when approval is required.
- Use `invoke_approve_post` or `invoke_reject_post` only for a post already awaiting approval. Before approval, state that approval schedules the post at the supplied, existing, or ASAP time.
- Clarify ambiguous dates, relative dates, or time zones before scheduling. Resolve them to an exact ISO 8601 timestamp with an explicit UTC offset.
- Treat scheduling as a queued future action, not proof that publication already happened.
- Require explicit confirmation of the exact post, account, and time before `invoke_schedule_post`, `invoke_reschedule_post`, or `invoke_cancel_scheduled_post`.
- Call `invoke_publish_now` only after the user explicitly confirms immediate publication for the exact post and account.
- Never treat approval of copy, a campaign, a plan, or a draft as authorization to schedule or publish it.
- Use `override_approval` only when the user explicitly asks to bypass a pending review.
- Retry only a confirmed FAILED publication with `invoke_retry_failed_publication`; do not retry a PUBLISHING post.
- Report success, failure, warnings, and platform errors exactly from the tool result; never claim publication from intent alone.

## Research on X

Use `invoke_x_live_read` only with a verified connected X account and for the requested read or search action. DM events may contain private communications, so retrieve them only when the user specifically asks for that authorized information. Never imply that this read tool can post, delete, or send messages.

## Guardrails

- Do not change workspaces, accounts, campaigns, drafts, approval state, schedules, attachments, or publication state without a user request that clearly authorizes that change.
- For ambiguous write requests, show the intended target and change, then ask one focused clarification.
- Prefer the least consequential tool that completes the request.
- Never silently select the first workspace, account, campaign, post, or asset when multiple plausible targets exist.
- Do not reveal tokens, raw provider responses, private DM content outside the user's specific request, or internal IDs.
- Summarize completed actions with friendly names, channel, lifecycle state, warnings, and the next safe available action.
