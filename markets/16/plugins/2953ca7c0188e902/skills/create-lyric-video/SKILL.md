---
name: create-lyric-video
description: "Plan and produce a lyric video: concept and style, typography and color, scene-by-scene text animation plan, timed lyrics (LRC/SRT), export specs for YouTube and vertical platforms, and, when the environment can run code and video tools, a rendered MP4. Use when the user asks for a lyric video, kinetic typography, or 'visualizer with words'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Content
  group: "Content & marketing"
  display_name: "Lyric Video"
  website: https://www.artispreneur.com
---

# Lyric Video

> A kinetic lyric video, ready to render, no editor skills needed.
> *Content desk · Content & marketing · about 30 minutes*

## When to use

- A release needs a quick video asset.
- The artist has the audio and lyrics but no video.
- The artist needs vertical cut-downs for short-form platforms.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Audio file or link and final lyrics (the artist's own).
- Timing: existing timestamps, or permission to build timing from the audio if tools allow.
- Style: mood, color palette, fonts, any brand guidelines or logo.
- Aspect ratios needed (16:9 for YouTube, 9:16 for short-form).
- Artwork or footage the artist owns.

## Workflow

1. Confirm the artist owns or licenses the audio, lyrics, and any footage or imagery.
2. Produce the timed lyrics (`lyrics.lrc` or `.srt`) using `transcribe-lyrics`. Check the timing against the audio.
3. Write the style brief: palette, fonts (licensed or open), motion language (for example slam-in, slow fade, word-by-word), background treatment, and how the chorus and verses differ.
4. Write the scene plan: for each section, text layout, motion, and background change.
5. Production route A, if the environment can run code and has ffmpeg: build the video from the timed lyrics (for example HTML or canvas frames or a video library) and render MP4 at 1920x1080 and 1080x1920. Review a short test render first.
6. Production route B, if no render tools exist: give a step-by-step build in a tool the artist already uses (Canva, CapCut, DaVinci Resolve, or similar) with exact text timings and layer settings.
7. Export checklist: resolution, frame rate, audio level, safe margins for captions and platform UI, filename, and thumbnail.

## Deliverables

- Timed lyrics file.
- Style brief and scene plan.
- Rendered MP4 (when tools are available) or a step-by-step build guide.
- Export checklist and vertical cut-down plan.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Lyrics on screen match the audio at every line.
- [ ] Text stays within safe margins and is readable at phone size.
- [ ] Contrast between text and background is high enough to read.
- [ ] Audio level is not clipped.
- [ ] Only licensed or owned assets are used.

## Guardrails

- Do not use footage, fonts, or images the artist cannot license.
- Do not claim a render happened if it did not; say which route was used.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `transcribe-lyrics`: timed lyrics
- `upload-music-video-to-youtube`: publish it
- `generate-social-media-content`: cut and caption short versions

## Start with

> Make a lyric video for my song. Here are the audio, the lyrics and the vibe.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
