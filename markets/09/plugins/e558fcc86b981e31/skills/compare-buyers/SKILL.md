---
name: compare-buyers
description: Use when the user asks for similarities, differences, patterns, or implications across two or more buyers based on canonical BuyerTwin intelligence.
---

Use this skill when the user asks to compare buyers, such as shared pains, differing triggers, contrasting objections, universal themes, buyer-specific priorities, or where messaging should be universal vs personalized.

Do not use this as the primary workflow for:
- simulated buyer reactions to a new idea or change
- role-play in buyer voice
- content generation
- messaging evaluation workflows
- buyer knowledge mutation

Core workflow:
1. Resolve requested buyer scope deterministically before comparison.
2. Retrieve canonical BuyerTwin intelligence relevant to the user question.
3. Compare evidence across at least two buyers.
4. Distinguish universal, majority, buyer-specific evidence, contrasting, and missing/unknown patterns only when evidence supports each label.
5. Provide implications as AI synthesis while preserving evidence boundaries.

Buyer scope rules:
- Named buyer means resolve that specific buyer.
- Multiple named buyers means resolve all named buyers.
- Explicit segment or subset means compare that exact subset.
- "All buyers" means all accessible buyers in scope.
- "My buyers" without narrowing defaults to all accessible buyers in scope.
- Do not silently narrow scope by model-defined relevance.
- Do not silently omit buyers because they appear redundant.
- If technical limits prevent full requested scope, disclose the limitation.
- If fewer than two buyers are available, explain that reliable comparison is not possible.

Canonical-first comparison rules:
- Use canonical BuyerTwin intelligence as the evidence base.
- Do not use ask_buyer as the normal comparison mechanism.
- If canonical intelligence can answer directly, do not generate simulation-based restatements.
- If evidence is missing, state what is missing instead of fabricating differences.

Evidence hierarchy:
- BuyerTwin Knowledge is authoritative for factual claims.
- AI Synthesis may infer implications from that knowledge.
- Do not present synthesis as a stored BuyerTwin fact.
- Do not treat missing evidence as negative evidence.
- Do not equate frequency with formal priority unless ranking evidence exists.

If the user asks what to write after the comparison, use its supported differences to recommend an angle or create requested buyer-specific versions. Follow [conversation continuity](../create-buyer-content/references/buyer-content-methodology.md#conversation-continuity), preserving the compared scope unless the user explicitly chooses a buyer/subset. Do not force a second comparison or average away meaningful differences.

For detailed methodology and edge-case handling, consult:
- references/comparison-methodology.md
