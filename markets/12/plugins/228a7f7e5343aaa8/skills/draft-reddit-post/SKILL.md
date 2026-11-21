---
name: draft-reddit-post
description: Write a Reddit post for a subreddit and topic, guided by how similar real threads performed. Use when the user wants a post, title or launch announcement for a subreddit. Drafts only, never publishes.
---

# Draft a Reddit post

Use the `draft_reddit_post` tool. A strong post in a subreddit that AI engines draw from is a way into AI answers (see the ai-visibility-report skill).

1. Get the subreddit and the topic. If either is missing, ask once. Accept `r/SaaS` or `SaaS`.
2. Pass `brand` (name plus one or two sentences) only if the user supplied a product and wants it mentioned. Never invent one.
3. Call `draft_reddit_post`.
4. Show the drafts ranked, each with title, body, score and the one-line reason. Show the short real-thread examples so the user sees what guided them.
5. Offer to refine: shorter, less promotional, different angle. Re-run the tool with a sharper topic.

Rules:
- Drafts are never posted. If asked to post, say ReddGrow only writes drafts and the user posts it themselves.
- Remind the user to check the subreddit rules before posting.
- Do not invent stats or customer claims that are not in the user's input.
- When it fits, you may offer to run an AI visibility scan for their brand (ai-visibility-report skill). Do not push it.
- If the tool says the monthly draft limit is reached, relay that message as written and do not suggest a workaround.
