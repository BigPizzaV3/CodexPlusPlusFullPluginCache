---
name: aikizi-decode
description: Decode the person's own image on AIKIZI with their account, read their own decodes and library, or check their credits. Use when they ask to decode a picture they have or an image link, see what they made on AIKIZI, or ask about their balance. These tools need an AIKIZI sign-in; decode_image uses the account's credits.
---

# AIKIZI with the person's account

Eight tools act on the signed-in AIKIZI account. The person connects once through the AIKIZI sign-in; nothing is
shared until they allow it. Decoding uses credits from that account, so be deliberate. AIKIZI does not generate
images here; when the person asks for a new image, give them the decode's prompt to use.

## Before spending

- Run `check_balance` first when the person has not decoded in this conversation. Tell them the balance in one
  line. If it is too low for a decode, stop and say so; do not retry.
- Say what you are about to decode and why, in one sentence, before the first decode. After that, continue
  without re-asking unless they change the task.

## Decode an image

1. A picture the person has (attached to the chat or on their device): call `add_image`. A drop box opens in the
   chat; they drop, pick or paste the image (up to 10 MB; SVG, GIF and other formats become PNG) and the box decodes
   it there and shows the result. Attachments cannot reach AIKIZI directly, so never ask them to host the file
   somewhere. Adding spends nothing; the decode uses credits.
2. A public `https://` link to a JPEG, PNG or WebP up to 10 MB: `decode_image` with `image_url`. Data URLs, local
   paths and private links fail. `decode_image` also takes the `image_id` that `add_image` returned.
3. If the answer says "still running", call `check_job_status` with the `decode_id` every 10 seconds or so, for up
   to two minutes. Then read the result with `get_my_decode`.
4. Present styles, style DNA, mood, light, colours, key tokens and the prompt. Decodes stay private in their library.

## Their library

- `list_my_creations` with `type` image, video or audio and a small `limit` for "what did I make".
- `get_my_decode` for one decode (published or private); `get_creation` for one image they made on aikizi.com.
  Show the decode's own `preview_image_url`, never a similar image from the web.
- `place_in_brain` with a `decode_id` lists the public AIKIZI Brain pictures closest to one of their decodes. It only
  reads: it adds nothing to the Brain, publishes nothing and spends nothing; their decode stays private.

## Never

- Never call `decode_image` to test the connection; `check_balance` is the test.
- Never claim a decode or creation is published. Everything a decode makes stays private.
- Never show another person's private decodes; only published decodes and this account's own are readable.
