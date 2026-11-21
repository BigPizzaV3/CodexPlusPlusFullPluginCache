---
name: directory-search
description: "Build a ranked target list (up to 15) of blogs, playlist curators, radio shows, podcasts, press, or venues that fit an artist's genre, size, and location, with fit reasons, source links, and the correct contact route. Use when the user asks 'who should I pitch', 'find me blogs or playlists for my genre', 'venues in my city', or before any outreach campaign."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Booking
  group: "Outreach"
  display_name: "Industry Contact Finder"
  website: https://www.artispreneur.com
---

# Industry Contact Finder

> Find the right blogs, playlists, radio, podcasts, press and venues for your genre.
> *Booking desk · Outreach · about 20 minutes*

## When to use

- Before pitching press, playlists, radio, podcasts, or venues.
- The artist does not know who covers their genre.
- A previous list is stale.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Genre and sound, plus three artists the audience also likes.
- Target type: blogs, playlists, radio, podcasts, press, or venues.
- Coarse target market or region (for example state, country, or tour region; never request precise street addresses or GPS coordinates).
- Artist size (draw, listeners) and what proof exists.
- The goal: a review, a playlist add, an interview, or a booking.

## Workflow

1. Define the target profile: type, genre, region, size band, and how recently active.
2. Search the Artispreneur industry directory at artispreneur.com/directory, which is searchable by type, genre, and location. If the artist has no access, use the manual method: look at where similar artists got coverage, venue calendars, curator profiles, and publicly listed submission pages.
3. For each candidate, verify it is active (recent posts, shows, or episodes), covers this genre, and accepts submissions. Record the source URL and the date checked.
4. Rank by fit: genre match, size match, recent activity, and a clear contact route. Keep the top 15.
5. For each target write: name, why it fits (one line), the correct contact route (submission form, public email, or booking page), and the next action.
6. Hand the list to the matching outreach skill.

## Deliverables

- Ranked list of up to 15 targets with fit reasons.
- Source URL and date checked for every target.
- Contact route and next action for each.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Output template

| Rank | Name | Type | Why it fits | Contact route (public) | Source URL | Date checked |
|---|---|---|---|---|---|---|

## Quality checks (run before handing over)

- [ ] Every row has a source URL and date.
- [ ] Each target was confirmed active.
- [ ] Contact details are publicly listed ones only.
- [ ] No contacts were invented or guessed.

## Guardrails

- Never invent contacts, emails, or submission policies.
- Use only publicly listed business contact routes.
- Do not scrape personal data or buy lists.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `booking-outreach`: venues and promoters
- `media-outreach`: blogs and journalists
- `playlist-outreach`: playlist curators
- `pr-campaign`: a full press sequence

## Start with

> Find me 15 targets for my genre and location. Here's my sound and my size.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
