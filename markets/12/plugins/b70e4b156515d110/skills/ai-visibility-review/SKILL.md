---
name: ai-visibility-review
description: Review how a brand appears in AI assistant answers and AI search using CitationLab AI Monitor. Use for questions about AI visibility, share of voice, citations, mentions or which competitors AI assistants recommend.
---

# AI visibility review

All tools need `projectId`; most accept `startDate`/`endDate` (YYYY-MM-DD) and `models[]` (`chatgpt`, `gemini`, `claude`, `perplexity`).

1. **Overview:** `get_ai_monitor_report` — topics, recent answers, sentiment and overall visibility in one call.
2. **Trend:** `get_ai_visibility_trend` — is visibility rising or falling over the period?
3. **Share of voice:** `get_ai_share_of_voice` — the brand against its competitors.
4. **Who wins instead:** `get_ai_competitors` — brands mentioned in the answers.
5. **Where the answers come from:** `get_ai_citations` with `view: "domains"`, then `view: "urls"` for the brand's own pages that get cited. `get_ai_mentions` for how the brand is named.
6. **Per assistant:** `get_ai_model_performance` with `view: "comparison"` when the person asks which assistant is weakest.
7. **The actual answers:** `list_ai_prompts`, then `get_ai_prompt_responses` with a `promptId` the person wants to read.

## How to report

- Lead with the change and its size over the period, then the two or three biggest gaps (assistants, topics or competitors), then concrete next steps.
- Quote numbers exactly as returned; say which date range and which assistants they cover.
- If the project has no prompts or no runs yet, say so: prompts are set up in the CitationLab app under AI Monitor.
- Offer to turn the next steps into actions (see the `actions-and-follow-up` skill).
