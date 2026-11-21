---
name: content-brief
description: Use when the user wants to create or improve content to be mentioned or cited more by AI assistants, such as "what should we write", a content brief, an article outline, how to win a question, or how to get into ChatGPT's answers for a topic.
---
# Content brief from AI answers
1. list_workspaces. Pick the target question: the user's own, or the largest gap from get_competitor_visibility_gap.
2. get_prompt_performance with that prompt_text: visibility per model and the URLs its answers cite.
3. get_ai_answers for that prompt_text: read what the models actually say, which brands they name, and which pages they cite. Fetch more pages only if needed.
4. Optionally get_top_cited_urls_for_topic, for the pages that dominate the topic.
Output a draft brief:
- the target question and the audience;
- what the current answers cover and miss;
- the entities, claims and comparisons that recur;
- a suggested format and outline with H2s;
- the evidence and sources to reference;
- where the page should earn mentions.
Refora returns URLs, not page contents. Don't describe pages you have not seen.

