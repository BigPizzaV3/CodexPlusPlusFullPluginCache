---
name: reply-thread
description: >
  Create a reply-based thread draft with two or more connected parts for X,
  Threads, or Bluesky. Use when the user says "create a thread", "tweet storm",
  "multi-part post", or references a numbered list of posts.
---

# Reply Thread

## Goal
Create one draft whose parts can be scheduled as a reply chain.

## Workflow

1. **Pick the brand.** Call `listContentGroups`. Ask the user to choose when the content group is ambiguous.

2. **Check accounts.** Call `listAccounts`. Only offer connected accounts.

3. **Collect the parts.** Use text the user supplies, or ask for a topic and propose a complete thread. Each part must fit the smallest selected platform limit:
   - X: 280 characters
   - Bluesky: 300 characters
   - Threads: 500 characters
   Use 5–10 parts unless the user requests another count.

4. **Select thread-capable platforms.** Only X, Threads, and Bluesky support reply threading. If the user asks for another platform, explain that it cannot receive the reply chain and ask whether to exclude it.

5. **Preview and confirm.** Show every part and destination before creating the draft.

6. **Create the draft.** Call `createPost` with the approved first-part content, selected platforms, and all approved thread parts. Keep it as a draft.

7. **Schedule if requested.** Confirm the exact time and timezone, then call `schedulePost` for the returned draft ID. If the user asks to publish immediately, explain that the connector has no immediate post-publishing tool and direct them to the PostQuickAI dashboard.

## Never do

- Never create a thread with fewer than two parts; use a normal post instead.
- Never target an account that `listAccounts` did not return.
- Never silently publish a reply chain to an unsupported platform.
- Never exceed any selected platform's character limit.
- Never schedule before the user confirms every part, destination, and time.
