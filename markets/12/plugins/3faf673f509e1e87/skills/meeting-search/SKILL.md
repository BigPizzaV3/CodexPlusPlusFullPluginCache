---
name: meeting-search
description: Use when the user asks about their meetings — what was discussed or decided, action items, who they met with, when or how often they met someone, or which meetings are scheduled in the future.
---

Answer questions about the user's meetings with the `ask-voithos-ai` tool.

- Pass the user's question as `question`, in the user's language. Keep names, companies, projects and dates exactly as the user wrote them.
- Resolve relative dates ("yesterday", "next week") to explicit dates in the question before calling the tool.
- For a broad request (e.g. "summarize my week"), split it into a few focused questions and call the tool once per question.
- Base the answer only on what the tool returns. If it finds nothing, say so and suggest how to narrow or rephrase the question; do not invent meeting details.
- If the tool returns an error, tell the user Voithos AI is temporarily unavailable and offer to retry.
