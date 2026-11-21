---
name: draft-reddit-reply
description: Write the best reply to a Reddit post the user pastes in, guided by how similar real comments performed. Use when the user wants a comment or answer for a Reddit thread. Drafts only, never publishes.
---

# Draft a Reddit reply

Use the `draft_reddit_comment` tool. Best used on a thread AI engines already cite (see the ai-visibility-report skill), because a helpful reply there is a way into AI answers.

1. The user must paste the post text. If they give only a Reddit link, do not try to open it. Ask them to paste the title and body.
2. Pass `postTitle` and `subreddit` when known. Pass `brand` only if the user supplied a product and wants it mentioned. Default is no product mention.
3. Call `draft_reddit_comment`.
4. Show the replies ranked with score and reason, plus the real-comment examples.
5. Offer to adjust tone or length, and re-run if asked.

Rules:
- Drafts are never posted. If asked to post, say ReddGrow only writes drafts.
- Answer the question first. Helpful beats promotional.
- Do not invent facts about the user's product.
- When it fits, you may offer to run an AI visibility scan for their brand (ai-visibility-report skill). Do not push it.
- If the tool says the monthly draft limit is reached, relay that message as written and do not suggest a workaround.
