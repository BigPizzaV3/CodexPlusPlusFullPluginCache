---
name: startupsprints-assets-and-launches
description: Use when a StartupSprints founder asks to create or revise a Distribution Kit asset, product description, demo, screenshot brief, listing, launch package, destination-specific submission, reusable resource, content draft, or launch readiness check.
---

# StartupSprints assets and launches

Produce a usable artifact or launch package grounded in the confirmed product and the founder's mission. A draft, submitted listing, approved listing and measured acquisition remain separate.

Read [MCP workflow](references/mcp-workflow.md) before work. Use [asset and launch preparation](references/asset-and-launch-preparation.md) for concrete deliverables and readiness checks; [prompt examples](references/prompt-examples.md) provide entry points.

## Inputs

Resolve startup/action, audience, confirmed product facts/limitations, existing approved assets, intended destination, current requirements, time/budget, identity/public preferences and any explicit publication or purchase approval.

## Read → select → act → save → review

1. **Read:** Discover actual tools. Resolve startup with `list_startups` and returned `actionId` with `list_actions`; read `get_startup_profile`, `get_execution_brief`, `get_action_workspace`, and `get_distribution_kit`. Use explicit `startupId` for all-startup grants. Read relevant previous results when choosing claims or launch scope.
2. **Select:** Choose the artifact that unblocks the action or tests its audience/mission hypothesis. Honor prerequisites and the live required description variant. Verify current destination eligibility, fees, promotion rules and submission requirements. Missing facts stay unresolved; a generated image or draft is not proof of product behavior.
3. **Act:** Create the actual copy, artifact or authorized artifact reference, with source-backed claims, affiliation, permissions, accessible caption/instructions and honest limitations. Prefer existing approved assets. Confirm each actual authenticated account before account-dependent work; preserve previous explicit confirmation. Prepare the destination, account, exact content/assets, fees and volume before missing authorization to publish, submit, book or buy. Reuse bounded prior approval; do not infer approval from readiness or public-identity preference.
4. **Save:** Save when included in the task. Action work uses the live template and full merged entries/notes with current `workRevision`; reread/merge conflicts and verify. Distribution Kit text/link content uses `save_asset_content` with actual `assetId` and current `expectedUpdatedAt`; this replaces content. Read current content and preserve relevant material. Logo/screenshot upload occurs in the app; text cannot create an uploaded image. Saving does not publish or establish readiness, execution or results.
5. **Review:** Return actual readiness gaps, draft/submission/publication state and evidence needed to evaluate audience response. Recommend the smallest next step toward the mission. On ambiguous “wrap up,” prepare a summary and clarify actual-result recording and completed/failed intent before `record_action_result`. That call ends the attempt; use current `attemptNumber`/`outcomeRevision` and only observed metrics in `measuredMetrics`. Unknown analytics is not measured zero; no inferred vote.

## Output and fallback

Return the usable artifact, claims/sources, current destination requirements, remaining gaps, save status and approval scope. If creation/upload/submission tools are unavailable, deliver honest text/specification or manual-ready materials and name the remaining step. Do not invent hosted links, uploads, accepted submissions or persistence.
