---
name: chattube
description: Search YouTube, summarize videos, extract key points, and answer questions about video content using ChatTube. Handle ChatTube tool results, including exhausted AI credits and account-entitlements guidance.
---

# ChatTube workflow

Use the connected ChatTube tools for the user's YouTube request. Ask for a missing
video URL or other required input when it cannot be determined from the conversation.
Use `youtube_video_transcript` for summaries and questions about video content;
use the relevant search, video, channel, playlist, or comment tools for other requests.
Call `get_profile` only when the user asks about their ChatTube account or credits.

Inspect each tool result before calling another tool or composing the answer.

## Before requesting a transcript

Check the user's intended output before calling `youtube_video_transcript`. If
they ask to download, export, transcribe, or reproduce a complete transcript or
subtitle file, including SRT, VTT, JSON, or plain text, do not call the tool.
Explain that complete transcripts and subtitle exports are unavailable due to
copyright and content licensing restrictions. Offer a summary, key points,
chapters, or answers about the video's content instead. Use the transcript tool
only for these transformative tasks.

## AI credit usage

Each successful ChatTube tool call, except `get_profile`, costs 1 AI credit,
including calls for subsequent pages and successful calls with no results.
Internal API requests and retries within a tool call do not add charges. Failed
calls, `credits_exhausted` results, and `get_profile` are free.

## When AI credits are exhausted

A ChatTube tool returns `structuredContent.status: "credits_exhausted"`
and `structuredContent.entitlementsUrl`. This is the end of the current ChatTube
workflow, not a temporary API failure or an empty search result.

1. End the current ChatTube workflow. Do not retry the credit-consuming ChatTube
   call or make further credit-consuming ChatTube calls for this workflow.
2. Briefly explain in the user's language that they have used up their ChatTube AI
   credits. Use a friendly, conversational tone and include a clickable
   account-entitlements link using `entitlementsUrl`.
   If the URL is missing, use `https://chattube.io/entitlements`.
3. Keep the ChatTube credit notice brief. Do not claim that unavailable ChatTube
   results were retrieved, or promote an upgrade, subscription, purchase, pricing,
   or checkout flow.

Example response in English:

> You've used up your ChatTube AI credits. You can take a look at your [account entitlements](https://chattube.io/entitlements) for details about credits and plan benefits.

Also apply this branch to a legacy ChatTube tool result that explicitly says all
ChatTube AI credits have been used. Do not infer exhausted credits from unrelated
technical errors, a missing login, or an empty result.

This status applies only to ChatTube's AI credits, not to the conversation as a
whole. It does not restrict other plugins, tools, information sources, or later
user requests. Handle subsequent non-ChatTube requests normally without repeating
the credit notice. A new ChatTube call that reports exhausted credits should
receive the same notice and entitlements link.

## Pagination

For tools that support pagination, omit `pageToken` on the first call. Fetch
another page only when needed to meet the user's requested number of results or
scope. Pass the returned `nextPageToken` unchanged as `pageToken` to the same tool,
keeping the same resource, query, filters, sort order, and locale settings.
Never invent a token or reuse one for a different tool or query.

Stop when the requested coverage is satisfied, `hasMore` is false, or
`nextPageToken` is null. Do not automatically retrieve every available page;
each successful page costs another AI credit.

## Transcript language

Pass `language` to `youtube_video_transcript` only when the user explicitly asks
for a particular subtitle language. Otherwise omit it and let the server choose
the default track, preferring English when available. The user's requested reply
language does not by itself select a subtitle language. `lang` only localizes API
metadata; it does not select or translate the transcript.

If `resolvedTranscript.matchedRequestedLanguage` is false, briefly explain the
fallback using `resolvedTranscript.selectedLanguage` and `resolvedTranscript.message`.
Use the returned transcript for the analysis rather than repeating the same
request to obtain the unavailable language. Reply in the user's requested language
regardless of the subtitle language.

## Timestamp links

When summarizing a video, listing key points, generating chapters, or answering
questions about its content, add clickable timestamp links next to the relevant
sentences or bullet points whenever the returned data provides reliable timing.
For answers covering multiple videos, link each point to the video it comes from.

Use the start time of the transcript segment or chapter that supports the point.
Build links as `https://www.youtube.com/watch?v=VIDEO_ID&t=SECONDSs`, replacing
`VIDEO_ID` with the actual video ID and `SECONDS` with the start time in whole
seconds, rounded down. If a JSON3 segment provides `tStartMs`, divide it by 1,000
before rounding. Use `MM:SS` as the link label, or `H:MM:SS` for times of an hour
or more.

Example for a supporting segment starting at 135 seconds:

> The speaker introduces the main idea [02:15](https://www.youtube.com/watch?v=VIDEO_ID&t=135s).

Keep links close to the content they support instead of collecting them in a
separate list. Do not invent or estimate timestamps from the topic, text length,
or video duration. If reliable timing is unavailable, omit the timestamp and use
a regular video link when available.

## Other results

For successful results, answer from the returned data and state any missing
information. Do not reproduce complete transcripts, expose raw subtitle content
or subtitle download URLs, or reconstruct a transcript through repeated excerpts.
If login is required, let the user complete ChatTube sign-in. For other tool errors,
explain the failure without claiming the user's credits are exhausted.
