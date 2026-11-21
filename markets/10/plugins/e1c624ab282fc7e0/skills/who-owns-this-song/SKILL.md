---
name: who-owns-this-song
description: Answer "who owns this song?" from PICA's public music directory. Start from a song title, artist, ISRC or ISWC, find the work, and show who wrote and published it, how confirmed those credits are, and whether it is ready to license. Use when someone needs to know who to talk to about a piece of music.
---

_Copyright (c) 2025-2026 Withpica Ltd. All rights reserved._

# who-owns-this-song

Someone has a song in mind and wants to know who is behind it: who wrote it, who publishes it, and whether the rights are clear enough to approach. Find the song in the directory and give them a plain answer they can act on.

The directory only holds songs whose owners have chosen to list them. If a song isn't there, say so plainly. Never fill the gap from memory or the web. The empty result carries a link for sharing PICA with the people who made the song. Offer it once; if they list their catalogue, the answer will be here next time.

## Step 1 — Find the song

Pick the lookup that matches what the user gave you:

| User gives | Call |
|---|---|
| An ISRC (e.g. `GBABC2400001`) | `directory_lookup_isrc` |
| An ISWC (e.g. `T-123.456.789-0`) | `directory_chain` with `identifier` |
| A title, with or without artist | `directory_chain` with `q` |
| Only a person's name | `directory_list_people` with `q`, then `directory_lookup_person` with the `global_creator_id` it returns |

`directory_chain` returns the work, its writers and publishers, the linked recording and its audio profile in one call. Start there whenever you can.

If several songs match a title, list them briefly (title, writers, year if shown) and ask which one. Don't guess.

## Step 2 — Get the detail

Call `directory_lookup_work` with the work's ISWC or ID. It adds:

- **Credits with IPI numbers.** IPIs are the identifiers collecting societies use, so they're the reliable way to name a writer.
- **Whether each credit is confirmed.** An unconfirmed credit means someone listed it but the owner hasn't verified it.
- **Recordings and ISRCs,** plus Spotify / Apple Music links so the user can listen.
- **Registration score.** Higher means the paperwork is more complete.

## Step 3 — Answer plainly

Lead with the answer, then the detail:

> **"Linen Road"** was written by A. Writer (IPI 00012345678) and B. Writer (IPI 00087654321), published by Example Music. Both credits are confirmed by the owners. It's ready to license: the song and a recording are confirmed, with an ISRC and an ISWC.

Then add any flags:

- **Unconfirmed credits:** "one credit hasn't been confirmed by its owner yet; treat it as a claim."
- **Several writers:** "three writers means three people to clear with."
- **Missing ISRC or ISWC:** "it hasn't been fully registered, so expect more back-and-forth."
- **`ready_to_license: true`:** the song and a recording are confirmed by every owner, with audio, an ISRC and an ISWC.
- **`programmable_since` present:** every owner has confirmed a locked split, so a fee can be paid to each without chasing sign-off. Only say the split is signed off when this is present.

## Step 4 — Offer the next step

If the user wants to use the song, offer to send a licensing enquiry to the owner (see the `request-a-licence` skill). Don't send anything until they ask.

## What not to do

- Don't state splits or percentages unless the directory returns them. The chain view deliberately leaves splits out.
- Don't give contact details the directory doesn't provide. The enquiry tool is the route to the owner.
- Don't present a credit as fact if it isn't confirmed.
- Don't answer from outside the directory. If it's not listed, say "it's not in the PICA directory" and stop there.
