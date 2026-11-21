---
name: upload-music-video-to-youtube
description: "Prepare a music video upload for YouTube: title, description with credits and links, tags, chapters, thumbnail brief, end screens and cards, captions, premiere settings, audience and rights settings, and a pre-publish checklist. Use when the user asks 'how do I upload to YouTube', 'YouTube title and description', 'premiere my video', or 'optimize my video'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Content
  group: "Content & marketing"
  display_name: "YouTube Upload"
  website: https://www.artispreneur.com
---

# YouTube Upload

> Everything ready to upload your video to YouTube.
> *Content desk · Content & marketing · about 20 minutes*

## When to use

- A music video or lyric video is finished and ready to publish.
- An existing upload is under-performing and needs better packaging.
- The artist wants a release-day premiere.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Video title, artist name, and the final export (confirm resolution and length).
- Credits and links (streaming, merch, mailing list, socials).
- Release date and whether to use a premiere.
- Lyrics or captions available.
- Related videos or playlists to link.

## Workflow

1. Write the title in a clear format: **Artist - Song Title (Official Music Video)** or the artist's chosen variant. Keep it truthful.
2. Write the description: first two lines carry the key link and a hook; then credits, streaming links, lyrics, social links, and contact.
3. Add chapters if the video has distinct parts; add captions or the SRT file.
4. Create the thumbnail brief: strong subject, readable text at small size, consistent look. Check the current size and size limit in YouTube Studio.
5. Choose tags and a category (Music). Tags matter little, so keep them accurate.
6. Set the audience setting accurately (most music videos are not made for kids) and license settings; add end screen and cards pointing to the next video.
7. Plan the premiere or scheduled publish and the first-hour community actions (comments, pinned comment, share).
8. Run the pre-publish checklist.

## Deliverables

- Title options.
- Full description.
- Thumbnail brief.
- End-screen and card plan.
- Pre-publish checklist.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Title, thumbnail, and content match (no misleading packaging).
- [ ] Credits are complete and spelled correctly.
- [ ] Links work and are tracked if the artist uses tracking.
- [ ] Audience and rights settings are correct.
- [ ] Captions are uploaded and match the audio.

## Guardrails

- Do not recommend misleading titles or thumbnails, bot views, or fake engagement.
- Only upload music and visuals the artist owns or licenses.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `transcribe-lyrics`: captions and lyrics
- `create-lyric-video`: if no video yet
- `generate-social-media-content`: promote the premiere

## Start with

> Prepare my YouTube upload. Here's the video, credits and links.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
