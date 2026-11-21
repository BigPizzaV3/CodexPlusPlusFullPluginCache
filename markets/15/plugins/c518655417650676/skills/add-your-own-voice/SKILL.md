---
name: add-your-own-voice
description: Add the user's own voice to Anam when no stock voice fits, by recording or uploading a sample on a Lab page, importing a voice from their ElevenLabs account, or importing by voice ID or share link, then use it on a persona. Use when the user wants a persona to sound like them, a colleague or a brand voice, or has a voice in ElevenLabs they want to bring over.
compatibility: Needs the Anam MCP server connected to an Anam account (the Anam plugin in ChatGPT, or https://lab.anam.ai/mcp elsewhere) and a plan with custom voices.
---

# Add your own voice

Anam can clone a voice from a short recording or import one from a voice
provider. Recording, uploading and signing in to ElevenLabs happen on a Lab
page the user opens in their browser, so their audio and provider keys never
go into this chat.

## 1. Check consent

Ask whose voice it is. Only add the user's own voice, or the voice of someone
who has agreed to it being cloned. If the answer is no or unclear, don't add
it; offer a stock voice instead (`pick-voice-and-avatar`).

Call `anam_connection_info`; adding a voice needs a connection that can
change voices (full access, or an API key with write access to voices).

## 2. Choose how

- **Record or upload a sample** (10 to 15 seconds of one person speaking
  clearly), or **import from their ElevenLabs account**: use the Lab page in
  step 3.
- **They already have a voice ID or an ElevenLabs share link**: use
  `anam_voice_import` (step 4).
- **The recording is already at a public URL**: `anam_voice_clone` takes
  `audioUrl` and `name`.

## 3. Send them to Lab

Call `anam_voice_add`. It creates nothing by itself and returns a `url`:

- `mode`: `record` opens on the recording script and `elevenlabs` on the
  ElevenLabs import; `upload` or `any` (the default) lets them upload a file
  or record.
- `name` and `language` (ISO 639-1, such as `en`) prefill the form.
- `personaId`: the persona the voice is for, so the page offers to use it.

Give the user the `url` and say:

- they sign in to Anam if asked, then record, upload or pick their ElevenLabs
  voice there, and tick the box confirming they have the speaker's
  permission;
- cloning or importing on that page is paid work on the organization's
  account, and an ElevenLabs import can use their ElevenLabs credits, so it
  only happens when they agree by clicking Clone voice or Import;
- the link works once, and must be used within 30 minutes.

When they say they're done, call `anam_voice_add_status` with the
`requestId`:

- `completed`: it returns `voiceId`, `name` and `sampleUrl` (a preview to
  play; it can be null for the first minute after a clone). Go to step 5.
- `pending`: the page hasn't handed a voice back. Don't assume nothing
  happened. Ask whether the page showed "Voice added" with a voice ID. If it
  did, ask them to paste the ID, check it with `anam_voice_get` (it should be
  the voice they just named) and use it as the `voiceId`. If they are still
  on the form, wait and check again. After the 30 minutes, `pending` means a
  clone or import that started in time hasn't reported back; the result says
  until when its voice can still arrive.
- `expired`: the link ended without a voice coming back through it. That
  doesn't mean no voice exists: one saved just as the link expired shows its
  ID on the page. Ask the same question and check a pasted ID with
  `anam_voice_get`, or look for the voice they named with `anam_voice_list`,
  before offering a new link.
- `cancelled`: they closed the page without adding a voice. Offer a new link
  if they still want one.

A voice ID is not a secret, so pasting it into the chat is fine. Never ask
for the audio or an API key.

Owners and admins can also save their team's ElevenLabs API key on that page.
Later imports can then use `useOrganizationKey: true` with
`anam_voice_import`, without the key going through the chat.

## 4. Import by voice ID or share link

`anam_voice_import` generates a speech sample to check the voice, which uses
the voice provider's account, or the team's ElevenLabs credits with
`useOrganizationKey: true`. Tell the user, and call it once they agree.

- A Voice Library or stock provider voice: `provider` (`ELEVENLABS`,
  `CARTESIA` or `FISH_AUDIO`) and `providerVoiceId`.
- An ElevenLabs Professional Voice Clone shared by link: `shareUrl`.
- An instant clone or designed voice in their ElevenLabs account:
  `provider` `ELEVENLABS`, `providerVoiceId` and `useOrganizationKey: true`,
  once their team's key is saved (step 3).

Each import adds another voice, so check `anam_voice_list` before trying
again.

## 5. Use the voice

With a `personaId` on the link, `anam_voice_add_status` says whether the
persona already has the voice:

- `personaUpdated: true`: the user chose "Use on <persona>" on the page.
  Don't update the persona again.
- `personaUpdated: false`, or no `personaId`: call `anam_persona_update` with
  the persona's `id` and `voiceId`, and `languageCode` if the language
  changes. The change is published at once.

Then give them a share link to hear it: from `anam_share_link_list`
(`personaId`), or a new one from `anam_share_link_create`.

## Rules

- Only add a voice with the speaker's consent.
- Never ask the user to paste an API key or audio into the chat; the Lab page
  takes them.
- Don't make a second link, or clone or import again, until you know the
  first attempt made no voice: each one adds another voice to the account.
