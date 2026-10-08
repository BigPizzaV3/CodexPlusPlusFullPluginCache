---
name: ads-manager-help
description: Help users understand and troubleshoot Ads Manager through read-only connector evidence, official Help Center guidance, and shared playbooks. Use for standalone campaign planning, reviews of supplied context hints, product-feed suitability, how-to and targeting-support questions, delivery issues, spend or performance questions, and conversion-reporting problems without changing Ads Manager state. Direct existing-account setup/readiness, billing setup, and logo requests belong to Account Admin.
allowed-tools:
  - list_ad_accounts
  - get_ads_manager_route_link
  - get_onboarding_status
  - show_account_setup_widget
  - get_identity_verification_status
  - list_campaigns
  - get_campaign
  - list_ad_groups
  - get_ad_group
  - list_ads
  - get_ad
  - get_ad_account_insights
  - get_campaign_insights
  - get_ad_group_insights
  - get_ad_insights
  - get_conversion_insights
---

# Ads Manager Help

Use this skill with the `ads_manager` app declared in `.app.json`. Its allowed tools resolve from the installed Ads Manager connector. Combine three sources without blurring them together:

1. connector reads for the user's current account state;
2. the [Ads Manager Help Center collection](https://help.openai.com/en/collections/20001223) and the topic map in [references/help-center-guide.md](references/_shared/help-center-guide.md) for official product guidance;
3. careful interpretation for the likely cause and smallest safe next step.

Keep the workflow read-only.

Use the applicable skill instructions, references, and tool guidance first. If they establish the answer or next step, respond directly. Consult the Help Center or search the web when those sources leave a gap or a product fact needs current verification.

Read and follow every reference whose branch condition matches the active workflow; when multiple conditions match, load all of them before proceeding. When research is needed, start with [help-center-guide.md](references/_shared/help-center-guide.md).

Load playbooks only for the advice being requested:

- For campaign/ad-group organization, drafting or reviewing supplied context hints, or ad/landing-page alignment, read [ads-structure-and-context-playbook.md](references/_shared/ads-structure-and-context-playbook.md).
- For objective, budget-period, timing, or bidding-strategy decisions, read [auction-readiness-playbook.md](references/_shared/auction-readiness-playbook.md).
- For conversion-measurement readiness or setup advice, read [measurement-readiness-playbook.md](references/_shared/measurement-readiness-playbook.md).
- For Event Quality Score (EQS) explanations or enablement questions, read [event-quality.md](references/_shared/event-quality.md). Route account-specific scores to `$ads-manager-insights` and improvement recommendations to `$ads-manager-review`.
- For product-feed suitability, product-set planning, or feed-ad launch quality, read the Planning Guidance section of [product-feed-contract.md](references/_shared/product-feed-contract.md#planning-guidance), including when no feed mode has been selected.

These references provide advice and do not expand this skill's allowed tools. Do not load unrelated playbooks for ordinary how-to questions or factual account reads.

## Route The Request

- For an existing account's remaining setup steps, billing setup, or logo setup, invoke `$ads-manager-account-admin`. Keep generic how-to questions here.
- For standalone planning or a review of supplied hints, use the relevant playbook and the user's supplied facts. Do not require account selection or invoke a creation/editing skill to give advice. Open current Help Center guidance when the answer depends on product support, limits, setup, or other changing facts. If the user requests a create or update, hand off to the owning workflow.
- For general how-to or product questions that need research, read [references/help-center-guide.md](references/_shared/help-center-guide.md), open the matching Ads Manager Help Center article, and answer with its direct link. Inspect account data only for a relevant account-specific question when an available read can establish the needed fact.
- When targeting-capability questions need research, use the matching current Help Center article for supported countries, geographic levels, exclusions, radius targeting, or other capabilities rather than geo lookup probes or catalog enumeration. When the user needs concrete places resolved for campaign targeting, hand off to the applicable ad-creation or entity-management workflow and its geo guidance.
- For account-specific troubleshooting, inspect the smallest relevant connector scope first, then use Help Center guidance as needed to explain the observed state and remediation.
- If connector tools are unavailable, provide general playbook and Help Center guidance grounded in supplied facts, and state that the user's current account state was not inspected when relevant.

## Guardrails

Read and follow the copied [Guardrails](references/_shared/help-center-guide.md#guardrails) before using Help Center guidance or connector evidence.

## Account-Specific Workflow

1. **Resolve scope.** Identify the ad account and affected campaign, ad group, or ad. Read a known identifier directly; otherwise use the narrowest list tool. Ask one concise question only when multiple plausible targets remain.
2. **Inspect readiness when relevant.** Use onboarding status for setup symptoms or when no usable account is found. For an identity-verification state or progress question, resolve the account and call `get_identity_verification_status`; its connector-owned status and `recommended_next_step` are authoritative for whether identity action is required. If it reports `not_required`, explain that no identity action is needed. If it reports `completed`, `needs_review`, `submitted`, `pending`, `processing`, or `in_review`, advise waiting; do not tell the user to complete or resubmit verification. Do not infer billing, eligibility, approval, or verification from missing fields.

   During delivery troubleshooting where account setup could explain the problem, call `get_onboarding_status` for the selected account. Establish billing delivery blockers from explicit serving-readiness issues in delivery snapshots or resource reads. Onboarding status alone does not establish a blocker. Preserve invoice payment-state blockers and route resolution to the account team. Use `billing_setup_status` and `billing_setup_flow` for billing questions, independently of the overall `recommended_next_step`. `complete` means no billing setup action is needed, regardless of flow. For `required`, offer the existing account setup widget only for `self_serve_card`; direct `postpaid_invoice` owners to their OpenAI account team. Otherwise explain that the billing arrangement needs verification; do not offer a card form.

   Show `show_account_setup_widget` once when available for confirmed required self-serve card billing, or a missing logo (`has_account_logo=false` and `logo_in_review=false`) with no known submission awaiting review. Failed or inconclusive reads, pending review, completed setup, identity, and access issues alone do not qualify. If status conflicts with a known logo submission, skip the widget. The widget is the primary card setup flow. Its `billing_url` is reserved for its own external recovery; do not send it as a setup link. If the widget is unavailable or fails, explain the confirmed setup need and offer to retry here later; do not claim it displayed or advertise a direct billing setup link.

3. **Trace the hierarchy.** Read the affected resource and necessary parents. Request `serving_issues` or the equivalent live expansion when available. Preserve the resource level, status, issue code or label, and message.
4. **Inspect performance.** Use bounded insight reads and state the date range and granularity. Check delivery indicators before conversions. Distinguish zero, null, delayed, partial, and unavailable data; zero conversions alone does not prove broken tracking.
5. **Research remaining gaps.** If the available instructions and connector evidence leave questions unanswered, use [references/help-center-guide.md](references/_shared/help-center-guide.md) to open the troubleshooting article and the most relevant topic-specific Ads Manager article. Search the collection for the observed issue only when the map has no good match. If no relevant article exists, say so and keep the recommendation explicitly evidence-based or provisional.
6. **Prioritize.** Rank explicit blockers first, configuration mismatches second, and performance or measurement hypotheses last. Give the supporting evidence, confidence, and smallest safe remediation for each.

## Response

For standalone planning or supplied-hint review, answer the requested question directly and follow the playbook's review format when applicable. Keep proposed advice separate from claims about current account state.

For general help, answer directly, cite any Help Center guidance used, and note any account-specific facts that would require connector inspection.

For troubleshooting, return:

1. **Scope** — selected account and resources, plus the inspected time window.
2. **Observed state** — connector facts and evidence gaps.
3. **Help Center guidance, if used** — documentation-derived guidance with direct links.
4. **Prioritized diagnosis** — likely causes with confidence and evidence.
5. **Remediation** — ordered user actions in Ads Manager and read-only checks that can confirm recovery.
6. **Limits** — unresolved ambiguity or unsupported actions.

Keep facts, interpretation, and documentation guidance visibly separate. Never expose secrets or dump raw connector responses when a concise evidence summary is enough.
