---
name: superpills
description: Post to social media and read views through Superpills. Use it when the person wants to send a photo carousel to TikTok as a draft, schedule a post on TikTok, Instagram, Facebook, Threads, YouTube, X, LinkedIn, Pinterest, Google Business or Bluesky, or find out how many views their accounts and posts got.
---

# Superpills

Superpills (https://superpills.app) connects a person's social media accounts, grouped in workspaces, one per brand. Its MCP server is `https://superpills.app/api/mcp`. The first time, the person signs in with their Superpills account; their social media passwords never reach the AI.

## Tools

| Tool | What it does |
|---|---|
| `list_channels` | The workspaces and connected accounts, with the ids and @handles the other tools take. `can_post` and `can_send_drafts` say what works on each account. |
| `get_views` | New views per day and per account, counted every morning. |
| `top_posts` | The most-viewed posts of the last N days, with likes, comments, shares, link and caption. |
| `send_tiktok_draft` | Sends 1 to 35 photos to a TikTok account's inbox as a draft. Nothing is published. |
| `draft_status` | Whether that draft reached the TikTok inbox. |
| `schedule_post` | Plans a post (text, photos or one video) on up to 30 accounts. It waits in the Superpills calendar until the person approves it. |
| `list_scheduled_posts` | What is planned, and how each post went. |
| `cancel_post` | Deletes a post that hasn't gone out yet. |

## Using it well

- Start with `list_channels` when you don't know the person's accounts yet.
- Before `send_tiktok_draft` or `schedule_post`, confirm the accounts, the photos or video, the text and the time with the person.
- Times need the person's time zone, like `2026-10-09T18:00:00-05:00`, or the word `now`.
- On TikTok everything arrives as a draft: the person opens TikTok, adds a sound and posts it.
- Each account is the brand's own (`kind: "brand"`) or a UGC account a creator runs for the brand (`kind: "ugc"`). When the person asks about one of them, pass that kind.
- A newly connected account shows 0 views on its first day, because there is no earlier count to subtract.

## Which networks work

TikTok works today. Instagram, Facebook, Threads, YouTube, Google Business Profile, LinkedIn company pages and Pinterest are waiting for each network to approve Superpills. `list_channels` shows what each connected account can do.
