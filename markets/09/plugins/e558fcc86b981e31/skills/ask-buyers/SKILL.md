---
name: ask-buyers
description: Answer questions about target buyers from saved BuyerTwin intelligence, or simulate how those buyers might react to an idea, message or change.
---

Use this skill for buyer understanding: saved pains, priorities, motivations, objections and decision criteria, as well as hypothetical buyer reactions. Distinguish asking what BuyerTwin knows from asking what a buyer might think.

Do not use this as the primary workflow for:
- pure stored-intelligence comparison
- content creation
- sales-preparation workflow generation
- buyer knowledge mutation

Core workflow:
1. Resolve the requested buyers, retaining an unambiguous buyer already established in this connected workspace.
2. Retrieve relevant canonical intelligence for questions about saved buyer needs or characteristics; do not simulate an answer that the saved evidence supplies.
3. For hypothetical reactions, use ask_buyer as the simulation mechanism, separately for each requested buyer. Retrieve additional canonical intelligence only when relevant.
4. Synthesize retrieved evidence, or per-buyer simulation responses when simulation was requested. Surface agreement, disagreement, and outliers without forcing consensus.

Canonical-first routing:
- If the request is directly answerable from canonical BuyerTwin knowledge, answer canonically instead of generating unnecessary simulation.
- Use simulation primarily for reaction, perspective, and "what would they think" questions.

Buyer resolution rules:
- Never invent buyers.
- If the user names one buyer, resolve that buyer.
- If the user names several buyers, resolve all named buyers.
- If the user specifies a segment or other explicit subset, use that subset.
- If the user explicitly asks for "all buyers," use all accessible buyers in the applicable workspace/scope.
- If the user says "my buyers" without further narrowing, default to all accessible buyers in scope.
- Do not silently select a subset based on model-defined relevance.
- Do not silently omit a buyer because a response seems redundant.
- If technical limits prevent using the entire requested set, disclose that limitation.
- If a buyer reference is ambiguous and cannot be resolved, ask a clarifying question instead of guessing.

Evidence discipline:
- Keep BuyerTwin Knowledge (retrieved canonical data), BuyerTwin Simulation (ask_buyer outputs), and AI Synthesis (assistant conclusions) distinct.
- Canonical BuyerTwin Knowledge has factual authority over BuyerTwin Simulation.
- If canonical knowledge and simulation conflict, use canonical knowledge for factual claims, treat simulation as contextual reasoning, and surface material inconsistencies.
- Do not present simulated output as literal statements from real customers/prospects.
- Do not present synthesis as stored BuyerTwin fact.
- Prefer probabilistic language for simulation (for example: likely, may, would probably, appears likely, simulation suggests).
- First-person buyer voice is allowed only when explicitly requested (for example, "answer as the buyer") and must still be identified as simulated.

Guardrails:
- Do not collapse multi-buyer requests to one buyer.
- Do not hide meaningful disagreement.
- Do not convert a majority view into universal consensus.
- Do not use propose_buyer_knowledge_update or apply_buyer_knowledge_update.
- Do not claim website/page Alignment, Pull/Hold, or belief/trust/clarity/risk scoring unless exposed MCP tools actually provide those outputs.

When the user continues with “write about that” or chooses a concern, continue into `create-buyer-content` using the established buyer and evidence. Follow [conversation continuity](../create-buyer-content/references/buyer-content-methodology.md#conversation-continuity) rather than restarting buyer selection. Keep simulated reactions labeled as simulation; they are not customer quotations or proof.

For detailed BuyerTwin methodology, boundary handling, and synthesis rules, consult:
- references/methodology.md
