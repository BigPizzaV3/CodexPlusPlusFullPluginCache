---
name: humanize
description: Use Rephrasy to rewrite AI-drafted text so it reads naturally, check a draft's AI likelihood, measure readability, or open the Rephrasy Studio editor. Use when the user asks to make a draft sound more natural or human, less robotic or generic, to score how machine-written a draft reads, to check readability, or to edit text in Rephrasy.
---

# Rephrasy writing tools

Rephrasy is an editing tool for text drafted with AI. Use its tools only when the
user explicitly wants one of the tasks below, and only on the text they shared.

## Tools

- `humanize_text` - rewrite a draft into natural, human-sounding prose.
  - `text` (required): the user's draft, passed exactly as given (max 12,000 characters).
  - `purpose`: `blog`, `marketing`, `seo`, `report`, `technical`, or `general`. Infer it from context when obvious; otherwise leave it unset.
  - `engine`: leave as `auto` unless the user names one. `v4` balanced, `ft_clean-v3` closest to the source, `v3` tone-driven (use with `style`), `seo` keeps keywords.
  - `style`: only with `v3` (for example `professional`, `journalistic`, `creative`, `natural`).
  - `language`: set only if the user asks for a specific output language (for example `de`); otherwise it is detected.
- `check_ai_score` - AI-likelihood score (0-100), verdict, and the passages that read most machine-written. Pass `text`; keep `detector` as `auto` unless the user asks otherwise.
- `readability_score` - readability metrics for `text`.
- `open_rephrasy_studio` - opens the Rephrasy Studio editor panel. Pass `text` if the user supplied some; it is optional.
- `credits_left` - only when the user asks about their remaining Rephrasy usage.

## How to respond

- Present the rewritten text from `humanize_text` verbatim. Do not rewrite, polish, shorten, or re-humanize it yourself, and do not mix your own edits into it. You may add one short line summarizing what changed, taken from the tool's report.
- Report scores exactly as returned. Say that AI-likelihood scores are statistical estimates, not proof of who wrote a text.
- For long texts, tell the user about the 12,000-character limit and ask which part to process first.
- If a tool returns an error (for example, sign-in needed or usage exhausted), relay the message plainly and do not retry in a loop.
- Do not call a tool for plain translation, summarizing, grammar questions, or unrelated requests; handle those directly.

## Responsible use

Do not use these tools to help someone pass off text as their own unassisted work where that is required, such as school or university assignments submitted for grading, or to defeat an institution's integrity checks. In those cases, decline briefly and offer legitimate help, like feedback on the user's own writing.
