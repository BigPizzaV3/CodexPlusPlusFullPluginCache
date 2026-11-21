---
name: mentionedon-answer-capture
description: "Prepare a repeatable log and prompt set for actual AI-answer captures supplied by the user, preserving assistant surface, date and missing results."
---

# Record comparable AI-answer evidence

Help the user record what assistants actually said about a business. This workflow can prepare prompts and a log without connecting MentionedOn. It does not query other assistants, start paid scans or create scheduled monitoring by itself. An answer generated in this conversation is not a clean capture from another product.

Use the actual business name, owned domain, buyer questions, service area and relevant assistants. Prepare a small fixed set of mostly unbranded buyer prompts plus useful branded/comparison questions. Use `references/prompt-library.md` when examples would help. Keep prompt wording, assistant surface, account/memory state, location and capture method consistent across sessions; record differences rather than assuming comparability.

Use `references/capture-log-template.md` for the per-answer fields. One row represents one actual answer for one prompt on one surface at a recorded ISO date/time with timezone. Record whether the business is named, its own or business-specific citations, and position only when a real ranking supports it. Keep API, consumer-app and search-AI captures separate. A citation alone is not necessarily a mention.

Use actual pasted answers, screenshots or authorized existing observations. Do not invent, simulate or estimate an answer, citation or rank. Log refusal, sign-in, errors and skipped tests with status error or skipped and a reason; unavailable is not not-mentioned. Preserve deliberate repeated runs rather than rerunning until a favorable answer appears.

If the user requests analysis, `summarize_scan_evidence` at https://mentioned-on.com/mcp accepts the supplied dated observations, currently up to 50 per call. Follow its current input schema and preserve denominator/coverage limitations. Without that connection, label any simple arithmetic as your own tally. A capture describes one observation and does not establish what all customers see or that an edit caused a change.

Agree a prospective recheck cadence when useful and write it in the log. This does not schedule or run later checks. Connection guidance: https://mentioned-on.com/developers/mcp.
