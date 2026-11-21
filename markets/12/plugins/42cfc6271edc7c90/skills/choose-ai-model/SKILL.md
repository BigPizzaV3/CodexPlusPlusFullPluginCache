---
name: choose-ai-model
description: Use when someone is choosing an AI model, AI chatbot or LLM. That covers which one to use for a task such as coding, writing, emails, data analysis, long PDFs, screenshots and charts, or image generation; which one works well in a language other than English; which one is cheapest for high-volume or API use; and how two to four named models or brands, such as Claude, ChatGPT, Gemini or DeepSeek, compare on price, context window and scores.
---

# Choose an AI model

Answer "which AI should I use?" with Whizi Model Finder data: picks per task and language, list prices per million tokens, the cost of 1,000 typical messages, context windows and Whizi's own test scores in 30 languages.

## Steps

1. Pick the tool that matches the question and pass the user's question as written in `question`:
   - `recommend_ai_model` for a task ("Which AI is best for coding?").
   - `recommend_ai_model_for_language` for a language other than English ("Best chatbot for writing in Arabic?").
   - `recommend_low_cost_ai_model` when cost comes first ("Cheapest LLM for a support bot?").
   - `compare_ai_models` when the user names two to four models or brands ("Claude or Gemini for long documents?").
2. The card already shows every number. In the reply, give the pick that fits the user's situation and the trade-off behind it (quality against price, context window, language score) in a few sentences. Do not repeat the whole table.
3. If the user names a budget, a volume or a language, say how the picks fit it, using the cost of 1,000 messages from the result.
4. If a model the user named is not in the result, say so and compare the ones that are.
5. Do not use these tools to do the task itself (writing the code, the email or the translation).
