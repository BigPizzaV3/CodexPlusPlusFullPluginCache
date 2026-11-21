---
name: get-started
description: How to work with a user's Reachlee workspace through the Reachlee tools - which tool to call first, how to pick the right account and period, and which actions to confirm before running.
---

# Working with Reachlee

Reachlee automates DMs on the social accounts a creator or business connects (Instagram and Facebook today, more channels as they launch): a comment with a keyword on a post or reel triggers a DM, leads are captured, and every conversation lands in one inbox. The tools act on the user's own Reachlee workspace, so always respect the account they mean.

## Start here

1. Call `list_accounts` first when the user has not named an account. It returns every workspace and every connected account with its channel and status. Use the account names when you answer.
2. For "how is it going" questions use `get_overview` with the period the user said. Default to the last 30 days when they did not say.
3. For "which post" or "which reel" questions use `rank_posts`. For "which automation" questions use `rank_automations`.
4. For details on a single automation use `get_automation`; to list them use `list_automations`.
5. For leads use `list_leads`. For the inbox use `list_conversations` and `get_conversation`.

## Confirm before changing anything

These tools change the user's account or send messages. State exactly what will happen and get a clear yes before calling them:

- `create_automation`, `update_automation`, `set_automation_status`
- `retrigger` (sends DMs to people who commented in the last 7 days but never received one)
- `reply_to_conversation` (sends a real DM to a customer)

Never invent keywords, links or message text. Ask for them.

## Limits to respect

- Reachlee cannot message people who never interacted: no broadcasts, no follower lists, no cold DMs.
- Comments older than 7 days cannot be replied to by DM. Say so instead of trying.
- If a tool reports that a feature is not available on the user's plan, say that plainly and move on. Do not pitch upgrades.
- Keep numbers exactly as returned. Do not estimate when a tool gives a figure.
