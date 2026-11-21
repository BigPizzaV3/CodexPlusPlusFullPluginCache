---
name: schedule-posts
description: Post and schedule to the user's own connected social accounts and show what is queued. Use when the user asks to post, schedule or queue something on Instagram, Facebook, TikTok, YouTube, LinkedIn, X, Threads, Pinterest, Bluesky or Telegram, or asks what is scheduled or what already went out.
---

# Schedule posts

Use this skill to put a post on the user's calendar and to report what is already queued. Hermoso posts only to
accounts the user connected in their Hermoso workspace, and only when the user asks. Explicit instructions from
the user always take priority over this skill, including the exact caption, time, channels and visibility.

## What is queued (read only)
Call `list_scheduled`. It is free and changes nothing. Report upcoming posts with their time, channels and a
short description of the creative. For a fired post, report each channel's outcome separately (for example
Instagram published and TikTok failed), never a single verdict for the whole post. Pass `id` to read one post in
full.

## Schedule a post
1. Call `list_connectors` to see which channels are connected. If a channel the user wants is not connected, say
   so and that it is connected in the Hermoso app under Connectors, in the sidebar. Never ask for a password
   or token in the chat.
2. Work out the media. Use the file the user just made in this conversation, one from `list_library`, or a public
   link to their own file turned into a URL with `upload_file`. A carousel keeps every slide, in order.
3. Work out the time. A specific time goes in `at`, with the user's `timezone` when they gave one. "Just queue it"
   means the brand's next free posting slot (`useQueue` set to true).
4. Show the user exactly what will go out: channels, time, caption per channel and the media. Ask for a clear yes
   before scheduling, unless the user has already confirmed these exact details in this conversation.
5. Call `schedule_post`. Use the user's caption as written. Only write or change a caption if the user asked you
   to, and show it before scheduling.
6. Read the answer back to the user from what `schedule_post` returned, per channel. If it refused a channel
   (for example a Pinterest board, a LinkedIn company page or one of several Facebook Pages has to be named), relay
   what it needs and ask the user to choose.

## Plan a week of posts
When the user wants a week of posts planned, use the plan-my-week skill, which starts with `plan_week`.

## Comments, messages and support conversations
Reading and answering comments, DMs, reviews and support conversations is the Reply to comments and DMs skill.

## Credits
Publishing, scheduling, reading the queue and answering comments and messages use no credits. Posting to X and
reading X data use a few credits per call, because X charges per request. If the user asks, `hermoso_credits`
reports the balance and the rule.

## Output
A short confirmation: when it will post, where, and with which caption, as reported back by Hermoso. If anything
was refused, say which channel and why.

## Do not
- Do not schedule anything the user did not ask for, and do not post to a channel they did not name.
- Do not change visibility: a scheduled post goes out publicly unless the user asks for private, unlisted or draft.
- Do not shorten or rewrite the user's caption silently. If a channel's length limit is exceeded, tell the user
  and ask how to shorten it.
- Do not claim a post went live until `list_scheduled` shows it fired on that channel.
