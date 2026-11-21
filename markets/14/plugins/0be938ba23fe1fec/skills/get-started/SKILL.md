---
name: get-started
description: Help a user who just installed ProsodyAI sign in, see what their account can do, and make a first piece of speech or video. Use when the user runs setup, asks how ProsodyAI works, or asks what they can make with it.
---

Use this skill to get a new ProsodyAI user from installation to a first result.
Explicit instructions from the user take priority over these steps; skip any
step the user does not want.

1. **Sign-in.** The first ProsodyAI tool call opens ProsodyAI's sign-in page.
   The user signs in with an existing ProsodyAI account (email and password,
   Google or Apple) and approves the connection. Never ask for a password or a
   code in the chat.
2. **Check the account.** Call `get_account` and tell the user their plan and
   what is left this month (premium characters, video seconds, images). Report
   only the figures the tool returns.
3. **Offer a first task.** Suggest one or two of these, in the user's language:
   - Speech: "Read this in Turkish with a warm, unhurried voice: ...".
     `list_voices` shows the voices for a language; `generate_speech` takes the
     text, the language code and the delivery in plain words.
   - Video: "Make a 5-second video of ...". `list_video_options` shows what the
     plan can make; `generate_video` starts the clip and `get_job` returns the
     link when it is finished (usually a few minutes).
   - Edits of a video ProsodyAI made: a voiceover with optional subtitles,
     merge, trim, remove silences or GIF, through `edit_video`.
   - Characters: `create_character`, then `approve_character`, then use its id
     in `generate_video` to keep the same person across clips.
   - Templates: "Turn this product photo into a product spin". `list_templates`
     shows the looks and their fields; `make_template_video` takes the photo the
     user attached (`photo`) or a link to it (`photo_url`).
   - Captions for a video ProsodyAI made: `transcribe_video`, read the lines
     with `get_job` (kind captions), fix words with `edit_captions`, then
     `burn_captions` for a new video with the captions in it.
   - Sound effects: "a short arcade coin pickup". `make_sound_effect` takes a
     synthesis recipe and returns a WAV.
4. **Before spending.** `generate_speech`, `generate_video`, `make_template_video`,
   `edit_video`, `transcribe_video`, `make_sound_effect`, `create_character` and
   `approve_character` use the account's allowance.
   Confirm the text, voice or video settings with the user before calling them
   when the request is ambiguous.
5. **Results.** Give the download link the tool returns. Links stay valid for
   7 days; results also appear at https://prosodyai.ai/history.

Do not:

- Offer voice cloning or imitate a real person's voice; ProsodyAI has only its
  built-in voices.
- Offer to edit or caption videos uploaded to the chat; `edit_video` and
  `transcribe_video` work only on videos ProsodyAI made for this account. A photo
  attached to the chat is used only as a template's picture. For the user's own
  video files, point to https://prosodyai.ai/captions.
- Sell, recommend or start a purchase of plans or credits. If a tool says the
  plan or allowance does not cover a request, relay that explanation as it is.
- Invent voice ids, job ids, links or allowance figures.
