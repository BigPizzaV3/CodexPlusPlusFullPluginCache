---
name: adneuron-campaign-router
description: Route AdNeuron advertising requests to Meta or Google campaign agents, read-only reporting, optimization, or approved management workflows.
---
# AdNeuron campaign router
## Architecture
Skills own conversation orchestration and agent step selection. MCP owns authenticated provider calls, validation evidence, and durable state when workflow endpoints are available. UI renders step progress, summaries, selections, warnings, and actual actionable approvals. Never claim a UI button has executed a provider action without a tool response.

## Routing
1. Determine intent: inspect/report, create, edit, pause/resume, remove, creative/assets, conversion tracking, optimize, or recover.
2. Determine platform and exact workspace/account. Do not infer an account from the previous user if multiple accounts are eligible. Use read-only discovery before writes.
3. Meta create/edit: follow `adneuron-meta-campaign-agent`. Google create/edit: follow `adneuron-google-campaign-agent`. For cross-platform analysis use `adneuron-reporting-optimization`.
4. For every mutating flow apply `adneuron-workflow-state` safeguards. Account connection and synchronization are themselves potentially consequential; do not run as part of a read-only check.
5. Use exact tool names in `references/tool-stage-map.json`, but rely on live tool schemas and server responses as authority. Missing tools are limitations, not reasons to invent API calls.

## Shared eight-step agent
1. Account: workspace, platform, account ID, currency, timezone, connection status.
2. Access: permissions, assets, policy eligibility, destination readiness.
3. Goal: objective, conversion or traffic outcome, campaign type.
4. Settings: budget, bidding, schedule, location, demographics, placements.
5. Assets: creative, Page/Instagram identity, Google ad groups, keywords, ads, conversion actions.
6. Review: complete, readable plan with defaults, warnings, evidence and exact planned API action.
7. Approval: explicit plan- and action-specific confirmation; creation defaults to paused where supported. Activation requires separate confirmation.
8. Verification: provider IDs, actual state, partial failures, next actions; reconcile uncertain writes before retry.

At each step show `Step N of 8`, completed/missing fields, what happens next, and a concise choice/action. Never mark a step complete based on assumption. Do not ask again for fields already known and verified.

## Product scope
Meta image/video/carousel and Google Search are supported only when corresponding MCP tools are exposed and validated. Google Display/Demand Gen require distinct plans and explicit user selection. Do not silently broaden placements or enable unapproved spend. Respect tool and provider permissions.
