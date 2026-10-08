---
name: dunsocial-social-publishing
description: Create, validate, schedule, and publish DunSocial content across connected social accounts and messaging channels.
---

# DunSocial social publishing

Use this skill when a user wants to create content, validate it, schedule it, publish it, or manage connected social destinations through DunSocial.

## Workflow

1. Use `list_workspaces` and `get_workspace` when workspace context is unclear.
2. Use `list_social_accounts` before choosing a destination account.
3. Call `validate_post` before `schedule_post` or `publish_now`. If validation returns `valid: false`, follow each `issues[].next` instruction and validate again.
4. For Discord, call `list_discord_channels` first, then use `schedule_discord_post` or `publish_discord_now` with a returned channel ID.
5. For Slack, call `list_slack_channels` first, then use `schedule_slack_post` or `publish_slack_now` with a returned channel ID.
6. For Pinterest, use `list_pinterest_boards`; if no suitable board exists, use `create_pinterest_board` before publishing.
7. For media, use `get_upload_url` and `complete_upload`, then reference the resulting media in the post.
8. Treat `publish_*` results as the only confirmation that external content was published. A draft or scheduled result is not a publication confirmation.

## Safety

- Ask for confirmation immediately before any publish or delete action when the user has not clearly requested it.
- Never claim content is live unless the corresponding publish tool returns a successful queued or published result.
- Do not retry write operations after a subscription-required response; report the returned access message and billing URL.
- Use dedicated platform tools for Reddit, Instagram, TikTok, Pinterest, Discord, and Slack when available.
