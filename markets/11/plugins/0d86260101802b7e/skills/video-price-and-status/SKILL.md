---
name: video-price-and-status
description: Use when the user asks APIhub to make or edit a video, asks what a video job costs, how many credits they have, or whether their video is ready. Covers getting the video (a link, start_upload, or a file attached where the app hands it over), pricing with get_price, waiting for the user's explicit OK, running the task once, following it with video_status and handing over the finished link.
---

# The steps of every APIhub video job

Every job follows the same six steps. The task skills (captions, reels, video from an idea, full edit) only add what to ask for.

## 1. Get the video

- **A public link works:** a direct link to the file (`https://…/clip.mp4`), or a Google Drive or Dropbox link shared with "anyone with the link".
- **A file on the user's phone or computer:** call `start_upload`. It shows an upload card with one button; when the file arrives the card says so and the chat continues by itself (or the user says "done" — then check `upload_status`). Pass the upload code as the video.
- **Attached in this chat:** only in ChatGPT, which hands the file to the tool — pass it as `video_file`, no link and no upload page needed. In Claude, Cursor and the other apps an attached file does not reach APIhub: ask for a link, or call `start_upload`.
- **A YouTube, Instagram or TikTok page is not a file.** Ask for the file itself, or for an upload.

## 2. Price it

Call `get_price` with the task name (`captions_for_video`, `reel_from_long_video`, `video_from_idea` or `full_edit_video`) and exactly the arguments you will run with. Nothing runs and nothing is charged. Its answer has a ready `call`: after the yes, send exactly that.

The one exception: a video the user wants edited without saying how. When `choose_edit` is among your tools, start there (the `full-edit-video` skill): it prices three kinds of edit for that video and shows four looks, nothing is charged, and each choice carries its own `call` and approval.

## 3. Show the price and wait for a yes

- Tell the user the price in credits and their balance, in their language, in one or two short lines.
- Wait for an explicit yes. Silence, "maybe" or "sounds interesting" is not a yes.
- A budget the user named earlier ("up to 50 credits") covers only a price within it. Above it, show the real price and ask.
- If the balance does not cover the price, say so plainly — the balance, the price — and stop. Nothing is charged. Pass on the link the answer gives (where the user can read how credits work); do not offer to add credits in the chat.

## 4. Run it once

Call the task tool with the same arguments, plus:

- `approved_estimate_id`: the id that `get_price` returned;
- `approved_credits`: the number the user agreed to, never one you chose for them.

If anything changes after the yes (style, length, language, the video), price it again and ask again.

## 5. Follow it to the end

A job answers with an id and the status `processing`. Call `video_status` with that id about every 15 seconds until it is `completed` or `failed`. Never start the same job again while it runs. Captions on a clip of about 40 seconds are usually ready in about a minute; reels and a full edit take a few minutes.

## 6. Hand it over

Give the link to the finished video and say what it cost. The video is also in the user's APIhub account. If the job failed, say so in plain words; failed work is not charged.

## Credits and wording

- `get_balance` shows the balance. Talk about prices and balances in credits only.
- When the user is unsure what to make, or asks for examples or caption styles, call `show_examples` (it shows them as running videos) — never list styles as text.
- Keep it short and plain: the user may never have edited a video. No technical words such as API, render or endpoint.
