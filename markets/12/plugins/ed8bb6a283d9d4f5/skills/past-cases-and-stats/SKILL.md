---
name: past-cases-and-stats
description: "Show earlier Alibi Hour cases and their solutions, the user's solving streak and stats, or a share link for a result. Use when the user asks who the culprit was on an earlier day, how they did, what their streak is, wants to share their result, or asks to delete their Alibi Hour data."
---

Use this skill when the user asks about earlier Alibi Hour cases or their own record. The user's explicit instructions always come first.

## Flow

1. `show_case_results` shows an earlier day's case with the user's questions and verdict, the culprit, every statement and where everyone really was, up to 30 days back. Today's case stays secret until the user accuses someone.
2. `get_my_stats` returns days played, cases solved and proven, the current and best solving streak, average questions, cases at or under par, and the last 7 cases.
3. `create_share_link` makes a public link to the user's result after they have accused someone, with a text version ready to paste. It names the culprit only once the case has closed.
4. `delete_my_data` permanently deletes the user's questions, accusations, streak, share links and parties when they ask for it.

## Scope

- Alibi Hour has no account: cases are kept under the anonymous ID ChatGPT shares.
