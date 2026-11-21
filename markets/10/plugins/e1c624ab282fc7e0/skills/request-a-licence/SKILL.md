---
name: request-a-licence
description: Help someone ask the owner of a song in PICA's public music directory about licensing it for a film, TV, ad, game, podcast or social project. Confirm the right song, gather the user's own details and project description, show them the enquiry before it goes, and send it only with their explicit go-ahead.
---

_Copyright (c) 2025-2026 Withpica Ltd. All rights reserved._

# request-a-licence

The user has found a song and wants to use it. This skill opens the conversation with the owner. **Nothing is agreed or priced here.** The enquiry simply reaches the owner, who replies to the user by email.

This sends a real message to a real person, so it is the one step in the directory you never take on your own.

## Step 1 — Confirm the song

You need the work's ID. If you don't have it yet, find the song with `directory_chain` (by title, ISWC or ISRC) or `directory_lookup_work`. Read the title and writers back to the user and confirm it's the right one. Many songs share a title.

Check `enquiries_open` in the `directory_lookup_work` result before asking for anything. If the owner isn't taking enquiries, say so now and offer to look for similar songs, so the user doesn't type their details for nothing.

It's worth mentioning whether the song is `ready_to_license` and whether its credits are confirmed, so the user knows what they're walking into.

## Step 2 — Gather the details (from the user, never invented)

Ask for anything you don't already have, in one short message:

**Required**
- Their **name**
- Their **email**. The owner will reply to it, and it is shared with them.
- **Project type:** film, tv series, commercial, trailer, video game, podcast, social media, or other
- **How the music would be used**, in their own words (scene, length, placement)

**Optional (include only if the user says it)**
- Company or production name
- Territory (e.g. "UK", "worldwide")
- Term (e.g. "1 year", "in perpetuity")
- Budget: an amount and currency, or a note such as "flexible" or "£2–5k"

Never fill in a name, email, budget or project detail the user hasn't given you.

## Step 3 — Show it before sending

Summarise exactly what will go to the owner:

> I'll send this to the owner of **"Linen Road"**:
> - From: Sam Jones (sam@example.com), Example Films
> - Project: film. "Opening credits of a short documentary, about 60 seconds."
> - Territory: UK · Term: 2 years · Budget: £1,500
>
> They'll reply to your email. Shall I send it?

Wait for a clear yes.

## Step 4 — Send

Call `directory_send_licensing_enquiry` once, with `work_id` and the fields the user gave.

Read the result honestly:

- **Sent:** tell them it's on its way and the owner will reply by email. A confirmation email to them usually follows but isn't guaranteed.
- **403:** this owner isn't taking enquiries right now. Say so, and offer to look for similar songs.
- **404:** the song isn't publicly listed any more.
- **429 (too many requests):** wait a minute and offer to try again. Nothing was sent.
- **Unknown outcome:** it may already have gone. **Do not resend** unless the user explicitly asks, to avoid a duplicate.

## What not to do

- Don't send without an explicit yes in this conversation.
- Don't send the same enquiry twice.
- Don't promise a price, a timeline or a yes. The owner decides.
- Don't send enquiries for several songs in one go. Confirm each one separately.
