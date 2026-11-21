---
name: ai-answer-research
description: Use when the user wants to see or quote what AI assistants actually say, such as "show me ChatGPT's answers about X", answers that don't mention us, examples for a slide or report, or checking which brands an AI recommends for a question.
---
# AI answer research
Use get_ai_answers, with the filters the user implies: prompt_text, model, brand_name with brand_mentioned true or false, and the period.
- Start with one page. Fetch more with offset only when needed, and say when the results are a partial page.
- Use full_text=true only for the single answer the user wants in full.
- Present each answer with question, model and date, a short excerpt or the requested quote, the brands mentioned and the cited URLs.
- Never present page counts as totals. Use total_answers for the full count.
These are recorded answers from Refora's scheduled monitoring, not new model runs.

