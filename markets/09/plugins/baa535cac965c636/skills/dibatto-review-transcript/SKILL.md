---
name: dibatto-review-transcript
description: "Find owned Dibatto episodes, summarize saved transcripts, or check recording and post-production status without starting new production."
---

# Review a saved episode

Use the connected service at https://dibatto.com/mcp through normal OAuth and current account access. Documentation: https://dibatto.com/developers. Use `dibatto_list_shows` and `dibatto_get_show` to identify the actual owned show, then `dibatto_list_episodes` to find the intended episode. Resolve ambiguity from returned dates, titles and identifiers.

Read `dibatto_get_episode`, `dibatto_get_transcript` and `dibatto_get_wrap_status` according to the question. Preserve actual transcript text, source timestamps when returned and recorded processing state. A missing transcript, pending wrap or unavailable episode is not completed production. Do not invent audio content, quotes, speakers or progress.

Prepare summaries, questions and editorial follow-up in conversation from the saved transcript. Separate suggested edits from changes actually saved to Dibatto. For return visits, reread state; without an earlier dated record do not claim what changed.

These reads do not record, render, upload, publish, rerun research or start post-production. A request for status or a transcript summary does not authorize provider work. Give an actual returned app link for app-only next steps, and report an error or unresolved result without creating a replacement episode.
