---
name: read-hanging-context-news
description: Answer questions about recent news with facts that link to their sources, using the Hanging Context tools. Use when the user asks what happened recently in AI, finance, sports, health, research or US government.
---

Use this skill when the user wants recent news with sources.

1. For a question, call `hc_ask` with the question in plain words.
2. For "latest" requests, call `hc_latest`. Pass a topic when the user names one; call `hc_topics` first if you need the topic ids.
3. For a keyword, call `hc_search`.
4. To read a whole story, call `hc_get_story` with its slug.
5. To show sources, call `hc_sources` with the story slug.
6. To get only new stories since an earlier call, call `hc_since` with the cursor from that call.

Rules:
- Quote facts as the tools return them and give the story link for each one.
- If a tool returns no match, say so. Do not invent stories, facts or sources.
- Stories are rebuilt every 12 hours. Hanging Context is not a real-time feed and has no paywalled sources.
- Explicit user instructions take priority over this skill.
