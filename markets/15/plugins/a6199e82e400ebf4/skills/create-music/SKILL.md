---
name: create-music
description: Generate songs or instrumental audio with Melyx AI from a music description or the user's lyrics. Query private music, listen, and download the audio. Do not use audio-generation tools for lyric editing alone.
---

# Melyx AI music workflow

Use the connected Melyx AI MCP tools. Never claim that text-only lyric writing has generated an audio file.

## Before any audio generation

Determine whether the user wants audio or only help writing/editing lyrics. For writing alone, stay in the conversation and do not call `generate_music`. Do not ask for account passwords, cookies, private API keys, payment details or provider tokens.

For audio, call `get_music_account`. Allow the host's OAuth flow to connect the user's own Melyx AI account. Explain the exact current `generation_credits` and seek explicit approval to spend that amount on this generation. General account authorization is not approval for unlimited generation. Do not initiate subscription purchases or direct the user to a checkout; report insufficient existing credits neutrally.

## Form a supported request

Simple mode: place the desired genre, mood, instruments and music description in `prompt` (up to 3000 characters). Set `instrumental=true` for no vocals. Do not send custom duration or vocal_gender in simple mode.

Custom mode: provide `title` (up to 80 characters), `style` (up to 1000), and the user's lyrics in `prompt` (up to 5000). For instrumental custom mode, omit lyrics and set `instrumental=true`. Custom duration applies only to lyrics mode (instrumental=false): it is 10–360 seconds and defaults to 300 seconds (5 minutes) when omitted; preserve an explicitly requested duration in lyrics mode. Do not send a custom duration for description-based or instrumental generation. It is a requested target, not a guaranteed exact result. Do not silently rewrite the user's supplied lyrics; ask about substantive edits. Use musical characteristics rather than promises to copy an identifiable performer or guarantee identical vocals. Respect applicable content rules and user-provided rights; do not make blanket copyright or commercial-license promises.

Generate one UUID for `request_id` (the account tool supplies a suggested UUID). Keep it unchanged for every retry of the SAME authorized generation. Pass the approved current cost as `confirmed_credits`. A different request ID is for a separately authorized new generation, not a workaround for an error. Do not accept client-supplied user IDs, external persona IDs or unsupported reference files.

## After submission

Use the returned task ID with `get_music_task`; report real status. Never say a job is finished until status is `completed`. Do not continuously loop in chat. The player performs bounded checks and provides a manual refresh. Do not promise background notifications.

For `submission_unconfirmed`, `submission_in_progress` or an uncertain provider result, keep the task/request identifiers and check the ORIGINAL task. Never automatically submit a replacement or assert that no credits were charged. The existing website ledger and support reconciliation decide billing outcomes.

For completed output, show the player and returned audio links. Do not invent URLs, completion times, audio quality, licensing entitlements or search ranking.

`list_my_music` is a private, paginated library for the connected user. WAV preparation is temporarily unavailable in this ChatGPT integration. Do not offer or call `prepare_wav_download`; use the existing audio download instead.

## First-version boundaries

Do not expose reference-media upload, continuation, separation, voice cloning, account deletion, billing changes, purchasing or public sharing as supported actions. Use the conversation's language; supported player locales are English, simplified Chinese, German, French, Spanish, Portuguese and Korean.
