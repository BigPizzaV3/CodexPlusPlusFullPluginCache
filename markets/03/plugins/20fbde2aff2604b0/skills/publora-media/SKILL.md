---
name: publora-media
description: >
  Attach images and video to a Publora post — by public URL or by uploading a
  local file — and fix media problems that block scheduling. Use when a post
  needs a picture or clip, when Instagram, TikTok or YouTube refuse a text-only
  post, or when media errors stop a post from being scheduled.
---

# Media in Publora

Two ways in, and one of them is much shorter.

## By URL, when the file is already on the web

Pass `mediaUrls` to `create_post` or `update_post`. Publora downloads the files
server-side, so nothing is uploaded from the conversation.

```
create_post
  platforms: ["<platformId>"]
  content: "<caption>"
  mediaUrls: ["https://example.com/image.png"]
  scheduledTime: "2026-08-12T09:00:00Z"
```

Requirements that actually bite:

- **Direct file URLs only.** A Google Drive or Dropbox share page is a web page,
  not a file, and the download fails.
- Images: jpeg, png, gif, webp, tiff, avif, up to 25 MB.
- Videos: mp4, mov, webm, up to 150 MB.
- Up to 10 files per post.

If a URL cannot be fetched, the whole call fails and the response names the
file and the HTTP status behind it. Report that to the user rather than
retrying the same URL — an expired or private link will not start working.

## By upload, when the file is local

Three steps per file, in order:

1. `get_upload_url` with a **unique** file name → returns a presigned URL and a
   `mediaId`. Reusing a name returns the same slot instead of adding a new one,
   which is how several files silently collapse into one.
2. `PUT` the bytes to that URL.
3. `complete_media` for that `mediaId` — Publora inspects the bytes and marks
   the file ready.

Create the post as a draft first (no `scheduledTime`), attach the media, then
`update_post` with `status: "scheduled"` and the time. Scheduling before the
media is ready fails validation.

## Networks that require media

Instagram, TikTok and YouTube cannot take a text-only post. If the user wants
one of those without a file, say so and offer either to attach something or to
drop that network — do not schedule and hope.

## Covers and network options

`platformSettings` carries the extras: an Instagram Reels cover image, a
YouTube title, tags and privacy, TikTok viewer setting. A cover URL follows the
same rule as any media URL — public, direct, https.

## When media blocks scheduling

Two errors show up in practice:

- **Too many media slots, or a slot that was never uploaded.** Call `get_post`
  and read its `media` array: each entry carries a status. Remove the offending
  file with `delete_media`.
- **A reference to a file that no longer exists.** `prune_media_reference`
  clears a dangling reference that `delete_media` cannot, because the underlying
  record is already gone.

Both are destructive and cannot be undone. Name the exact file you are about to
remove, and let the user confirm before you remove it.
