---
name: ads-manager-delivery-recovery
description: Diagnose why an existing Ads Manager account, campaign, ad group, or ad is not delivering or scaling, then produce a prioritized read-only recovery plan grounded in live connector evidence and official Help Center guidance. Use when the user reports low or zero impressions, spend, clicks, or conversions; delivery drops; limited delivery; serving issues; or uncertainty about what is blocking expansion.
allowed-tools:
  - list_ad_accounts
  - get_onboarding_status
  - show_account_setup_widget
  - get_identity_verification_status
  - list_campaigns
  - get_campaign
  - show_campaign_delivery
  - list_ad_groups
  - get_ad_group
  - list_ads
  - get_ad
  - get_ad_account_insights
  - get_campaign_insights
  - get_ad_group_insights
  - get_ad_insights
  - list_conversion_sources
  - list_conversion_event_settings
  - list_conversion_events
  - get_conversion_insights
---

# Ads Manager Delivery Recovery

Identify the first constrained layer in the delivery funnel before recommending expansion. Keep the entire workflow read-only.

## Use the Help Center Guide

Read and follow the [shared Help Center guide](references/_shared/help-center-guide.md) before reading account data. Use its topic map, source-separation rules, and safety guardrails directly. Do not invoke `$ads-manager-help`, duplicate its Help Center research, or use another documentation source.

Before advancing into diagnosis, read and follow every reference whose branch condition matches the active workflow; when multiple conditions match, load all of them before proceeding. Before interpreting or comparing performance or conversion metrics, read and follow [insights-contract.md](references/_shared/insights-contract.md). Before using Help Center guidance, also read and follow [help-center-guide.md](references/_shared/help-center-guide.md).

## Diagnose the Delivery Funnel

For campaign delivery questions, use `show_campaign_delivery` when available:
`request.view="summary"` with the resolved account for account-wide checks, or
`request.view="detail"` with that account and the exact campaign ID for a selected
campaign's diagnosis or readiness. Choose by intent, not result count; complete
healthy checks are also useful. Show known issues from the snapshot; follow the
deeper funnel below when the user needs further diagnosis. Keep account blockers separate and
do not interpret skipped or unavailable checks as an all-clear. Review issues
link to the returned Ads Manager page. If the widget is unavailable, use existing
reads and a concise text explanation.

1. Resolve one ad account and the affected campaign, ad group, or ad. Ask only when multiple plausible resources remain.
2. Establish the requested time window and a comparable prior window when available. State both.
3. Trace the selected resource and its required parents. Request live serving issues when the tool schema supports them.
4. Inspect delivery in order: impressions, spend, clicks, then conversions. Distinguish zero, null, delayed, partial, and unavailable data.
5. Identify the earliest supported constraint:
   - account readiness, access, identity, or billing guidance returned by the connector;
   - campaign status, schedule, budget, or explicit campaign-level issue;
   - ad-group bidding, targeting, status, or explicit ad-group issue;
   - ad status, review, creative, landing-page, or explicit ad-level issue;
   - measurement or attribution when delivery exists but conversions are absent;
   - insufficient evidence when no explicit blocker or meaningful comparison exists.
6. Open the most relevant Ads Manager Help Center article using the [shared Help Center guide](references/_shared/help-center-guide.md). Use documentation to explain remediation, never to claim that a user-specific condition exists.
7. Rank explicit blockers before configuration mismatches, performance hypotheses, and expansion ideas.

When account setup could explain the delivery problem, call `get_onboarding_status` for the selected account. Establish billing delivery blockers from explicit serving-readiness issues in delivery snapshots or resource reads. Onboarding status alone does not establish a blocker. Preserve invoice payment-state blockers and route resolution to the account team. Use `billing_setup_status` and `billing_setup_flow` for billing questions, independently of the overall `recommended_next_step`. `complete` means no billing setup action is needed, regardless of flow. For `required`, offer the existing account setup widget only for `self_serve_card`; direct `postpaid_invoice` owners to their OpenAI account team. Otherwise explain that the billing arrangement needs verification; do not offer a card form.

Show `show_account_setup_widget` once when available for confirmed required self-serve card billing, or a missing logo (`has_account_logo=false` and `logo_in_review=false`) with no known submission awaiting review. Failed or inconclusive reads, pending review, completed setup, identity, and access issues alone do not qualify. If status conflicts with a known logo submission, skip the widget. During delivery recovery, the confirmed setup need must explain the delivery problem. The widget is the primary card setup flow. Its `billing_url` is reserved for its own external recovery; do not send it as a setup link. If the widget is unavailable or fails, explain the confirmed setup need and offer to retry here later; do not claim it displayed or advertise a direct billing setup link.

Prioritize account blockers before campaign changes. A confirmed lifetime-budget
blocker or low-bid warning can support a targeted proposal, but resolving it may
reveal downstream issues skipped by the earlier check. Do not recommend expansion
from performance alone before checking readiness, serving, and measurement.
Zero conversions alone does not prove a delivery failure.

The widget's increase, `unpause_campaign`, and `unpause_ads` actions start a
proposal request owned by `$ads-manager-entity-management`. Its `create_ads`
action starts drafting for the
selected campaign in `$ads-manager-ad-creation`; preserve the attached account
and campaign IDs for validation there. These clicks do not authorize a write. Keep
this diagnostic workflow read-only. Refresh delivery after an approved change
and distinguish acceptance of the change from observed recovery.

## Return a Recovery Plan

Return:

1. **Scope** — account, resources, current window, and comparison window.
2. **Delivery funnel** — impressions, spend, clicks, and conversions, noting unavailable evidence.
3. **Primary constraint** — the first constrained layer, supporting connector evidence, confidence, and the relevant Help Center guidance.
4. **Recovery steps** — ordered user actions in Ads Manager, starting with the smallest safe fix.
5. **Verification** — the exact read-only checks and time window that can confirm recovery.
6. **Expansion readiness** — `blocked`, `ready to test`, or `insufficient evidence`, with the reason.

Keep connector facts, Help Center guidance, and inference visibly separate. Never create, edit, pause, activate, upload, appeal, or otherwise mutate Ads Manager state.
