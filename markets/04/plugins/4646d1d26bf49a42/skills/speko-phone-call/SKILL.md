---
name: speko-phone-call
description: Place a real outbound phone call through Speko and read back what was said. Use when the user wants someone actually called on the telephone — booking, confirming, chasing, asking a business a question — or wants to rehearse such a call first, or wants to review a call that already happened.
---

# Placing a phone call with Speko

Speko dials a real phone number with a voice agent, stays on the line, and returns a transcript and
a recording when the call ends. This skill covers the whole loop: decide who to call, rehearse,
confirm, dial, watch, read back.

## When this applies

Use it when the user wants a real telephone call made or reviewed. Phrases that mean this: "call
them", "ring the clinic", "book me a table", "chase the quote", "find out if they're open", "what
did they say on that call", "rehearse this call first".

Do **not** use it to send a message, an email or a text — Speko is voice on the telephone network.

## Before you dial: three things, every time

**1. Read the number back.** Say the full E.164 number out loud in your reply — `+14155550142`, not
"the dentist". A wrong digit means a stranger's phone rings.

**2. Say what the call is for.** One sentence, in the user's words, so they can catch a
misunderstanding before it is spoken to a person.

**3. Get an explicit yes.** One confirmation, one call. Never batch. If the user asks for several
numbers, take them one at a time with a separate confirmation each, and say that is what you are
doing.

If the user has not given a number — only a business name — ask for it. Do not guess a number and
do not look one up and dial it without showing it first.

## Rehearsing first

When the call matters, or the user seems unsure what the agent should say, offer
`agents.test_call` before `sessions.phone.create`. It runs the whole conversation between the agent
and a synthesized caller inside Speko, with **no phone leg at all** — nobody's phone rings. Pass
the user's goal as `objective`.

It returns session ids immediately and the conversation runs in the background. Poll `calls.get`
with the agent session id until it ends, then read `sessions.transcript.get`. Show the user that
transcript and ask whether to make the real call.

## Making the call

Use `sessions.phone.create`. The body needs `to` in E.164 form, plus either an `agentId` from
`agents.list` or an `intent` naming the language — for example
`{"to": "+14155550142", "intent": {"language": "en"}}`. Put what the agent should accomplish in
`systemPrompt`.

The call opens by disclosing it is an AI. That is applied server-side and is not yours to remove or
soften; if the user asks you to hide it, say plainly that Speko always discloses.

If the account owns more than one number, `phone_numbers.list` shows which ones can be used as
`from`. Leave it unset to use the default.

Calls are recorded by default, and `sessions.recording.get` returns the audio afterwards. Say so
when you confirm the call — "this will be recorded" — because many places require everyone on a
call to know. If the user would rather not have a recording, say that recording is controlled in
the Speko dashboard rather than from here.

## Watching and reading back

`sessions.phone.create` returns a session id and comes back before the call is over. Poll
`sessions.get` with that id. When it has ended:

- `sessions.transcript.get` — what was actually said, both sides
- `sessions.recording.get` — a signed URL to the audio

Summarise the outcome first — did the thing the user wanted happen? — then offer the transcript.
Do not paraphrase a commitment the other party did not make; quote them.

`sessions.list` finds earlier calls when the user asks about one that already happened.

## Building an agent for a repeated call

For a one-off, pass `systemPrompt` straight to `sessions.phone.create` — no agent needed. When the
user will make the same kind of call repeatedly, create one:

Call `agents.preview_stacks` with a one-line description of the job. It returns three options —
**Quality**, **Fastest**, **Cheapest**. Show all three with their speech, language-model and voice
picks and ask the user which they want. Do not choose for them. Then call `agents.create` with
`intent.optimizeFor` set to `quality`, `latency` or `cost` to match.

## Transcribing and speaking

`audio.transcribe` turns audio into text. It takes an **HTTPS URL**, not an uploaded file — the
signed URLs from `sessions.recording.get` and `calls.recording.get` work directly, which is the
common case. If the user has a file rather than a link, say so plainly and ask for a link; do not
pretend to have read audio you could not fetch.

`audio.synthesize` speaks text in one of Speko's catalogue voices, including languages and voices
ChatGPT cannot produce itself. Pass the language in `intent` and Speko routes to a voice on its own,
so you never have to pick one — but when the user asks what is available, or wants a particular
kind of voice, call `voices.list` and show them rather than guessing. `models.list` answers the same
question for speech-to-text, language and text-to-speech models.

Synthesis selects from the published catalogue; it does not clone a voice and takes no reference
audio. If someone asks you to make it sound like a specific person, say that is not something Speko
does.

## What Speko will not do here

Buying a phone number, changing a plan and reading account credit are not available in ChatGPT —
send the user to the Speko dashboard for those. Deleting agents, numbers or knowledge bases is not
available either. Bulk, scheduled and unattended calling do not exist on this surface by design:
every call is one explicit request the user confirmed.

`docs.search` answers questions about how Speko itself works.
