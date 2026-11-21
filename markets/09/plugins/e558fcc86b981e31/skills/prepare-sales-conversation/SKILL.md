---
name: prepare-sales-conversation
description: Use when the user asks to prepare for a sales conversation with one or more buyers using canonical BuyerTwin intelligence plus any user-provided prospect context.
---

Use this skill when the user asks for practical preparation before a discovery, demo, qualification, proposal, executive, follow-up, or related sales conversation.

Do not use this as the primary workflow for:
- pure buyer-reaction simulation
- canonical buyer-comparison requests
- supplied-message diagnosis
- net-new content generation requests
- buyer knowledge mutation

Core workflow:
1. Resolve BuyerTwin scope deterministically.
2. Identify user-provided prospect, account, offering, meeting objective, and stage context.
3. Retrieve only BuyerTwin intelligence materially relevant to this conversation.
4. Separate BuyerTwin patterns from prospect-specific facts and unknowns to validate.
5. Prepare likely priorities, triggers/context, desired outcomes, decision criteria, objections/concerns, proof areas, discovery questions, listening cues, framing guidance, and stakeholder differences where relevant.
6. Use ask_buyer selectively for rehearsal/reaction testing when useful.
7. Do not convert BuyerTwin patterns into asserted facts about the specific prospect.

Prospect-vs-BuyerTwin boundary:
- BuyerTwin intelligence describes buyer-type patterns.
- User-provided prospect context describes the actual person/account/opportunity.
- AI synthesis provides preparation recommendations.
- Do not claim BuyerTwin knows specific prospect beliefs unless the user supplied that prospect-specific evidence.

Buyer scope rules:
- One named BuyerTwin means that buyer.
- Multiple named BuyerTwins means all named buyers.
- Explicit segment/subset means that subset.
- "All buyers" means all accessible buyers in scope.
- "My buyers" without narrowing defaults to all accessible buyers in scope.
- Do not silently choose buyers by model-defined relevance.
- If prospect-role mapping to BuyerTwin is ambiguous, surface the ambiguity instead of assuming an exact match.

Authority by domain:
- BuyerTwin Knowledge is authoritative for what BuyerTwin canonically knows about buyer type and buyer context patterns.
- User-provided prospect/opportunity facts are authoritative for the specific person, account, and meeting.
- BuyerTwin Simulation (ask_buyer) is optional reasoning and authoritative for neither domain.
- AI Synthesis provides preparation recommendations.
- BuyerTwin describes the buyer pattern. Prospect evidence describes this prospect.
- If BuyerTwin patterns and prospect facts differ, do not treat this as a global contradiction where one source overrides all others.
- Use prospect-specific facts for this meeting while retaining relevant BuyerTwin context as broader hypothesis/background where appropriate.

Sales-prep guardrails:
- Do not assume CRM, email, call-recording, account-intelligence, or private prospect-history access unless user provides it.
- Do not invent product capabilities, customer outcomes, ROI values, or certifications.
- Do not invent certainty scores such as close probability or deal-risk percentages.
- If stage is unknown, provide useful general preparation without inventing a stage.

For a follow-up email or other finished artifact, continue with `create-buyer-content` using [conversation continuity](../create-buyer-content/references/buyer-content-methodology.md#conversation-continuity). Retain the buyer and supplied meeting/prospect facts, distinguish suggested talking points or simulated rehearsal from events that actually occurred, and apply the requested saved writing voice. Preparation alone is not evidence that a meeting happened or a commitment was made.

For detailed sales-prep methodology and edge-case handling, consult:
- references/sales-conversation-methodology.md
