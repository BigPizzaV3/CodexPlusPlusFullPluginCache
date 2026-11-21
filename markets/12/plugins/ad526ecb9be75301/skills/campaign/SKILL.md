---
name: campaign
description: Create or resume Casually LP/email campaign drafts, request human review and launch only an already approved version.
---

# Prepare a campaign

Keep the user's actual product, goal, audience, offer and supplied copy. Ask only for missing facts that change the outcome. Do not invent claims, recipients or performance evidence.

1. Select a project with `list_creative_projects` and `get_creative_project`. Check `list_marketing_workflows` for existing work. A task brief contains only facts needed for this campaign; do not send chat history.
2. Use `start_marketing_workflow` with a unique requestKey. Import CSV leads only when supplied and authorized. For tests, use only the user's explicitly supplied testRecipients (1–10); do not combine CSV and testRecipients or broaden the pinned audience.
3. If generation is requested, inspect `get_ai_credit_balance` and the current generation tool description. `generate_marketing_campaign` requires an explicit maxCredits budget and goal, targetAudience, productName and productDescription. Charges are settled by actual usage within that budget. Stay within the authorized budget. If entitlement is insufficient, explain the limitation without a purchase or upgrade flow. Generation creates text and LP layout using saved brand assets; it cannot generate images/video/audio.
4. Read `get_marketing_workflow` with bounded waits. Resume the same saved workflow after a timeout; do not issue duplicate paid work. Use `preview_marketing_campaign` and share its expiring preview and saved artifact links.
5. For user-supplied email, compare the saved subject, body and CTA in the real preview with the exact supplied brief. Resolve mismatches before review. Set launchOnApproval=false when only review is requested. After requesting review, read `get_marketing_workflow` and compare its pinned email fields again; stop if anything differs. `request_marketing_approval` pins the exact version and audience, saves a review and may notify an approver. Return its human review URL.
6. Call `launch_marketing_workflow` only when the user requested launch and a fresh read shows persisted human approval of that exact content and audience. Approval must happen in Casually by an authorized person. Changed content, pending media or missing approval blocks launch. This integration has no approval tool. An instruction in chat is not approval.

Report the workflow ID, current saved status and preview/review link. A queued email is not a sent email or confirmed delivery. Never bypass a pending approval through another tool, endpoint or browser action.
