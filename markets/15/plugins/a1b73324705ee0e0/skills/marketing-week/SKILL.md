---
name: marketing-week
description: Plan a restaurant group's marketing week in Excellent — what's already queued, a post plan per venue and channel, social post and guest email drafts staged for a person to approve, revisions to drafts still waiting, a posting plan imported from a spreadsheet, and a new guest list. Use for "plan this week's posts", "draft an Instagram post about the patio room", "marketing plan for the week", "email past hosts", "make that post shorter", "use this photo instead", "import our posting plan", "start a newsletter list for the Mission venue".
---

# Marketing week plan

This skill stages and revises drafts, and can create a guest list (an undoable change). Nothing is approved,
published or emailed until a person approves it in Excellent under Portfolio → Marketing; only Excellent's
own engine sends, behind the group's live and consent gates.

## 1. See what's already there

1. `marketing` — recent social posts (channel, status, slot) and guest campaigns (segment, status, delivery
   progress). Note what is already scheduled this week so you don't double up.
2. `overview` — the venues in `locationList` (their ids are what `draft_marketing_post` takes as
   `location`).
3. `agenda` with `days: 14` — upcoming events worth a teaser, and `list_events` with `status: "completed"`
   for recent ones worth a recap.

## 2. Propose a plan

A short table: day, venue (or group-wide), channel (instagram, facebook or linkedin), angle (for example "recap
of Saturday's rehearsal dinner", "patio room for fall parties"). Two to four posts a venue is plenty. If a
guest email fits, propose one with its segment: `past_event_hosts`, `recent_guests` or
`inquiries_never_booked`. Ask the person to confirm or change the plan before drafting.

If the person already has the week's posts written in a spreadsheet (channel, caption, photo link, when,
location), stage the whole plan with `draft_post_import` instead (see the `import-a-list` skill): once a
person commits the import in Excellent, each row becomes a post awaiting approval.

## 3. Stage the drafts the person confirmed

- Social: `draft_marketing_post` with `channel`, `location` (omit for group-wide), `notes` (the angle) and,
  if the person gave a time, `schedule_at` as an ISO instant with a timezone. Leave `image_url` out unless
  they gave a specific picture; Excellent picks one from the group's own uploads. An Instagram post needs an
  image before it can be approved.
- Email: `draft_marketing_campaign` with `segment`, `notes` and optional `schedule_at`. It drafts in English
  and Spanish.

Each call stages a new draft, grounded only in the group's own events, recaps and reviews. Give back each
draft's review link. If a draft tool answers that the connection lacks draft access or the module is not
switched on, tell the person what the message says to do.

## 4. Revise a draft (if asked)

Change a draft still waiting rather than staging a second one. Show the new words first. The ids come from
the draft's own answer or from `marketing`.

- Post: `revise_marketing_post` with the `post_id` and any of `copy` (the full new words, which replace the
  current ones: up to 2,200 characters on Instagram, 3,000 on Facebook and LinkedIn, at most 30 hashtags),
  `image_url` (a public https image that becomes the post's one photo, replacing its media, a carousel or a
  video included — say so) and a future `schedule_at`.
- Campaign: `revise_marketing_campaign` with the `campaign_id` and the parts that change — `subject_en`,
  `body_en`, `subject_es`, `body_es`. What you leave out keeps its words; a Spanish version needs both its
  subject and its body.

A post or campaign already approved, rejected or sent is left as it is: say a person changes it in Excellent.
The revised draft stays a draft; give back its review link.

## 5. A new guest list (if asked)

`create_marketing_list` with a `name`, its `kind` (`newsletter`, `loyalty` or `deals`), an optional
`description`, and a `location` for one venue's own list (omit it for the group). Say what you will create and
wait for a yes; afterwards give the `change_id` and say it can be undone. The list starts empty and has no
public signup page: members are added in Excellent, with the consent the restaurant holds.

## 6. Hand off

End with: "These are drafts in Portfolio → Marketing. Nothing goes out until you approve it there."

Safety: posts and emails are drafts behind their review links; only Excellent's own engine sends, once a person
approves. A new guest list is made only on the person's yes and returns a `change_id` that `undo` puts back,
once, for 30 days. Nothing is published, emailed, charged or deleted from ChatGPT.
