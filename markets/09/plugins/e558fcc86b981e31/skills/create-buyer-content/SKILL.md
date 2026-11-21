---
name: create-buyer-content
description: Create or rewrite buyer-facing content and briefs from BuyerTwin insights, including follow-up drafts and saved company or named voices.
---

Use this skill for content strategy/briefs, finished drafts and follow-up writing for buyers, segments or supplied audiences. It also handles a request to write or rewrite in a saved company/person voice without a buyer-persona requirement.

Do not use this as the primary workflow for:
- buyer reaction simulation requests
- stored buyer comparison requests
- supplied-message evaluation requests
- sales-call preparation workflows
- buyer knowledge mutation

Core workflow:
1. Carry forward an unambiguous buyer and selected insight from the conversation; otherwise resolve requested buyer scope. For voice-only writing, use the supplied audience/task without inventing a buyer.
2. For buyer-grounded work, establish buyer context before drafting: situation, objective movement, relevant tensions, likely questions, objections, proof needs, and useful terminology.
3. Retrieve only canonical BuyerTwin intelligence needed for the requested artifact; voice-only work does not require buyer research.
4. Determine whether the user asked for brief mode or finished-content mode.
5. Load saved company or named-voice writing context using the guidance below.
6. For multi-buyer requests, identify shared versus buyer-specific intelligence before writing.
7. Create strategy and/or content grounded in evidence, preserving meaningful differences.
8. Use ask_buyer selectively only when reaction testing materially improves strategy.
9. Treat compatible saved voice preferences as the writing defaults, not suggestions to mention and ignore. Before drafting, identify the applicable requirements, preferences and examples; before returning copy, make one editorial pass and correct departures throughout the artifact. For a saved count or limit, allocate the allowed instances across the whole artifact and express other ideas as statements. Inspect actual occurrences of questions (including rhetorical questions), paragraph length, opening style, vocabulary, punctuation and calls to action where the guide specifies them; do not claim a count based only on the closing paragraph. Carry these defaults through follow-up rewrites without requiring the user to restate them. Respect channel/format scope and explicit brief overrides; do not promote preferences to binding shared rules. Read the shared writing reference below for the complete procedure.

Buyer scope rules:
- One named buyer means that buyer.
- Multiple named buyers means all named buyers.
- Explicit segment/subset means that subset.
- "All buyers" means all accessible buyers in scope.
- "My buyers" without narrowing defaults to all accessible buyers in scope.
- Do not silently choose a relevance-based subset.

Evidence hierarchy:
- BuyerTwin Knowledge is authoritative for buyer facts.
- BuyerTwin Simulation (ask_buyer) is optional and selective.
- AI Synthesis covers strategy, structure, and generated content.
- Generated content is not canonical BuyerTwin knowledge.
- BuyerTwin establishes buyer relevance, buyer context, and buyer perspective; it does not establish factual truth of company, product, competitor, customer, or market claims.

Content guardrails:
- Do not invent company/product/market facts, proof, statistics, quotes, case-study outcomes, or competitor claims.
- If evidence is needed but unavailable, request it or use explicit placeholder guidance.
- Do not start with generic copy and then append persona keywords.
- Adapt depth to artifact type and message purpose.
- If buyers are too different for one artifact, recommend variants rather than forcing an artificial average.
- Do not claim Website Alignment analysis unless exposed MCP tools provide those outputs.

For “write about that,” a selected concern, a new format, or a named-voice revision, follow [conversation continuity](references/buyer-content-methodology.md#conversation-continuity). Keep the buyer evidence and requested scope while changing only what the new brief asks for. A request for finished content does not require a separate brief or approval of an angle unless a consequential choice is unresolved.

For detailed buyer-content strategy methodology, consult:
- references/buyer-content-methodology.md

## Shared writing guidance

For finished drafting, including rewrites, use applicable published writing guidance. Initially retrieve `get_company_writing_guide` for the connected workspace. Reuse an already retrieved applicable voice snapshot within the immediate revision when target/channel and version information remain valid; refresh after a known guide change or when freshness is uncertain. When a person voice is requested, resolve it with `list_named_voices`, then call `get_voice_writing_context` with its stable `target_profile_id` and the requested channel. Ask about duplicate names or unavailable voices; do not silently substitute another target. If no guide exists, disclose that and continue with the user’s supplied style or offer setup. Tool unavailability is not evidence that no guide exists.

Follow [using saved writing guidance](../manage-writing-guidance/references/use-saved-writing-guidance.md) for canonical entry resolution, example provenance, format conditions and voice checks. Use the returned effective/applied guidance and canonical entry references. Company requirements and terminology remain binding; apply person and channel overrides only as resolved by the service. Retain author names plus the selected qualities to borrow/avoid and blend direction when forming the writing instructions. Do not flatten the blend into anonymous adjectives or invent author attribution. Published writing examples inform expression according to their annotations; saving one does not establish author approval or evidence about products or buyers.

Drafting does not save guidance, create a guide example or update buyer knowledge. For explicit shared-guide changes, use `manage-writing-guidance`; for buyer knowledge mutation, use `update-buyer-knowledge`. A request to try a sample alone is not approval to publish a rule or example. Do not claim an in-app private sample was stored through a public MCP tool.

For portable instructions, use `get_writing_instructions_markdown` with the resolved company/person target and requested mode/channel. Return its Markdown faithfully with snapshot metadata; do not substitute the draft article or private chat. If the connected catalog lacks writing tools, disclose that limitation rather than inventing calls or saved guidance.
