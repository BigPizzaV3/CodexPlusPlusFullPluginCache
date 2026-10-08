---
name: visibility-report
description: Report how visible a brand is in AI answers (ChatGPT, Gemini, Perplexity, Copilot, Google AI Mode, AI Overviews) for a Radarkit project over a date range, broken down by model and by day, with the sentiment and position of the mentions. Use when the user asks how their brand is doing, how visible they are, whether visibility went up or down, or which AI model mentions them least.
---

Use this skill when the user asks about their brand's visibility, mentions, or trend in AI answers.

1. Call `list_projects`. If the account has one project, use it. If it has several and the user
   did not name one, ask which project before spending credits.
2. Work out the window. Default to the last 30 days ending today. Accept "last week", "this
   month", "since 1 August" and convert to `from` and `to` as YYYY-MM-DD. Visibility accepts up
   to 366 days in one call.
3. Call `get_visibility` with the project id and the window. Read `summary` for the overall
   score, `by_model` for one row per AI model, and `series` for the day-by-day line.
4. If the user asks why, or which answers drove the number, call `get_sentiment` for the
   sentiment split and `list_responses` with `brand_mentioned: false` to show the answers that
   left the brand out. Keep `include_content` off unless the user wants the answer text.
5. Report: the overall visibility percentage, the best and worst model with their numbers,
   the direction of the trend (compare the first and last week of the series), and the
   sentiment split. Name the models the way Radarkit does: ChatGPT, Gemini, Perplexity,
   Copilot, Google AI Mode, AI Overviews. Mention how many API credits were spent.

Do not average numbers across models yourself; `summary` already does that. Do not describe
days that have no data as zero visibility; say there was no run that day. Do not call the
same tool twice for the same window.
