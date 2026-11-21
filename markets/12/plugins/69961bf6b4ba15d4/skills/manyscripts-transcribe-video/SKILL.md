---
name: manyscripts-transcribe-video
description: Extract complete transcripts, creator captions, and metadata from public YouTube, TikTok, Instagram Reel, X/Twitter, Facebook, or Xiaohongshu (beta) video URLs with ManyScripts. Use when a user wants verbatim speech or analysis or translation grounded in a social video. Do not use for ordinary webpages, profiles, Stories, private videos, or uploaded files.
---

# ManyScripts Transcribe Video

Call `extractTranscript` with the exact public video URL the user supplied.

## Deliver the requested result

- When the user asks for a transcript, return the complete transcript verbatim. Do not substitute a summary or silently shorten a long transcript.
- Keep the creator-written caption separate from the spoken transcript and label both clearly when returning both.
- When the user asks for analysis, a summary, translation, quotes, hooks, or action items, ground the answer in the returned transcript. Include the full transcript only when the user also requested it.
- For an Instagram carousel, TikTok photo post or Xiaohongshu photo note, the tool returns the caption and the text on each slide; label them as slide text, not speech.
- For multiple URLs, call the tool once for each supported URL and label every result with its source URL.

## Handle unsupported or failed inputs

- Do not call the tool for an ordinary webpage, channel or profile, Story, private video, uploaded audio or video file, or shortened `t.co` link.
- Surface the tool's useful error message and ask for a supported public video URL when the input can be corrected.
- Never invent missing transcript text or claim that a video was processed when the tool did not return a transcript.
