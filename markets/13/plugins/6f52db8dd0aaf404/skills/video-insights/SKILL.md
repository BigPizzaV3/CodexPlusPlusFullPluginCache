---
name: video-insights
description: Get transcripts, metadata, and structured data from public YouTube, TikTok, Instagram, X, and Facebook videos with Supadata. Use when the user shares a video or post link and wants a transcript, summary, quotes, stats, or specific details pulled from it.
---

# Video insights with Supadata

Use the Supadata tools when the user gives a link to a public video or social post and wants to know what is in it.

## Pick the tool

- **What is said in the video** (transcript, summary, quotes, translation of the spoken content): `supadata_transcript`.
- **Facts about the video or post** (title, author, publish date, duration, views, likes, tags): `supadata_metadata`.
- **Specific fields that need the visuals or a fixed shape** (products shown, steps in a tutorial, a list of items as JSON): `supadata_extract` with a `prompt`, a JSON `schema`, or both.

## Transcripts

1. Call `supadata_transcript` with the `url`. Set `text: true` when the user wants plain text and timestamps are not needed; leave it off when they ask for timestamps or chapters.
2. Set `lang` to the language the user is writing in or asked for (an ISO 639-1 code such as `en`). The response lists `availableLangs`; if the returned `lang` is not the one the user wants and it is available, call again with that `lang`.
3. If the response contains a `jobId` instead of content, the video is being transcribed. Call `supadata_check_transcript_status` with that id every few seconds until the status is `completed` or `failed`.
4. Base summaries and quotes only on the returned transcript. Quote exactly, and say so if the transcript is unavailable.

## Structured extraction

1. Call `supadata_extract` with the `url` and a clear `prompt`. Add a JSON `schema` when the user needs a predictable structure.
2. It always returns a `jobId`. Poll `supadata_check_extract_status` until `completed`, then present the `data`.

## Limits

- Only public content is supported. Do not ask the user for a password, cookies, or login details, and do not attempt private, age-gated, or paywalled videos.
- The tools read content. They cannot download video or audio files, post, comment, like, or message.
- If a tool reports that the account's plan or usage limit does not cover the request, tell the user plainly and stop.
