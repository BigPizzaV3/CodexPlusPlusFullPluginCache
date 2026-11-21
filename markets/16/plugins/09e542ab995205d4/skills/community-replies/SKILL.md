---
name: "community-replies"
description: "Find the cited Reddit threads where a helpful reply fits, and draft replies that state the writer's real role."
---

# Community replies

Use this guidance to plan replies in the Reddit threads that AI apps cite. A reply helps only when it is useful to the people in the thread. A reply that reads as an ad gets removed and can get the account banned.

## Steps

1. Call `get_sources` for the project and the scan in the request. Read the subreddits, with `threads_status` and `threads_needing_check`.
2. Use host browsing to read the cited Reddit threads and subreddit rules. The Frontmost AI MCP does not provide public-page browsing. If browsing is unavailable, request the thread text and rules. Leave reply eligibility unverified and stop drafting until the required checks are complete.
3. Keep a thread only when all of these are true:
   - AI apps cite it in this scan's period.
   - The thread does not list the business. A thread that needs a check is not confirmed: read it first.
   - The question in the thread is one that the product really answers.
   - The thread still takes replies. An archived or locked thread cannot. Say so, and leave it out.
4. Read the subreddit's rules before you draft. If the rules forbid self-promotion, do not draft a reply for that subreddit. Say why.
5. Draft one reply for each thread that remains.

## The reply

- First line: the writer's real role, for example "I work at Acme" or "I am the founder of Acme".
- Answer the question first. The answer must help a reader who never tries the product.
- Mention the product once, where it fits the question. Say who it does not fit.
- No link unless the thread asks for one. No sales words.
- Write it for one real person to post from their own account.

## Never suggest

- Fake accounts, more than one account, or coordinated posts.
- A reply that hides the writer's role.
- Requests for upvotes, or replies from employees who pretend to be customers.
- The same reply in more than one thread.
- A post in a thread where the product does not fit the question.
- Any promise that AI apps will mention the business after the reply.

## Rules

- Draft only. The person posts. Do not post for them.
- Report each number with its counts. Link the `url` of the Sources tab.
- Plan a small number of replies. Three good replies are better than ten that look the same.

## Output

For each thread, up to 5: the thread, why it fits (the citing answers with counts, and the question it asks), the subreddit rule that applies, and the draft reply. Then the threads that you left out, with the reason for each.
