---
name: get-started
description: Research how consumer apps grow on TikTok and Instagram with Social Growth Engineers. Use when the user asks about viral app videos, hooks, hook trends, app marketing strategies, similar apps, or app growth case studies, and to choose the right Social Growth Engineers tool.
---

Explicit user instructions take priority over this guidance.

## Without sign-in

- `search_articles` finds published articles and case studies on app growth.
- `get_article` returns the full text of one article from those results.

Use these for questions about published research, tactics, or case studies.

## Requires sign-in

These tools need the user's Social Growth Engineers account. If a call reports that sign-in is required, tell the user to connect their account, then retry.

- `search_videos`: find viral TikTok and Instagram videos for an app, niche, or topic.
- `get_similar_videos`: find videos similar to a given video.
- `analyze_video`: shot-by-shot breakdown of one video (hook, pacing, on-screen text).
- `hook_intelligence`: winning hooks, templates, formats, and evidence for an app, niche, or market.
- `hook_trends`: which hook patterns are rising or declining.
- `search_apps`, `list_apps`: find apps in the library.
- `get_similar_apps`: apps similar to a given app.
- `app_strategy`: how an app grows on short-form video.
- `generate_report`: create a shareable research report.

## Tool rules

- `hook_intelligence` for a niche: prefer `scope_type` "vertical" with a one-word niche in `scope_primary_vertical` (for example "meditation", "fitness", "finance"). `scope_label` is a display title only and does not filter results.
- Hook language defaults to English. Set `language` only when the user asks about another market or language.
- `generate_report` publishes a public page anyone with the link can open. Confirm the user wants a shareable report before calling it.
- For which creators post for an app, point the user to the app card's "View on SGE" page, which has the creator breakdown.
- Link results back to the original posts and articles. Do not invent metrics, view counts, or video details that the tools did not return.
- Do not mention pricing, plans, or upgrades.
