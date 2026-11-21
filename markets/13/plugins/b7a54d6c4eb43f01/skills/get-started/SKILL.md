---
name: get-started
description: Set up SocialDesk after connecting it. Finds the user's space and connected social accounts, then suggests what to do first. Use when the user has just connected SocialDesk or asks what it can do.
---

# Get started with SocialDesk

SocialDesk manages a user's social media accounts: scheduling and publishing posts, drafts, analytics, direct messages and comments. Accounts are grouped in spaces (one space per brand).

## Steps

1. Call `list_spaces`.
   - No spaces: tell the user to create a space and connect a social account in the SocialDesk app at https://app.socialdesk.ai, then stop.
   - One space: use it.
   - Several spaces: list them by name and ask which one to work in. Use that space's id as `spaceId` for the rest of the conversation.
2. Call `list_connected_social_accounts_in_a_space` with that `spaceId`. Show each account's platform and username.
   - No accounts: explain that social accounts are connected in the SocialDesk app, not from ChatGPT, then stop.
3. Suggest a few things to try, based on what is connected:
   - "What posts do I have scheduled this week?"
   - "How did my accounts perform this week?"
   - "Save a draft for Instagram about our new product."
   - "Show my latest direct messages." (only if an Instagram, Facebook or WhatsApp account is connected)

## Rules

- Looking things up (spaces, accounts, posts, drafts, analytics, messages, comments) needs no confirmation.
- Before publishing or scheduling a post, sending a direct message, posting a comment or deleting anything, show the user exactly what will happen (text, media, accounts, time) and wait for their explicit confirmation.
- Only work with the spaces and accounts the tools return. Never guess ids.
