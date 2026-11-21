---
name: publish-video
description: Render, share and publish Crealix videos, with the final MP4, a share or download link, or a post on the user's connected TikTok, YouTube and Instagram accounts. Use when the user asks to export, render, download, share, post or publish a video or an AI clip, or whether a post went live.
---

# Render, share and publish

## 1. Render (the final MP4)

- Only when the user asks for the final video. Never right after creating.
- The card's Render button renders it at the price it shows. In the chat,
  `render_project` with the quality they want (1080p unless they ask for 720p or
  4K). It costs credits by length and quality: say the price; if Crealix answers
  `CONFIRMATION_REQUIRED`, ask and wait for a yes.
- It takes a few minutes. Follow it quietly with `get_status`; when it is done,
  the card shows the final video to play and download.
- Some plans don't include cloud rendering. If so, say it plainly: they can
  still preview it and export from the editor (share its link). Never suggest
  upgrading.

## 2. Share

`create_share_link` gives a public page to watch and download a rendered video
or a finished AI generation, for people without Crealix. Optionally it expires
after some hours.

## 3. Publish to social networks

Only when the user asks, and only after they approved exactly what goes where.
1. `list_social_accounts`: which TikTok, YouTube and Instagram accounts are
   connected and healthy. None, or one needs reconnecting: they connect it in
   Crealix (share the link). Never sign in for them.
2. `get_publish_options` for the video and the accounts they chose. Relay what
   they must decide for each network:
   - TikTok: the creator account, a privacy level the user picks (there is no
     default), which interactions to allow, and the consent line, shown as
     given;
   - YouTube: title, privacy, and whether it is made for kids;
   - Instagram: the business account and feed sharing.
   Write a caption and hashtags that suit the video, and let them edit.
3. Show the full plan (each account, caption, privacy) and wait for an explicit
   yes.
4. `publish_video` with `userConfirmed`. Posting cannot be undone from here.
5. `list_posts` shows each post's status and its link once live. If one failed,
   say why in plain words and what to do.
