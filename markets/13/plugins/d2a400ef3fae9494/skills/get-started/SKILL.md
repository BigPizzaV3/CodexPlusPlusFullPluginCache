---
name: get-started
description: Make a short vertical video ad (TikTok, Instagram Reels, YouTube Shorts) from the user's website with adkix, step by step, asking before every spend. Use when the user wants a video, a reel or a video ad of their site, brand or product.
---

# adkix — get started

adkix turns a website, an Instagram @account or a one-line idea into a finished 9:16 video ad
(15 s, 30 s or 1 min): brand, story angle, style, cast, script, voice-over, AI-filmed shots, music, titles.

**adkix does the work, the user decides, you show and ask.**

0. **First contact** (the user just connected adkix, says hi, or asks what adkix does): call `adkix_get_account`.
   When `freeVideo` is `"available"`, their first video can start right away: ask only for their website address,
   then start it with `adkix_create_content` (`url`). No website: ask for the business name and one sentence on what
   it does, and start it with `idea` and `name`. adkix films the first 15 seconds of this 30-second video (about
   10 minutes): when `state.teaser.status` is `"ready"`, show `state.video.shareUrl` and say it is the beginning of the
   video, then give `state.teaser.unlockUrl`, the video's page on adkix where the rest is made. Never say the whole video is ready. Don't wait for them to know what to ask.
1. Ask for the website (or the @account, or the idea) and the length. Call `adkix_create_content`.
2. Follow the content with `adkix_get_content` (use `waitSec: 25` while a step runs). After each step,
   show what adkix proposes (`adkix_view_preview` for pictures, `shareUrl` links for audio and video)
   and ask the user to pick or validate before calling that action's tool, `adkix_<action>`
   (only the names in `state.actions`, e.g. `adkix_pick_angle`).
3. **Never spend credits without an explicit yes.** A priced action returns a `quote`: give the exact
   price in credits, wait for the user's yes, then call `adkix_confirm_quote`. A refusal → `adkix_cancel_quote`.
4. The shoot takes 15 to 20 minutes on adkix's side: tell the user, check back with `waitSec`, never loop silently.
5. At the end, give the user the film's `downloadUrl` (MP4, 9:16).

Not enough credits? Say so and point to https://adkix.ai/pricing — purchases happen on adkix.ai, never in the chat.
Never put a real, identifiable person (celebrity, public figure, someone's photo) in a video without their consent;
adkix draws fictional characters.
