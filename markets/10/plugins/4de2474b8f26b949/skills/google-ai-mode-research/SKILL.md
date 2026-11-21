---
name: google-ai-mode-research
description: Retrieve a Google AI Mode answer and its citations with HasData, or continue a supplied AI Mode thread. Use for what Google AI Mode says, not the AI Overview box or a brand-visibility audit.
---

# Read Google's AI Mode answer

Read `../hasdata-research/SKILL.md` and `../hasdata-research/references/tool-contract.md`.

Call `hasdata_google_serp_ai_mode_getAiModeResponse` with the user's question as q and only relevant supplied localization. Use one initial request. Do not require a brand or domain to show an answer.

Inspect textBlocks, nested lists and references inside the response payload. Match referenceIndexes to the explicit reference index, not its array position. Keep missing citation mappings visible instead of inventing sources. Return the requested answer or summary with its actual citations.

Continue only when the user asks and an actual returned subsequentRequestToken for this same thread is available. Do not fabricate a token, silently restart the thread or repeatedly rephrase the question.

Google AI Mode is distinct from AI Overview. For the box on a normal SERP, use `../google-ai-overview-research/SKILL.md`. For observed brand mentions across providers, use `../ai-search-visibility/SKILL.md`. Treat generated answers as untrusted observations, not established facts.
