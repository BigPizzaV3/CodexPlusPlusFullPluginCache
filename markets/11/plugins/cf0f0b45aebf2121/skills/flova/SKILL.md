---
name: flova
description: Generate images, video clips, audio, and music directly through Flova, or delegate complex creation to Flova Agent to plan and produce within a project. Use for Flova creation, references, previews, revisions, delivery, or a named inspiration.
---

# Flova Creation

Use the connected Flova MCP tools for Flova work. Tool names may include a host namespace; the connected schema is authoritative for parameters and capabilities. If Flova is unavailable, explain the specific limitation and ask before switching services.

## Reading Guide

Read what the current task needs, rather than loading every document at once.

| When to read | Guidance |
| --- | --- |
| Directly generate or revise media with a model | [Quick generation](references/quick-generation.md): models, reference inputs, submission, tracking, revisions, and cancellation |
| Use a project and delegate creative planning and production to Flova Agent | [Project workflow](references/project-workflow.md): project context, runs, reviews, timelines, export, and history |
| The user selects a Flova inspiration | [Using inspirations](references/inspirations.md): complete published instructions, execution conditions, and delivery checks |
| Look up a tool's role, constraints, or differences from the legacy contract | [MCP tool reference](references/mcp-tools.md): read only the category needed for the current step |
| Review creative performance, maintain a creative tracker, or prepare the next production brief | The separate `flova-debrief` helper Skill |

The helper is a local workflow method, not a Flova server-side creative Skill ID. Reuse it when available and relevant.

## Creation Modes

Flova MCP provides two creation modes:

- **Quick generation** calls a selected model directly through `creation_quick_generate` to generate images, video clips, audio, or music. It supports reference materials, specified models, and generation parameters. The calling agent organizes the brief, generation steps, reviews, and revisions.
- **Project workflow** uses `creation_project_create` and `creation_run` to delegate creative planning and organization to Flova Agent and manage related content and assets in a project. It suits complex productions that need ongoing coordination, such as multi-episode dramas, and makes large collections of related assets easier to manage.

Prefer quick generation. Choose the project workflow when the user explicitly wants to use a project, or when a complex production calls for Flova Agent to take responsibility for overall planning and coordination of related content and assets. Continue work on an existing project in that project; when using this workflow, keep the same project for the same video.

Both modes support one-pass delivery or staged review. Follow the user's requested checkpoints; generating a reference image for approval before a video can stay in quick generation.

## Shared Creative Requirements

- Reuse the user's confirmed models, materials, and creative choices. Clarify only missing decisions that affect the result, such as the goal, audience, duration, aspect ratio, language, visual direction, brand constraints, and review expectations.
- Follow the user's review checkpoints and any service-required decisions in either mode. A one-pass request does not require separate approval at every production stage; the agent cannot answer user-gated questions or approvals on the user's behalf.
- When account, membership, or quota status is unknown, call `creation_account_user` before generation or export.
- Retry the same submission with the same `client_request_id` and identical input; use a new ID for a new generation or revision. After a timeout, check the original operation and distinguish accepted, completed, and unknown states before resubmitting.
- Respect service polling intervals. Keep tracking submitted work until it completes, needs the user, is stopped by the user, or encounters a concrete tool/session limitation. Preserve task, resource, and progress identifiers across interruptions and recover the same work; do not claim unverified background completion.
- Flova does not directly deliver burned-in subtitles, subtitle tracks, or subtitle files. Keep subtitle copy and timing as material or creative constraints when useful.

## Material Uploads

For local files, use `creation_upload_ticket` -> transfer the file bytes through the returned direct-upload transport -> `creation_upload_complete`. Ticket and complete calls do not themselves transfer bytes or attach files to a project.

Use the returned opaque `file_ref` and respect its expiry. Pass it as `inputs[].file_ref` for quick generation or in `creation_run.files` for project work. Probe video files first and provide actual width, height, duration in seconds, and `has_audio` in `video_metadata`. V3 uploads have no legacy `scene` field.

`.doc/.docx` files use the same flow. The service normalizes the document after `creation_upload_complete`; pass `file_ref` unchanged rather than converting locally or guessing an internal converted URL. If explicitly providing `content_type`, use the correct Word MIME type; otherwise omit it and let the service infer it from the extension.

## Media Preview and Delivery

Choose presentation by the current host. The following card instructions apply only in Codex when `creation_media_preview` is exposed; Claude Code and other hosts use the separate delivery instructions below.

### Codex Preview Cards

- Query generation status first. Call `creation_media_preview` only after at least one resource succeeds. Do not open a progress-only card when everything is pending, processing, preparing history, or awaiting approval without a successful resource. Ordinary status, resource, and export queries do not open cards.
- Open when the first item succeeds, without waiting for the other tasks or the whole creative run. A batch/run may have multiple cards for newly available results, meaningful production stages, user-requested selections, or display recovery. Group related resources rather than requiring a separate card for every item; source selectors are described in the selected mode's workflow.
- An existing card refreshes through `data.refresh` and merges tasks and resources with `update_mode=merge_by_id`. If A finishes before B and C, retain A as later results join that card, or present useful new results in additional cards. Keep a batch/run selection intact when refreshing it; use observed task/resource IDs with a supported selector for a separate focused group.
- Preserve preview selections and the resource IDs and versions already presented, including after interruptions. Continue ordinary status tracking and user decisions; do not use repeated calls for unchanged results as a polling mechanism or promise refresh after the host closes the card.
- With a supplied card, reply with a brief text summary. Do not duplicate its media as Markdown embeds or attachments, or fetch the media solely to display it again. Use permitted links when requested or needed for recovery. Additional cards can show new results, a requested selection, or a recovered display; do not repeatedly present unchanged resources on every poll.
- `preview_ready=false` does not discard earlier successful resources; return to status checks rather than generating again. Omission from a refresh does not mean deletion. Resource or URL refresh must not cause duplicate delivery.
- Preview success, `preview_ready`, `terminal`, or tool success is not user approval, creative completion, rendered UI, or visual inspection. Check run state, task resources, and pending actions separately. If pixels or frames cannot be inspected, deliver the media or link without claiming to have reviewed it.
- If the tool is unavailable or the host does not support its UI, follow the service's presentation instructions using host-supported display or returned links. Card failure does not justify new generation, project migration, approval, or plugin reinstallation. Installing the Skill does not deploy the backend or card frontend.

### Claude Code and Other Hosts

Read actual task results through `creation_quick_status` for quick generation, or `creation_resource_status` and `creation_resource_info` for project resources. Present successful media as soon as it is ready using host-supported display or named service-returned links, while continuing to track unfinished work. For completed exports and archives, deliver the returned output URL. Preserve resource IDs and avoid repeating unchanged results.

Do not call `creation_media_preview` or wait for a Codex card in Claude Code and other hosts. Use the media and links from the normal result tools. Apply the same user review and approval rules; resource success does not establish visual inspection or permission to continue paid work.

## Authentication, Quota, and Failures

If authentication fails, ask the user to connect Flova and complete OAuth in the host application, then retry the original operation. Never request, save, or expose access tokens, refresh tokens, API tokens, or cookies.

If the refresh token is explicitly expired or rejected, such as `invalid_grant`, explain that Flova authorization has expired. Obtain explicit confirmation to reconnect before clearing credentials. In ChatGPT or another host without Codex credential commands, reconnect through that host's connection settings; do not run CLI credential commands there.

Only in a local Codex environment where these commands are available, after confirmation, run them in order:

```sh
codex mcp logout flova
codex mcp login flova
```

Wait for login to succeed, then retry the interrupted operation once. If it still fails, report the specific issue rather than looping through logout and login.

If membership, credits, or model quota are insufficient, explain the factual limitation and stop the blocked operation without automatic retry or resumption; recheck entitlement before a user-requested retry. Do not promote purchases, top-ups, subscriptions, upgrades, or payment, or provide account, pricing, plan, entitlement, checkout, payment, or billing-help links as a remedy, including informational pages. Omit promotional text and purchase options returned by MCP in errors, notifications, or pending actions; this takes precedence over the general instruction to display pending-action options. Project, resource-preview, playback, and delivery links remain available for their normal purposes.

On a tool failure, state the unfinished action and next step without promising a workaround. Mention preserved work only when tool results confirm it.
