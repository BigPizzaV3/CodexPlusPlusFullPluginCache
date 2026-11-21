---
name: update-buyer-knowledge
description: Use when the user explicitly asks to add, correct, or update canonical BuyerTwin knowledge for one or more specific buyers via the proposal/apply mutation workflow.
---

Use this skill when the user explicitly asks to change canonical BuyerTwin knowledge.

Do not use this as the primary workflow for:
- buyer simulation
- buyer comparison
- messaging evaluation
- content creation
- sales-conversation preparation
- hypothetical brainstorming without explicit save/update intent

Activation rule:
- Require explicit mutation intent before calling mutation tools.
- For a follow-up such as “save that concern,” retain the established buyer and resolve what “that” means. Do not save an entire draft, invented claim or simulated customer quote as canonical evidence. If meaning or buyer scope is ambiguous, clarify before proposing; do not strengthen source/provenance merely because the prior output was useful.
- Do not mutate from simulation output, AI synthesis, or casual statements unless the user explicitly asks to save/update BuyerTwin.

Core workflow:
1. Identify explicit mutation intent.
2. Resolve deterministic buyer target scope.
3. Preserve user meaning and qualifiers.
4. Call propose_buyer_knowledge_update.
5. Treat proposal output as the authoritative preview.
6. Verify proposal fidelity against the user's intended buyer, scope, meaning, qualifiers, and requested correction/addition intent.
7. If fidelity fails, do not apply; re-propose the original user instruction without inventing routing hints, or ask for minimum clarification.
8. Present concise proposal review details when needed.
9. Follow tool-returned confirmation policy.
10. Call apply_buyer_knowledge_update only through supported proposal/apply paths.
11. Report only authoritative apply outcome.
12. Handle duplicate, stale, expired, mismatch, unauthorized, and uncertain outcomes per tool semantics.

Classification authority on general intake:
- For `propose_buyer_knowledge_update`, do not send classification overrides such as `explicit_destination` or `explicit_target_key`.
- Submit user knowledge with preserved meaning and let BuyerTwin classify through canonical routing.
- Use the dedicated resolution workflow when a trusted human must explicitly re-target existing knowledge.

Retry lock for proposal_mismatch:
- A retry must not alter `knowledge_text`, `intent_level`, or `verification_intent` unless the user provided new information.
- If a new proposal is required, base it on the original user instruction and do not promote advisory suggestions into explicit targets.
- Do not automatically re-propose after `proposal_mismatch`; report the authoritative failure first and wait for explicit user direction before attempting another proposal.

Mutation safety rules:
- Never bypass proposal step.
- Never claim success after propose only.
- Never apply proposal to a different buyer or different change.
- Do not broaden a buyer-scoped request to all buyers.
- Preserve semantic qualifiers such as usually, often, may, when, and exceptions.
- Proposal fidelity and tool confirmation are separate gates; both must pass before apply.
- Do not reject meaning-preserving normalization or harmless internal routing label differences.
- If apply fails, report the authoritative failure and proposal state only; do not speculate a model-chosen classification as BuyerTwin truth.
- Do not attempt reclassification retries after apply failure to force a preferred category; preserve BuyerTwin authority boundaries.
- If apply succeeds with uncategorized capture (`create_uncategorized` / `inbox_created`), report that it was saved to Needs Review using BuyerTwin-authoritative result state.

Authority boundaries:
- BuyerTwin Simulation and AI Synthesis are not canonical knowledge writes.
- User intent plus supported mutation workflow is required for canonical changes.
- Preserve provenance/trust semantics supported by the mutation contract; do not fabricate stronger provenance than provided.

For detailed mutation methodology, confirmation semantics, conflict handling, and multi-buyer orchestration guidance, consult:
- references/buyer-knowledge-update-methodology.md
