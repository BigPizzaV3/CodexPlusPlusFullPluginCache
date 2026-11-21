---
name: brand-perception-audit
description: Use when the user asks how AI assistants describe their brand, about brand sentiment, reputation in AI answers, whether AI says anything wrong or outdated about them, or how their messaging comes across in ChatGPT, Claude, Gemini or Perplexity.
---
# Brand perception audit
1. list_workspaces. Then get_sentiment_breakdown: the overall score, per-model scores and excerpts.
2. get_ai_answers with brand_mentioned=true: read a page or two of answers that mention the brand.
Output:
- how AI describes the brand: themes, strengths, weaknesses;
- differences between models;
- statements that look inaccurate, outdated or off-message, each quoted with model and date, for the user to verify;
- the gap between how AI describes the brand and how the user wants to be positioned, if they say;
- what to publish or correct so future answers improve.
Flag claims to check. Never assert they are false without evidence.

