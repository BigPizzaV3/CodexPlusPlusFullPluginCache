---
name: post-to-meeloop
description: Draft, publish or schedule a meeloop post or story, optionally with a photo or video from the conversation. Use when the user asks to post, share, publish, schedule or put something on meeloop, or to edit, delete or cancel one of their meeloop posts.
---

Explicit instructions from the user override this skill.

## Before anything is published

Posts and stories are public to the user's audience. Never publish, schedule,
edit, delete or cancel without the user's go-ahead in this conversation.

1. Draft the caption if the user didn't give exact text. Keep their voice and
   don't add hashtags, mentions, links or emoji they didn't ask for. Captions
   can be up to 5,000 characters.
2. Show the exact final caption, which media will be attached, and, when
   scheduling, the date, time and time zone. Ask the user to confirm.
3. If the user already gave exact text and clearly said to post it now, that is
   the confirmation; don't ask again.

## Attaching photos or videos

1. Call `import_media` with the file the user shared or one you created in
   this conversation. Use `purpose` "story" for stories and
   "profile_picture" for a profile picture; otherwise "post".
2. Pass the returned `media_url` (and `file_type`) to the next tool. Never
   make up media URLs or reuse URLs from elsewhere.
3. Limits: posts up to 100 MB, stories up to 50 MB, profile pictures up to
   10 MB. If a file is rejected, tell the user why.

## Publishing

- Post now: `create_post` with `caption` and/or `media`. For a link card, put
  the link in the caption and pass it as `link_url` (ignored when the post has
  media).
- Later: `schedule_post` with `scheduled_at` as ISO 8601 with the user's
  offset (for example `2026-10-09T09:00:00-04:00`). It must be at least a
  minute ahead and within 90 days. If you don't know the user's time zone,
  ask.
- Story: `create_story` with `text` and/or `media_url` and `media_type`.
  Stories disappear after 24 hours. `scheduled_for` schedules one.

Each call creates a new post. If a call fails, check `list_my_posts` before
retrying so you don't post twice.

After publishing, share the post link from the result. For scheduled posts,
restate when it will go out.

## Changing existing posts

- Find the post with `list_my_posts` when the user doesn't give an id. If
  more than one could match, ask which one.
- `edit_post` changes the caption or link card only; media can't be changed.
  Show the new caption before saving.
- `delete_post` and `cancel_scheduled_post` need confirmation that names the
  post. Deleted posts stay in Recently Deleted in the app for 30 days.

## Out of scope

Say so plainly if asked to send or read direct messages, like, comment,
follow, browse other people's feeds, or post on anyone else's account.
