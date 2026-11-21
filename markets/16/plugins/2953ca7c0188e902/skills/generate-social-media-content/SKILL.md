---
name: generate-social-media-content
description: "Write a pack of platform-native social posts (hooks, captions, on-screen text, shot ideas, calls to action, alt text) in the artist's voice for Instagram, TikTok, YouTube Shorts, X, Threads, or Facebook. Use when the user asks for captions, post ideas, a content pack for a release, or 'write posts for me'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Content
  group: "Content & marketing"
  display_name: "Social Content Pack"
  website: https://www.artispreneur.com
---

# Social Content Pack

> Platform-native posts in your voice, ready to publish.
> *Content desk · Content & marketing · about 20 minutes*

## When to use

- A release, show, or milestone needs posts.
- The artist has a calendar but no copy.
- Posts feel generic or inconsistent.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- What the posts are for (release, show, behind the scenes, offer).
- Platforms and formats (Reel, carousel, short, text post).
- Brand voice (or the output of `write-brand-guidelines`) and example captions the artist liked.
- Facts and assets available (clips, photos, lyrics lines the artist owns).
- The action each post should drive (stream, save, follow, sign up).

## Workflow

1. Load the voice. If no guide exists, write three sample captions and have the artist pick the closest.
2. For each post, write: **hook** (first line or first two seconds), **caption**, **on-screen text**, **shot or visual idea**, **call to action**, and **alt text**.
3. Make each piece native to its platform: short and visual for short video, scannable for carousels, conversational for text posts.
4. Vary the pillars (music, process, story, community, offer) so the feed is not all promotion.
5. Use hashtags sparingly and only relevant ones; the artist can add platform-specific tags.
6. Mark any claim, number, or tag of another account that needs the artist's confirmation `[CONFIRM]`.
7. Add disclosure language when a post is paid or sponsored.

## Deliverables

- Post pack: 7 to 15 posts with all fields.
- Hook bank.
- Alt text for every image.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Each post has a hook in the first line.
- [ ] No claims or numbers the artist did not provide.
- [ ] Voice is consistent across the pack.
- [ ] Calls to action vary and are not spammy.
- [ ] Sponsored posts carry disclosure.

## Guardrails

- Do not quote or paraphrase another artist's lyrics.
- Do not tag people or brands that the artist has not named.
- No engagement bait that platform rules prohibit.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `create-content-calendar`: schedule the pack
- `write-brand-guidelines`: lock the voice
- `analyze-social-media-engagement`: learn from results

## Start with

> Write social posts for my release. Here's the vibe and what I have to show.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
