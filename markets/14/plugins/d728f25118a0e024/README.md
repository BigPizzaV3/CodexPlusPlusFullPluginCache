# WoopSocial

Write, publish and schedule posts to Facebook, Instagram, Threads, LinkedIn, Bluesky, X, Pinterest, TikTok and YouTube from a conversation, plan your content, and check how the posts you sent through WoopSocial were delivered and performed, all through your WoopSocial account.

This plugin adds the WoopSocial connector and 17 skills.

**Post and schedule**

| Skill | What it does |
|---|---|
| `publish-posts` | Publish or schedule a post to any connected account and report how it was delivered. |
| `instagram-posts` | Write and schedule Instagram posts, carousels, Reels, Stories and Trial Reels. |
| `tiktok-posts` | Write captions for and schedule TikTok videos and photo carousels, with the right privacy and labels. |
| `linkedin-posts` | Write and schedule LinkedIn posts for a personal profile or a company page. |
| `cross-post-everywhere` | Post one piece of content to every platform at once, adjusted per platform. |
| `bulk-schedule-posts` | Schedule many posts at once from a spreadsheet, CSV, Notion table or a folder of photos and videos. |

**Manage your accounts and queue**

| Skill | What it does |
|---|---|
| `connect-social-accounts` | Connect your social accounts so the assistant can post to them. |
| `manage-post-queue` | See what's scheduled, move or cancel posts, or pause everything and resume later. |
| `fix-failed-posts` | Find posts that didn't go out, explain why, fix them and re-send. |
| `social-media-report` | See how your posts performed and what to post more of. |

**Plan and create**

| Skill | What it does |
|---|---|
| `instagram-carousel-maker` | Write a carousel slide by slide with the caption and a design spec, render simple text slides when code execution is available, then schedule it once the slide images exist. |
| `content-calendar-generator` | Plan a month of posts with captions, then schedule the ready ones and save the rest as drafts. |
| `content-ideas-generator` | Post ideas for your niche, built on your best posts sent through WoopSocial when connected. Picked ideas can be saved as drafts. |
| `social-media-audit` | Review an account and get a ranked fix list and a two-week plan. |
| `weekly-social-autopilot` | Each week: review last week, draft next week in your voice, approve, schedule. |
| `real-estate-instagram-posts` | A week of listing, open house and local posts for real estate agents, scheduled after you approve them. |
| `restaurant-instagram-posts` | A week of menu, specials, events and behind-the-scenes posts for restaurants, cafes and bars. |

The skills that write posts for you show every post before it goes out, and the assistant asks before scheduling several posts at once or deleting, moving or pausing them.

## Getting started

1. Create a WoopSocial account at [woopsocial.com](https://woopsocial.com/) and connect your social accounts.
2. Install the plugin and sign in to WoopSocial when asked. No API key is needed.
3. Ask, for example: "Schedule this video to TikTok, YouTube and Instagram for Friday at 18:00."

## Data

The plugin ships no code of its own and stores nothing. To upload media or render carousel slides, the assistant may run commands in your code execution environment or shell. The post content, schedule and selected accounts are sent to your WoopSocial account through `api.woopsocial.com`, and media is uploaded to presigned URLs on `r2.cloudflarestorage.com`. WoopSocial then publishes to the social platforms you connected. Some skills can save files you approve, such as a content calendar CSV, to your working folder. See WoopSocial's [privacy policy](https://woopsocial.com/privacy-policy) and [terms of service](https://woopsocial.com/terms-of-service).

## Support

If you run into any issues, email us at `contact@woopsocial.com` or open an issue at [github.com/WoopSocial/mcp](https://github.com/WoopSocial/mcp/issues).
