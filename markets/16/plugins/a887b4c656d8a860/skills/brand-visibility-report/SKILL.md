---
name: brand-visibility-report
description: Build an AI visibility report for a brand monitored in First Answer, covering mention rate, sentiment, competitor ranking, most cited sources and open recommendations for a date range. Use when the user asks how their brand is performing in AI answers, how it compares with competitors, or what to do to improve its AI visibility.
---

Use this skill when the user asks for an overview of a brand's visibility in AI-generated answers using their First Answer data.

Explicit user instructions take priority over these steps.

1. Call `list_brands`. If the account has more than one brand and the user did not name one, ask which brand to analyze. Do not guess.
2. Define the date range. Use the range the user gave. If none was given, use the last 30 days ending today and say so in the answer. Dates use the YYYY-MM-DD format.
3. Call `get_dashboard` with the `brand_id` and the date range. If the user asked about a specific AI model, pass `ai_model` (chat_gpt, perplexity, bing_copilot, google_ai, gemini, grok, google_ai_mode).
4. Call `list_cited_sources` with the same filters to get the most cited domains.
5. Call `list_recommendations` with `status='open'` and `order_by='-priority'`.
6. Answer with:
   - Summary metrics: total prompts, total responses, brand mention rate and average sentiment.
   - Competitor ranking from the dashboard.
   - Top cited domains.
   - Open recommendations, highest priority first, with title and category.

Rules:

- Report only values returned by the tools. Do not estimate or invent metrics, competitors, domains or recommendations.
- If a tool returns no data for the period, say that no data was found for that period.
- If a tool returns an error object, explain the error message to the user and do not retry the same call.
- This report only reads data. Do not create prompts, competitors, groups or categories while building it. If the user then asks to add prompts or competitors, set a competitor's website, or to create, rename or change groups and categories, use the First Answer write tools only after the user confirms the exact change, and call `get_usage_limits` first to check the plan limits.
- Deleting anything, and editing brands, prompt texts, competitor names or recommendations, is not available in the tools. Explain that this must be done in the First Answer app.
