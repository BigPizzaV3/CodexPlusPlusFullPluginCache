---
name: kinetik-accounts
description: Use when the user wants to understand a social account, their own or someone else's by handle (how it performs, what to post next, what to stop doing), connect Instagram, TikTok or LinkedIn, or post there. Connecting accounts, analyzing them, and posting with the user's consent.
---

# Social accounts

## Connecting

Kinetik posts, and reads a user's own results, only through an account they connected. When a request
needs an account that is not connected yet, Kinetik says so. Show that account's card,
`instagram-connect`, `tiktok-connect` or `linkedin-connect` (their markup is in `kinetik-show`), and
wait: the user connects in their browser and comes back, then do what they asked. Instagram takes a
Business or Creator account, and its sign-in page is Composio's.

## Analyzing

- **Their own account:** once it is connected, Kinetik reads its posts and results.
- **Someone else's, by handle:** no connection is needed, and only public posts are read.

An analysis answers what the user really wants to know: how the account is doing, what to post next
and what to stop doing. Offer to make what it suggests.

## Posting

Posting is the one thing that leaves Kinetik, so the user always sees the post as it will look and
says yes first. A request to post comes back as that preview with a question: show it, ask it, and
post on a clear yes to that exact post. A changed caption or picture is a new preview.

Instagram and LinkedIn posts go live. A TikTok video is saved to the user's TikTok drafts instead, and
they finish posting it in TikTok; say so.
