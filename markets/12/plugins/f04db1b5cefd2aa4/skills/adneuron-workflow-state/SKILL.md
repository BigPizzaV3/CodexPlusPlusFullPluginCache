---
name: adneuron-workflow-state
description: Owns workflow intelligence and renders visible agent progress for Meta and Google Ads; derives the current stage from authoritative MCP evidence, not imagined server state.
---
# AdNeuron workflow intelligence and visible state

## Ownership
The skill owns step selection, next-action logic, progress presentation, missing-input questions, gating decisions, and user-facing state summaries. MCP owns authoritative durable storage, permissions, provider writes, idempotency, audit records, and provider verification. Never claim the skill's in-conversation state is durable across sessions without a confirmed backend workflow record. Do not store OAuth secrets or user credentials in a skill.

## Canonical agent stages
INTAKE, ACCOUNT_SELECTED, ACCESS_CHECKED, OBJECTIVE_SELECTED, CONFIGURED, ASSETS_READY, VALIDATED, PREVIEWED, APPROVED, EXECUTING, CREATED_PAUSED, VERIFIED, ACTIVE. Exceptions: NEEDS_INPUT, BLOCKED, FAILED, AMBIGUOUS, CANCELLED. Track current stage, completed stages, next required step, platform, selected account, plan revision, validation evidence, missing inputs, approvals, execution outcome, provider readback and error details. Distinguish agent stage from live delivery status.

## Render state to user
For every campaign agent turn, show a concise **Campaign setup progress** block with (a) platform and account; (b) completed/total applicable steps, (c) current stage and status; (d) completed checks and missing requirements; (e) next user action; (f) draft or provider IDs when verified. Use a progress bar or numbered steps when supported, never an inert button. Use interactive controls only when they perform their advertised action. If state is only conversation-local, label it **Session progress — not saved to AdNeuron**. If persisted by workflow_get or equivalent, label it **Saved draft** and include workflow ID/revision. Never fabricate progress percentages, provider results, or approvals.

## Eight user-facing steps
1. Choose platform and account
2. Verify connection, permissions and assets
3. Choose campaign objective and destination
4. Configure targeting, budget, bidding and schedule
5. Prepare creative, keywords and conversion readiness
6. Validate complete plan
7. Review preview and explicitly approve exact operation
8. Execute, reconcile and verify provider objects
Each step is only complete when required evidence exists. If a step is not applicable, mark skipped with reason.

## State transition rules
Read-only requests never perform writes. Preview is not approval. An approval is specific to the account, action, revision and exact plan fingerprint. Material edits invalidate approval. Creating paused never implies authorization to activate. Image upload, create, activate, modify, pause/resume and delete are distinct approvals. In-flight/ambiguous writes must be reconciled by backend/provider before retry. Report raw provider error codes and actionable next steps. The skill must not simulate idempotency or claim persistence.

## Platform rules
Meta: verify Page and Instagram identity independently; never substitute a page-backed Instagram identity for a real IG account. Facebook-only plans must omit Instagram identity and placements. Pixel is not automatically mandatory for link-click traffic.
Google: check conversion goals and action readiness for conversion-oriented campaigns; show keyword research, match types, ad groups, assets and tracking in Search plans. Missing conversion tracking may be a warning or blocker depending on objective and bidding, not universally mandatory.

## Tool orchestration
Use available live MCP tools and their schemas. Discover account and assets before creation; validate before preview; obtain explicit approval before any write; verify objects after execution. When durable workflow MCP operations are absent, do not invent calls; show session-only progress and recommend backend workflow_get/upsert_draft/validate/record_approval/execute/reconcile operations.

## Example state display
Campaign setup progress — Session progress (not saved to AdNeuron)
Platform: Google Search | Account: [verified account]
Progress: 3 of 8 steps complete
Completed: Account selected; access checked; objective selected
Current: Configure targeting, budget and schedule
Needs: Daily budget, location, schedule
Next: Ask user for the missing configuration; no changes made
