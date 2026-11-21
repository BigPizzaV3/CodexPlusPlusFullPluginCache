---
name: get-started
description: First steps after connecting a WordPress site through AI Engine. Use when the user has just connected their site, asks what they can do with it, or seems unsure where to start.
---

# Getting started with your WordPress site

1. Call `wp_get_site_info` and `wp_count_posts` to greet the user with their site's name and a one-line picture of it (published posts, drafts).
2. Offer three concrete next steps that fit what you saw, for example:
   - "Summarize your latest posts" (uses `wp_get_posts` and `wp_get_post`)
   - "Write a new draft" (see the write-a-draft skill)
   - "Find posts that need attention" (see the content-audit skill)
3. Explain the safety rules once, briefly: new content is created as a draft, deleting only moves items to the trash, and settings, users, plugins and themes are not reachable from here.

Keep the first reply short. Do not list every tool.
