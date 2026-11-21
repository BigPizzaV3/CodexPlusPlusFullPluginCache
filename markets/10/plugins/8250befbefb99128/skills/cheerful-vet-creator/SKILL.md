---
name: cheerful-vet-creator
description: "Review one creator's public profile against the user's brief in Cheerful: audience size, engagement, niche fit, recent posts, whether a public email exists, and whether the user has already saved or contacted them. Read-only. Use when the user asks \"vet @handle\", \"is @handle a good fit\", \"tell me about this creator\", \"check this influencer\", \"should I work with @handle\", \"have we contacted @handle before\", or pastes an Instagram, TikTok or YouTube profile link."
---

# Vet a creator

Check one creator against the user's brief and against what the user already has in Cheerful.
Read-only: it saves nothing and contacts no one.

## Step 0: Check the connection

If a Cheerful tool is unavailable, or a call answers "Tool not found" or asks to reconnect, stop
and tell the user: "Connect Cheerful from the plugin page, then ask me again." Don't retry.

## Read this first: what the data can and can't tell you

- **The platform must match.** The same handle can be a different person on another platform.
  Take the platform from the link or the user's words; if neither says, use Instagram and say
  so in your reply rather than asking.
- **"Not enriched yet" is not "no audience".** TikTok and YouTube creators Cheerful hasn't seen
  before come back with `is_enriched` false and no detail. Say "not enriched yet"; Cheerful fills
  it in when the creator is added to a campaign.
- **Most creators have no public email.** That is the common case, not a red flag.
- **A first look is slow.** A profile Cheerful hasn't loaded recently can take about a minute.
  Tell the user it is working and don't call it twice.
- **Low engagement is a flag, not a verdict.** Under about 0.5% on 50k+ followers often means a
  bought audience; say so plainly and let the user decide.

## Workflow

1. **Identify.** Get the handle (drop the @) and platform from the message or link. If the user
   gave a brief earlier in the chat, use it; otherwise vet on general quality and say so.
2. **Profile.** Call `creator_profile` with `handle` (or the pasted link) and `platform`. Note
   followers, `engagement_rate`, bio, recent posts (topic, how recent, how they perform), where
   the audience is (`audience`, when present) and whether a public email exists.
3. **Already saved?** Call `list_read` with `action="index"`. For lists whose names suggest a match,
   call `list_read` with `action="get"` and that `list_id`, and look for the handle. Stop after 3
   lists.
4. **Already contacted?** Call `inbox_read` with `action="search"` and `search` set to the handle
   (and the creator's name if the profile has one). Report any conversation with its campaign and
   where it stands.
5. **Verdict.** Score fit against the brief on niche, audience size, engagement and recent
   activity: **Good fit**, **Possible fit** (say what's uncertain) or **Not a fit** (say why).
6. **Offer, don't act.** Offer to save them to a list. Only if the user says yes, call
   `save_creators_to_list` with this creator, `platform` set to the platform from step 1 (always
   pass it; there is no default), and their `list_id` or a `new_list_name`.

## Output layout

In ChatGPT the profile appears as a creator card automatically. After the card, write at most 2
sentences: the verdict and the main reason, plus anything from steps 3-4 (already saved or
contacted). Don't repeat the card's numbers in prose.

Where no card is shown (for example in Codex), use this layout:

```
**@zardyplants · Liz and Paul · Instagram** — Good fit for "US vegan cooking"

- **Audience:** 95.2k followers · 1.8% engagement
- **Niche:** easy plant-based comfort food; posts new recipes weekly
- **Recent posts:** 3 in the last 2 weeks, all recipes
- **Contact:** has a public email
- **In Cheerful:** on your list "Vegan food creators (US)" · not contacted yet

**Why:** on-niche, consistent posting, healthy engagement for the size.
Want me to save them to a list?
```

## Rules

- Plain language: no ids, field names, status codes or "tool" in the reply.
- Never print the creator's email address or phone number; say "has a public email".
- Never email or message the creator yourself. If they fit and `create_campaign_draft` is listed, offer
  to add them to a campaign (the user sends it from the launch card); otherwise outreach is set
  up in Cheerful at https://app.cheerful.ai.
- Don't promote plans or purchases.
