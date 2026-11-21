---
name: dativue-video-repurposing
description: Use Dativue when a user wants to transcribe, summarize, analyze, quote, or repurpose a public YouTube, TikTok, or Instagram video.
---

# Video transcript analysis and repurposing

Use this workflow when the user provides a public YouTube, TikTok, or Instagram video and wants analysis or derivative content.

1. Retrieve the public video directly. Use `research_credit_quote` when the user asks for an estimate or the work may exceed 50 credits. Each additional 15-minute transcript segment has the same fixed transcript price.
2. Retrieve the public video metadata with `social_get`, then the first transcript segment with `social_transcript`.
3. Follow `nextCursor` only when more of the transcript is necessary. Ask for approval if the complete plan exceeds 50 credits. Use the opaque cursor unchanged.
4. Distinguish claims found in the transcript from your own editorial suggestions. Never invent quotations or details missing from the public source.
5. Summarize the argument, strongest moments, examples, and reusable ideas with timestamps where available.
6. Produce a short-video outline, LinkedIn post outline, and email outline suited to their formats. Cite the original video URL.

Default maximum: 2 credits for video metadata and the first 15 transcript minutes.
