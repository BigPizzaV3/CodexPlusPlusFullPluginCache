---
name: evaluate-messaging
description: Use when the user asks how well supplied messaging aligns with what BuyerTwin knows about one or more buyers, including what works, what is missing, and what should change.
---

Use this skill when the user asks to evaluate a supplied message against buyer intelligence, such as a headline, value proposition, positioning statement, CTA, paragraph, email, ad copy, campaign concept, sales message, or product description.

Do not use this as the primary workflow for:
- pure buyer-reaction simulation without message evaluation
- stored buyer comparison without evaluating a supplied message
- net-new content generation
- sales call preparation
- buyer knowledge mutation

Core workflow:
1. Resolve buyer scope deterministically.
2. Determine the apparent purpose of the supplied message artifact (for example headline, value proposition, CTA, positioning statement, short ad, email opener, objection-handling paragraph, or sales message).
3. Retrieve canonical BuyerTwin intelligence relevant to the supplied message, purpose, and question.
4. Evaluate message-to-evidence alignment (what works, what is missing, what mismatches, what needs substantiation, and what remains unknown).
5. Preserve buyer-specific differences and tradeoffs for multi-buyer evaluations.
6. Recommend targeted improvements grounded in evidence and clearly labeled AI synthesis.
7. Use ask_buyer selectively only when simulated reaction materially deepens evaluation.

Buyer scope rules:
- One named buyer means evaluate for that buyer.
- Multiple named buyers means evaluate for all named buyers.
- Explicit segment/subset means evaluate that subset.
- "All buyers" means all accessible buyers in scope.
- "My buyers" without narrowing defaults to all accessible buyers in scope.
- Do not silently select a subset by model-defined relevance.

Evidence hierarchy:
- BuyerTwin Knowledge is authoritative for retrieved buyer facts, not verification of company/product/customer claims.
- BuyerTwin Simulation (ask_buyer) is optional and cannot override canonical knowledge.
- AI Synthesis provides diagnosis and recommendations.
- Do not present synthesis as stored BuyerTwin fact.

Evaluation guardrails:
- Do not invent numeric alignment scores or proprietary scoring dimensions unless an exposed MCP tool returns them.
- Do not claim Website Alignment or page-level analysis outputs unless exposed MCP tools provide them.
- Treat missing evidence as unknown, not automatically negative.
- "Missing" means BuyerTwin contains intelligence materially relevant to this message objective and omitting it weakens the message; it does not mean every known buyer priority must appear in every message.
- Evaluate messages relative to what that artifact can reasonably accomplish; do not penalize short artifacts (for example headlines) for not containing every objection, proof point, or criterion.
- If message purpose is uncertain, limit confidence and conclusions rather than inventing a purpose.
- Avoid using ask_buyer to replace available canonical evidence.

If the user explicitly asks to improve or rewrite after evaluation, diagnose first, then provide concise revisions grounded in diagnosed buyer issues. Retain the established buyer, selected insight and supplied facts using [conversation continuity](../create-buyer-content/references/buyer-content-methodology.md#conversation-continuity). For finished revisions, use [saved writing guidance](../manage-writing-guidance/references/use-saved-writing-guidance.md), including the requested company/person voice, channel and actual examples. Pure diagnosis does not require loading a voice. Do not force a separate skill switch or rewrite when only evaluation was requested.

For detailed messaging-evaluation methodology and edge-case handling, consult:
- references/messaging-evaluation-methodology.md
